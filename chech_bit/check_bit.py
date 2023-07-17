def check_bit(number,check):
    for i in range(check):
        number >>= 1
    if number & 1:
        return 1
    else:
        return 0

number=int(input("Enter the Number : "))
check=int(input("Enter the Bit to Check : "))
print(check_bit(number,check))