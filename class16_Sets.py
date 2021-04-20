Uso de sets en Python
Los sets son muy similares a las listas, pero estas no permiten elementos repetidos.

Cuando trabajamos con sets, podemos realizar las operaciones básicas de conjuntos, esto quiere decir que se puede calcular los valores de intercepción, diferencia, unión.

Declarar sets

s = set([1,2,3])
t = set([3,4,5])
Operaciones con sets

s.union(t) # set([1,2,3,4,5])
s.intersection(t) # set([3])
s.difference(t) # set([1,2])


s = {1,2,3}
t = {3,4,5}

print(s | t)
print(s & t)
print(s-t)
print(s ^ t)

>>> s = set([1, 2, 3])
>>> t = set([3, 4, 5])
>>> s.union(t)

>>> s.intersection(t)
{3}
>>> s.difference(t)
{1, 2}
>>> t.difference(s)
{4, 5}
>>> s.symmetric_difference(t)
{1, 2, 4, 5}
>>> s.intersection({4})

1 in s
1 in t
1 not in s
1 not in t