import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

updated_list = []
for num in random_numbers:
    if num > 50:
        updated_list.append(random.randint(20, 30))
    elif num < 50:
        updated_list.append("XX")
    else:
        updated_list.append(num)

print(f"Original list: {random_numbers}")
print(f"Updated list:  {updated_list}")