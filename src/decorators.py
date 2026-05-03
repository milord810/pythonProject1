from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Callable], Callable]:
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
                print("*****")
                print(f"function {func.__name__} with args: args - {args}, kwargs - {kwargs}")
                if status == "OK":
                    print(f"Result: {status} - {result}")
                else:
                    print(f"Result: {status} - {type(error).__name__}: {error_text}")
                print("*****")

            else:
                with open(f"../{filename}", "a", encoding="UTF-8") as file:
                    file.write("*****")
                    file.write(f"function {func.__name__} with args: args - {args}, kwargs - {kwargs}")
                    if status == "OK":
                        file.write(f"Result: {status} - {result}")
                    else:
                        file.write(f"Result: {status} - {type(error).__name__}: {error_text}")
                    file.write("*****")

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
