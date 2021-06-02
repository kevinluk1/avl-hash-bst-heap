# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


import random
import sys

sys.setrecursionlimit(1500)


# from bst import *
class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
        YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)

    def __repr__(self):
        return self.value


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------

    def rec_rebalance(self, node):

        if node is None:
            return
        if self.get_balance_factor(node) < -1:
            if self.get_balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
                node.left.parent = node
            whatever = node.parent
            new_sub_root = self.rotate_right(node)
            new_sub_root.parent = whatever
            if new_sub_root.parent is not None:
                if new_sub_root.value < new_sub_root.parent.value:
                    new_sub_root.parent.left = new_sub_root
                if new_sub_root.value > new_sub_root.parent.value:
                    new_sub_root.parent.right = new_sub_root

            if new_sub_root.parent is None:
                self.root = new_sub_root

        if self.get_balance_factor(node) > 1:
            if self.get_balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
                node.right.parent = node
            whatever = node.parent
            new_sub_root = self.rotate_left(node)
            new_sub_root.parent = whatever

            if new_sub_root.parent is not None:
                if new_sub_root.value < new_sub_root.parent.value:
                    new_sub_root.parent.left = new_sub_root
                if new_sub_root.value > new_sub_root.parent.value:
                    new_sub_root.parent.right = new_sub_root

            if new_sub_root.parent is None:
                self.root = new_sub_root




        else:
            self.update_height(node)

        self.rec_rebalance(node.parent)

    def rebalance(self, node):

        self.rec_rebalance(node)

    def rotate_right(self, node):
        c = node.left
        node.left = c.right
        if node.left is not None:
            node.left.parent = node
        c.right = node
        node.parent = c
        self.update_height(node)
        self.update_height(c)
        return c

    def rotate_left(self, node):
        c = node.right
        node.right = c.left

        if node.right is not None:
            node.right.parent = node

        c.left = node

        node.parent = c

        self.update_height(node)
        self.update_height(c)
        return c

    def update_height(self, node):
        if node.right is not None:
            right_height = node.right.height
        else:
            right_height = - 1

        if node.left is not None:
            left_height = node.left.height
        else:
            left_height = -1

        node.height = max(left_height, right_height) + 1

    def get_balance_factor(self, node):
        if node.right is not None:
            right_height = node.right.height
        else:
            right_height = - 1

        if node.left is not None:
            left_height = node.left.height
        else:
            left_height = -1

        balance_factor = right_height - left_height
        return balance_factor

    def get_height(self, node):

        self.rec_get_height(node)

    def rec_get_height(self, node):
        if node is None:
            return
        if node.left is not None:
            node_left_height = node.left.height
        else:
            node_left_height = -1

        if node.right is not None:
            node_right_height = node.right.height
        else:
            node_right_height = -1

        node.height = max(node_left_height, node_right_height) + 1

        self.rec_get_height(node.parent)

    # -----------------------------------------------------------------------

    def rec_add(self, parent, new_node):

        if parent.value < new_node.value and parent.right is None:
            parent.right = new_node
            new_node.parent = parent
            return

        if parent.value > new_node.value and parent.left is None:
            parent.left = new_node
            new_node.parent = parent
            return

        if parent.value > new_node.value:
            self.rec_add(parent.left, new_node)
        if parent.value < new_node.value:
            self.rec_add(parent.right, new_node)

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """
        new_node = TreeNode(value)
        parent = self.root

        if self.root is None:
            self.root = new_node
            return

        if self.root is not None:
            self.rec_add(parent, new_node)

        self.get_height(new_node.parent)
        self.rebalance(new_node.parent)

    # -----------------------------------------------------------------------------------
    def helper_contains(self, value, node):  # node now points to either node.left or node.right
        if node is None:
            return False

        if node.value == value:
            return True

        elif value < node.value:
            return self.helper_contains(value, node.left)  # traverses

        elif value > node.value:
            return self.helper_contains(value, node.right)

    def contains(self, value: object) -> bool:
        """
        Check to see if tree contains a node of x value
        """
        return self.helper_contains(value, self.root)

    def get_first(self) -> object:
        """
        Returns the first ndoe
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    def get_target(self, value, node, parent):
        """
        Helper node to traverse to target during removal
        """
        if value == node.value:
            return node
        if value < node.value:
            return self.get_target(value, node.left, node.left)
        if value > node.value:
            return self.get_target(value, node.right, node.left)

    def get_target_parent(self, node, target_node_value):
        """
        Helper node to get parent of target during removal
        """
        if target_node_value == node.value:
            return None
        if node.right is not None:
            if node.right.value == target_node_value:
                return node
        if node.left is not None:
            if node.left.value == target_node_value:
                return node
        if target_node_value > node.value:
            return self.get_target_parent(node.right, target_node_value)
        if target_node_value < node.value:
            return self.get_target_parent(node.left, target_node_value)

    def helper_get_successor_node(self, value, right_node,
                                  parent):  # pass in the node to the right of node being removed as 'right_node'
        """
        Get in order successor node
        """
        if right_node is None:
            return None
        if right_node.left is None:
            return right_node
        return self.helper_get_successor_node(value, right_node.left, right_node)

    def helper_get_parent_of_successor_node(self, node,
                                            successor_node_value,
                                            target) -> int:  # find the parent of the successor node
        """
        Get parent node of inorder successor
        """
        if node.right is not None:
            if node.right.value == successor_node_value and node.right is not target:
                return node

        if node.left is not None:
            if node.left.value == successor_node_value and node.left is not target:
                return node

        if successor_node_value >= node.value:
            return self.helper_get_parent_of_successor_node(node.right, successor_node_value, target)

        if successor_node_value < node.value:
            return self.helper_get_parent_of_successor_node(node.left, successor_node_value, target)

    def remove_first(self) -> bool:
        """
        Remove first node from tree
        """

        if self.root is None:
            return False

        if self.root.right is None and self.root.left is None:  # if no children
            self.root = None
            return True

        if self.root.right is None and self.root.left is not None:  # if 1 child

            self.root = self.root.left
            self.root.parent = None
            self.remove_rebalance_helper(self.root)
            return True

        if self.root.left is None and self.root.right is not None:  # if 1 child
            self.root = self.root.right
            self.root.parent = None
            self.remove_rebalance_helper(self.root)
            return True

        # ----------------- 2 children ----------------- #

        if self.root.left is not None and self.root.right is not None:
            successor_node = self.helper_get_successor_node(0, self.root.right, self.root)
            successor_node_parent = self.helper_get_parent_of_successor_node(self.root, successor_node.value, self.root)

            # ----------------- 2 sub-cases ----------------- #

            if successor_node is not self.root.right:
                successor_node.left = self.root.left
                self.root.left.parent = successor_node
                successor_node_parent.left = successor_node.right  # replaces successor node with successor node's right child (there won't be a left child ever)
                if successor_node.right is not None:
                    successor_node.right.parent = successor_node_parent
                successor_node.right = self.root.right
                self.root.right.parent = successor_node
                successor_node.parent = None

                self.root = successor_node

                self.remove_rebalance_helper(self.root)
                self.get_height(successor_node_parent)
                return True

            if successor_node is self.root.right:
                successor_node.left = self.root.left
                if self.root.left is not None:
                    self.root.left.parent = successor_node
                self.root = successor_node
                self.root.parent = None
                self.remove_rebalance_helper(self.root)
                self.get_height(successor_node_parent)
                return True

    def remove_rebalance_helper(self, p):
        while p is not None:
            self.rebalance(p)
            p = p.parent

    # -----------------------------------------------------------------------------------

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        if not self.contains(value):
            return False

        if self.root is None:
            return False

        if value == self.root.value:
            self.remove_first()
            return True

        target = self.get_target(value, self.root, 0)
        target_parent = self.get_target_parent(self.root, target.value)

        if target.right is None and target.left is None:
            if target.value < target_parent.value:
                target_parent.left = None
            if target.value > target_parent.value:
                target_parent.right = None
            p = target_parent
            self.remove_rebalance_helper(p)
            return True

        if target.value > target_parent.value and target.right is None:  # if 1 child
            target_parent.right = target.left
            target.left.parent = target_parent
            p = target_parent
            self.remove_rebalance_helper(p)
            return True

        if target.value > target_parent.value and target.left is None:
            target_parent.right = target.right
            target.right.parent = target_parent
            p = target_parent
            self.remove_rebalance_helper(p)
            return True

        if target.value < target_parent.value and target.left is None:
            target_parent.left = target.right
            target.right.parent = target_parent
            p = target_parent
            self.remove_rebalance_helper(p)
            return True

        if target.value < target_parent.value and target.right is None:
            target_parent.left = target.left
            target.left.parent = target_parent
            p = target_parent
            self.remove_rebalance_helper(p)
            return True

        if target.right is not None and target.left is not None:  # if 2 children

            successor_node = self.helper_get_successor_node(0, target.right, self.root)
            successor_node_parent = self.helper_get_parent_of_successor_node(self.root, successor_node.value, target)

            if successor_node is not target.right:
                successor_node.left = target.left
                target.left.parent = successor_node.left
                successor_node_parent.left = successor_node.right  # replaces successor node with successor node's right child (there won't be a left child ever)
                if successor_node.right is not None:
                    successor_node.right.parent = successor_node_parent
                successor_node.right = target.right
                target.right.parent = successor_node.right

                if target_parent.value > target.value:
                    target_parent.left = successor_node
                    successor_node.parent = target_parent
                    p = target_parent
                    self.remove_rebalance_helper(p)
                    self.get_height(successor_node_parent)
                    return True

                if target_parent.value <= target.value:
                    target_parent.right = successor_node
                    successor_node.parent = target_parent
                    p = target_parent
                    self.remove_rebalance_helper(p)
                    self.get_height(successor_node_parent)
                    return True

            if successor_node is target.right:
                successor_node.left = target.left
                target.left.parent = successor_node #.left
                if target is target_parent.left:
                    target_parent.left = successor_node
                    successor_node.parent = target_parent
                    p = target_parent
                    self.remove_rebalance_helper(p)
                    self.get_height(successor_node_parent)
                    return True

                if target is target_parent.right:
                    target_parent.right = successor_node
                    successor_node.parent = target_parent
                    p = target_parent
                    self.remove_rebalance_helper(p)
                    self.get_height(successor_node_parent)
                    return True




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':
    """ add() example #1 """

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)
        print(avl.is_valid_avl())


    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),  # RR, RR
        (10, 20, 30, 50, 40),  # RR, RL
        (30, 20, 10, 5, 1),  # LL, LL
        (30, 20, 10, 1, 5),  # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)
        print(avl.is_valid_avl())
    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL()
        for value in case:
            avl.add(value)
        if not avl.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)
        print(avl.is_valid_avl())

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)
        print(avl.is_valid_avl())

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)



    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl, avl.root.value)
        avl.remove(avl.root.value)
        print('RESULT :', avl)
        print(avl.is_valid_avl())
    # # #
    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     avl = AVL(case)
    #     for value in case[::2]:
    #         avl.remove(value)
    #     if not avl.is_valid_avl():
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('remove() stress test finished')
