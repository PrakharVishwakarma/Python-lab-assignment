def largest_num(x, y, z):  # function for finding the largest number out of three input number
    if x > y:
        if x > z:
            return x
        else:
            return z

    elif y > x:
        if y > z:
            return y
        else:
            return z
        
num1 = int(input("Enter 1st number : ")) 
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))  

print("Largest number is : ", largest_num(num1, num2, num3))