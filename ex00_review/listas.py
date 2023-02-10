# main.py
'''
Tipo de dados: List
Descrição: Um objeto tipo List é uma coleção ordenada (possui índice), mutável e permite duplicatas.

Mutável é quando algo tem a capacidade de mudar. 
Em Python, ‘mutável’ é a capacidade dos objetos de mudar seus valores. 
Geralmente, esses são os objetos que armazenam uma coleção de dados.

Objetos mutáveis:
    Lists
    Sets
    Dictionaries

Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis.
'''

# definição de list
lista_um = ['uva', 'pêra', 'maçã']
# P1
print("P1: {}".format(lista_um))

# cria um objeto list
tupla = ('laranja', 'uva', 'roxo')
lista_dois = list(tupla)
# P2
print("P2: {}".format(lista_dois))

# O método append() acrescenta um elemento ao final da lista.
lista_um.append('morango')
# P3
print("P3: {}".format(lista_um))

# O método insert() insere o valor especificado na posição especificada.
lista_um.insert(2, 'mamão')
# P4
print("P4: {}".format(lista_um))

# O método copy() retorna uma cópia da lista especificada.
lista_tres = lista_um.copy()
# P5
print("P5: {}".format(lista_tres))

# O método extend() adiciona os elementos de um objeto iterável ao final da lista atual.
lista_tres.extend(lista_dois)
# P6
print("P6: {}".format(lista_tres))

# O método sort() classifica a lista em ordem crescente por padrão. Pode-se usar uma função para decidir o(s) critério(s) de classificação.
lista_tres.sort(reverse=False, key=(lambda e: len(e)))
# P7
print("P7: {}".format(lista_tres))

# O método reverse() inverte a ordem de classificação dos elementos.
lista_tres.reverse()
# P8
print("P8: {}".format(lista_tres))

# O método count() retorna o número de elementos com o valor especificado.
el = 'uva'
n_el = lista_tres.count(el)
# P9
print("P9: {} ocorrências de {}.".format(n_el, el))

# O método index() retorna a posição na primeira ocorrência do valor especificado.
el = 'maçã'
i_el = lista_tres.index(el)
# P10
print("P10: {} está no índice {}.".format(el, i_el))

# O método remove() remove a primeira ocorrência do elemento com o valor especificado.
el = 'uva'
lista_tres.remove(el)
# P11
print("P11: {}".format(lista_tres))

# O método pop() remove o elemento na posição especificada.
i_el = 4
lista_tres.pop(i_el)
# P12
print("P12: {}".format(lista_tres))

# O método len() retorna o número de itens da lista.
n = len(lista_tres)
# P13
print("P13: a lista possui {} itens.".format(n))

# O método remove() remove a primeira ocorrência do elemento com o valor especificado.
lista_tres.clear()
# P14
print("P14: {}".format(lista_tres))
