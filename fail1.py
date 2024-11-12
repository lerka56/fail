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

def display_cook_book(cook_book):
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  - {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
        print()  

def main():
    file_path = 'recipes.txt' 
    try:
        cook_book = read_recipes(file_path)
        display_cook_book(cook_book)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()