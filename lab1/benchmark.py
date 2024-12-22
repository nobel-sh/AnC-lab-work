import random
import time
from algorithms import linear_search, binary_search

def generate_test_data(size):
    return sorted(random.sample(range(size * 2), size))

def run_benchmarks():
    sizes = range(100000, 3000000, 100000)
    results = {
        'sizes': list(sizes),
        'linear_best': [],
        'linear_worst': [],
        'binary_best': [],
        'binary_worst': []
    }
    
    for size in sizes:
        arr = generate_test_data(size)
        
        start = time.time()
        linear_search(arr, arr[0])
        results['linear_best'].append(time.time() - start)
        
        start = time.time()
        linear_search(arr, -1)
        results['linear_worst'].append(time.time() - start)
        
        item = arr[len(arr)//2] 
        start = time.time()
        binary_search(arr, item)
        results['binary_best'].append(time.time() - start)
        
        start = time.time()
        binary_search(arr, -1)
        results['binary_worst'].append(time.time() - start)
    
    return results
