# -*- coding: utf-8 -*-
"""
<# Лабораторная работа №1
## Выполнил студент группы БФИ2202 Сидорук Данил Вадимович

### Оглавление
1. [Задание 1](#Задание-№1)
2. [Задание 2](#Задание-№2)
3. [Задание 3](#Задание-№3)
4. [Вывод](#Вывод)

### Задание №1
<i> Вызвать функцию print() и передать туда строку Hello, World! </i>
"""

print("Hello, World!")

"""### Задание №2
Написать генератор случайных матриц(многомерных), который принимает
опциональные параметры <b>m</b>, <b>n</b>, <b>min_limit</b>, <b>max_limit</b>, где <b>m</b> и <b>n</b> указывают размер
матрицы, а <b>min_lim</b> и <b>max_lim</b> - минимальное и максимальное значение для
генерируемого числа.
"""

import random
import time

def gen_matrix(m, n, min, max):
  return [
    [random.randint(min, max) for _ in range(n)]
    for _ in range(m)
  ]

user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())

print(gen_matrix(user_m, user_n, user_min_limit, user_max_limit + 11))

"""### Задание №3
Реализовать методы сортировки строк числовой матрицы в соответствии с
заданием. Оценить время работы каждого алгоритма сортировки и сравнить его со
временем стандартной функции сортировки. Испытания проводить на сгенерированных
матрицах.
"""

import time
import copy

def sort_matrix(matrix, sort_f):
  return [sort_f(row) for row in matrix]

def timer(source_matrix, func, debug = False):
    matrix_a = copy.deepcopy(matrix)
    start_time = time.time()
    sort_arr = sort_matrix(matrix_a, func)
    print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
    if debug == True:
      print(sort_arr)

# Selection sort
def selection_sort(arr):
  if len(arr) <= 1:
    return arr

  index_min = min(range(len(arr)), key=arr.__getitem__) # N
  arr[0], arr[index_min] = arr[index_min], arr[0]

  return [arr[0], *selection_sort(arr[1:])] # Рекурсивный вызов, дорисовывающий
                                            # К нашей N квадрат
  # Total: N^2

matrix = gen_matrix(100, 100, 1, 100)
timer(matrix, selection_sort)
timer(matrix, lambda r: r.sort())

# Insertion sort
def insertion_sort(arr):
  for i in range(1, len(arr)): # N
    j = i
    while j > 0 and arr[j - 1] > arr[j]: # N
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      j = j - 1
  return arr
  # Total: N^2

matrix = gen_matrix(100, 100, 1, 100)
matrix_c = copy.deepcopy(matrix)

timer(matrix, insertion_sort)
timer(matrix, lambda r: r.sort())

# Bubble sort
def bubble_sort(arr):
  for i in range(len(arr)): # N
    for j in range(i, len(arr)): # N
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr
  # Total: N^2

matrix = gen_matrix(100, 100, 1, 100)
timer(matrix, bubble_sort)
timer(matrix, lambda r: r.sort())

# Shell sort
def shell_sort(arr):
  n = len(arr)
  step = n // 2
  while step > 0: # log N, так как step уменьшается вдвое
    for i in range(step, n): # N
      j = i
      while (j - step) >= 0 and arr[j - step] > arr[j]: # N / step
        arr[j - step], arr[j] = arr[j], arr[j - step]
        j -= step
    step //= 2
  return arr
  # Суммарно: log N * N * (N / step) = log N * N^2/step
  # Но доминирует тут: N^2

matrix = gen_matrix(100, 100, 1, 100)
timer(matrix, shell_sort)
timer(matrix, lambda r: r.sort())

# Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot] # N
        greater = [x for x in arr[1:] if x > pivot] # N
        return quick_sort(less) + [pivot] + quick_sort(greater) # N^2
    # Total: N^2

matrix = gen_matrix(100, 100, 1, 100)
timer(matrix, quick_sort)
timer(matrix, lambda r: r.sort())

import heapq

# Heap sort
def heap_sort(arr):
  heapq.heapify(arr) # N log N
  return [heapq.heappop(arr) for i in range(len(arr))] # N log N
  # Total: N log N

matrix = gen_matrix(100, 100, 1, 100)
timer(matrix, heap_sort)
timer(matrix, lambda r: r.sort())



"""### Вывод

В ходе данной лабораторной работы мы познакомились с понятием временной сложности и убедились, что алгоритмы с большей временной сложностью при $n \to \infty$ показывают худшие результаты, чем алгоритмы с более малой временной сложностью.

Однако так же заметили, что не все алгоритмы с одинаковой асимптотической сложностью $O(g(n))$ равны. Это можно объяснить влиянием константы, не учитываемой при оценке о-большого. А также тем, что алгоритмы не всегда выполняются при наихудших условиях: некоторые из них показывают лучше себя при рандомизированных входных данных, а некоторые наоборот хуже.
"""