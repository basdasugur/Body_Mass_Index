#Input
print("Welcome to the Body  Mass Index (BMI) calculator 2.0!")
height = float(input("Enter you height in m : "))
weight = float(input("Enter you weight in kg : "))


#Output
#BMI = (weight(kg) / height**2)

bmi = round(weight / (height ** 2), 2 )
print(f"Your Body Mass Index is {bmi}")

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they have are overweight
#Over 30 but below 35 they have are obese
#Above 35 they are clinically obese

if bmi <= 18.5:
  print(f"Your BMI score {bmi}, Underweight")
elif bmi <= 25:
  print(f"Your BMI score {bmi}, Normal Weight")
elif bmi <= 30:
  print(f"Your BMI score {bmi}, Overweight") 
elif  bmi <= 35:
  print(f"Your BMI score {bmi}, Obese")
else:
  print(f"Your BMI score {bmi}, Clinically Obese")
  
