# Course: CS261 - Data Structures
# Student Name: Kevin Luk
# Assignment: 3
# Description: Binary Search Tree implementation


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

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __repr__(self):
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

    def dequeue(self) -> object:
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
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)

    # def __repr__(self):
    #     return "VALUE: " + str(self.value) + ", LEFT: " + str(self.left) + ", RIGHT: " + str(self.right)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    # def __repr__(self):
    #     values = []
    #     self._str_helper(self.root, values)
    #     return "TREE pre-order { " + ", ".join(values) + " }"

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def rec_add(self, parent, new_node):

        if parent.value <= new_node.value and parent.right is None:
            parent.right = new_node
            return

        if parent.value > new_node.value and parent.left is None:
            parent.left = new_node
            return

        if parent.value > new_node.value:
            self.rec_add(parent.left, new_node)

        if parent.value <= new_node.value:
            self.rec_add(parent.right, new_node)

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """
        new_node = TreeNode(value)
        parent = self.root

        if self.root == None:
            self.root = new_node
            return

        if self.root != None:
            self.rec_add(parent, new_node)


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

    def helper_get_target_parent(self, node, target_node_value):
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
            return self.helper_get_target_parent(node.right, target_node_value)
        if target_node_value < node.value:
            return self.helper_get_target_parent(node.left, target_node_value)

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
            return True

        if self.root.left is None and self.root.right is not None:  # if 1 child
            self.root = self.root.right
            return True

        # ----------------- 2 children ----------------- #

        if self.root.left is not None and self.root.right is not None:
            successor_node = self.helper_get_successor_node(0, self.root.right, self.root)
            successor_node_parent = self.helper_get_parent_of_successor_node(self.root, successor_node.value, self.root)

            # ----------------- 2 sub-cases ----------------- #

            if successor_node is not self.root.right:
                successor_node.left = self.root.left
                successor_node_parent.left = successor_node.right  # replaces successor node with successor node's right child (there won't be a left child ever)
                successor_node.right = self.root.right
                self.root = successor_node
                return True

            if successor_node is self.root.right:
                successor_node.left = self.root.left
                self.root = successor_node
                return True

    def remove(self, value) -> bool:
        """
        Remove specified node from tree
        """

        if not self.contains(value):
            return False

        if self.root is None:
            return False

        if value == self.root.value:
            self.remove_first()
            return True

        target = self.get_target(value, self.root, 0)
        target_parent = self.helper_get_target_parent(self.root, target.value)

        if target.right is None and target.left is None:
            if target.value < target_parent.value:
                target_parent.left = None
            if target.value > target_parent.value:
                target_parent.right = None
            return True

        if target.value > target_parent.value and target.right is None:  # if 1 child
            target_parent.right = target.left
            return True

        if target.value > target_parent.value and target.left is None:
            target_parent.right = target.right
            return True

        if target.value < target_parent.value and target.left is None:
            target_parent.left = target.right
            return True
        if target.value < target_parent.value and target.right is None:
            target_parent.left = target.left
            return True

        if target.right is not None and target.left is not None:  # if 2 children
            successor_node = self.helper_get_successor_node(0, target.right, self.root)
            successor_node_parent = self.helper_get_parent_of_successor_node(self.root, successor_node.value, target)

            if successor_node is not target.right:
                successor_node.left = target.left
                successor_node_parent.left = successor_node.right  # replaces successor node with successor node's right child (there won't be a left child ever)
                successor_node.right = target.right
                if target_parent.value > target.value:
                    target_parent.left = successor_node
                    return True
                if target_parent.value <= target.value:
                    target_parent.right = successor_node
                    return True
            if successor_node is target.right:
                successor_node.left = target.left

                if target is target_parent.left:
                    target_parent.left = successor_node
                    return True

                if target is target_parent.right:
                    target_parent.right = successor_node
                    return True

    def pre_order_traversal(self) -> Queue:
        """
        Traverse tree, pre-order
        """
        queue1 = Queue()

        if self.root is None:
            return queue1
        self.helper_pre_order_traversal(queue1, self.root)
        return queue1

    def helper_pre_order_traversal(self, queue1, node):
        queue1.enqueue(node.value)

        if node.left is not None:  # we must go from left to right in pre-order traversal
            self.helper_pre_order_traversal(queue1, node.left)
            #  after last frame popped from call stack on left side, we check the right side by moving to line below
        if node.right is not None:
            self.helper_pre_order_traversal(queue1, node.right)

    def in_order_traversal(self) -> Queue:
        """
        Traverse, in order
        """
        queue = Queue()
        if self.root is None:
            return queue
        self.helper_in_order_traversal(queue, self.root)
        return queue

    def helper_in_order_traversal(self, queue, node):
        if node.left is not None:
            self.helper_in_order_traversal(queue, node.left)
        queue.enqueue(node.value)
        if node.right is not None:
            self.helper_in_order_traversal(queue, node.right)

    def post_order_traversal(self) -> Queue:
        """
        Traverse, post order
        """
        queue = Queue()
        if self.root is None:
            return queue

        self.helper_post_order_traversal(queue, self.root)
        return queue

    def helper_post_order_traversal(self, queue, node):
        if node.left is not None:
            self.helper_post_order_traversal(queue, node.left)

        if node.right is not None:
            self.helper_post_order_traversal(queue, node.right)

        queue.enqueue(node.value)

    def by_level_traversal(self) -> Queue:
        """
        Traverse horizontally, breadth first search (BFS)
        """
        g = Queue()
        h = Queue()
        g.enqueue(self.root)

        if self.root is None:
            return h

        while not g.is_empty():
            x = g.dequeue()
            if x is not None:
                h.enqueue(x)
                g.enqueue(x.left)
                g.enqueue(x.right)
        return h


    def is_full(self) -> bool:
        """
        Checks to see if a tree is full (every node has either 0 or 2 children)
        """
        if self.root is None:
            return True
        if self.height == 0 and self.root is not None:
            return True

        return self.rec_is_full(self.root)

    def rec_is_full(self, node):
        """ recursive helper, is_full"""
        if node.left is None and node.right is None:
            return True
        if node.left is None and node.right is not None:
            return False
        if node.right is None and node.left is not None:
            return False

        if node.left is not None and node.right is not None:
            g = self.rec_is_full(node.left)
            h = self.rec_is_full(node.right)
            if g is True and h is True:
                return True
            else:
                return False


    def is_complete(self) -> bool:
        """BFS search to determine whether node is complete or not (nodes all tend to left)"""

        # edge cases
        if self.root is None:
            return True
        if self.root.left is None and self.root.right is None:
            return True
        if self.size() % 2 == 1 and not self.is_full():
            return False
        if self.is_perfect():
            return True
        bfs_queue = Queue()
        bfs_queue.enqueue(self.root)
        incomplete = False  # boolean
        while bfs_queue.is_empty() is False:
            node_being_checked = bfs_queue.dequeue()
            if node_being_checked is not None:  # use a queue to perform level order binary tree traversal (bfs search)
                bfs_queue.enqueue(node_being_checked.left)
                bfs_queue.enqueue(node_being_checked.right)
            if incomplete is True:
                if node_being_checked is not None:
                    if node_being_checked.left is not None or node_being_checked.right is not None:
                        return False
            if incomplete is False and node_being_checked is not None:
                if node_being_checked.left is None or node_being_checked.right is None:  # determine whether the level we are on has been 'filled'
                    if node_being_checked.left is None and node_being_checked.right is not None:  # determine whether the single child node is leftmost or not
                        return False
                    incomplete = True  # set 'flag'
            if self.is_perfect():
                return True

        else:
            return True

        # first attempt
        # if self.root.left is not None and self.root.right is None and self.size() == 2:
        #     return True
        # if self.is_perfect():
        #     return True
        # z = False
        # g = Queue()
        # h = Queue()
        # g.enqueue(self.root)
        # while not g.is_empty():
        #     x = g.dequeue()
        #
        #     if x is not None:
        #         h.enqueue(x)
        #         g.enqueue(x.left)
        #         g.enqueue(x.right)
        #     if x is not None:
        #         r = self.helper_get_target_parent(self.root, x.value)
        #         if r.left is None and r.right is not None:
        #             return False
        #         if r.left is not None and x.left is not None and r.right is None:
        #             return False

        # return True

    def is_perfect(self) -> bool:
        """
        Determines whether tree is perfect (fully balanced, 2 children each except for leaves)
        """

        g = self.size()
        h = self.height()

        if self.root is None:
            return True

        if self.root.right is None and self.root.left is None:
            return True

        if h != 0 or None:
            correct_size = 2**(h+1) - 1
            # print(correct_size)
            if g == correct_size:
                return True
            if g!= correct_size:
                return False
        else:
            return False


    def size(self) -> int:
        """
        Finds size of the tree
        Dequeue each element from returned queue and add 1 to counter until queue is empty
        """
        # stack = Stack()

        counter = 0
        returned_queue = self.post_order_traversal()
        while not returned_queue.is_empty():
            returned_queue.dequeue()
            counter = counter + 1
            # print(counter)
        return counter

    #
    def rec_height(self, node):

        if node is None:
            return 0

        right_height = self.rec_height(node.right)
        left_height = self.rec_height(node.left)
        max_of_two_heights = max(left_height, right_height)
        return max_of_two_heights + 1


    def height(self) -> int:
        """
        Finds the height of the tree recursively by comparing left height to right height for each node.
        Recursively checks each node. Removes 1 to account for the fact that root node doesn't count as a level.
        """
        return self.rec_height(self.root) - 1

    def rec_count_leaves(self, node):
        if self.root is None:
            return 0
        if node.right is not None and node.left is None:  # if there is no node on the left, call rec function on right node
            return self.rec_count_leaves(node.right)
        if node.left is not None and node.right is None:  # if there is no node on the right, call rec function on the left node
            return self.rec_count_leaves(node.left)
        if node.right is None and node.left is None:  # if there is no node on either side, return 1 ('count' that node as a leaf node)
            return 1
        if node.right is not None and node.left is not None:  # if there are nodes on either side, check left, and then check right -- view the node with 2 children as the 'root'
            g = self.rec_count_leaves(node.left)
            h = self.rec_count_leaves(node.right)
            return g + h  # as we recurse out we eventually check every single node

    def count_leaves(self) -> int:
        """
        Count the number of leaves in a tree
        """
        return self.rec_count_leaves(self.root)

    def count_unique(self) -> int:
        """
        Count unique nodes in a tree
        """
        counter = 0
        size = self.size()
        previous_value = None
        returned_queue = self.in_order_traversal()
        for i in range(size):
            current_value = returned_queue.dequeue()
            if current_value == previous_value:  # use two pointers on a sorted list to calculate uniques
                counter += 1
            previous_value = current_value
        uniques = size - counter
        # print(uniques)
        return uniques

# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
#
#    """ add() example #1 """
#     # print("\nPDF - method add() example 1")
#     # print("----------------------------")
#     #
# tree = BST()
# print(tree)
# tree.add(10)
# tree.add(15)
# tree.add(5)
# print(tree)
# tree.add(15)
# tree.add(15)
# print(tree)
# tree.add(5)
# print(tree)
    #
    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # # print(tree.height())
    # print(tree.count_leaves())

    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))
    #
    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))
    #
    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)
    #
    # tree = BST([-4, -7, -5, 4, -2, -4, -2, -2, 6])
    # print(tree.remove(-2))
    # print(tree)
    #
    tree = BST([21, 9, 3, 0, 6, 15, 12, 18, 27, 24, 30, 33])
    print(tree.remove(21))
    print(tree)
    #
    # """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))
    # # #
    # """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.count_leaves())
    # print(tree.remove(20))
    # print(tree)
    # #
    # """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree.remove(20))
    # print(tree)
    #
    # # """gradescope remove example"""
    # # tree = BST(["PY", "O", "I", "AZ", "A", "BP", "AZ", "X", "XC" ])
    # # print(tree.remove("AZ"))
    # # print(tree)
    #
    # """gradescope remove example"""
    # tree = BST(["GU", "GD", "J", "H", "GU", "Z", "J", "ZO"])
    # print(tree.remove("J"))
    # print(tree)
    #
    # """gradescope remove example"""
    # tree = BST([0, -6, -7, -8, -3, -6, 8 ])
    # print(tree.remove(-6))
    # print(tree)

    # """ """comment out the following lines
    #  if you have not yet implemented traversal methods
    #  print(tree.pre_order_traversal())
    #  print(tree.in_order_traversal())
    #  print(tree.post_order_traversal())
    #  print(tree.by_level_traversal())
    #
    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([4034, -8626, -8783, -9342, -9445, -9015, -5996, -7286, -7492, -7519, -7901, -8494, -8522, -8126, -7891, -7110, -5998, -6511, -6760, -6819, -6738, -6029, -5981, -4714, -5040, -5915, -5014, 4627, 4080, 4141, 4533, 4435, 7147, 5031, 4850, 4774, 5783, 5750, 5209, 5550, 6592, 6313, 6017, 6401, 6492, 6802, 6709, 7603, 7546, 7169, 7536, 7788, 7806, 8514, 9985, 9744, 9357 ])
    # print(tree.remove_first())
    # print(tree)
    # # # #
    # # # # # #
    # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # #
    # tree = BST([10, 20, 5, 15, 17, 7])
    # #
    # print(tree.remove_first())
    # print(tree)
    # # # #
    # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # # #
    # """ remove_first() example 4 """
    # print("\nPDF - method remove_first() example 4")
    # print("-------------------------------------")
    # tree = BST([-7, 0, -4, -3, -4, -2, 6, 6])
    # print(tree.remove_first())
    # print(tree)
    #
    # """ remove_first() example 5 """
    # print("\nPDF - method remove_first() example 4")
    # print("-------------------------------------")
    # tree = BST([-4, -7, -5, 4, -2, -4, -2, -2, 6])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 6 """
    # print("\nPDF - method remove_first() example 4")
    # print("-------------------------------------")
    # tree = BST([-4, -7, -5, 4, -2, -4, -2, -2, 6])
    # print(tree.remove_first())
    # print(tree)

    # tree = BST([1,1,1])
    # z = tree.count_unique()

    # print(tree)
    # print(tree.count_leaves())
    # print(tree.is_perfect())
    # print(tree.is_full())
    # print(tree.is_complete())
    #
    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    # #
    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')
