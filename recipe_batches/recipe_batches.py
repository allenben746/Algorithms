#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  totals = []
  if len(recipe) is not len(ingredients):
    return 0
  for i in recipe:
    if i in ingredients:
      totals.append(ingredients[i] // recipe[i])
      print(" totals :", totals)
    else:
      totals.append(0)
  return min(totals) 


recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 51, 'flour': 51 }
recipe_batches(recipe, ingredients)
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))