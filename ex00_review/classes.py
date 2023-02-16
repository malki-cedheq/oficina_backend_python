# classes.py

from datetime import datetime


class Pessoa(object):
    def __init__(self,  *args) -> None:
        self.nome = args[0]
        self.data_nascimento = args[1]

    def __call__(self) -> None:
        fmt = '<Pessoa nome: {}, data de nascimento: {}>'
        print(fmt.format(self.nome, self.data_nascimento))

    def __repr__(self) -> str:
        fmt = '<Pessoa Nome: {}, Data de nascimento: {}>'
        return fmt.format(self.nome, self.data_nascimento)

    def idade(self) -> int:
        data = datetime.strptime(self.data_nascimento, '%m/%d/%Y')
        return int((datetime.today() - data).days/365)


class Aluno(Pessoa):
    instituicao = 'UFPE'

    def __init__(self,  *args) -> None:
        Pessoa.__init__(self, args[0], args[1])
        self.curso = args[2]
        self.periodo = args[3]

    def __call__(self) -> None:
        fmt = '<Aluno Nome: {}, Data de nascimento: {}, Curso: {}, Período: {}, Instituição: {}>'
        print(fmt.format(self.nome, self.data_nascimento,
              self.curso, self.periodo, Aluno.instituicao))

    def __repr__(self) -> str:
        fmt = '<Aluno Nome: {}, Data de nascimento: {}, Curso: {}, Período: {}, Instituição: {}>'
        return fmt.format(self.nome, self.data_nascimento, self.curso, self.periodo, Aluno.instituicao)

    def up_periodo(self, arg) -> str:
        self.periodo = arg
        return ('Novo período {}'.format(self.periodo))

    @classmethod
    def up_instituicao(cls, arg) -> str:
        cls.instituicao = arg
        return ('Nova instituição {}'.format(cls.instituicao))


# Classe Pai (parent)
pessoa = Pessoa('Pedro Fernando', '05/07/1992')  # initialization
pessoa()  # call
print(pessoa)  # representation
print(pessoa.idade())  # class function

# Classe Filha (child)
aluno = Aluno('José Maria', '01/02/1980',
              'Engenharia Elétrica', '7')  # initialization
aluno()  # call
print(aluno)  # representation
print(aluno.idade())  # class function
print(Aluno.up_instituicao('Universidade Federal de Pernambuco'))
aluno()
aluno.up_periodo(10)
print(aluno)
