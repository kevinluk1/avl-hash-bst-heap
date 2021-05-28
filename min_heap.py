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
        minimum = self.get_min()
        self.heap.swap(0, last_index)
        self.heap.pop()


        left_child_index = 1
        right_child_index = 2

        return self.rec_remove_min(0, left_child_index, right_child_index, minimum)

    def rec_remove_min(self, parent_index, left_child_index, right_child_index, minimum):

        # if self.heap.length() == 1:
        #     return minimum
        #
        # if self.heap.length() == 2:
        #     self.heap.swap(0,1)
        #     return minimum

        if left_child_index > self.heap.length()-1 and right_child_index > self.heap.length()-1:
            return minimum

        if left_child_index > self.heap.length()-1 >= right_child_index:  # if one element is out of bonds and the other is not
            smallest_child_index = right_child_index
        if right_child_index > self.heap.length()-1 >= left_child_index:
            smallest_child_index = left_child_index

        if left_child_index <= self.heap.length()-1 and right_child_index <= self.heap.length()-1:
            if self.heap[right_child_index] < self.heap[left_child_index]:
                smallest_child_index = right_child_index
            if self.heap[left_child_index] <= self.heap[right_child_index]:
                smallest_child_index = left_child_index
            # if self.heap[left_child_index] == self.heap[right_child_index]:
            #     smallest_child_index = left_child_index

        if self.heap[parent_index] < self.heap[smallest_child_index]:
            return minimum

        if self.heap[parent_index] > self.heap[smallest_child_index]:
            self.heap.swap(parent_index, smallest_child_index)
            parent_index = smallest_child_index
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_remove_min(parent_index, left_child_index, right_child_index, minimum)

        if self.heap[parent_index] == self.heap[smallest_child_index]:
            return minimum

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """

        first_non_leaf = ((da.length()-1)//2) - 1
        parent_index = first_non_leaf

        left_child_index = (2 * parent_index) + 1
        right_child_index = (2 * parent_index) + 2

        counter = parent_index
        returned_da = self.rec_build_heap(counter, parent_index, left_child_index, right_child_index)
        da_to_be_heap = DynamicArray()
        for i in range(returned_da.length()):  # de-reference returned DA, ed discussion
            da_to_be_heap.append(returned_da[i])
        self.heap = da_to_be_heap


    def rec_build_heap(self, counter, parent_index, left_child_index, right_child_index):

        if counter < 0:
            return da


        if left_child_index > da.length() - 1 and right_child_index > da.length() - 1:
            counter = counter - 1
            parent_index = counter
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index)

        if left_child_index <= da.length()-1 and right_child_index <= da.length()-1:
            if da[right_child_index] < da[left_child_index]:
                smallest_child_index = right_child_index
            if da[left_child_index] <= da[right_child_index]:
                smallest_child_index = left_child_index


        if da[parent_index] < da[smallest_child_index]:
            counter = counter - 1
            parent_index = counter
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index)

        if da[parent_index] > da[smallest_child_index]:
            da.swap(parent_index, smallest_child_index)
            parent_index = smallest_child_index
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index)


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

    # h = MinHeap([-37, -37, -37, -36, -35, -35, -36, -36, -32, -34, -35, -32, -34, -36, -36, -36, -35, -28, -29, -28, -33, -20, -29, -32, -31, -11, -30, -29, -34, -16, -24, -35, -34, -34, -34, -22, -23, -27, -24, -16, -24, -30, -21, -14, -20, -28, -8, -30, -18, -6, -29, -10, -1, -29, -30, -24, -11, -23, -4, -14, -16, -21, -13, -28, -35, -7, -29, -15, -33, -8, -11, -15, -22, -16, -12, -26, -21, -15, -4, 12, -15, 4, 5, -24, -26, -6, 1, -7, -7, -19, -18, -20, -3, 14, 14, -23, 4, 1, -15, -1, -6, -23, -16, 14, 13, 0, 40, -23, -24, 5, -9, 47, 19, -9, 0, 5, -19, 14, 9, 5, 13, -9, 30, 44, -4, 3, 5, -12, -1, -26, -22, 59, -5, 9, -5, -13, 9, -17, -7, -6, 4, -3, -6, -2, -1, -17, -18, -16, -12, 30, -10, 9, -18, 5, 6, -3, -6, 1, 41, 32, 17, 12, -14, 4, 11, 7, 12, -17, 34, 7, 0, 4, -3, 58, 9, 31, -1, 2, 10, 21, 53, 30, 68, 10, 3, 8, 6, 31, 30, 34, 19, -18, -13, 43, 4, 61, 18, 2, -7, 59, 15, 4, -3, 10, 40, -9, 0, 74, 72, 48, 44, 52, 80, 50, 50, 39, -15, 18, 44, 30, 54, 10, 5, 51, 54, 72, 56, 48, 1, 14, 7, 12, 14, 60, 39, 18, 44, 68, 36, 64, 23, 18, 33, 14, 35, 35, 32, 48, 64, 22, 51, 4, 6, 30, 73, 6, -5, 45, 26, 17, 22, -15, -17, 69, 73, 36, 28, 47, 25, 16, 45, 23, 71, 27, 23, -6, 15, 75, -1, 33, 37, 13, 37, -2, 39, 14, 29, 23, 16, 48, 19, 54, -17, 26, 6, 44, 17, -1, -10, 51, 73, 10, 86, 38, 18, 0, 53, 47, 13, 55, 65, 90, 93, 97, 30, 26, 93, 88, 51, 74, 38, 78, 28, 60, 89, -6, 41, 31, 62, 21, 40, 34, 82, 42, 48, -14, 2, 65, 72, 75, 96, 57, 44, 88, 88, 40, 82, 84, 61, 80, 26, 55, 99, 57, 57, 34, 39, 34, 66, 60, 25, 89, 64, 37, 59, 76, 82, 35, 74, 99, 4, 70, 86, 50, 22, 98, 74, 75, 64, 73, 63, 50, 81, 95, 11, -2, 6, 86, 72, 19, 81, 92, 79, 99, 59, 7, 45, 68, 70, 79, 70, 22, 86, 19, 86, 52, 89, 90, 49, 73, 95, 53, 46, 54, 90, 98, 80, 86, 76, 86, 68, 90, 89, 94, 63, 92, 84, 82, 82, 99, 99, 66, 96, 24, 16, 36, 82, 67, 77, 62, 84, 97, 99, 46, 56, 43, 25, 98, 55, 60, 77, 81, 99, 80, 79, 56, 56, 18, 52, 99, 76, 10, 34, 33, 55, 30, 33, 85, 98, 85, 95, 38, 19, 51, 58, 81, 75, 65, 59, 82, 80, 35, 97, 38, 96, 50, 46, 71, 26, 60, 89, 91, 94, 50, 43, 64, 78, 82, 85, 34, 45, 58, 63, 19, 60, 25, 49, 72, 96, 83, 99, 90, 32, 56, 41, 68, 57, 61, 73, 72, 30, 76, 87, 89, 80, 38, 21, 94, 80, 85, 73, 43, 53, 44, 89, 51, 88, 38, 71, 80, 34, 95, 76, 86, 61, 83, 86, 53, 35, 39, 78, 73, 60, 58, 17])
    #
    #
    #
    # print(h.remove_min())
    # print(h.__str__())
    #
    #
    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
