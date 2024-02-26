import csv

'''
переменная s отвечает за введённое в консоль название компании
'''
while True:
    s = input()
    if s == 'None':
        break

    '''
    читаем содержимое файла в список answer
    '''
    with open('vacancy.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter=';')
        answer = list(reader)[1:]

        '''
        переменная flag принимает значение 1 только в случае, если введённое название компании есть в файле
        по умолчанию значение flag = 0, если оно не изменилось при работе цикла, значит названия компании нет в файле
        '''
        flag = 0

        '''
        переменные Salary, Work_Type, Company_Size, Role, Company отвечают за соответствующие поля в списке answer
        '''
        for Salary, Work_Type, Company_Size, Role, Company in answer:

            if Company == s:
                flag = 1
                print(f'В {Company} найдена вакансия: {Role}. З/п составит: {Salary}')

        if flag == 0:
            print('К сожалению, ничего не удалось найти')