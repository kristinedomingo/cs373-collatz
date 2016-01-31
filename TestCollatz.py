#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, get_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "0 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

    def test_read_3 (self) :
        s    = "1 2147483647\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 2147483647)

    ## ------------
    ## cycle_length
    ## ------------

    def test_get_cycle_length_1 (self) :
        v = get_cycle_length(1)
        self.assertEqual(v, 1)

    def test_get_cycle_length_2 (self) :
        v = get_cycle_length(500)
        self.assertEqual(v, 111)

    def test_get_cycle_length_3 (self) :
        v = get_cycle_length(5000)
        self.assertEqual(v, 29)

    def test_get_cycle_length_4 (self) :
        v = get_cycle_length(999999)
        self.assertEqual(v, 259)

    def test_get_cycle_length_5 (self) :
        v = get_cycle_length(543210)
        self.assertEqual(v, 147)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(1, v)

    def test_eval_6 (self) :
        v = collatz_eval(63, 64)
        self.assertEqual(108, v)

    def test_eval_7 (self) :
        v = collatz_eval(78, 90)
        self.assertEqual(111, v)

    def test_eval_8 (self) :
        v = collatz_eval(90, 78)
        self.assertEqual(111, v)

    def test_eval_9 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(174, v)

    def test_eval_10 (self) :
        v = collatz_eval(477095, 477792)
        self.assertEqual(382, v)

    def test_eval_11 (self) :
        v = collatz_eval(54691, 1)
        self.assertEqual(340, v)

    def test_eval_12 (self) :
        v = collatz_eval(409818, 415101)
        self.assertEqual(449, v)

    def test_eval_13 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(525, v)

    def test_eval_14 (self) :
        v = collatz_eval(999999, 999999)
        self.assertEqual(259, v)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 30, 30, 30)
        self.assertEqual(w.getvalue(), "30 30 30\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 1\n63 64\n78 90\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n63 64 108\n78 90 111\n")

    def test_solve_3 (self) :
        r = StringIO("2315 2319\n12345 12346\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "2315 2319 108\n12345 12346 113\n")

    def test_solve_4 (self) :
        r = StringIO("96206 11382\n978863 978942\n122755 134378\n716906 717693\n521409 523944\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "96206 11382 351\n978863 978942 290\n122755 134378 344\n716906 717693 349\n521409 523944 333\n")

    def test_solve_5 (self) :
        r = StringIO("13374 48709\n87591 1876\n57722 84\n92076 41717\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "13374 48709 324\n87591 1876 351\n57722 84 340\n92076 41717 351\n")

    def test_solve_6 (self) :
        r = StringIO("574005 568276\n639309 639309\n483590 480482\n704510 700488\n689640 695066\n725388 726056\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "574005 568276 377\n639309 639309 173\n483590 480482 382\n704510 700488 411\n689640 695066 442\n725388 726056 305\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
coverage3 run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
coverage3 report -m                      >> TestCollatz.tmp
cat TestCollatz.tmp
................................
----------------------------------------------------------------------
Ran 32 tests in 0.771s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          47      0     20      0   100%
TestCollatz.py     124      0      0      0   100%
------------------------------------------------------------
TOTAL              171      0     20      0   100%

"""
