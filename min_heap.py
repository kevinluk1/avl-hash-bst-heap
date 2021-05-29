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


        first_non_leaf = ((da_copy.length()) // 2) - 1
        parent_index = first_non_leaf
        left_child_index = (2 * parent_index) + 1
        right_child_index = (2 * parent_index) + 2
        counter = parent_index

        g = self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)
        self.heap = g

    def rec_build_heap(self, counter, parent_index, left_child_index, right_child_index, da_copy):
        # if da_copy.length() % 2 == 0:
        #     if counter > (da_copy.length()-1)//2:
        #         return da_copy

        # if da_copy.length() % 2 !=0:
        if counter < 0:
            return da_copy

        if left_child_index > da_copy.length() - 1 and right_child_index <= da_copy.length() - 1:  # left element out of bounds, right is not
            smallest_child_index = right_child_index
        if right_child_index > da_copy.length() - 1 and left_child_index <= da_copy.length() -1: # right element out of bounds, left is not
            smallest_child_index = left_child_index

        if left_child_index > da_copy.length() - 1 and right_child_index > da_copy.length() - 1:    #  both elements out of range

            # if da_copy.length() % 2 != 0:
            counter = counter - 1
            # else:
            #     counter = counter +1
            parent_index = counter
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)

        if left_child_index <= da_copy.length() - 1 and right_child_index <= da_copy.length() - 1:  # both elements in range
            if da_copy[right_child_index] < da_copy[left_child_index]:
                smallest_child_index = right_child_index
            if da_copy[left_child_index] <= da_copy[right_child_index]:
                smallest_child_index = left_child_index

        if da_copy[parent_index] <= da_copy[smallest_child_index]:
            # if da_copy.length() % 2 != 0:
            counter = counter - 1
            # else:
            #     counter = counter + 1
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
    da = DynamicArray([-80, -288, -613, -114, -744, -277, 594, -482, -353, 159, -859, 240, -228, 461, 620, 887, 662, -328, -714, 201, 479, 991, -970, 892, -832, -432, -968, 621, 80, 415, 229, -318, -155, -969, 519, 979, 998, -15, -323, 84, 63, 391, -633, -384, -820, -598, 209, 506, -560, -318, 178, -434, 344, -842, -754, 532, -651, -686, 734, 424, -248, -633, -353, 172, -598, -182, -141, -269, -925, -45, 827, -399, 775, 42, -949, -466, -53, -275, -831, 468, -274, -877, -270, -65, -182, -399, -929, -241, -111, -464, 712, 56, 888, 634, -989, -799, 426, -499, 416, -252, -213, -463, 833, 996, 347, 649, 8, -357, 812, -872, 152, -933, -699, 62, -629, -348, -589, -538, 799, 771, -219, -294, 419, -29, -368, 363, 81, 848, 477, -786, 137, 131, 885, -185, -499, -600, -643, -943, 641, -95, 582, -945, -747, -135, -454, 81, 56, -941, -58, 316, -335, -512, 138, 919, -171, -246, -113, 548, -376, 469, 662, 285, -13, 651, -31, -87, -189, 15, 846, 862, 858, 478, -720, 18, 926, 514, -71, 957, 555, 918, 735, 320, 79, -144, 467, 423, 625, 177, -300, 121, -841, -543, -796, 225, -540, 790, 3, 27, 345, 555, -603, -272, -933, 867, -878, 384, 476, -325, -68, -895, -131, -639, -917, 869, -469, 555, -811, 603, 163, 304, -136, -816, 377, 686, -239, -920, 823, -153, -415, -67, 55, -856, 96, 95, 893, 151, 538, -356, -260, -332, -799, -872, -805, -128, -690, -46, 530, 115, -215, -586, -438, -158, 251, -969, -58, 849, 469, 423, 650, 549, 652, -711, 592, 27, -441, 923, 455, -277, -782, -256, -532, 940, -671, 959, 945, 694, 675, -676, -52, -227, -56, -79, -140, -980, -550, -385, -992, -734, -581, 708, -192, -555, 320, -547, 824, 492, -726, 112, 18, 20, 788, -947, 955, 360, 792, 354, 855, -204, -205, 5, 644, 694, 81, 704, 358, 265, 421, 550, 960, -319, 342, 919, 296, -816, -955, -917, -322, -588, 40, 929, -841, -158, 572, -977, 432, 227, 148, 618, -332, -7, 400, -403, -62, 3, -938, -484, -361, 951, -443, 179, 207, 977, 870, 886, 633, 357, 98, 986, 444, 819, -628, -418, 632, 447, -469, 221, 610, 573, -284, -576, -814, 138, -436, 280, 802, -548, 101, -830, 95, 935, 305, 681, -974, 485, -730, -986, -901, -972, -599, 249, -724, 670, -34, 32, -915, -65, 11, 413, 140, -198, 117, 246, -833, -382, 909, 131, -962, 362, 256, -575, -282, 71, -183, 823, 931, 194, -6, -32, -357, 829, 953, 689, -465, -490, 2, -938, 912, 983, 107, 491, -435, 12, -776, -970, -801, -322, -333, -408, 391, 580, 786, 113, 71, 818, -308, 877, -676, -494, 167, -938, 608, -968, -645, 351, -514, -151, 51, 694, -467, -315, -378, 880, -863, 680, -127, -228, 631, 187, -106, 462])

    # da = DynamicArray([32,12,8,2])
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # da = DynamicArray([32,12,2,8])

    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)