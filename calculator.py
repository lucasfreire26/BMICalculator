import datetime

class Calculator:

    name = None

    weight_in_kilos = None

    height_in_cm = None

    bmi = None

    def set_weight_in_pounds(self, stones, pounds):
        total_pounds = (stones * 14) + pounds
        total_kilos = total_pounds * 0.45
        self.weight_in_kilos = total_kilos

    def set_height_in_inches(self, feet, inches):
        total_inches = (feet * 12) + inches
        total_cm = total_inches * 2.54
        self.height_in_cm = total_cm

    def calculate_bmi(self):
        height_in_meters = self.height_in_cm / 100
        self.bmi = self.weight_in_kilos / (height_in_meters ** 2)
        return self.bmi

    def calculate_bmi_group(self):
        if self.bmi < 18.5:
            return 'Underweight'

        elif 18.5 <= self.bmi < 25:
            return 'Normal'

        elif 25 <= self.bmi < 30:
            return 'Overweight'

        elif self.bmi >= 30:
            return 'Obese'

    def save_result(self):
        # name, weight, height, bmi, group, time

        f = open("results.csv", "a")
        f.write("{},{},{},{},{},{}".format(
            self.name, self.weight_in_kilos, self.height_in_cm,
            self.bmi, self.calculate_bmi_group(),
            datetime.datetime.now()
        ))
        f.close()


calculator = Calculator()
# please pick a system: metric or imperial [m/i]:
name = input('What is your name?')
calculator.name = name

system = None

while system not in ['m','i']:
    system = input('please pick a system: metric or imperial [m/i]:')

    if system == 'm':
        height = int(input('enter your height [cm]:'))
        calculator.height_in_cm = height

        weight = int(input('enter your weight [kg]:'))
        calculator.weight_in_kilos = weight

    elif system == 'i':
        feet = int(input('enter your height [ft]:'))
        inches = int(input('enter your height [in]:'))
        calculator.set_height_in_inches(feet, inches)

        stones = int(input('enter your weight [st]:'))
        pounds = int(input('enter your weight [lb]:'))
        calculator.set_weight_in_pounds(stones, pounds)

    else:
        print('{} is not a valid system'.format(system))
        continue

print('Your BMI:', round(calculator.calculate_bmi(), 2))

print('Your BMI Group:', calculator.calculate_bmi_group())

calculator.save_result()
