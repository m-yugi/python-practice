x = len(digits)
if (x == 1):
    return digits[0] + 1
else:
    temp = digits[x - 1] + 1
    digits.insert(temp, x - 1)
return digits