import random
import time
from abc import ABCMeta, abstractmethod
from pygame.surfarray import array_alpha

class SortingAlgorithms():
    def __init__(self, name):
        self.name = name
        self.array_to_sort = random.sample(range(512), 512)
        self.start_time = time.time()

    def udpate_display(self, index1 = None , index2 = None):
        import SortingVisualizer
        SortingVisualizer.update_window(self, index1, index2)

    def run(self):
        self.start_time = time.time() 
        self.algorithm()
        time_elapsed = time.time()-self.start_time
        return (self.array_to_sort, time_elapsed)

    @abstractmethod
    def algorithm(self):
        raise TypeError("")


class SelectionSort(SortingAlgorithms):
    def __init__(self):
        super().__init__("Selection Sort")

    def algorithm(self):
        for i in range(len(self.array_to_sort)):
            min_index = i
            for j in range(i+1, len(self.array_to_sort)):
                if self.array_to_sort[min_index] > self.array_to_sort[j]:
                    min_index = j

            tmp = self.array_to_sort[i]
            self.array_to_sort[i] = self.array_to_sort[min_index]
            self.array_to_sort[min_index] = tmp
            self.udpate_display(self.array_to_sort[i], self.array_to_sort[min_index])


class InsertionSort(SortingAlgorithms):
    def __init__(self):
        super().__init__("Insertion Sort")

    def algorithm(self):
        for i in range(1, len(self.array_to_sort)):
            current = self.array_to_sort[i]
            j = i -1
            while j >= 0 and self.array_to_sort[j] > current:
                self.array_to_sort[j+1] = self.array_to_sort[j]
                j -= 1
            self.array_to_sort[j+1] = current
            self.udpate_display(self.array_to_sort[j+1], self.array_to_sort[i])


class MergeSort(SortingAlgorithms):
    def __init__(self):
        super().__init__("Merge Sort")


    def algorithm(self, array_to_sort = []):
        if array_to_sort == []:
            array_to_sort = self.array_to_sort
        if len(array_to_sort) < 2:
            return array_to_sort
        mid = len(array_to_sort) // 2
        l = self.algorithm(array_to_sort[:mid])
        r = self.algorithm(array_to_sort[mid:])
        return self.merge(l, r)

    def merge(self, left, right):
        sorted_array = []
        i, j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j+=1
            self.udpate_display()
        sorted_array+=left[i:]
        sorted_array+=right[j:]
        self.array_to_sort = sorted_array
        self.udpate_display()
        return sorted_array

