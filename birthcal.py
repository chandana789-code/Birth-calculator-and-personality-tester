from datetime import datetime

# Function to calculate age
def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Function to give personality description based on month of birth
def personality_by_month(month):
    personality_traits = {
        1: "You are ambitious, determined, and love challenges. You're a natural-born leader!",
        2: "You are compassionate, sensitive, and intuitive. You are a dreamer and very empathetic.",
        3: "You are creative, communicative, and love socializing. You're great at making new connections.",
        4: "You are practical, hard-working, and reliable. You appreciate stability and have a strong work ethic.",
        5: "You are energetic, adventurous, and curious. You seek new experiences and love change.",
        6: "You are nurturing, protective, and deeply family-oriented. You have a strong sense of responsibility.",
        7: "You are intellectual, introspective, and have a deep understanding of life. You're a natural philosopher.",
        8: "You are confident, powerful, and determined. You're a go-getter and always aim for success.",
        9: "You are generous, compassionate, and have a great sense of humor. You're a natural entertainer.",
        10: "You are diplomatic, charming, and seek balance in all aspects of life. You have a strong sense of fairness.",
        11: "You are determined, resourceful, and have a deep emotional strength. You face challenges head-on.",
        12: "You are optimistic, adventurous, and love freedom. You're philosophical and always seeking meaning in life."
    }
    
    # Return personality trait based on month
    return personality_traits.get(month, "Invalid month")

# Main program
def main():
    # Taking user's birthdate as input
    print("Welcome to the Birth Calculator and Personality Tester!")
    birth_date_input = input("Enter your birthdate (in format YYYY-MM-DD): ")
    
    try:
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please enter a valid birthdate.")
        return
    
    # Calculate age
    age = calculate_age(birth_date)
    
    # Get personality based on month of birth
    month = birth_date.month
    personality = personality_by_month(month)
    
    # Output results
    print(f"\nYour age is: {age} years old.")
    print(f"Your personality based on your birth month ({month}): {personality}")

# Run the program
if __name__ == "__main__":
    main()
