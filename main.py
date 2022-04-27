# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=round((float(weight) / float(height)** 2))
if bmi <= 18.5:
  print(f"Your BMI is {int(bmi)}, you are \033[1m underweight.\033[0m")
  
print(f"Your BMI is {int(bmi)}")



