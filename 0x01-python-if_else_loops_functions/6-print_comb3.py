#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{:02d}".format(i), ":02d}".format(j), sep=", ",end=", "\
                 if i != 8 or j != 9 else "\n")
