from os import cpu_count

N = 36
NCORES = int(cpu_count())


def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise Exception('Fib(n) is undefined for n < 0 ')
    return fib(n - 1) + fib (n - 2)
  
class FibWorker(object):
    def fib(self, n):
        return fib(n)
