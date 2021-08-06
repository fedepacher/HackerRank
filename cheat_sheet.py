s = 'hola como estas'
char_rep = s.count('a') #cuenta la cantidad de veces que se repite 'a', devuelve entero
print(char_rep)

ar=[1,2,1,2,1,3,2]#lista
my_dic = {i:ar.count(i) for i in ar}#crea un diccionario con la cantidad de valores de la lista {1:3, 2:3, 3:1}
print(my_dic) 

max = float('-inf')#flotante muy chico

array = [0] * 3#crea un arreglo de 3 elementos inicializados a 0

a = [1,2,3,4,5]
d = 4
c=a[d:len(a)]#se queda co a[5]->d:len(a)= de d a len(a)
e=a[0:d]#a[de 0 a d]
a[:] = c + e#rotacion a la izquierda [c:e]


arr = [p - 1 for p in a]#se crea un arreglo igual a a pero a cada elemento se le resta 1 
i=0
arr[i+1], arr[i] = arr[i], arr[i+1]#inversion de valores

for i,elem in enumerate(arr):
    print(f'i:{i}, P:{elem}')#itera de 0 a len(arr) e impieme el valor de P e i

s1 = "geek"    
print (list(enumerate(s1,2)))# crea una lista [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]#empezando de 2
l1 = ["eat","sleep","repeat"]
for ele in enumerate(l1):
    print (ele)
# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')

#for j in range(max(P-1,0),i): #aca se usa el max para que se quede con el max entre P-1 y 0 asi nunca es negativo, si P-1 < 0 => se queda con el 0

#for i in reversed(arr):#va de atras para adelante

#Dictionary get method 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#key:value
x = car.get("model", "")#obtiene el valor del key "model" y el segundo parametro es opcional y es lo que devuelve si no encuentra el valor
print(x)


#Counter
from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
obj1 = Counter(list1)#type counter, devuelve un counter  con la cantidad de cada elemento
print(obj1)#Imprime -> Counter({'x': 4, 'y': 2, 'z': 2})
#se puede restar a otro counter y si el resultado es {} quiere decir que un counter esta contenido en otro counter
#ej
magazine = "give me one grand today night"
note = "give one grand today"
obj1 = Counter(magazine)
obj2 = Counter(note)
obj3 = obj2 - obj1
if obj3 == {}:
    print("Yes")
else:
    print("No")


#Defauldict
#El diccionario estándar incluye el método setdefault () para recuperar un valor y 
# establecer un valor predeterminado si el valor no existe. Por el contrario, defaultdict 
# permite que la persona que llama especifique el valor predeterminado (valor a devolver) 
# al inicio cuando se inicializa el contenedor
from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)#si no encuentra el key devuelve un 0 por default
d.default_factory = lambda: 1#se cambia el valor de devolucion a 0 si no encuetra el key
for k in s:
    d[k] += 1
print(d.items())#dict_items([('i', 4), ('p', 2), ('s', 4), ('m', 1)])
print(d)#defaultdict(<function <lambda> at 0x7fa49cb7aa60>, {'m': 2, 'i': 5, 's': 5, 'p': 3})

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)#si no encuentra el key devuelve un [] por default
for k, v in s:
    d[k].append(v)
print(d.items())#dict_items([('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])])

results = []
results.append(1 if d.get('blue') else 0)#agrega uno si existe el key blue
print(results)#[1]

#Range
#range(start, stop, step) start y step opcionales

#Frozenset congela la lista y la hace inmutable
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)#frozenset({'cherry', 'apple', 'banana'}) no mantiene el orden

#Set almacena multiples items sin repetir, es de tipo set, y no se puede cambiar (inmutable)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)#{'banana', 'apple', 'cherry'} no mantiene el orden
# se permiten utilizar & que hace la interseccion entre dos conjuntos set ej
thisotherset = {"apple"}
obj3 = thisset & thisotherset
if len(obj3) > 0:
    print("YES")
else:
    print("NO")

prices = [1, 5, 4, 3]
prices.sort(reverse=False)#ordena de forma ascendente
print(prices)#[1,3,4,5]