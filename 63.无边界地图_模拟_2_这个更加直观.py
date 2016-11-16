#!/usr/bin/python
# coding: utf-8

from sets import Set

__author__ = 'Sayakiss'

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]


def is_ng_alive(x, y, original_set):
    cnt = 0;
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) in original_set:
            cnt += 1
    if (x, y) in original_set:
        if cnt in [2, 3]:
            return True
    else:
        if cnt == 3:
            return True
    return False

def sim(original_set):
    new_set = Set()
    for (x, y) in original_set:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_ng_alive(nx, ny, original_set):
                new_set.add((nx, ny))
        if is_ng_alive(x, y, original_set):
            new_set.add((x, y))
    return new_set

def print_cell_set(cell_set, x_size=10, y_size=10):
    for x in range(-x_size, x_size):
        for y in range(-y_size, y_size):
            if (x, y) in cell_set:
                print '*',
            else:
                print '.',
        print ''


cell_set = Set([(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)])
max_size = 0
max_gen = 0
for i in range(1500):
    cell_set = sim(cell_set)
    gen_size = len(cell_set)
    if gen_size > max_size:
        max_size = gen_size
        max_gen = i + 1
    print str(i + 1) + " generation population: " + str(gen_size)

print str(max_gen) + "-" + str(max_size)
