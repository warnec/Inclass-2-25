def calcFib(n):
    if n<0:
        print("You must enter a value of 0 or greater")
        return None
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return calcFib(n-1)+calcFib(n-2)

def calcFactorial(b):
    fact = 1
    for i in range(1, b + 1):
        fact = fact * i

    return fact

def main():
    result = calcFib(3)
    print(result)
    result2 = calcFactorial(5)
    print(result2)

main()

