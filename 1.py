with open("D:\Job\Python\dataset_3363_4.txt") as inf:
    read = inf.readlines()
print(read)
tabl = []
for i in read:
    boy = i.strip().split(';')
    tabl.append(boy)
print(tabl)


def average_1_boy():
    average = 0
    tabl_average = []
    for i in range(len(tabl)):
        for j in range(len(boy)):
            if tabl[i][j].isdigit():
                average += int(tabl[i][j])
        average = average / (len(boy) - 1)
        tabl_average.append(average)
        average = 0
    return tabl_average


print(average_1_boy())


def average_all_boy():
    math = 0
    physics = 0
    rus = 0
    tabl_average = []
    for i in range(len(tabl)):
        for j in range(len(boy)):
            if j == 1:
                math += int(tabl[i][j])
            elif j == 2:
                physics += int(tabl[i][j])
            elif j == 3:
                rus += int(tabl[i][j])
    tabl_average = [math / len(tabl), physics / len(tabl), rus / len(tabl)]
    return tabl_average


print(average_all_boy())
tabl_test = []
tabl_test = average_1_boy() + average_all_boy()
print(tabl_test)
with open("D:\Job\Python\dataset_3363_4 — копия.txt", 'w') as inf:
    for line in average_1_boy():
        inf.write(f"{line}\n",)
    for line in average_all_boy():
        inf.write(f"{line}\t")
