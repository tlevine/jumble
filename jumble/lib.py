import concurrent.futures

def jumble(func, iterable, max_workers = 50)
    jobs = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers) as e:
        for i, item in iterable:
            jobs[i] = e.submit(func, item)
        
        while len(jobs) > 0:
            for i, future in jobs.items():
                if future.done():
                    del(jobs[i])
                    yield future
