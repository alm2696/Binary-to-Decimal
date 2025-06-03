# Function to convert binary to decimal
def bin_to_dec(bin_str):
    dec = 0
    power = 0

    # Iterate through the binary string from right to left
    for digit in reversed(bin_str):
        if digit == '1':
            dec += 2 ** power
        power += 1
    return dec

# Input a binary number as a string
bin_str = input("Enter a binary number: ")

# Check if the input is a valid binary string (contains only '0' and '1')
if all(bit in '01' for bit in bin_str):
    dec_result = bin_to_dec(bin_str)
    print(f"The decimal representation of {bin_str} is {dec_result}")
else:
    print("Invalid binary input. Try again!")