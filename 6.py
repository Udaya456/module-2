import random
#for a  3-digit code  between 0 and 9
digit1 = random.randint(0,9)
digit2= random.randint(0,9)
digit3=random.randint(0,9)
three_digit_code= str(digit1)+str(digit2)+str(digit3)

#for a 4_digit code between 1 and 6
digit1=random.randint(1,6)
digit2=random.randint(1,6)
digit3=random.randint(1,6)
digit4=random.randint(1,6)

print("3-digitcode:", three_digit_code)
print("4-digitcode:",digit1,digit2,digit3,digit4)



