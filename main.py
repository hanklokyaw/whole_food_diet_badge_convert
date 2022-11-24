import csv

diet_num_list = []
product_diet_list = []
count = 0

with open('diet.csv', 'r', newline='') as file:
    diet_var = csv.reader(file)
    for i in diet_var:
        diet_num_list.append(i)

with open('produce_default.csv', 'r', newline='') as file:
    diet_var = csv.reader(file)
    for i in diet_var:
        product_diet_list.append(i)

# print(diet_num_list)
# print(product_diet_list)
# print(diet_num_list[2])
# print(diet_num_list[2][:1])
# print(diet_num_list[0:][1:])

# first loop to fill up match cases
for product_id in range(1, len(product_diet_list)):
    # print(product_diet_list[product_id][1:])
    for diet_id in range(1, len(diet_num_list)):
        # print(diet_num_list[diet_id][1:])
        if product_diet_list[product_id][1:] == diet_num_list[diet_id][1:]:
            # the following print statement is to log the output and track error
            # print('>>>', product_diet_list[product_id][0:], ' >>>', diet_num_list[diet_id][0:])
            product_diet_list[product_id][:1] = diet_num_list[diet_id][:1]
        elif product_diet_list[product_id][1:] != diet_num_list[diet_id][1:] and product_diet_list[product_id][:1] == \
                [''] and diet_num_list[diet_id][:1] == [f'{len(diet_num_list) - 1}']:
            # the following print statement is to log the output and track error
            # print('===', product_diet_list[product_id][0:], ' ===', diet_num_list[diet_id][0:])
            product_diet_list[product_id][:1] = [f'{len(diet_num_list)}']
            diet_num_list.append(product_diet_list[product_id][0:])

# fill in first empty id
# for product_id in product_diet_list:
#     if product_id in diet_num_list:
#         print("they have")
#     else:
#         print(len(diet_num_list) + count)
#         print(product_id[:1])
#         product_diet_list[:1] = [f'{len(diet_num_list) + count}']
#         count += 1
#         print(product_id[:1])
#         break

# second loop to fill up unmatch cases
# for diet_id in range(1, len(diet_num_list)):
#     # print(diet_num_list[diet_id][1:])
#     for product_id in range(1, len(product_diet_list)):
#         # print(product_diet_list[product_id][1:])
#         # print(product_diet_list[product_id][:1])

        # if product_diet_list[product_id][:1] == ['']:
        #     product_diet_list[product_id][:1] = [f'{len(diet_num_list) + 1}']

#     # for j in range(1, len(product_diet_list)):
#     #     if product_diet_list[j][1:] != diet_num_list[diet_id][1:]:
#     #         print(product_diet_list[j][1:])
#     #         print(diet_num_list[diet_id][1:])
#     #         diet_num_list.append(f'{len(diet_num_list) + 1},{diet_num_list[diet_id]}')

# print(diet_num_list)
# print(product_diet_list)

print('\n\n')

for i in diet_num_list:
    print(i)

for i in product_diet_list:
    print(i)

with open('diet_output.csv', 'w', newline='') as file:
    diet_output = csv.writer(file)
    diet_output.writerows(diet_num_list)

with open('product_output.csv', 'w', newline='') as file:
    product_output = csv.writer(file)
    product_output.writerows(product_diet_list)