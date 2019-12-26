def fib(n):
    lst = []
    a = 0
    b = 1
    flag = True
    while flag:
        c = a + b
        a = b
        b = c
        if b > n:
            flag = False
        lst.append(b)
    return lst

fibo = fib(4000000)
print(fibo)

def checkeven(lst):
    even = []
    for i in lst:
        if i % 2 is 0:
            even.append(i)
    return even

evenlst = checkeven(fibo)
print(evenlst)

evensum = sum(evenlst)
print(evensum)
