def calcFib(n):
    if n<0:
        print("You must enter a value of 0 or greater")
        return None
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)