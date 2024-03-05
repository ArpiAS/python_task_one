# 1. Создайте функцию merge_lists_to_dict
# 2. У функции должно быть два параметра
# 3. Функция должна объединять два списка, используя встроенную функцию zip
# 4. Конвертируйте объект zip в словарь и верните его из функции
# 5. Вызовите функцию, передав ей два списка в качестве аргументов
# 6. Выведите результат вызова функции в терминал

def merge_lists_to_dict(fruits, price):
    zip_file= zip(fruits, price)
    result_dict = dict(zip_file)
    return result_dict
 

fruits = ['apple', 'orange', 'banana']
price = [10, 15, 30]

result = merge_lists_to_dict(fruits, price)

print(result)
    
