"""
Eu criei este módulo apenas para testar
classes e fazer debug. Não serve para nada.
-Gil
"""
from Expert import Expert
from ExpertsCollection import ExpertsCollection

expert1 = Expert('Toze', 'lisbon', ('s1', 's2'), 4, 2, 'N/A', 'N/A', 10)
col1 = ExpertsCollection()

col1.addExpert(expert1)

col1.setCriteria(4, 4, 'lisbon')

# print(expert1)

# print experts in the collection:
for i in col1.items():
    print(i)
