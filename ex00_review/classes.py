from datetime import datetime


class Pessoa(object):
    nome: str
    data_nascimento: str

    def __init__(self,  *args):
        self.nome = args[0]
        self.data_nascimento = args[1]

    def __call__(self):
        fmt = '<Pessoa nome: {}, data de nascimento: {}>'
        print(fmt.format(self.nome, self.data_nascimento))

    def __repr__(self) -> str:
        fmt = '<Pessoa Nome: {}, Data de nascimento: {}>'
        return fmt.format(self.nome, self.data_nascimento)

    def idade(self):
        data = datetime.strptime(self.data_nascimento, '%m/%d/%Y')
        return int((datetime.today() - data).days/365)


class Aluno(Pessoa):
    curso: str
    periodo: str

    def __init__(self,  *args):
        Pessoa.__init__(self, args[0], args[1])
        self.curso = args[2]
        self.periodo = args[3]

    def __call__(self):
        fmt = '<Aluno Nome: {}, Data de nascimento: {}, Curso: {}, Período: {}>'
        print(fmt.format(self.nome, self.data_nascimento, self.curso, self.periodo))

    def __repr__(self) -> str:
        fmt = '<Aluno Nome: {}, Data de nascimento: {}, Curso: {}, Período: {}>'
        return fmt.format(self.nome, self.data_nascimento, self.curso, self.periodo)


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
