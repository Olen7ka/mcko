import csv

#переменная s отвечает за введённое в консоль название компании
while True:
    s = input()
    if s == 'None':
        break

    with open('vacancy.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter=';')
        answer = list(reader)[1:]
        print(answer)

        flag = 0
        for Salary, Work_Type, Company_Size, Role, Company in answer:

            if Company == s:
                flag = 1
                print(f'В {Company} найдена вакансия: {Role}. З/п составит: {Salary}')

        if flag == 0:
            print('К сожалению, ничего не удалось найти')