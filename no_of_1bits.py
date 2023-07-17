def count_one_bits(num):
    binary=bin(num)
    count=binary.count('1')
    return count
num=int(input("enter a number:"))
print(count_one_bits(num))
