num = int(input("Enter : "))

def check(num):
    if num%2==0: 
        print("Even")
    else: 
        print("odd")



def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")


def sum(num):
    sum = 0
    for i in range(num+1):
        sum+=i

    return sum


def square(num):
    sum = 0
    for i in range(num+1):
        sum+=i*i

    return sum

def dice_problem(num):
    if num == 1:
        return 6
    elif num == 2:
            return 5
    elif num == 3:
            return 4
    elif num == 4:
            return 3
    elif num == 5:
            return 2
    elif num == 6:
            return 1
    else:
         return 0
# print(dice_problem(num))

def sum_of_digits(num):
    sum=0
    while num > 0:
          rem = num % 10
          sum+=rem
          num = num//10
    return sum

def reverse_digits(num):
    r_digit=0
    while num > 0:
          rem = num % 10
          r_digit = r_digit*10 + rem
          num = num//10
    return r_digit


def check_prime(num):
    if num == 0 or num == 1:
        return "Not Prime"

    for i in range(2,round(num**0.5)+1):
        if num%i == 0:
            return "Not Prime"

    return "Prime"


# def power_testing(num):
#     num1 = int(input("Enter : "))
#     for i in range()


     
print(check_prime(num))
          