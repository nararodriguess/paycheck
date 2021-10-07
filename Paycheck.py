employee = []
def include():
    name = str(input("Employee name: ")).title()
    salary_gross = float(input("Salary: "))
    employee.append([name, salary_gross])


def inss_discount(i):
    if employee[i][1] <= 1100:
        disc = (0.075 * employee[i][1])
    elif employee[i][1] <= 2203.49:
        disc = (82.5 + ((employee[i][1] - 1100) * 0.09))
    elif employee[i][1] <= 3305.23:
        disc = (181.81 + ((employee[i][1] - 2203.49) * 0.12))
    elif employee[i][1] <= 6433.57:
        disc = (314.02 + (employee[i][1] - 3305.23) * 0.14)
    else:
        disc = 751.99
    return round(disc, 2)


def irrf_discount(i):
    base_irrf = employee[i][1] - inss_discount(i)
    if base_irrf <= 1903.98:
        disc_irrf = 0
    elif base_irrf <= 2826.65:
        disc_irrf = (base_irrf * 0.075) - 142.80
    elif base_irrf <= 3751.05:
        disc_irrf = (base_irrf * 0.15) - 354.80
    elif base_irrf <= 4664.68:
        disc_irrf = (base_irrf * 0.225) - 636.13
    else:
        disc_irrf = (base_irrf * 0.275) - 869.36
    return round(disc_irrf, 2)

def net_salary (i):
  salary_net = employee[i][1] - inss_discount(i) - irrf_discount (i)
  return salary_net

while True:

   print('--'*14)
   print(f'{"CHOICE AN OPTION":^26}')
   print('| 1 - Include an employee;\n| 2 - View the paycheck;\n| 0 - Close.')
   print('--' * 14)
   option = input("-> ")

   if option == '1':
       print('--' * 14)
       include()
   elif option == '2':
       print('--' * 14)
       which_employee = int(input("Which is the employee code: "))
       print('**' * 14)
       print(f'{"PAYCHECK":^26}')
       print(f'Name: {employee[which_employee][0]} \nSalary: R${employee[which_employee][1]} \n'
             f'INSS: {inss_discount(which_employee)} \nIRRF: {irrf_discount(which_employee)} \n'
             f'Net salary: {net_salary(which_employee)}')
       print('**' * 14)
   elif option == '0':
       break
   else:
       print("Digite um código válido.")


