try:
    from concurrent.futures import ThreadPoolExecutor
except ImportError:
    from futures import ThreadPoolExecutor

def jumble(func, iterable, max_workers = 50):
    '''
    Run a function a bunch of times, and return results as futures in the order
    that they finish.

    :param func: A function that takes one argument
    :param iterable: The function will be applied to each element of this iterable.
    :param max_workers: Because this is running in parallel
    '''
    jobs = {}
    with ThreadPoolExecutor(max_workers) as e:
        for i, item in enumerate(iterable):
            jobs[i] = e.submit(func, item)
        
        while len(jobs) > 0:
            for i in list(jobs.keys()):
                if jobs[i].done():
                    yield jobs[i]
                    del(jobs[i])
