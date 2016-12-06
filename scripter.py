
filename = open('out', 'r')
attribute_order = {0: 'director_name', 1: 'actor_2_name', 2 :'genres', 3: 'actor_1_name', 4:'outcome'}


setter = {}
for it in attribute_order.values():
    setter[it] = set()
print(setter)


for line in filename:
    temp = line.split(",")

    index = 0
    for vl in temp:
        setter[attribute_order[index]].add(vl)
        index = index+ 1

for k, v in setter.items():
    print(k)
    print(v)
# filename = open('car', 'r')
# attribute_order = {0: 'director_name', 1: 'actor_2_name', 2: 'gross', 3:'genres', 4: 'actor_1_name', 5: 'budget', 6:'outcome'}
#
# filewrit = open('out', 'a')
#
# setter = {}
# for it in attribute_order.values():
#     setter[it] = set()
#
#
# for line in filename:
#     new_line = ""
#     temp = line.split(",")
#     if '' in temp or "\n" in temp:
#         continue
#     temp.append("")
#
#     index = 0
#
#     for vl in temp:
#         if index == 2 or index == 5:
#             index = index + 1
#             continue
#         if index == 6:
#             if int(temp[5]) - int(temp[2]) > 0:
#                 new_line = new_line + "Success"
#                 index = index + 1
#             else:
#                 new_line = new_line + "Flop"
#                 index = index + 1
#             break
#         new_line = new_line + vl + ","
#         index = index + 1
#
#     filewrit.write(new_line + "\n")
#
#
#
#
#
#
#
#
#
