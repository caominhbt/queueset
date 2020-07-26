import numpy as np
from time import time
import multiprocessing as mp
import timeit




# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]


import multiprocessing as mp



# Step 1: Redefine, to accept `i`, the iteration number
def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0

    for n in row:
        print("Insite main function!")
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)


# Step 2: Define callback function to collect the output in `results`
def collect_result(result):
    global results
    print(results)
    results.append(result)




if __name__ == '__main__':
    cores = mp.cpu_count()
    pool = mp.Pool(cores)
    results = []
    #results = pool.map(howmany_within_range_rowonly, [row for row in data])

    #results2 = pool.map(howmany_within_range_rowonly2, [row for row in data])

    #pool.close()

    #print(results[:10], results2[:10])
    # Step 3: Use loop to parallelize
    for i, row in enumerate(data):
        pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result)

    # Step 4: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    # Step 5: Sort results [OPTIONAL]
    results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]

    print(results_final[:10])