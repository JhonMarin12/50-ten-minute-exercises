# Summing numbers

def mysum(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result

print(mysum(1,2,3,4))