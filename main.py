def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro: "))

count = 0
number = 2

while count < n:
    if is_prime(number):
        print(number)
        count += 1
    number += 1
