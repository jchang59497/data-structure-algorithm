#Say "Hello, World!" With Python
print("Hello, World!")

#Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

##Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a//b)
    print (a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print (i,end='')