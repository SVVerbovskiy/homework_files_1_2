from pprint import pprint

cook_book = {}

with open('recipe.txt', encoding='utf-8') as file:
    for recipe in file:
        recipes = recipe.strip()
        ingredients = int(file.readline(2))
        recipe_list = []
        for i in range(ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            recipe_list.append({"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure})
        cook_book[recipes] = recipe_list
        file.readline()

pprint(cook_book, sort_dicts=False, width=150)
print()


def get_shop_list_by_dishes(dishes, person):
    dishes_dict = {}
    for i in dishes:
        if i not in cook_book.keys():
            print('There is no such dish on the menu!')
            return
        else:
            ingredients_list = cook_book[i]
            for i in ingredients_list:
                y = i.setdefault('ingredient_name')
                z = {'measure': i.setdefault('measure'), 'quantity': i.setdefault('quantity') * person}
                if y not in dishes_dict.keys():
                    dishes_dict[y] = z
                else:
                    dishes_dict[y] = {'measure': i.setdefault('measure'),
                                      'quantity': i.setdefault('quantity') + dishes_dict[y]['quantity']}
    pprint(dishes_dict, sort_dicts=False)
    return


get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Драники'], 5)
