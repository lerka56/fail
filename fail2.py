def read_recipes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return parse_recipes(file.read())

def parse_recipes(content):
    cook_book = {}
    lines = content.strip().split('\n')

    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        num_ingredients = int(lines[i + 1].strip())
        ingredients = []

        for j in range(num_ingredients):
            ingredient_line = lines[i + 2 + j].strip()
            ingredient_parts = ingredient_line.split(' | ')
            ingredient = {
                'ingredient_name': ingredient_parts[0],
                'quantity': int(ingredient_parts[1]),
                'measure': ingredient_parts[2]
            }
            ingredients.append(ingredient)

        cook_book[dish_name] = ingredients
        i += 2 + num_ingredients  

    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:  
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list

def display_shop_list(shop_list):
    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")

def main():
    file_path = 'recipes.txt'  
    try:
        cook_book = read_recipes(file_path)
        
        dishes_to_prepare = ['Запеченный картофель', 'Омлет']
        person_count = 2
        shop_list = get_shop_list_by_dishes(cook_book, dishes_to_prepare, person_count)
        
        display_shop_list(shop_list)
    
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()