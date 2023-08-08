print('Welcome to the BMI Calculator.')
weight = float(input('What is your weight in kg?\n'))
height = float(input('What is your height in meters?\n'))   
bmiHeight = height ** 2 
bmi = int(weight // bmiHeight)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, and you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, and you are normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, and you are over weight.')
elif bmi <  35:
    print(f'Your BMI is {bmi}, and you are obese.')
else:
    print(f'Your BMI is {bmi}, and you are clinically obese.')
