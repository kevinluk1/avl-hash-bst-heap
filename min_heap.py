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

        da_copy = DynamicArray()
        for i in range(da.length()):
            da_copy.append(da[i])


        first_non_leaf = ((da_copy.length() - 1) // 2) - 1
        parent_index = first_non_leaf
        left_child_index = (2 * parent_index) + 1
        right_child_index = (2 * parent_index) + 2
        counter = parent_index

        g = self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)
        self.heap = g

    def rec_build_heap(self, counter, parent_index, left_child_index, right_child_index, da_copy):
        if counter < 0:
            return da_copy

        if left_child_index > self.heap.length() - 1 >= right_child_index:  # if one element is out of bonds and the other is not
            smallest_child_index = right_child_index
        if right_child_index > self.heap.length() - 1 >= left_child_index:
            smallest_child_index = left_child_index

        if left_child_index > da_copy.length() - 1 and right_child_index > da_copy.length() - 1:
            counter = counter - 1
            parent_index = counter
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)

        if left_child_index <= da_copy.length() - 1 and right_child_index <= da_copy.length() - 1:
            if da_copy[right_child_index] < da_copy[left_child_index]:
                smallest_child_index = right_child_index
            if da_copy[left_child_index] <= da_copy[right_child_index]:
                smallest_child_index = left_child_index

        if da_copy[parent_index] <= da_copy[smallest_child_index]:
            counter = counter - 1
            parent_index = counter
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)

        if da_copy[parent_index] > da_copy[smallest_child_index]:
            da_copy.swap(parent_index, smallest_child_index)
            parent_index = smallest_child_index
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)


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
    da = DynamicArray([-100, -100, -100, -100, -100, -99, -99, -99, -96, -100, -99, -99, -90, -95, -98, -97, -98, -95, -93, -88, -99, -97, -91, -98, -99, -86, -89, -89, -85, -96, -69, -93, -95, -95, -91, -94, -95, -87, -90, -59, -79, -94, -94, -82, -84, -79, -88, -92, -95, -75, -96, -85, -71, -88, -83, -83, -86, -79, -78, -89, -85, -63, -65, -86, -75, -95, -82, -73, -90, -79, -76, -92, -91, -94, -79, -74, -79, -71, -84, -39, -54, -65, -78, -69, -81, -66, -80, -74, -78, -52, -56, -54, -73, -75, -87, -80, -88, -87, -93, -70, -60, -72, -92, -79, -83, -31, -48, -75, -85, -64, -76, -78, -78, -38, -65, -78, -60, -36, -22, -61, -83, -61, -74, -46, -19, 0, -62, -41, -54, -7, -62, -84, -94, -74, -64, -30, -63, -65, -37, -28, -44, -18, -75, -48, -67, -86, -59, -76, -69, -36, -48, -42, -40, -71, -51, -5, -64, -73, -47, -33, -21, -46, -41, -41, -33, -21, -36, -25, -53, -72, -72, -49, -60, -57, -76, -69, -49, -52, -58, -28, -45, -39, -51, -38, -50, -64, -64, -32, -65, -79, -79, -78, -62, -56, -5, -83, -83, -74, -63, -50, -69, -59, -37, -19, -30, -70, -84, -2, -54, -59, -69, -24, -27, -36, -36, -5, -15, -76, -59, -62, 43, -4, -52, -54, -77, -26, -49, -5, -13, -1, -16, -74, -13, -56, -46, 30, -21, -2, -11, -19, -51, -24, 42, 18, 30, 8, 56, 6, 49, 13, 3, 20, 11, -56, -42, -39, -41, 26, -42, -5, 21, -41, -61, -60, -20, -55, -79, 22, -49, -28, 8, 3, 47, -57, -59, -10, -41, -26, -34, -11, 35, -24, -38, 51, -10, -15, -60, -6, -41, -29, -41, 19, -29, -27, -30, -19, 37, -25, 1, -7, -33, -20, -26, -32, 3, -25, -23, 12, -35, -31, -40, 28, 10, 31, -20, 18, -23, -24, -9, -22, -9, 6, 14, -6, -44, 29, -26, -8, -19, 8, -4, 40, -9, 64, -31, -21, 21, -11, 22, -22, -52, -5, -60, -36, -44, 0, -42, -47, -14, -63, -64, -42, -51, -21, -47, 29, -44, -27, -37, -12, 10, 69, 6, -37, -35, 15, -44, 32, -38, -13, -17, 64, 2, -12, -41, -27, -19, 4, 8, 23, -71, -26, -50, 67, -23, -21, -52, -9, -41, 47, -1, 11, 35, -40, -8, -27, 15, 12, -22, 22, -41, -22, -49, -28, -48, -32, -3, 15, -6, -21, -20, -1, -38, -79, -12, 45, 12, 32, -39, -45, -40, -12, -9, -12, 11, 19, -2, 27, -10, -35, -4, 7, 3, 5, -13, -76, -56, -22, -50, -10, -43, 44, 81, 41, 29, 24, -8, -4, -14, 68, -3, 94, 84, -28, 83, 40, 85, 47, 93, 97, 46, 54, 39, 2, -30, 60, -11, 40, 6, 85, 79, 65, 62, 62, -16, 88, 81, 40, 71, 80, 79, 97, 91, 72, -8, 52, 93, 18, 40, 77, 97, 78, 39, 97, 69, 80, 13, 65, 80, 60, 34, 10, 89, 52, 61, 19, 12, 76, 61, 76, 40, 80, 18, 44, -12, 38, 67, 18, -11, 3, -1, 62, 97, -27, 3, 90, 15, 44, -33, 38, 88, 57, -20, 78, 64, 43, 32, -33, 78, 56, -2, 78, 41, 88, 18, 87, 86, 60, -52, 70, -16, 45, 9, 82, 4, 39, 64, 81, 37, 61, 44, 94, 77, 47, -14, 58, 59, 76, 82, 6, 45, 92, 70, 70, 47, 47, 79, 57, -16, 33, 63, -3, -33, 20, 52, -1, 16, 25, 1, 4, -1, 63, -9, 43, 62, 59, 16, 68, 64, 26, 49, 96, 39, -8, -18, 53, -18, 88, -19, 15, 31, 30, 27, 74, 91, 82, 50, 52, -15, 32, 22, -21, 24, 73, 34, 53, 15, 99, 41, 65, 62, 73, 58, 81, 33, 83, 11, 9, 25, 78, 24, 54, 34, 60, 7, 65, 76, 86, 36, 73, -44, 50, 88, 46, 12, 82, 48, 75, 54, 95, 8, 76, 3, 83, 64, 51, 48, 81, 65, 60, -6, 86, -11, 45, 34, 89, 87, 98, 43, 54, 1, 30, -33, 95, 82, 34, 13, 51, 29, 57, -25, 51, 59, 90, 34, 72, -15, 46, 81, 82, 13, -42, 66, 50, -1, 6, 0, 61, 27, -27, 53, 76, 75, 63, 39, 24, 73, 97, 78, 90, 92, 34, 30, 85, 75, 97, 23, 91, 43, 70, -9, 77, 72, 27, 16, 68, 47, 66, -16, 89, 58, 29, 31, 77, 72, 23, 89, 72, 14, 49, 46, 42, -4, 30, -15, 65, 44, 47, 12, 67, 84, 27, 24, 82, 21, 67, -29, 72, 85, -22, -22, 25, 3, 97, -26, 56, 52, 73, 31, 71, 70, 3, 73, 99, 73, 48, 38, 67, 52, 54, -4, 59, 38, 22, 92, 31, 32, 97, 96, 80, 96, 71, 15, 10, -15, 56, 25, 82, 59, 27, 21, 19, 2, 99, 34, 92, 35, 61, 14, -16, -10, -13, 96, 68, 4, 0, 88, -49, 29, -9, 55, 88, 94, 49, 45, 75, 81, 79, 35, 60, -5, -20, 3, 36, 53, 79, 17, 88, 52, 65, 21, 91, 26, 38, 9, 76, 63, -8, -8, -3, -26, 78, 72, 94, 75, 84, 77, 71, 53, 98, 51, 73, -12, 50, 4, 20, 14, 69, -3, 71, -2, 69, -12, 87, 84, 86, 91, 77, 71, 35, 89, 49, 74, 75, 9, 94, 31, 0, 71, 70])
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])

    h = MinHeap(['zebra', 'apple'])
    # print(h)
    h.build_heap(da)
    print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)