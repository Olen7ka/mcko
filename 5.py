import csv

with open('vacancy.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    answer = list(reader)[1:]

    hash_table = {}
    for Salary, Work_Type, Company_Size, Role, Company in answer:
        if Company not in hash_table[Company]:
            hash_table[Company] = Role, Salary, Work_Type
            hash_table.append(hash_table[Company])