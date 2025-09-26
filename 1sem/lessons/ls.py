n = int(input())
count = 0

for i in range(n):
    word = input()
    if word.find('зайка') != -1:
        print(word.find('зайка')+1)
    else:
        print("Заек нет =(")
