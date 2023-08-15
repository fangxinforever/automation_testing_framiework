# hold runtime args
options = {}


def set(k, v):
    options[k] = v


def get(k):
    return options.get(k)
