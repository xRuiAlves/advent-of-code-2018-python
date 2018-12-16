input = [0, 7, 4, 5, 0, 1]

recipes = [3, 7]
e1 = 0
e2 = 1

while True:
    new_recipe = map(int, list(str(recipes[e1] + recipes[e2])))
    recipes += new_recipe
    e1 = (e1 + recipes[e1] + 1) % len(recipes)
    e2 = (e2 + recipes[e2] + 1) % len(recipes)
    idx = len(recipes) - 6
    for shift in range(2):
        if input[0] == recipes[idx - shift] and input[1] == recipes[idx-shift+1] and input[2] == recipes[idx-shift+2] and input[3] == recipes[idx-shift+3] and input[4] == recipes[idx-shift+4] and input[5] == recipes[idx-shift+5]:
            print(idx-shift)
            raise SystemExit