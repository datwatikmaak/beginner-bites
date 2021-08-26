from functools import wraps


def make_html(element):
    def tag_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return f"<{element}>" + fn(*args, **kwargs) + f"</{element}>"
        return wrapper
    return tag_decorator
