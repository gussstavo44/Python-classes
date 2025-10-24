##aula dia 23 ex1

class Pessoa:

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        print(f'{self.nome} é um(a) {self.cargo}')

    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        print(f'{self.nome} foi promovido(a) para {self.cargo}!')

    def ajustar_salario(self, novo_salario):
        self.salario = novo_salario
        print(f'O salário de {self.nome} agora é {self.salario}')

    def apresentacao_final(self):
        print(f'{self.nome} é agora um(a) {self.cargo} com um novo salário de {self.salario}')


pessoa1 = Pessoa("Sara", 'Analista Júnior' , 2500.00)
pessoa1.apresentar()
pessoa1.promover('Analista Pleno')
pessoa1.ajustar_salario(3500.00)
pessoa1.apresentacao_final()