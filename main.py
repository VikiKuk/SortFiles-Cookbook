def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        for ingredients in dictionary[dish]:
            ingredient_count = int(ingredients['quantity']) * int(person_count)
            if ingredients['ingredient_name'] in all_ingredients:
                all_ingredients[ingredients['ingredient_name']]['quantity'] += ingredient_count
            else:
                all_ingredients[ingredients['ingredient_name']] = {}
                all_ingredients[ingredients['ingredient_name']]['measure'] = ingredients['measure']
                all_ingredients[ingredients['ingredient_name']]['quantity'] = ingredient_count

    print('Для приготовления ', dishes, 'необходимы следующие ингредиенты:')
    print(all_ingredients)

def save_filedata_to_list(name_file):
    list = []
    with open(name_file, 'r') as file:
        file_contents = file.read()
        line_count = len(file_contents.split('\n'))
        list.append(file.name)
        list.append(line_count)
        list.append(file_contents)
    return (list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dictionary = {}
    with open("recipes.txt", "r") as file:
        while True:
            dishes = file.readline()
            if not dishes:
                break
            if dishes.strip() == '':
                dishes = file.readline()
            dishes = dishes.strip()
            dictionary[dishes] = dishes
            count_dishes = file.readline().strip()
            dictionary[dishes] = []
            for m in range(int(count_dishes)):
                ingredients = {}
                k = file.readline().strip().split('|')
                ingredients['ingredient_name'] = k[0]
                ingredients['quantity'] = k[1]
                ingredients['measure'] = k[2]
                dictionary[dishes].append(ingredients)
    print('Книга рецептов:')
    print(dictionary)
    print()

    get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
    print()
    files = [save_filedata_to_list('1.txt'), save_filedata_to_list('2.txt'), save_filedata_to_list('3.txt')]
    sorted_list = sorted(files, key=lambda x: x[1])

    for k in sorted_list:
        for l in k:
            print(l)
        print()
