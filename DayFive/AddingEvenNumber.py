target = int(input())

total_even_number = 0
for n in range(2, target+1, 2):
    total_even_number += n

print(str(total_even_number))