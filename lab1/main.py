import unittest
from test_search import TestSearchAlgorithms
from benchmark import run_benchmarks
from plotting import plot_results

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchAlgorithms)
    unittest.TextTestRunner(verbosity=2).run(suite)
    results = run_benchmarks()
    plot_results(results)

if __name__ == '__main__':
    main()
