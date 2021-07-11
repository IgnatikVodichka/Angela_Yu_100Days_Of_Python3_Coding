

def prime_checker(suspect):

    is_prime = True

    for i in range(2, suspect - 1):
        if suspect % i == 0:
            is_prime = False

    if is_prime == False:
        print(f"The {suspect} is not a prime number!")
    else:
        print(f"The {suspect} is a prime number!")


prime_checker(1)
