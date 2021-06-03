# Course: CS261 - Data Structures
# Student Name: Kevin Luk
# Assignment: 5
# Description: min_heap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *
import sys

sys.setrecursionlimit(1500)


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
        last_index = self.heap.length() - 1
        minimum = self.get_min()
        self.heap.swap(0, last_index)
        self.heap.pop()

        left_child_index = 1
        right_child_index = 2

        return self.rec_remove_min(0, left_child_index, right_child_index, minimum)

    def rec_remove_min(self, parent_index, left_child_index, right_child_index, minimum):

        if left_child_index > self.heap.length() - 1 and right_child_index > self.heap.length() - 1:
            return minimum

        if left_child_index > self.heap.length() - 1 >= right_child_index:  # if one element is out of bonds and the other is not
            smallest_child_index = right_child_index
        if right_child_index > self.heap.length() - 1 >= left_child_index:
            smallest_child_index = left_child_index

        if left_child_index <= self.heap.length() - 1 and right_child_index <= self.heap.length() - 1:
            if self.heap[right_child_index] < self.heap[left_child_index]:
                smallest_child_index = right_child_index
            if self.heap[left_child_index] <= self.heap[right_child_index]:
                smallest_child_index = left_child_index

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
        if counter < 0:  # once we reach the leftmost element of the array, there's nothing left to sort.
            return da_copy

        if left_child_index > da_copy.length() - 1 and right_child_index <= da_copy.length() - 1:  # left child out of bounds, right is not
            smallest_child_index = right_child_index

        if right_child_index > da_copy.length() - 1 and left_child_index <= da_copy.length() - 1:  # right child out of bounds, left is not
            smallest_child_index = left_child_index

        if left_child_index > da_copy.length() - 1 and right_child_index > da_copy.length() - 1:  # both children out of bounds

            counter = counter - 1
            parent_index = counter  # check the node prior to the node just checked in the array and percolate if necessary
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)

        if left_child_index <= da_copy.length() - 1 and right_child_index <= da_copy.length() - 1:  # both children in bounds

            if da_copy[right_child_index] < da_copy[left_child_index]:
                smallest_child_index = right_child_index
            if da_copy[left_child_index] <= da_copy[right_child_index]:
                smallest_child_index = left_child_index

        if da_copy[parent_index] <= da_copy[smallest_child_index]:  # if parent is smaller than smallest child, DO NOT SWAP
            counter = counter - 1
            parent_index = counter
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)

        if da_copy[parent_index] > da_copy[smallest_child_index]:  # if parent is greater than smallest child, SWAP
            da_copy.swap(parent_index, smallest_child_index)
            parent_index = smallest_child_index
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2
            return self.rec_build_heap(counter, parent_index, left_child_index, right_child_index, da_copy)  # recursive call, will either continue to percolate parent node value downwards, OR will begin checking to see if value prior to node just checked is a heap



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

    # da = DynamicArray([354, 83, 273, 541, 287, -686, -448, -502, -662, -665, -343, -894, 260, 842, -288, -84, 596, 536, -331, 103, 878, -413, 834, 284, 746, -397, -679, -74, -512, 239, -956, 407, 209, 515, 358, -201, -673, 501, -446, 983, 98, -392, -798, 648, -681, -947, -12, 855, 671, -832, -793, -309, 826, 440, 711, 153, -132, -429, 276, -872, -250, -986, -974, -514, -533, 244, 169, -932, 199, 916, 224, 317, 958, -469, -233, -395, 4, -759, 709, -57, -974, -883, 975, -246, -830, 782, 773, -449, 711, 750, -827, -909, 461, 752, -802, 991, 968, 64, 271, 634, -409, 618, 115, -458, -778, -689, 777, -42, -514, -531, -375, 599, 61, 45, -766, -61, -640, 759, -228, 3, -699, 618, -708, 12, 915, 285, -815, 242, 794, -906, -124, 437, 604, 478, 559, -748, -269, 621, 783, 136, 106, 217, -400, 615, 280, 315, 741, -631, -212, 720, -133, 427, 276, -290, -698, 525, -544, 314, 506, 684, -611, 475, 655, -462, 337, -564, 923, 199, 418, -583, 161, 609, 559, -917, -441, -33, 94, -190, -622, -935, 803, -912, 929, -910, -860, 794, 802, -69, 936, -864, -204, -332, 296, -308, -260, 454, 894, 484, 922, 611, -963, 793, -885, -769, 785, -112, -71, -820, 259, -180, 204, 366, 579, 448, 137, -110, -850, -64, -5, -355, -326, -511, 716, -671, -283, -592, 449, 653, 293, 316, 901, 978, -265, -373, -31, -120, 772, 165, 249, 744, -187, -330, 253, 395, -620, 492, 36, -312, -114, 9, 108, 892, -866, 643, -154, -538, 609, 76, 684, -842, 424, -533, 950, 402, -71, -399, -242, 404, -79, -219, 374, -467, -397, 421, -91, -810, 712, -798, 249, -771, -890, 720, 154, -807, -492, 237, -114, -5, 74, -236, 342, 474, 524, -608, 163, -227, -486, -515, 316, -844, -245, 776, -969, -600, 717, 441, 661, -861, 658, -293, -648, 681, -352, 997, 750, 383, 127, -304, 652, -812, -530, -41, -356, 857, 106, 479, 426, -151, -9, -908, 114, 48, 481, 304, 686, 267, -73, 709, 386, -957, -495, -476, -66, -889, -153, -717, 236, -6, -764, -977, 111, 698, 709, -640, -963, -938, -597, 533, -3, 699, -309, -478, -535, -291, 414, 99, 881, -83, 663, -600, -972, 359, 139, -330, 548, 785, -958, 108, -324, -773, 237, -149, -694, -993, 325, -704, -125, -321, 121, 923, -380, 735, 183, -471, 815, 245, -946, 799, 746, 389, -985, 8, 903, 642, -458, -16, 376, 350, 944, -349, 820, 142, -574, 650, -519, 919, -457, -267, 833, 279, 616, 326, -932, -261, -490, -963, -447, 451, -718, 931, 785, 368, 350, 672, -717, -924, -129, 565, 920, 478, 653, 883, 457, 980, 410, 101, 440, -539, 587, 911, -212, 610, 321, -343, -349, 202, 895, 688, 20, 754, -790, 16, -698, 647, -500, -124, -366, -453, -88, -711, 807, -661, -930, -998, 363, 479, 501, -193, -474, -383, 740, 922, -554, -126, -407, -30, 666, 767, -744, -795, 204, 581, -564, 725, 224, -707, -532, 956, -529, -110, 381, 634, -89, -28, 445, -473, 63, -176, -101, -632, -471, 425, -253, 111, -624, 169, 305, 111, 917, 94, 803, -494, -721, 717, 57, -529, 217, 304, 178, 471, 893, 381, 649, 566, -76, 567, 198, -534, -940, -205, -961, -812, 396, -159, -603, -740, -953, 471, 616, -844, -840, -993, 325, -746, 762, 463, -406, -978, 406, -846, -657, 663, -686, 880, 822, 994, -462, 201, -913, -183, 753, 772, -63, 914, -148, 63, -105, -808, 842, 328, 808, 52, -324, -497, 132, -117, 165, -747, -859, 808, 755, -61, -605, -833, 583, 48, -208, -120, 13, -346, 4, 263, 760, 352, 229, -314, -538, -125, 334, 186, -50, 263, 111, -265, 534, -437, 247, 773, -537, 790, 669, 235, -723, 846, -830, -148, 427, -103, 378, -595, -207, 713, 686, 977, 551, 218, -696, 604, -402, 754, -488, -98, 116, 428, 994, 512, 185, 706, 51, 918, 789, 486, -794, 938, 1, 986, -484, -803, -512, 994, 772, -860, -172, -294, 243, -573, 384, 214, -966, -894, 105, 464, -375, 808, -316, 713, 555, 226, -194, 560, -807, 314, -112, 838, -161, 396, 320, -622, 577, 338, -503, -729, -513, -452, 453, 848, -661, -79, 712, -306, 874, -715, -763, -379, -388, 443, 922, 555, -607, 393, 883, 444, -674, 386, -76, -385, -377, 255, 525, -795, -982, -268, 697, -209, 63, 328, 488, -512, -689, -526, 235, 523, -454, -493, 645, -660, -5, 975, -955])
    da = DynamicArray(
        [425, 548, 599, -505, 961, 170, 346, 57, -393, 225, 131, -836, -5, -68, 739, 612, 110, -401, 395, -694, -331,
         -102, 532, -623, -739, -670, 570, -269, -255, -692, 873, -42, -609, -557, -967, 541, -67, -579, -235, 120,
         -977, -535, -104, 508, 650, -745, -701, -732, 378, 329, -768, -334, -133, 785, -545, -399, 88, 293, 144, 267,
         825, -240, 767, 798, -851, 414, -588, -305, -327, -744, -254, 47, 85, -781, -570, 777, 143, 173, 312, 920,
         -865, -752, -354, 426, 687, -218, -545, -16, 377, 884, 220, -631, -820, 822, 660, 664, 975, 201, -511, 40,
         -796, 223, -177, 197, 974, -583, -51, -110, 915, -152, -180, 334, 41, 404, -822, 762, -516, -864, -595, 608,
         -880, 473, 612, 725, 817, -114, -767, -647, 605, 615, 294, 936, 857, 545, 169, 202, 739, -582, -695, 69, -464,
         56, -732, 97, 512, 13, -221, 629, 817, -30, -560, 847, -574, 618, -135, -88, -84, -775, -1000, -141, 778, -952,
         -283, -334, 43, 243, -55, -929, -557, 450, 251, -775, -308, 736, -198, -654, 110, 684, -810, -190, -723, 766,
         -19, 616, 687, 952, 487, -102, -449, -867, 689, -39, -326, 938, 248, -674, 233, 629, -952, -372, 997, -714,
         737, 610, -940, 589, 626, -146, -228, 919, -751, 756, -999, -471, 940, -922, -961, 162, 596, 847, 308, -3,
         -129, 478, -564, 651, -998, -399, 832, 202, 499, -620, 511, 880, 799, -876, -726, 785, 227, -796, 930, 846,
         -356, 624, -536, 120, 859, -631, -996, 237, -496, 390, -734, -384, -803, -818, 550, 850, 981, 724, -936, 424,
         -651, -339, 800, -703, -180, -448, 290, 331, 41, -218, -462, -200, -560, -735, 238, 46, 713, 642, -553, 525,
         -166, -850, 774, -985, 523, -625, -558, -676, 586, 421, 814, 446, -978, -163, -870, 25, 997, -726, 459, 504,
         852, 227, -46, -560, 605, 215, 568, -39, -293, 936, 986, -280, -993, -255, 695, 577, 97, 821, 649, 304, -866,
         -298, -479, 583, 982, -560, -706, -88, 813, -1000, 794, -866, -12, 939, 620, 994, 758, -166, 105, 217, -298,
         -521, 858, 888, 459, 585, 271, -959, 178, 503, 412, 316, -829, -327, 567, 391, -497, 920, 659, -498, 26, 57,
         -20, -854, 458, -694, 778, -971, 39, 968, -318, -820, -413, -488, -440, 274, -843, 695, -369, 579, -181, 934,
         -171, 561, 766, -679, 324, -103, 653, 353, 469, -181, 592, -690, -234, 905, -300, -145, 591, -971, -429, -802,
         758, -767, -931, 714, 475, 111, -25, -399, -106, -864, -586, 568, 296, 381, -418, -491, -82, -513, 841, -642,
         647, -662, 28, 472, -277, 510, -691, -636, 323, 580, 207, 254, 344, -504, -775, -38, -997, -807, -903, 67,
         -942, 773, 123, 630, -168, -169, 231, -551, 871, -666, 28, 553, -524, 810, 189, 192, 205, -842, 763, 411, 667,
         -868, -267, 68, 538, -67, 336, 707, -846, -711, 396, 865, 794, 221, -845, 42, -124, -310, 308, 262, -975, 511,
         686, -606, 192, 449, 269, 359, 13, -102, 340, -845, -799, -792, 793, 533, 872, 537, 547, 273, -871, 789, 965,
         -877, -265, -842, -951, 11, -793, 311, -504, -550, 190, 779, -214, 22, -700, 100, 727, 631, 771, -271, -949,
         961, 127, -708, -14, 670, 134, 242, -672, 576, 717, 973, 396, -999, 700, 961, -913, 48, -768, -52, -892, 412,
         -920, 999, 972, -78, 556, 885, -49, 682, -818, 464, 255, -702, 883, 852, 89, 967, -366, 297, -125, -976, -450,
         -463, 571, -845, -756, 730, -348, 559, 473, -916, -84, -41, 799, 581, -393, -739, 247, -599, 527, -543, 279,
         -898, -479, -108, -454, -370, -428, -591, -480, 599, 251, 743, -189, 798, -857, -562, -324, 337, -207, -380,
         -27, 925, -334, 593, 301, 897, -499, -382, 954, -2, -251, -467, 553, 71, -437, 59, 251, -890, 182, -502, -734,
         -793, 12, -198, 956, -248, -894, 442, -132, -746, -620, -302, 669, -700, 180, -694, -973, 772, 578, -710, -193,
         164, -436, 581, 384, 218, 277, -787, -722, -440, 144, -876, -518, -286, -488, -944, 665, 577, 152, -944, 707,
         -419, 819, 53, 712, 175, 122, 713, -65, -576, -797, 613, -634, -709, -196, -268, -393, 953, 317, 683, -542,
         -428, 67, 202, 339, 598, -606, 313, 675, -135, -904, 964, -7, -637, -210, -323, -164, 148, -453, 805, 343,
         -349, -904, 948, 132, 302, -51, -189, 820, 672, -423, 574, 150, -783, -899, -130, 91, 309, -569, 857, 555,
         -608, -883, 416, -573, -57, 166, -263, 245, -916, 107, 253, 123, 293, -425, -794, 173, -472, 635, 357, -733,
         649, -321, -425, 33, 301, 873, -755, -301, 139, 774, 0, 942, -185, 167, 245, -662, -424, 350, 683, -429, 698,
         800, -781, 377, -528, -225, 365, -188, -133, 173, -675, -12, 732, 717, 512, 728, -586, 980, -463, 824, 422,
         -341, -503, -203, -769, 454, 935, -880, -645, -977, -484, -492, 995, -599, 56, -744, -345, -446, 642, -785,
         -787, -613, 621, -151, -946, 106, -830, -166, 886, 662, 747, 120, 998, -222, 699, -438, -492, 940, 412, -485,
         828, -361, -306, 738, 244, -229, 763, 111, 913, 900, 38, 454, 110, -809, -160, 976, 236, -171, 844, 25, 804,
         293, 141, -254, 614, -291, -846, 902, 440, -794, -904, 820, -928, -224, 515, -405, 312, 915, 687, 829, 483,
         114, -752, 352, -466, -828, -68, 533, 31, 1, 653, 675, -46, -341, 139, 835, -528, -652, 879, -238, 531, 364,
         -434, -689, 857, -938, 289, -122, -881, -499, -147, 700, 576, -985, -395, -588, -904, -236, 218, 6, 580, -935,
         -194, 552, 589, 243, -151, -811, -733, 254, 204, 435, -945, 448, 863, -724, -639, 313, 740, 372, 604, -476,
         907, -567, -26, -81, 782, -564, 340, -658, 198, -267, 602, 99, -386, 95, 767, -195, 754, 259, 382])

    # print(locals())
    h = MinHeap(['zebra', 'apple'])
    # print(h)
    h.build_heap(da)
    print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
