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
