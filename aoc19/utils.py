class defaultlambdadict(dict):
    def __init__(self, f, items=None):
        self.f = f
        try:
            for key, value in items.items():
                self[key] = value
        except:
            try:
                for (key, value) in items:
                    self[key] = value
            except:
                "Items Not Valid"

    def __missing__(self, key):
        return self.f(key)


def get_time(f):
    from time import perf_counter

    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret = f(*args, **kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        print("Time", total_time, "seconds")
        return ret

    return wrapper
