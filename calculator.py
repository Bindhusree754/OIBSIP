def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kilograms and height in meters.
    """
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    
    return weight / (height ** 2)

def classify_bmi(bmi):
    """
    Classify the BMI value into categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        
        if weight <= 0:
            raise ValueError("Weight must be greater than 0")
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"Your BMI is {bmi:.2f}")
        print(f"Category: {category}")
    
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
