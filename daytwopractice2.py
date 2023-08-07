print('Welcome to the BMI Calculator.')
weight = float(input('What is your weight in kg?\n'))
height = float(input('What is your height in meters?\n'))
bmiHeight = height ** 2 
bmi = int(weight // bmiHeight)
print(bmi)