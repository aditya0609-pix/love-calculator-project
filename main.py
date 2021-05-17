print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
conames= name1+name2
lname=conames.lower()
T=lname.count("t")
R=lname.count("r")
U=lname.count("u")
E=lname.count("e")
f_digit=T+R+U+E
L=lname.count("l")
O=lname.count("o")
V=lname.count("v")
E=lname.count("e")
l_digit=L+O+V+E
total_digit=f_digit+l_digit
if total_digit<10 or total_digit>90:
  print(f"your score is{total_digit},you go together like coke and mentos")
elif total_digit >40 and total_digit <50:
  print(f"your score is{total_digit},you are alright together")
else:
  print(f"your score is{total_digit}")  


  





