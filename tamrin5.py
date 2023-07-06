num= int(input("Enter number : "))
if 10 < num < 16:
    num0 = float(input("Enter number"))
    if num == 11:
        m = num0 + 273.15
    elif num == 12:
        m = (num0 * 9 / 5) + 32
    elif num == 13:
        result = num0 - 273.15
    elif num == 14:
        m = (num0 - 273.15) * 9 / 5 + 32
    elif num == 15:
        m = (num0 - 32) * 5 / 9 
    else:
        m = (num0 - 32) * 5 / 9 + 273.15
    print(m)
else:
    print("again")