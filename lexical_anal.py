from numba import jit, njit, prange, vectorize
import numpy as np
import mypy
import re
from lex_tabel import tabel


def preaperer():
    f = open("../source.txt", "r")

    in_pipe = f.read()  # strips of white spaces

    in_pipe = ''.join(in_pipe.split())
    f.close()

    return in_pipe


def f_state_machine(x, y):
    list_values, string_to_compare = x.values(), y
    word = ''
    comp_sec_check = ''
    sec_check = []
    final = []
    for i in string_to_compare:
        word += i
        print(word)

        for dict in list_values:

            for item in dict:

                value_of_item = dict[item]

                if value_of_item == word:
                    sec_check.append(item)
                    word = ''
                    print('match found')


                else:

                    for i in sec_check:
                        print(i)
                    continue
    print(f' final words: {final} \n sec check: {sec_check}')


f_state_machine(tabel, preaperer())
