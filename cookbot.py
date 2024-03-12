import json
import random
from nltk.tokenize import word_tokenize

# Load recipes from JSON file
with open(r"C:\TK\recipes.json", 'r') as file:
    recipes = json.load(file)


def suggest_recipe(ingredients):
    # Find recipes that contain at least one of the provided ingredients
    possible_recipes = []
    for recipe in recipes:
        recipe_ingredients = recipe['ingredients']
        if any(ingredient in recipe_ingredients for ingredient in ingredients):
            possible_recipes.append(recipe)

    if possible_recipes:
        # Pick a random recipe from the possible ones
        suggested_recipe = random.choice(possible_recipes)

        # Print the suggested recipe
        print("I suggest making", suggested_recipe['name'] + ". Here are the ingredients you'll need:")
        for ingredient in suggested_recipe['ingredients']:
            print("-", ingredient)
        print("Instructions:")
        print(suggested_recipe['instructions'])
    else:
        print("Sorry, I couldn't find a recipe with those ingredients.")


# Main loop for interacting with the user
def main():
    print("Welcome to the Chef Tharun Bot!")
    while True:
        user_input = input("Please enter up to 5 ingredients (separated by commas): ").lower()
        user_ingredients = word_tokenize(user_input)[:5]  # Tokenize the user input and take the first 5 tokens
        suggest_recipe(user_ingredients)

        user_choice = input("Would you like to suggest another recipe? (yes/no): ").lower()
        if user_choice != 'yes':
            print("Okay, goodbye!")
            break


if __name__ == "__main__":
    main()
