'''
Given an array with numbers and a given index (i), write a program that efficiently answer queries of the form:
A). Which is the nearest greater number from number at position  i ?
B). What is the distance between the two array indices. 

For example in the array [1,4,3,2,5,7], the nearest greater number from 4 (index 1) is 5, and its distance between indices is 3
Additional note: the greater number can be to left or right of the given index
'''

import sys

array = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    array.append(ele)  # adding the element


given_index = int(input("Enter your given index:"))
target_number = array[given_index]
dist_near_great_num = sys.maxsize
index_greater_number = sys.maxsize

for index in range(len(array)):
    if array[index] > target_number:
        
        distance = abs(given_index - index)
        if distance < dist_near_great_num:
            index_greater_number=index
            dist_near_great_num=distance


print("the nearest greater number position is:"+ str(index_greater_number))

print("distance between the two array indices:" + str(dist_near_great_num))


