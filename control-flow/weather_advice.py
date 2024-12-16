# Compact Version:
# Weather recommendation program

# Constants for weather types
SUNNY = "sunny"
RAINY = "rainy"
COLD = "cold"

# Prompt user for the weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Recommendations using if-elif-else for clarity
if weather == SUNNY:
    recommendation = "Wear a t-shirt and sunglasses."
elif weather == RAINY:
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather == COLD:
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."

print(recommendation)

"""
# Weather  recommendation program: initial version

# Prompt user for the weather condition
weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
"""
