num= int(input("enter number:"))
n = str(abs(num))
c = "1,3,5,7,9" 
v = "0,2,4,6,8"
b = 'number'.count(0)+  'number'.count(2)+ 'number'.count(4) + 'number'.count(6) + 'number'.count(8)
a = 'number'.count(1) + 'number'.count(3) + 'number'.count(5) + 'number'.count(7) + 'number'.count(9) 
if a > b :
    print(a)
elif b > a:
    print(b)    
else :
    ("agane")









number = int(input("enter youre number:\n"))
number = str(abs(number))
choose_odd = "13579"
choose_even = "02468"
odd = 0
even = 0

odd += number.count(choose_odd[0])
odd += number.count(choose_odd[1])
odd += number.count(choose_odd[2])
odd += number.count(choose_odd[3])
odd += number.count(choose_odd[4])
even += number.count(choose_even[0])
even += number.count(choose_even[1])
even += number.count(choose_even[2])
even += number.count(choose_even[3])
even += number.count(choose_even[4])

if odd > even:
    print("odd")
elif even > odd:
    print("even")
else:
    print("equal")
print("odd:", odd,"even:", even)