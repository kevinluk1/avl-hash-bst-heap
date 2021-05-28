# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        self.heap.append(node)
        child_index = self.heap.length() - 1
        parent_index = (child_index - 1) // 2

        self.rec_add(parent_index, child_index)

    def rec_add(self, parent_index, child_index):
        if parent_index < 0:
            return
        if self.heap[child_index] > self.heap[parent_index]:
            return
        if self.heap[child_index] < self.heap[parent_index]:
            self.heap.swap(child_index, parent_index)
            child_index = parent_index
            parent_index = (child_index - 1) // 2
            self.rec_add(parent_index, child_index)

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException

        return self.heap[0]

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """


        if self.is_empty():
            raise MinHeapException
        last_index = self.heap.length()-1
        self.heap.swap(0, last_index)
        minimum = self.heap.pop()



        left_child_index = 1
        right_child_index = 2

        return self.rec_remove_min(0, left_child_index, right_child_index, minimum)

    def rec_remove_min(self, parent_index, left_child_index, right_child_index, minimum):
        if self.heap.length() == 1:
            return minimum

        if self.heap.length() == 2:
            self.heap.swap(0,1)
            return minimum

        if left_child_index > self.heap.length()-1 and right_child_index > self.heap.length()-1:
            return minimum

        if left_child_index > self.heap.length()-1:  # if one element is out of bonds and the other is not
            smallest_child_index = right_child_index
        else:
            smallest_child_index = left_child_index

        if left_child_index <= self.heap.length()-1 and right_child_index <= self.heap.length()-1:
            if self.heap[right_child_index] < self.heap[left_child_index]:
                smallest_child_index = right_child_index
            if self.heap[left_child_index] < self.heap[right_child_index]:
                smallest_child_index = left_child_index
            if self.heap[left_child_index] == self.heap[right_child_index]:
                smallest_child_index = left_child_index

        if self.heap[parent_index] < self.heap[smallest_child_index]:
            return minimum

        if self.heap[parent_index] > self.heap[smallest_child_index]:
            self.heap.swap(parent_index, smallest_child_index)
            parent_index = smallest_child_index
            left_child_index = (2 * parent_index) +1
            right_child_index = (2 * parent_index) +2
            return self.rec_remove_min(parent_index, left_child_index, right_child_index, minimum)







    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        pass


# BASIC TESTING
if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    #
    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())
    #

    h = MinHeap([686, 705, 689, 706, 718, 698, 704, 720, 723, 802, 765, 699, 792, 715, 913, 721, 782, 815, 847, 896, 807, 892, 837, 960, 807, 808, 930, 851, 801, 970, 933, 754, 764, 909, 861, 950, 909, 869, 899, 935, 931, 860, 873, 904, 991, 910, 924, 972, 975, 862, 968])



    print(h.remove_min())
    print("HEAP [689, 705, 698, 706, 718, 699, 704, 720, 723, 802, 765, 807, 792, 715, 913, 721, 782, 815, 847, 896, 807, 892, 837, 960, 862, 808, 930, 851, 801, 970, 933, 754, 764, 909, 861, 950, 909, 869, 899, 935, 931, 860, 873, 904, 991, 910, 924, 972, 975, 968]")
    print(h.__str__())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    #
    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
