#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    lowest_amount = None

    for key in recipe:
        if key not in ingredients:
            return 0

        num_of_times = ingredients[key] // recipe[key]
        if lowest_amount is None or num_of_times < lowest_amount:
            lowest_amount = num_of_times

    return lowest_amount




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
