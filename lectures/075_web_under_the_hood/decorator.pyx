def logger2(f):
    print("Just ran logger2")
    def inner_func(*args, **kwargs):
        print(f"Starting execution of function {f.__name__}")
        rslt = f(*args, **kwargs)
        print(f"Finished execution of function {f.__name__}")
        return rslt
    return inner_func

@logger2
def say_bye(name):
    return f"Good bye {name}"

#print("==============")
#print(say_bye("Shahbaz"))