#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(array):
    return array[len(array) - 1] == 6
print(first_last6([1, 2, 6]))
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False


#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(array):
    return array[0] == array[len(array) - 1]
print(same_first_last([1, 2, 3, 1]))
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True


#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

def common_end(a,b):
    return a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]
print(common_end([1, 2, 3], [7, 3, 2]))   
# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(array):
    count = 0
    for i in array:
        if i % 2 == 0:
            count += 1
    return count
print(count_evens([2, 1, 2, 3, 4]))
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(array):
    return max(array) - min(array)
print(big_diff([10, 3, 5, 6]))
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def average(array):
    sum = 0
    for i in range(len(array)):
        if array[i] == min(array) or array[i] == max(array):
            sum += 0
        else:
            sum += array[i]
    return sum // (len(array) - 2)


def centered_average(array):
    sum = 0
    array.sort()
    array.pop()
    array.pop(0)
    
    for i in range(len(array)):
        sum += array[i]
    return sum // (len(array))

print(centered_average([1, 1, 5, 5, 10, 8, 7]))

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(array):
    sum = 0 if array[0] == 13 else array[0]
    
    if len(array) == 0:
        return sum

    for i in range(1, len(array)):
        if array[i - 1] == 13:
            sum += 0
            continue
            
        if array[i] != 13:
            sum += array[i]
        
    return sum

print(sum13([1, 13, 13, 1, 2]))    
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13, 3]) → 6


# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(array):
    for i in range(len(array) - 1):
        if array[i] == 2 and array[i + 1] == 2:
            return True
    return False
print(has22([1, 2, 1, 2]))
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([ [i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z+1) if ((i + j + k) != n )])

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    numDict = {}
    for i in arr:
        numDict[i] = 0
    new_array = list(numDict.keys())
    new_array.sort()
    print(new_array[len(new_array)-2])

#Nested Lists
if __name__ == '__main__':
    mark_sheet = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark_sheet.append([name,score])
        score_list.append(score)
    second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]
    for name,marks in sorted(mark_sheet):
        if marks == second_lowest_mark:
            print(name)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks[query_name][scores])

#Lists
if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        arr = input().split(" ")
        command = arr[0]
        if command == 'insert':
            result.insert(int(arr[1]), int(arr[2]))
        elif command == 'print':
            print(result)
        elif command == 'remove':
            result.remove(int(arr[1]))
        elif command == 'append':
            result.append(int(arr[1]))
        elif command == 'sort':
            result == result.sort()
        elif command == 'pop':
            result.pop()
        elif command == 'reverse':
            result == result.reverse()