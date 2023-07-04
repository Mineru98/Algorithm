# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline


def check_case_1(strings: str):
    pattern, l_pattern, s_pattern = [], [], []
    open_pattern = []
    for w in strings:
        if w == "(" or w == ")":
            if w == "(":
                open_pattern.append(w)
            s_pattern.append(w)
            l_pattern.append(None)
            pattern.append(w)
        elif w == "[" or w == "]":
            if w == "[":
                open_pattern.append(w)
            s_pattern.append(None)
            l_pattern.append(w)
            pattern.append(w)
    r_pattern = pattern[::-1]
    l_pattern = l_pattern[::-1]
    s_pattern = s_pattern[::-1]
    open_pattern = open_pattern[::-1]
    print(open_pattern)
    pattern = "".join(pattern)
    last_large_idx, last_small_idx = 0, 0
    if pattern.startswith(")") or pattern.startswith("]") or len(pattern) % 2 == 1:
        return False
    else:
        count = 0
        for w in pattern:
            last_pattern = r_pattern.pop()
            l_pattern.pop()
            s_pattern.pop()
            if w == "(":
                last_small_idx += 1
            elif w == ")":
                last_small_idx -= 1
                test = open_pattern.pop()
                # print("TEST1", test, last_small_idx)
                if test != "(" and last_small_idx != 0:
                    return False
            elif w == "[":
                last_large_idx += 1
            elif w == "]":
                last_large_idx -= 1
                test = open_pattern.pop()
                # print("TEST2", test, last_large_idx)
                if test != "[" and last_large_idx != 0:
                    return False
            if last_small_idx == -1:
                return False
            if last_large_idx == -1:
                return False
            count += 1

        if last_small_idx == 0 and last_large_idx == 0:
            return True
        else:
            return False


lines = ""
while True:
    line = input()[:-1]
    if lines == ".":
        break
    elif line.endswith("."):
        lines += line
        if check_case_1(lines):
            print("yes")
        else:
            print("no")
        lines = ""
    else:
        lines += line
