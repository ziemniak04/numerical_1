"""
Benchmark script for comparing execution times of Sieve of Eratosthenes implementations.

This script benchmarks implementations in C++, Java, and Python across different input sizes
(N values from 10^3 to 10^6) and generates a comparison plot.
"""

import subprocess
import os
import tempfile
import matplotlib.pyplot as plt


def benchmark_language(lang, n, cwd='/home/madzia/C++/nm1'):
    """
    Benchmark a single language implementation with a given N value.
    
    Args:
        lang (str): Programming language ('cpp', 'java', or 'python')
        n (int): Input size parameter for the Sieve of Eratosthenes
        cwd (str): Working directory for command execution
        
    Returns:
        float: Execution time in seconds
    """
    if lang == 'cpp':
        cmd = f'./nm1_cpp {n}'
    elif lang == 'java':
        cmd = f'java -jar nm1_java.jar {n}'
    elif lang == 'python':
        cmd = f'/home/madzia/C++/nm1/.venv/bin/python nm1.py {n}'
    
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        time_file = f.name
    
    full_cmd = f'/usr/bin/time -f "%e" -o {time_file} {cmd} > /dev/null'
    subprocess.run(full_cmd, shell=True, cwd=cwd)
    
    with open(time_file, 'r') as f:
        t = float(f.read().strip())
    
    os.unlink(time_file)
    return t


def run_benchmarks(langs, Ns):
    """
    Run benchmarks for all languages and N values.
    
    Args:
        langs (list): List of programming languages to benchmark
        Ns (list): List of N values to test
        
    Returns:
        dict: Dictionary mapping each language to a list of execution times
    """
    times = {lang: [] for lang in langs}
    
    for lang in langs:
        for n in Ns:
            t = benchmark_language(lang, n)
            times[lang].append(t)
            print(f'{lang} N={n}: {t:.3f}s')
    
    return times


def plot_results(langs, Ns, times):
    """
    Generate and save a plot comparing execution times across languages.
    
    Args:
        langs (list): List of programming languages benchmarked
        Ns (list): List of N values tested
        times (dict): Dictionary mapping languages to execution times
    """
    plt.figure(figsize=(10, 6))
    
    for lang in langs:
        plt.plot(Ns, times[lang], marker='o', label=lang.upper())
    
    plt.xlabel('N (10^k)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Execution Times for Sieve of Eratosthenes')
    plt.legend()
    plt.grid(True)
    plt.xticks(Ns, ['10^3', '10^4', '10^5', '10^6'])
    plt.savefig('benchmark_plot.png')
    plt.show()


if __name__ == '__main__':
    Ns = [1000, 10000, 100000, 1000000]
    langs = ['cpp', 'java', 'python']
    
    times = run_benchmarks(langs, Ns)
    plot_results(langs, Ns, times)
