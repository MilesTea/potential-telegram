cook_book = dict()
with open('recipes.txt', encoding='UTF-8') as file:
    for line in file:
        food_name = line.strip()
        count = int(file.readline())
        temp_list = list()
        for i in range(count):
            row = file.readline().split('|')
            temp_list.append({'ingredient_name': row[0].strip(), 'quantity': int(row[1].strip()), 'measure': row[2].strip()})
        cook_book[food_name] = temp_list
        file.readline()


def get_shop_list_by_dishes(dishes, person_count=1):
    ingredients_dict = dict()
    temp_dict = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name in temp_dict:
                if temp_dict[name]['measure'] == measure:
                    temp_dict[name]['quantity'] += quantity
                else:
                    return 'Ошибка, измерения ингредиентов не сходятся'
            else:
                amount = {'measure': measure, 'quantity': quantity}
                temp_dict[name] = amount

    return temp_dict


print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3))
