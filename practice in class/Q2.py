import random

def ball_lottery(number):
    if number < 2 or number > 20:
        print("Error: Input must be between 2 and 20")
    else:
        total = number
        result_pick = 0
        while True:
            random_n1 = random.randint(1, 10)
            random_n2 = random.randint(1, 10)
            if random_n1 + random_n2  == total:
                result_pick += 1
                print(f"Result of picks {result_pick}: {random_n1} + {random_n2}")
                break
            else:
                result_pick += 1
                print(f"Result of picks {result_pick}: {random_n1} + {random_n2}")
                
        print(f"You got your total in {result_pick} picks!")

def main():
    print("Ball lottery")
    print("=============")
    number = int(input("Enter the number you choose: "))
    ball_lottery(number)

main()
