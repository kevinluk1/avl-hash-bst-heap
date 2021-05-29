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

    da = DynamicArray([354, 83, 273, 541, 287, -686, -448, -502, -662, -665, -343, -894, 260, 842, -288, -84, 596, 536, -331, 103, 878, -413, 834, 284, 746, -397, -679, -74, -512, 239, -956, 407, 209, 515, 358, -201, -673, 501, -446, 983, 98, -392, -798, 648, -681, -947, -12, 855, 671, -832, -793, -309, 826, 440, 711, 153, -132, -429, 276, -872, -250, -986, -974, -514, -533, 244, 169, -932, 199, 916, 224, 317, 958, -469, -233, -395, 4, -759, 709, -57, -974, -883, 975, -246, -830, 782, 773, -449, 711, 750, -827, -909, 461, 752, -802, 991, 968, 64, 271, 634, -409, 618, 115, -458, -778, -689, 777, -42, -514, -531, -375, 599, 61, 45, -766, -61, -640, 759, -228, 3, -699, 618, -708, 12, 915, 285, -815, 242, 794, -906, -124, 437, 604, 478, 559, -748, -269, 621, 783, 136, 106, 217, -400, 615, 280, 315, 741, -631, -212, 720, -133, 427, 276, -290, -698, 525, -544, 314, 506, 684, -611, 475, 655, -462, 337, -564, 923, 199, 418, -583, 161, 609, 559, -917, -441, -33, 94, -190, -622, -935, 803, -912, 929, -910, -860, 794, 802, -69, 936, -864, -204, -332, 296, -308, -260, 454, 894, 484, 922, 611, -963, 793, -885, -769, 785, -112, -71, -820, 259, -180, 204, 366, 579, 448, 137, -110, -850, -64, -5, -355, -326, -511, 716, -671, -283, -592, 449, 653, 293, 316, 901, 978, -265, -373, -31, -120, 772, 165, 249, 744, -187, -330, 253, 395, -620, 492, 36, -312, -114, 9, 108, 892, -866, 643, -154, -538, 609, 76, 684, -842, 424, -533, 950, 402, -71, -399, -242, 404, -79, -219, 374, -467, -397, 421, -91, -810, 712, -798, 249, -771, -890, 720, 154, -807, -492, 237, -114, -5, 74, -236, 342, 474, 524, -608, 163, -227, -486, -515, 316, -844, -245, 776, -969, -600, 717, 441, 661, -861, 658, -293, -648, 681, -352, 997, 750, 383, 127, -304, 652, -812, -530, -41, -356, 857, 106, 479, 426, -151, -9, -908, 114, 48, 481, 304, 686, 267, -73, 709, 386, -957, -495, -476, -66, -889, -153, -717, 236, -6, -764, -977, 111, 698, 709, -640, -963, -938, -597, 533, -3, 699, -309, -478, -535, -291, 414, 99, 881, -83, 663, -600, -972, 359, 139, -330, 548, 785, -958, 108, -324, -773, 237, -149, -694, -993, 325, -704, -125, -321, 121, 923, -380, 735, 183, -471, 815, 245, -946, 799, 746, 389, -985, 8, 903, 642, -458, -16, 376, 350, 944, -349, 820, 142, -574, 650, -519, 919, -457, -267, 833, 279, 616, 326, -932, -261, -490, -963, -447, 451, -718, 931, 785, 368, 350, 672, -717, -924, -129, 565, 920, 478, 653, 883, 457, 980, 410, 101, 440, -539, 587, 911, -212, 610, 321, -343, -349, 202, 895, 688, 20, 754, -790, 16, -698, 647, -500, -124, -366, -453, -88, -711, 807, -661, -930, -998, 363, 479, 501, -193, -474, -383, 740, 922, -554, -126, -407, -30, 666, 767, -744, -795, 204, 581, -564, 725, 224, -707, -532, 956, -529, -110, 381, 634, -89, -28, 445, -473, 63, -176, -101, -632, -471, 425, -253, 111, -624, 169, 305, 111, 917, 94, 803, -494, -721, 717, 57, -529, 217, 304, 178, 471, 893, 381, 649, 566, -76, 567, 198, -534, -940, -205, -961, -812, 396, -159, -603, -740, -953, 471, 616, -844, -840, -993, 325, -746, 762, 463, -406, -978, 406, -846, -657, 663, -686, 880, 822, 994, -462, 201, -913, -183, 753, 772, -63, 914, -148, 63, -105, -808, 842, 328, 808, 52, -324, -497, 132, -117, 165, -747, -859, 808, 755, -61, -605, -833, 583, 48, -208, -120, 13, -346, 4, 263, 760, 352, 229, -314, -538, -125, 334, 186, -50, 263, 111, -265, 534, -437, 247, 773, -537, 790, 669, 235, -723, 846, -830, -148, 427, -103, 378, -595, -207, 713, 686, 977, 551, 218, -696, 604, -402, 754, -488, -98, 116, 428, 994, 512, 185, 706, 51, 918, 789, 486, -794, 938, 1, 986, -484, -803, -512, 994, 772, -860, -172, -294, 243, -573, 384, 214, -966, -894, 105, 464, -375, 808, -316, 713, 555, 226, -194, 560, -807, 314, -112, 838, -161, 396, 320, -622, 577, 338, -503, -729, -513, -452, 453, 848, -661, -79, 712, -306, 874, -715, -763, -379, -388, 443, 922, 555, -607, 393, 883, 444, -674, 386, -76, -385, -377, 255, 525, -795, -982, -268, 697, -209, 63, 328, 488, -512, -689, -526, 235, 523, -454, -493, 645, -660, -5, 975, -955])
    # print(locals())
    h = MinHeap(['zebra', 'apple'])
    # print(h)
    h.build_heap(da)
    print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)