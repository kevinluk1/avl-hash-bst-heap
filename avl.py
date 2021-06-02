# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


import random
import sys
sys.setrecursionlimit(1175)

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





    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':
    """ add() example #1 """

    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # test_cases = (
    #     (1, 2, 3),  # RR
    #     (3, 2, 1),  # LL
    #     (1, 3, 2),  # RL
    #     (3, 1, 2),  # LR
    # )
    # for case in test_cases:
    #     avl = AVL(case)
    #     print(avl)
    #


    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
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
    #
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

    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # test_cases = (
    #     ((1, 2, 3), 1),  # no AVL rotation
    #     ((1, 2, 3), 2),  # no AVL rotation
    #     ((1, 2, 3), 3),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # avl = AVL(case)
    # for del_value in case:
    #     print('INPUT  :', avl, del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # avl = AVL(case)
    # for _ in case[:-2]:
    #     print('INPUT  :', avl, avl.root.value)
    #     avl.remove(avl.root.value)
    #     print('RESULT :', avl)
    #
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
