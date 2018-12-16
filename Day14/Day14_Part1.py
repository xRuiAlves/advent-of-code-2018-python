input = 74501
recipes = [3, 7]
e1 = 0
e2 = 1

while len(recipes) < input + 11:
    new_recipe = map(int, list(str(recipes[e1] + recipes[e2])))
    recipes += new_recipe
    e1 = (e1 + recipes[e1] + 1) % len(recipes)
    e2 = (e2 + recipes[e2] + 1) % len(recipes)

print(recipes[input:input+10])