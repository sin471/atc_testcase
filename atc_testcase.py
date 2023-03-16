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


def __create_int(min_value: int, max_value: int):
    return random.randint(min_value, max_value)


def __create_float(min_value: int, max_value: int):
    return round(random.uniform(min_value, max_value), 3)


def __create_str(min_len: int, max_len: int):
    str_len = random.randint(min_len, max_len)
    return random.choices(string.ascii_lowercase, k=str_len)


def one_value(
    min_value: int = 1,
    max_value: int = 15,
    value_type: str = "int",
    write_to_file: bool = True,
):
    """値Nをランダムで一つ出力する

    出力形式

    N

    生成した値はコンソールへ出力し、
    write_to_file=Trueの場合、同時にinput.txtも上書きする

    Args:
        min_value (int, optional): 要素の値の最小値(value_type="str"の場合は文字数). Defaults to 1.
        max_value (int, optional): 要素の値の最大値(value_type="str"の場合は文字数) Defaults to 30.
        value_type (str, optional): 要素の型 Defaults to "int".
        write_to_file (bool, optional): ファイルにも出力するか Defaults to True.
    """
    if value_type == "int":
        n = __create_int(min_value, max_value)
    elif value_type == "float":
        n = __create_float(min_value, max_value)
    elif value_type == "str":
        n = "".join(__create_str(min_value, max_value))
    else:
        print("Type Unknown")
        return

    if write_to_file:
        with open(PATH, mode="w") as f:
            f.write(str(n))
    print(n)


def one_dimensional_list(
    min_len: int = 1,
    max_len: int = 15,
    min_value: int = 1,
    max_value: int = 30,
    value_type: str = "int",
    write_to_file: bool = True,
) :
    """一次元リストを出力する

    出力形式

    N

    a_1 , a_2 , ... , a_n

    生成した値はコンソールへ出力し、
    write_to_file=Trueの場合、同時にinput.txtも上書きする

    Args:
        min_len (int, optional): リストの長さの最小値 Defaults to 1.
        max_len (int, optional): リストの長さの最大値 Defaults to 30.
        min_value (int, optional): 要素の値の最小値 Defaults to 1.
        max_value (int, optional): 要素の値の最大値 Defaults to 30.
        value_type (str, optional): 要素の型 Defaults to "int".
        write_to_file (bool, optional):ファイルにも出力するか Defaults to True.
    """
    length = random.randint(min_len, max_len)
    
    if value_type == "int":
        lis = [__create_int(min_value, max_value) for _ in range(length)]
    elif value_type == "float":
        lis = [__create_float(min_value, max_value) for _ in range(length)]
    elif value_type == "str":
        lis = ["".join(__create_str(min_value, max_value)) for _ in range(length)]

    else:
        print("Type Unknown")
        return

    if write_to_file:
        with open(PATH, mode="w") as f:
            f.write(str(length) + "\n")
        with open(PATH, mode="a") as f:
            f.write(" ".join(map(str, lis)))

    print(length)
    print(*lis)


def two_dimensional_list(
    min_h: int = 1,
    max_h: int = 10,
    min_w: int = 1,
    max_w: int = 10,
    min_value: int = 1,
    max_value: int = 15,
    value_type: str = "int",
    write_to_file: bool = True,
):
    """二次元リストを出力する

    出力形式

    H W

    A_1,1 , A_1,2 , ... , A_1,W

    A_i,1 , A_i,2 , ... , A_i,W

    A_H,1 , A_H,2 , ... , A_H,W

    生成した値はコンソールへ出力し、
    write_to_file=Trueの場合、同時にinput.txtも上書きする


    Args:
        min_h (int, optional): リストの行(縦)の最小値 Defaults to 1.
        max_h (int, optional): リストの行(縦)の最大値 Defaults to 10.
        min_w (int, optional): リストの列(横)の最小値 Defaults to 1.
        max_w (int, optional): リストの列(横)の最大値 Defaults to 10.
        min_value (int, optional): リストの要素の最小値 Defaults to 1.
        max_value (int, optional): リストの要素の最大値 Defaults to 30.
        value_type (str, optional): リストの要素の型 Defaults to "int".
        write_to_file (bool, optional): ファイルにも出力するか Defaults to True.
    """
    h = random.randint(min_h, max_h)
    w = random.randint(min_w, max_w)

    if value_type == "int":
        a = [[__create_int(min_value, max_value) for _ in range(w)] for _ in range(h)]

    elif value_type == "float":
        a = [[__create_float(min_value, max_value) for _ in range(w)] for _ in range(h)]

    elif value_type == "str":
        a = [
            ["".join(__create_str(min_value, max_value)) for _ in range(w)]
            for _ in range(h)
        ]

    else:
        print("Type Unknown")
        return

    if write_to_file:
        with open(PATH, mode="w") as f:
            f.write(str(h) + " " + str(w))
        with open(PATH, mode="a") as f:
            for i in range(h):
                f.write("\n")
                f.write(" ".join(map(str, a[i])))

    print(h, w)
    for i in a:
        print(*i)
