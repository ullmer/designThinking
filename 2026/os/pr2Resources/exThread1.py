import threading

NTHREADS = 4

results = [None] * NTHREADS
threads = []

def go(n):
    print(f"Hello from thread {n}")

    # equivalent to thread_exit(10 + n)
    results[n] = 10 + n

    # any code after the "return value" would still execute
    # unless you explicitly return
    return

for i in range(NTHREADS):
    t = threading.Thread(target=go, args=(i,))
    threads.append(t)
    t.start()

for i in range(NTHREADS):
    threads[i].join()
    exit_value = results[i]
    print(f"Thread {i} returned with {exit_value}")

print("Main thread done.")

### end ###
