from time import time


def log(filename=None):
    def decorator(my_function):
        def wrapper(*args, **kwargs):
            log_str = ""
            try:
                time_start = time()
                my_function(*args, **kwargs)
                time_end = time()
                time_summ = time_end - time_start
                log_str += f"my_function is ok\n"

            except Exception as e:
                log_str += f"my_function error: {e} Inputs: ({args}, {kwargs}\n"

            if filename:
                with open(filename, "a") as f:
                    f.write(log_str)
            else:
                print(log_str)

        return wrapper

    return decorator


@log()
def my_function(x, y):
    return x / y


my_function(1, 0)
