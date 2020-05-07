import pygame
import os
import time
import random

x = 100
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

width = 1640
height = 980

pygame.init()
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen.fill(black)

pygame.display.set_caption("Sorting Algorithm Visualizer")

def createArr(bar_size):
    i = 0
    while i < width:
        value = random.randint(0, height)
        pygame.draw.rect(screen, white, (i, height - value, bar_size, height))
        arr.append(value)
        i += bar_size

    pygame.display.flip()
    return arr

def bubbleSort(arr, bar_size):
    pygame.display.set_caption("Bubble Sort")
    for iter_number in range(len(arr) - 1, 0, -1):
        for index in range(iter_number):
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp
                if index % 80 == 0:
                    x = 0
                    screen.fill(black)
                    for j in range(len(arr)):
                        pygame.draw.rect(screen, white, (x, height - arr[j], bar_size, height))
                        x += bar_size
                    pygame.display.flip()
    x = 0
    screen.fill(black)
    for j in range(len(arr)):
        pygame.draw.rect(screen, white, (x, height - arr[j], bar_size, height))
        x += bar_size
    pygame.display.flip()
    screen.fill(black)

def insertionSort(arr, bar_size):
    pygame.display.set_caption("Insertion Sort")
    for i in range(1, len(arr)):
        j = i - 1
        nxt_element = arr[i]

        while (arr[j] > nxt_element) and (j >= 0):
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = nxt_element
        x = 0
        screen.fill(black)
        for j in range(len(arr)):
            pygame.draw.rect(screen, white, (x, height - arr[j], bar_size, height))
            x += bar_size
        pygame.display.flip()
    screen.fill(black)

def shellSort(arr, bar_size):
    pygame.display.set_caption("Shell Sort")
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            if i % 5 == 0:
                x = 0
                screen.fill(black)
                for j in range(len(arr)):
                    pygame.draw.rect(screen, white, (x, height - arr[j], bar_size, height))
                    x += bar_size
                pygame.display.flip()
        gap = gap // 2
    x = 0
    screen.fill(black)
    for j in range(len(arr)):
        pygame.draw.rect(screen, white, (x, height - arr[j], bar_size, height))
        x += bar_size
    pygame.display.flip()
    screen.fill(black)

def selectionSort(arr, bar_size):
    pygame.display.set_caption("Selection Sort")
    for idx in range(len(arr)):

        min_idx = idx
        for j in range( idx + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        x = 0
        screen.fill((0, 0, 0))
        for j in range(len(arr)):
            pygame.draw.rect(screen, white, (x, height - arr[j], bar_size, height))
            x += bar_size
        pygame.display.flip()
    screen.fill(black)





bar_size = 3

arr = []
arr = createArr(bar_size)
time.sleep(1)
bubbleSort(arr, bar_size)
time.sleep(1)

arr = []
arr = createArr(bar_size)
time.sleep(1)
insertionSort(arr, bar_size)

arr = []
arr = createArr(bar_size)
time.sleep(1)
shellSort(arr, bar_size)

arr = []
arr = createArr(bar_size)
time.sleep(1)
selectionSort(arr, bar_size)

time.sleep(1)
pygame.quit()