from time import time


def log(filename=None):
    """
    Декоратор log будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки
    """

    def decorator(my_function):
        def wrapper(*args, **kwargs):
            log_str = ""
            result = None
            try:
                time_start = time()
                result = my_function(*args, **kwargs)
                time_end = time()
                time_summ = time_end - time_start
                log_str += f"my_function is ok\n"

            except Exception as e:
                log_str += f"my_function error: {e} Inputs: ({args}, {kwargs}\n"
                # print(filename)
            if filename:
                with open(filename, "a") as f:
                    f.write(log_str)
            else:
                print(log_str)

            return result

        return wrapper

    return decorator


@log()
def function(x, y):
    return x / y


print(function(1, 2))
