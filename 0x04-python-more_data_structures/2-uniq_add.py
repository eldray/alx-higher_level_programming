#!/usr/bin/python3
q_add(my_list=[]):
    unique = []
    for i in my_list:
        if i not in unique:
            unique.append(i)
    return sum(unique)
