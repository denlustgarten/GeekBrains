"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""


def dig_count(remain_seq_len: int, find_dig: int, count: int) -> int:
    if remain_seq_len > 0:
        num = int(input(f"Введите число (осталось ввести {remain_seq_len} чисел): "))
        while num > 0:
            dig = num % 10
            num //= 10
            if dig == find_dig:
                count += 1
        return dig_count(remain_seq_len - 1, find_dig, count)
    else:
        return count


sequence_len = int(input("Введите длину последовательности: "))
find_digit = int(input("Введите цифру, которую необходимо найти: "))
count_dig = dig_count(sequence_len, find_digit, 0)
print(f'В веденной последовательности чисел, цифра {find_digit} встретилась {count_dig} раз')
