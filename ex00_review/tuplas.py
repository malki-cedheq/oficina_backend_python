# tuplas.py
'''
Tipo de dados: Tuple

As tuplas são usadas para armazenar vários itens em uma única variável.
Tuple é um dos 4 tipos de dados embutidos em Python usados para armazenar coleções de dados,
os outros 3 são List, Set e Dictionary, todos com diferentes qualidades e uso.
Uma tupla é uma coleção ordenada e imutável. Tuplas são escritas com colchetes.

Itens de tupla são ordenados (indexados), imutáveis e permitem valores duplicados.

Imutável é quando nenhuma mudança é possível ao longo do tempo. 
Em Python, diz-se imutável se o valor de um objeto não pode ser alterado ao longo do tempo.
Uma vez criados, o valor desses objetos é permanente.

Objetos imutáveis: 
    Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
    Strings
    Tuples
    Frozen Sets

Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis.    
'''


# definição de tupla
tupla_um = ('uva', 'pêra', 'maçã', 'uva')
# P1
print("P1: {}".format(tupla_um))

# definição de tupla sem parenteses (finalizar com vírgula)
tupla_dois = 'laranja', 'uva', 'roxo',
# P2
print("P2: {}".format(tupla_dois))

# O método len() retorna o número de itens da tupla.
n = len(tupla_um)
# P3
print("P3: a tupla possui {} itens.".format(n))


# O método count() retorna o número de vezes que um valor especificado aparece na tupla.
el = 'uva'
n_el = tupla_um.count(el)
# P4
print("P4: {} ocorrências de {}.".format(n_el, el))


# O método index() localiza a posição da primeira ocorrência do valor especificado.
# OBS: Gera uma exceção se o valor não for encontrado.
el = 'uva'
i_el = tupla_um.index(el)
# P5
print("P5: {} está no índice {}.".format(el, i_el))
