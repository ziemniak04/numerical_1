import subprocess
import re
import matplotlib.pyplot as plt

# N values: 10^3 to 10^6
Ns = [1000, 10000, 100000, 1000000]
langs = ['cpp', 'java', 'python']
times = {lang: [] for lang in langs}

import subprocess
import matplotlib.pyplot as plt

for lang in langs:
    for n in Ns:
        if lang == 'cpp':
            cmd = f'./nm1_cpp {n}'
        elif lang == 'java':
            cmd = f'java -jar nm1_java.jar {n}'
        elif lang == 'python':
            cmd = f'/home/madzia/C++/nm1/.venv/bin/python nm1.py {n}'
        
        # Run with /usr/bin/time, output to file, suppress program output
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
            time_file = f.name
        full_cmd = f'/usr/bin/time -f "%e" -o {time_file} {cmd} > /dev/null'
        subprocess.run(full_cmd, shell=True, cwd='/home/madzia/C++/nm1')
        with open(time_file, 'r') as f:
            t = float(f.read().strip())
        times[lang].append(t)
        print(f'{lang} N={n}: {t:.3f}s')
        import os
        os.unlink(time_file)

# Plot
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