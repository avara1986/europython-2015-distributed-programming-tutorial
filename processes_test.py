from threading import Thread
import concurrent.futures as cf
from time import time
from europy import fib, NCORES, N

if __name__ == '__main__':
    print ('running on a system with %d cores' % NCORES)

    t0 = time()
    serial_result = fib(N)
    dt_serial = time() - t0
    print ('fib(%d) = %d (time: %.02fs)' % (N, serial_result, dt_serial))

    args = [N for i in range(NCORES)]
    t0 = time()
    with cf.ProcessPoolExecutor(max_workers=NCORES) as pool:
            results = pool.map(fib, args)
    dt_parallel = time() - t0

    result = set(results)
    assert len(result) == 1
    result = result.pop()
    assert result == serial_result

    print ('%dx fib(%d) = %d (time: %.02fs) speedup (vs %dx fib(%d): %.02f )' % (NCORES, N, result, dt_parallel, NCORES, N, dt_serial * NCORES / dt_parallel))
