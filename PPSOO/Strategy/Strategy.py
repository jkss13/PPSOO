import random
import time
import BubbleSort
import InsertionSort
import MergeSort
import QuickSort

class SortStrategy:
    def sort(self, arr):
        pass

# Cliente
class SortClient:
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy
    
    def set_sort_strategy(self, sort_strategy):
        self.sort_strategy = sort_strategy
    
    def do_sort(self, arr):
        start_time = time.time()
        sorted_arr = self.sort_strategy.sort(arr)
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
        return sorted_arr

if __name__ == '__main__':
    arr_sizes = [10000, 50000, 100000]
    for size in arr_sizes:
        arr = [random.randint(1, 1000000) for _ in range(size)]
        print(f"Testando com {size} elementos...")
        client = SortClient(BubbleSort())
        sorted_arr = client.do_sort(arr)
        client.set_sort_strategy(InsertionSort())
        sorted_arr = client.do_sort(arr)
        client.set_sort_strategy(MergeSort())
        sorted_arr = client.do_sort(arr)
        client.set_sort_strategy(QuickSort())
        sorted_arr = client.do_sort(arr)