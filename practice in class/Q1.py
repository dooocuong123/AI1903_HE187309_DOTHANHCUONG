
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n% i==0:
            return False
    return True
def find_prime(input_string):
    prime_numbers = []
    numbers = input_string.split()
    for number in numbers:
        try:
            num = int(number)
            if is_prime(num):
                prime_numbers.append(num)
        except ValueError:
            pass
    return prime_numbers
def largest_prime(n):
    a = max(n)
    return a
def total_prime(list):
    total=0
    for num in list:
        total += num
    return total
def print_list_without_brackets(lst):
    for item in lst:
        print(item, end=" ")
def main():
    print("The prime numbers")
    print("==================")
    input_string = input("The sequence of numbers:")
    prime_number = find_prime(input_string)
    large_p = largest_prime(prime_number)
    total = total_prime(prime_number)
    print("The prime numbers:",end=" ")
    for item in prime_number:
        print(item, end=" ")
    print()
    print("The largest number:", large_p)
    print("you got the total of the prime number:", total)
main()


    