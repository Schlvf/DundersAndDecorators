def my_decorator(n: int):
    def decorator(f):
        def wrapper():
            for _ in range(n):
                print("Before function")
            f()
            for _ in range(n):
                print("After function")

        return wrapper

    return decorator


@my_decorator(n=3)
def execute_task():
    print("Executing task…")


def do_twice(f):
    def wrapper_do_twice(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)

    return wrapper_do_twice


# @do_twice
# def count_to(n):
#     message = "".join([i for i in range(1, n+1)])


if __name__ == "__main__":
    execute_task()
