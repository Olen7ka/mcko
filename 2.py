import csv

def quik_sort(array, value):
    #array - массив, который нужно отсортировать
    #value - критерий, по которому нужно отсортировать
    pivot = array[0][value]

    left = [x for x in array if array[0] <= pivot]
    right = [x for x in array if array[0] > pivot]
    return quik_sort(left, value) + array[0] + quik_sort(right, value)

answer = []
with open('vacancy.csv', 'r', encoding='utf8') as f:
    reader = list(csv.reader(f, delimiter=';'))[1:]


    for Salary, Work_Type, Company_Size, Role, Company in reader:
        answer.append(quik_sort(reader, 2))
for Salary, Work_Type, Company_Size, Role, Company in answer:
    if 'классный руководитель' in Role:
        print(f'В компании {Company} есть заданная профессия: {Role}, з/п в такой компании составит: {Salary}')