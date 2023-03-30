#ejericio 2
lista_numeros = [18, 50, 210, 80, 145, 333, 70, 30]

#Imprimir el número en caso de que sea múltiplo de 10 y menor que 200

for numero in lista_numeros:
    if numero % 10 == 0 and numero < 200:
        print(numero)
#Parar el programa si llega a un número mayor que 300

for numero in lista_numeros:
    if numero > 300:
        print("El número {} es mayor que 300. Se detiene el programa.".format(numero))
        break
    elif numero % 10 == 0 and numero < 200:
        print(numero)
#Organizar la lista mediante el método de ordenamiento merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    i = 0
    j = 0
    merged_arr = []

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1

    merged_arr += left_half[i:]
    merged_arr += right_half[j:]

    return merged_arr


arr = [18, 50, 210, 80, 145, 333, 70, 30]
sorted_arr = merge_sort(arr)
print(sorted_arr)

#Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista
lista_numeros = [18, 30, 50, 70, 80, 145, 210, 333]
valor_buscar = 145

try:
    indice = lista_numeros.index(valor_buscar)
    print("El valor {} se encuentra en el índice {} de la lista.".format(valor_buscar, indice))
except ValueError:
    print("El valor {} no se encuentra en la lista.".format(valor_buscar))
    indice = -1
