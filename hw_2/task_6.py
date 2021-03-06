"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя."""
"""Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например, название. Тогда значение — список значений-характеристик, например, список названий товаров."""

if __name__ == '__main__':
    invite = lambda: print('Введите 1 для добавления нового товара. \n'
                           'Введите 2 для просмотра добавленных товаров. \n'
                           'Введите 3 для получения статистики о товарах. \n'
                           'Введите 0 для завершения программы. \n')

    operation_dict = {'exit': 0,
                      'add': 1,
                      'print': 2,
                      'statistic': 3,
                      }
    product_list = []

    while True:
        invite()
        operation = int(input())

        if operation == operation_dict['add']:
            product = (input('Номер товара: '), {'название': input("Название продукта: "),
                                                 'цена': input("Цена продукта: "),
                                                 'количество': input("Кол-во продукта: "),
                                                 'единица измерения': input("Единица измерения продукта: "),
                                                 })
            product_list.append(product)
        elif operation == operation_dict['print']:
            for product in product_list:
                print(f'Номер товара: {product[0]} \n'
                      f'Название продукта: {product[1].get("название")} \n'
                      f'Цена продукта: {product[1].get("цена")} \n'
                      f'Кол-во продукта: {product[1].get("количество")} \n'
                      f'Единица измерения продукта: {product[1].get("единица измерения")} \n\n')

        elif operation == operation_dict['statistic']:
            if product_list:
                statistic_dict = {k: [] for k in product[1].keys()}
                for product in product_list:
                    for key, val in product[1].items():
                        statistic_dict[key].append(val)
                statistic_dict['единица измерения'] = list(set(statistic_dict['единица измерения']))
                print(statistic_dict)
            else:
                print('Товаров пока не добавлено. \n')

        else:
            break
