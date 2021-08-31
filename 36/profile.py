def get_profile(name: str, age: int, *args, **kwargs):
    if type(age) != int or len(args) > 5:
        raise ValueError

    if len(args) > 1:
        args = (sorted(args))

    result = {"name": name, "age": age}
    if args:
        result["sports"] = sorted(args)
    if kwargs:
        result["awards"] = kwargs

    return result
