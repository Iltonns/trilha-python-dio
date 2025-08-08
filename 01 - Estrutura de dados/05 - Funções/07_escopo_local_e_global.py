salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)

def funcao(*args, **kwargs):
    print(args)
    print(kwargs)


n = funcao("python", 2022, curso="dio")
print(n)
