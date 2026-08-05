def check_disarium(num):
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = num // 100

    total= (hundreds ** 1) + (tens ** 2) + (ones ** 1)

    if total == num:
        print(num, "is a disarium number")
    else:
        print(num, "is NOT a disarium number")

number = int(input("Enter a 3-digit number:"))
check_disarium(number)
        