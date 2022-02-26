"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу."""


def sum_numbers_in_str(num_str: str) -> (float, bool):
    try:
        stop_flag = False
        stop_index = len(num_str)
        if 'q' in num_str:
            stop_index = num_str.index('q')
            stop_flag = True
        return sum([float(num) for num in num_str[:stop_index].split()]), stop_flag
    except ValueError:
        print("Введены некорректные данные!")
        return None


if __name__ == '__main__':
    accumulator = 0
    new_sum = 0
    stop = 0
    while True:
        input_str = input('Введите строку их чисел, символ "q" означает окончание программы: ')
        new_sum, stop = sum_numbers_in_str(input_str)
        accumulator += new_sum
        print(f'{accumulator = }')
        if stop:
            break
