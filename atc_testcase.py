"""競プロのテストケースを生成する

グローバル定数
PATH

関数
one_value
one_dimensional_list
two_dimensional_list
"""

import random
import string

PATH = ".\\input.txt"


def __create_value(min_: int, max_: int, type_: str):
    if type_ == "int":
        return random.randint(min_, max_)
    elif type_ == "float":
        return round(random.uniform(min_, max_), 3)
    elif type_ == "str":
        str_len = random.randint(min_, max_)
        chars = random.choices(string.ascii_lowercase, k=str_len)
        return "".join(chars)
    else:
        raise TypeError("invalid type")


def one_value(
    min_value: int = 1,
    max_value: int = 8,
    value_type: str = "int",
    write_to_file: bool = True,
):
    """
    出力形式

    N

    Args:
        min_value (int, optional): 要素の値の最小値(value_type="str"の場合は文字数). Defaults to 1.
        max_value (int, optional): 要素の値の最大値(value_type="str"の場合は文字数) Defaults to 8.
        value_type (str, optional): 要素の型 Defaults to "int".
        write_to_file (bool, optional): ファイルにも出力するか Defaults to True.
    """
    value = __create_value(min_value, max_value, value_type)
    if write_to_file:
        with open(PATH, mode="w") as f:
            f.write(str(value))

    return value


def one_dimensional_list(
    min_len: int = 1,
    max_len: int = 8,
    min_value: int = 1,
    max_value: int = 8,
    value_type: str = "int",
    write_to_file: bool = True,
):
    """
    出力形式

    N

    a_1 , a_2 , ... , a_n

    Args:
        min_len (int, optional): リストの長さの最小値 Defaults to 1.
        max_len (int, optional): リストの長さの最大値 Defaults to 8.
        min_value (int, optional): 要素の値の最小値 Defaults to 1.
        max_value (int, optional): 要素の値の最大値 Defaults to 8.
        value_type (str, optional): 要素の型 Defaults to "int".
        write_to_file (bool, optional):ファイルにも出力するか Defaults to True.
    """
    n = random.randint(min_len, max_len)

    a = [__create_value(min_value, max_value, value_type) for _ in range(n)]

    if write_to_file:
        with open(PATH, mode="w") as f:
            f.write(str(n) + "\n")
        with open(PATH, mode="a") as f:
            f.write(" ".join(map(str, a)))

    return n, a


def two_dimensional_list(
    min_h: int = 1,
    max_h: int = 8,
    min_w: int = 1,
    max_w: int = 8,
    min_value: int = 1,
    max_value: int = 8,
    value_type: str = "int",
    write_to_file: bool = True,
):
    """
    出力形式

    H W

    A_1,1 , A_1,2 , ... , A_1,W

    A_i,1 , A_i,2 , ... , A_i,W

    A_H,1 , A_H,2 , ... , A_H,W

    Args:
        min_h (int, optional): リストの行(縦)の最小値 Defaults to 1.
        max_h (int, optional): リストの行(縦)の最大値 Defaults to 8.
        min_w (int, optional): リストの列(横)の最小値 Defaults to 1.
        max_w (int, optional): リストの列(横)の最大値 Defaults to 8.
        min_value (int, optional): リストの要素の最小値 Defaults to 1.
        max_value (int, optional): リストの要素の最大値 Defaults to 8.
        value_type (str, optional): リストの要素の型 Defaults to "int".
        write_to_file (bool, optional): ファイルにも出力するか Defaults to True.
    """
    h = random.randint(min_h, max_h)
    w = random.randint(min_w, max_w)

    a = [
        [__create_value(min_value, max_value, value_type) for _ in range(w)]
        for _ in range(h)
    ]

    if write_to_file:
        with open(PATH, mode="w") as f:
            f.write(str(h) + " " + str(w))
        with open(PATH, mode="a") as f:
            for i in range(h):
                f.write("\n")
                f.write(" ".join(map(str, a[i])))

    return h, w, a
