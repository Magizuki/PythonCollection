
def prime_checker(number):
    for x in range(1, number + 1):
        if x != 1 and x != number and number % x == 0:
            print("Not prime number")
            return
    print("Prime number")

number = int(input())
prime_checker(number=number)