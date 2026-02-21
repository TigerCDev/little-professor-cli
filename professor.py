"""
Little Professor CLI

A math quiz generator that adapts difficulty by level (1–3).
Users are given 10 addition problems with up to 3 attempts each.
"""

import random

def main():
    level = get_level()
    score = run_quiz(level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n

        except ValueError:
            continue

def run_quiz(n):

    point = 0

    #find the low & high
    low = 10 ** (n-1)
    high = 10 ** n - 1
    if n == 1:
        low = 0

    #get questions
    for _ in range(10):
            x, y = random.randint(low, high), random.randint(low, high)
            answer = x + y

            for _ in range(3):
                try:
                    user = int(input(f"{x} + {y} = "))
                    if user == answer:
                        point += 1
                        break
                    else:
                        print("EEE")

                except ValueError:
                    print("EEE")
            else:
                print(f"{x} + {y} = {answer}")

    return point


if __name__ == "__main__":
    main()
