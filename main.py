import random
import time

def test(arr, sort, sortBy):
    print(sort)
    start_time = time.time()
    if sortBy == "choice":
        sortByChoice(arr)
    elif sortBy == "quick":
        quickSort(arr, 0, len(arr) - 1)
    end_time = time.time()
    duration = (end_time - start_time) * 1000
    print("Время: " + str(duration) + " мс\n")

def generateArray(number):
    arr = [random.randint(1, 800) for _ in range(number)]
    return arr

def generateSortArray(number):
    arr = [i for i in range(number)]
    return arr

def generateBadArray(number):
    arr = [i for i in range(number - 1, -1, -1)]
    return arr

def sortByChoice(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quickSort(array, low, high):
    if len(array) == 0:
        return
    if low >= high:
        return
    middle = low + (high - low) // 2
    pivot = array[middle]
    i, j = low, high
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if low < j:
        quickSort(array, low, j)
    if high > i:
        quickSort(array, i, high)

arrMedium = generateArray(1000)
arrMedium2 = generateArray(100000)
arrBad = generateBadArray(1000)
arrBad2 = generateBadArray(100000)
arrGood = generateSortArray(1000)
arrGood2 = generateSortArray(100000)

# Средний случай
test(arrMedium, "Средний случай, сортировка выборкой, 1000 элементов", "choice")
test(arrMedium, "Средний случай, быстрая сортировка, 1000 элементов", "quick")
test(arrMedium2, "Средний случай, сортировка выборкой, 100.000 элементов", "choice")
test(arrMedium2, "Средний случай, быстрая сортировка, 100.000 элементов", "quick")

# Лучший случай
test(arrGood, "Лучший случай, сортировка выборкой, 1000 элементов", "choice")
test(arrGood, "Лучший случай, быстрая сортировка, 1000 элементов", "quick")
test(arrGood2, "Лучший случай, сортировка выборкой, 100.000 элементов", "choice")
test(arrGood2, "Лучший случай, быстрая сортировка, 100.000 элементов", "quick")

# Худший случай
test(arrBad, "Худший случай, сортировка выборкой, 1000 элементов", "choice")
test(arrBad, "Худший случай, быстрая сортировка, 1000 элементов", "quick")
test(arrBad2, "Худший случай, сортировка выборкой, 100.000 элементов", "choice")
test(arrBad2, "Худший случай, быстрая сортировка, 100.000 элементов", "quick")
