def hex_to_decimal(hex_string):
    try:
        decimal_value = int(hex_string, 16)
        print(f"The decimal value of {hex_string} is {decimal_value}.")
    except ValueError:
        print(f"{hex_string} is not a valid hexadecimal string.")


hex_string = input("Enter a hexadecimal string: ")
hex_to_decimal(hex_string)
