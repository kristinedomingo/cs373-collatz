#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ----------------
# get_cycle_length
# ----------------

def get_cycle_length (i) :
    """
    i the integer to get the cycle length of
    return the cycle length of i
    """

    assert i > 0
    assert i < 1000000

    cycle_length = 1

    while i != 1:
        if i % 2 != 0:
            i = (3 * i) + 1
        else:
            i = i // 2

        cycle_length += 1

    return cycle_length

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    assert i > 0
    assert j > 0
    assert i <= 1000000
    assert j <= 1000000

    # Check for i > j case - if so, switch the two numberes
    if i > j:
        i, j = j, i

    max_cycle_length = get_cycle_length(i)
    new_cycle_length = 1

    while i < j:
        i = i + 1
        new_cycle_length = get_cycle_length(i)

        if new_cycle_length > max_cycle_length:
            max_cycle_length = new_cycle_length

    return max_cycle_length

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
