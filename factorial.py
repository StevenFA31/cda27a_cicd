"""

Module pour calculer la factorielle

"""

import time

final_list = []


def factorial(n):
    """
    Fonction pour calculer la factorielle de n

    Args:
        n : nombre

    Returns:
        la factorielle
    """
    time.sleep(.1)
    factorial = 1

    for i in range(1, n+1):
        factorial = factorial * i

    return factorial


def sum_factorial():
    """
    Fonction pour calculer la factorielle de n

    Args:
        n : nombre

    Returns:
        la factorielle
    """
    for i in range(50):
        final_list.append(factorial(i))
    result = sum(final_list)
    print(f"Final SUM = {result}")

    return result


if __name__ == "__main__":
    sum_factorial()
