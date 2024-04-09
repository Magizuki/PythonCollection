height = input()
weight = input()
bmi = float(int(weight)/float(height)**2)

if bmi > 35:
    print('Clinically Obese')
elif bmi > 30:
    print('Obese')
elif bmi > 25:
        print('Slightly Overweight')
elif bmi > 18.5:
    print('Normal')
else: 
    print('Underweight')
input()