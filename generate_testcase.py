import random
import string


def generate(n_begin=1, n_end=30, type_="int", write_to_file=True):
    """
    PrintFormat
    ---------
    N

    Parameters
    ----------
    n_begin (= 1): int (if type_=="float": int or float)
        minimum value of n
        (if type_=="str":n is str_length)
    n_end (= 30): int (if type_=="float": int or float)
        maximum value of n
        (if type_=="str":n is str_length)
    type_ (="int"): str
        select type("int","float","str")
    write_to_file (=True): bool
        write to input.txt
    """
    if type_ == "int":
        n = random.randint(n_begin, n_end)
    elif type_ == "float":
        n = round(random.uniform(n_begin, n_end), 3)

    elif type_ == "str":
        n = "".join(random.choices(string.ascii_letters,
                                   k=random.randint(n_begin, n_end)))

    if write_to_file:
        path = ".\\input.txt"
        with open(path, mode="w") as f:
            f.write(str(n))
    else:
        print(n)


def generate_list(n_begin=1, n_end=30, a_begin=1, a_end=30, type_="int", write_to_file=True):
    """
    PrintFormat
    ---------
    N

    A1 A2 ... Ai ... AN

    Parameters
    ----------
    n_begin (= 1): int
        minimum value of n
    n_end (= 30): int
        maximum value of n
    a_begin (= 1): int (if type_=="float": int or float)
        minimum value of a
        (if type_=="str":a is str_length)
    a_end (= 30): int (if type_=="float": int or float)
        maximum value of a
        (if type_=="str":a is str_length)
    type_ (="int"): str
        select type("int","float","str")
    write_to_file (=True): bool
        write to input.txt
    """
    if type_ == "int":
        n = random.randint(n_begin, n_end)
        a = [random.randint(a_begin, a_end) for _ in range(n)]
    elif type_ == "float":
        n = random.randint(n_begin, n_end)
        a = [round((random.uniform(a_begin, a_end)), 3) for _ in range(n)]
    elif type_ == "str":
        n = random.randint(n_begin, n_end)
        a = ["".join(random.choices(string.ascii_letters, k=random.randint(a_begin, a_end)))
             for _ in range(n)]

    if write_to_file:
        path = ".\\input.txt"
        with open(path, mode="w") as f:
            f.write(str(n)+"\n")
        with open(path, mode="a") as f:
            f.write(" ".join(map(str, a)))

    else:
        print(n)
        print(*a)


def generate_two_dimensional(h_begin=1, h_end=10, w_begin=1, w_end=10, a_begin=1, a_end=30, type_="int", write_to_file=True):
    """
    PrintFormat
    ---------
    H W

    A(1,1) ... A(1,j) ... A(1,w)

    A(i,1) ... A(i,j) ... A(i,w)

    A(h,1) ... A(h,j) ... A(h,w)

    Parameters
    ----------
    h_begin,w_bigin (=1,1): int
        minimum value of h or w:
    h_end,w_end (=10,10): int
        maximum value of h or w:
    a_begin (= 1): int (if type_=="float": int or float)
        minimum value of a
        (if type_=="str":a is str_length)
    a_end (= 30): int (if type_=="float": int or float)
        maximum value of a
        (if type_=="str":a is str_length)
    type_ (="int"): str
        select type("int","float","str")
    write_to_file (=True): bool
        write to input.txt

    """
    h = random.randint(h_begin, h_end)
    w = random.randint(w_begin, w_end)

    if type_ == "int":
        a = [[random.randint(a_begin, a_end)
              for _ in range(w)] for _ in range(h)]
    elif type_ == "float":
        a = [[round(random.uniform(a_begin, a_end), 3)
              for _ in range(w)] for _ in range(h)]
    elif type_ == "str":
        a = [["".join(random.choices(string.ascii_letters, k=random.randint(a_begin, a_end)))
              for _ in range(w)] for _ in range(h)]

    if write_to_file:
        path = ".\\input.txt"
        with open(path, mode="w") as f:
            f.write(str(h)+" "+str(w))
        with open(path, mode="a") as f:
            for i in range(h):
                f.write("\n")
                f.write(" ".join(map(str, a[i])))

    else:
        print(h, w)
        print(*a)