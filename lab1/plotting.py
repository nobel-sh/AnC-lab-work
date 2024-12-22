import matplotlib.pyplot as plt
import numpy as np

def plot_results(results):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    ax1.plot(results['sizes'], results['linear_best'], 'b-', label='Linear Search')
    ax1.plot(results['sizes'], results['binary_best'], 'r-', label='Binary Search')
    ax1.set_xlabel('Input Size')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('Best Case Performance')
    ax1.legend()
    ax1.grid(True)
    
    ax2.plot(results['sizes'], results['linear_worst'], 'b-', label='Linear Search')
    ax2.plot(results['sizes'], results['binary_worst'], 'r-', label='Binary Search')
    ax2.set_xlabel('Input Size')
    ax2.set_ylabel('Time (seconds)')
    ax2.set_title('Worst Case Performance')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('search_performance.png')
    plt.close()
