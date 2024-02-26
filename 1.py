import csv

'''
Вы поняли, что хотите сначала проанализировать какие профессии самые востребованные 
и высокооплачиваемые в разных компаниях. Для этого создайте таблицу vacancy_new.csv 
в которую запишите три столбца company, role, Salary. При этом сама вакансия(Role) 
должна иметь максимальный размер зарплаты в компании. После этого выведите топ-3 
самых высокооплачиваемых профессий в формате: <компания> - <вакансия> - <зарплата>
'''

with open('vacancy.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    answer = list(reader)[1:]
    print(answer)

    max_salaries = {}
    role_salary = {}
    for Salary, Work_Type, Company_Size, Role, Company in answer:
        role_salary[Company] = Role
        role_salary[Company][Role] = Salary
        max_salaries[Company] = answer[-1]
        max_salaries[Role] = answer[-2]
        max_salaries[Salary] = max(role_salary[Company][Role])



with open('vacancy_new.csv', 'w', encoding='utf8') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Company', 'Role', 'Salary'])
    writer.writeheader()
    writer.writerows(max_salaries)