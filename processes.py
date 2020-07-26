import os
import multiprocessing as mp

processes = ('process1.py', 'process2.py')


def run_python(process):
    os.system('python {}'.format(process))


if __name__ == "__main__" :

    pool = mp.Pool(processes=2)
    pool.map(run_python, processes)