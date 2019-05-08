
import os 
import time 

def cal_fib(n):
    start_time = time.time()
    print(fib(n), " ", time.time() - start_time, " seconds")

def fib(n): 
    start_time = time.time()
    if n < 0:
        return 0 
    if n <= 2: 
        return 1
    if n > 2: 
        return fib(n-2) + fib(n-1)

def fib_up(n): 
    start_time = time.time()
    if n < 0: 
        print(n, " ", time.time() - start_time, " seconds")
        return 0
    a = 0 
    b = 1
    c = 1
    for i in range(2, n+1):
        c = a + b 
        a = b 
        b = c
    print(c, " ", time.time() - start_time, " seconds")
    return c 

def listsum(numlist):
    start_time = time.time()
    thesum = 0 
    for i in numlist: 
        thesum = thesum + i
    print(thesum, " ", time.time() - start_time, " seconds")


fibArray = [1, 1]
def fibonacci(n):
    if n < 0: 
        print(n)
    elif n <= len(fibArray):
        return fibArray[n-1]
    else:
        temp_fib = fibonacci(n-1) + fibonacci(n-2)
        fibArray.append(temp_fib)
        return temp_fib

def fib_down(n):
    start_time = time.time()
    print(fibonacci(n), " ", time.time() - start_time, " seconds")



    
    


if __name__ == "__main__":
    cal_fib(3)
    fib_up(24000)  
    # listsum([10, 12,23,23,232,32,323,23,23,23,123])
    fib_down(650)

