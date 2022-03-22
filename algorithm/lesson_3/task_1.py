"""В диапазоне натуральных чисел от 2 до 99 определить, сколько
из них кратны каждому из чисел в диапазоне от 2 до 9."""

count_dict = {}
for div in range(2, 10):
    count_dict[div] = 99 // div

for key, val in count_dict.items():
    print(f'{key}: {val}')
