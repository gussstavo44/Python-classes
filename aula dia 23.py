##aula dia 23

class Cachorro:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.raca = ''

    def mostrar_nome(self):
        print(f'O nome do cachorro é: {self.nome}')

    def mostrar_ano_nascimento(self, ano_atual):
        ano_nascimento = ano_atual - self.idade
        return ano_nascimento
    
    def atribuir_raca(self, raca):
        self.raca = raca

    def mostrar_todos_dados(self):
        print(f'O nome é {self.nome} , a idade é {self.idade} e é da raça {self.raca}')


cachorro1 = Cachorro('Nico' , 3)
cachorro2 = Cachorro('Lailah' , 13)

cachorro1.mostrar_nome()
cachorro2.mostrar_nome()

print(cachorro1.mostrar_ano_nascimento(2025))
print(cachorro2.mostrar_ano_nascimento(2025))

cachorro1.atribuir_raca('Vira-Lata')

cachorro1.mostrar_todos_dados()
cachorro2.mostrar_todos_dados()