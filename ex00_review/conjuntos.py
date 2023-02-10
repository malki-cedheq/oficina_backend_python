# main.py
'''
Tipo de dados: Set
Descrição: 
    Um objeto tipo Set é uma coleção não-ordenada (não possui índice), mutável e não permite duplicatas.
    Não é permitido modificar um valor porém pode-se remover e adicionar valores.

Mutável é quando algo tem a capacidade de mudar. 
Em Python, ‘mutável’ é a capacidade dos objetos de mudar seus valores. 
Geralmente, esses são os objetos que armazenam uma coleção de dados.

Objetos mutáveis:
    Lists
    Sets
    Dictionaries

Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis.
'''

# definição de set
conjunto_um = {'uva', 'pêra', 'maçã'}
# P1
print("P1: {}".format(conjunto_um))

# cria um objeto list
tupla = ('laranja', 'uva', 'roxo')
conjunto_dois = set(tupla)
# P2
print("P2: {}".format(conjunto_dois))

# O método add() adiciona um elemento ao conjunto.
conjunto_um.add('morango')
# P3
print("P3: {}".format(conjunto_um))

# O método copy() retorna uma cópia da lista especificada.
conjunto_tres = conjunto_um.copy()
# P4
print("P4: {}".format(conjunto_tres))

# O método union() retorna um conjunto que contém todos os itens do conjunto original e todos os itens do(s) conjunto(s) especificado(s).
s1 = conjunto_tres.union(conjunto_dois)
# P5
print("P5: {}".format(s1))

# O método de interseção() retorna um conjunto que contém a similaridade entre dois ou mais conjuntos. Não altera o original.
s2 = conjunto_tres.intersection(conjunto_dois)
# P6
print("P6: {}".format(s2))

# O método intersection_update() remove os itens que não estão presentes em ambos os conjuntos (ou em todos os conjuntos se a comparação for feita entre mais de dois conjuntos).
# P7
conjunto_quatro = conjunto_um.copy()
conjunto_quatro.intersection_update(conjunto_dois)
print("P7: {}".format(conjunto_quatro))

# O método difference() retorna um conjunto que contém a diferença entre dois conjuntos. Não altera o original.
s3 = conjunto_tres.difference(conjunto_dois)
# P8
print("P8: {}".format(s3))

# O método difference_update() remove os itens que existem em ambos os conjuntos.
# P9
conjunto_cinco = conjunto_um.copy()
conjunto_cinco.difference_update(conjunto_dois)
print("P9: {}".format(conjunto_cinco))

# O método isdisjoint() retorna True se nenhum dos itens estiver presente em ambos os conjuntos, caso contrário, retorna False.
# P10
s4 = conjunto_um.isdisjoint(conjunto_dois)
print("P10: {}".format(s4))

# O método issubset() retorna True se todos os itens do conjunto existirem no conjunto especificado, caso contrário, retorna False.
# P11
s5 = conjunto_um.issubset(conjunto_dois)
print("P11: {}".format(s5))

# O método issuperset() retorna True se todos os itens do conjunto especificado existirem no conjunto original, caso contrário, retorna False.
# P12
s5 = conjunto_um.issuperset(conjunto_dois)
print("P12: {}".format(s5))

# O método discard() remove o item especificado do conjunto.
el = 'maçã'
conjunto_tres.discard(el)
# P13
print("P13: {}".format(conjunto_tres))

# O método pop() remove um item aleatório do conjunto.
conjunto_tres.pop()
# P14
print("P14: {}".format(conjunto_tres))

# O método len() retorna o número de itens da lista.
n = len(conjunto_tres)
# P15
print("P15: o conjunto possui {} itens.".format(n))

# O método remove() remove a primeira ocorrência do elemento com o valor especificado.
conjunto_tres.clear()
# P16
print("P16: {}".format(conjunto_tres))
