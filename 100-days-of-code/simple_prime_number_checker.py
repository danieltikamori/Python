# Very simple prime number checker

def prime_checker(number: int) -> None:
    """
    Check if a given number is prime.

    Args:
        number (int): The number to be checked.

    Returns:
        None
    """
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Input the number to be checked: ")) # Check this number
prime_checker(number=n)
