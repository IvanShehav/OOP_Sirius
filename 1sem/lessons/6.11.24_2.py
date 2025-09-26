# last_name = {}
# for _ in range(int(input())):
#     name = input()
#     last_name[name] = last_name.get(name, 0) + 1
#
# last_name = dict(sorted(last_name.items()))
#
# flag = False
#
# for name in last_name:
#     if last_name[name] > 1:
#         print(name, '-', last_name[name])
#         flag = True
#
# if not flag:
#     print("Однофамильцев нет")
#


n, m = int(input()), int(input())

list1 = set()
list2 = set()

for _ in range(n+m):
    string = input()
    if string in list1:
        list2.add(string)
    else:
        list1.add(string)

res = set(list1) ^ set(list2)

if len(res) != 0:
    for word in sorted(res):
        print(word)
else:
    print("Таких нет")
