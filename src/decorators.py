from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Callable], Callable]:
    """ Декоратор, регистрирующий детали выполнения функций """
    def my_dec(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                status = "OK"
            except Exception as e:
                status = "ERROR"
                error = e
                error_text = str(error)

            if not filename:
                print("*****\n")
                print(f"function {func.__name__} with args: args - {args}, kwargs - {kwargs}\n")
                if status == "OK":
                    print(f"Result: {status} - {result}\n")
                else:
                    print(f"Result: {status} - {type(error).__name__}: {error_text}\n")
                print("*****\n")

            else:
                with open(f"../{filename}", "a", encoding="UTF-8") as file:
                    file.write("*****\n")
                    file.write(f"function {func.__name__} with args: args - {args}, kwargs - {kwargs}\n")
                    if status == "OK":
                        file.write(f"Result: {status} - {result}\n")
                    else:
                        file.write(f"Result: {status} - {type(error).__name__}: {error_text}\n")
                    file.write("*****\n")

            if status == "ERROR":
                raise error

            return result

        return wrapper

    return my_dec


@log(filename="mylog.txt")
def my_dec(x: int, y: int) -> int:
    """Функция умножает числа и выдает результат в файл mylog.txt"""
    return x * y


print(my_dec(9, 12))
