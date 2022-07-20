from pprint import pprint

cook_book = {}

with open('recipe.txt', encoding='utf-8') as file:
    for recipe in file:
        recipes = recipe.strip()
        ingredients = int(file.readline(2))
        recipe_list = []
        for i in range(ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            recipe_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[recipes] = recipe_list
        file.readline()

pprint(cook_book, sort_dicts=False, width=150)


def get_shop_list_by_dishes(dishes):
    dishes_list = []
    for k, v in cook_book.items():
        dishes_list.append(k)
    ingredient_dict = {}
    ingredient_list = []
    for i in dishes:
        if i not in dishes_list:
            print('There is no such dish on the menu!')
            break
    for k, v in cook_book.items():
        ingredient_list.append(v)
    for item in ingredient_list:
        for j in item:
            for k, v in j.items():
                print(k, v)
    print(ingredient_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'])
