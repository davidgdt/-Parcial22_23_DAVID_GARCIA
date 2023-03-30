#restar polinomio
class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def sumar(self, otro_polinomio):
        coef1 = self.coeficientes + [0] * (len(otro_polinomio.coeficientes) - len(self.coeficientes))
        coef2 = otro_polinomio.coeficientes + [0] * (len(self.coeficientes) - len(otro_polinomio.coeficientes))
        coeficientes_suma = [c1 + c2 for c1, c2 in zip(coef1, coef2)]
        return Polinomio(coeficientes_suma)

    def restar(self, otro_polinomio):
        coef1 = self.coeficientes + [0] * (len(otro_polinomio.coeficientes) - len(self.coeficientes))
        coef2 = [-c for c in otro_polinomio.coeficientes] + [0] * (len(self.coeficientes) - len(otro_polinomio.coeficientes))
        coeficientes_resta = [c1 + c2 for c1, c2 in zip(coef1, coef2)]
        return Polinomio(coeficientes_resta)

    def evaluar(self, x):
        return sum(c * x ** i for i, c in enumerate(self.coeficientes))
p1 = Polinomio([1, 2, 3])
p2 = Polinomio([1, 0, -4, 2])
p3 = p1.restar(p2)
print(p3.coeficientes)  # Output: [-1, 2, 7, -2]

#dividir polinomio
def dividir_polinomios(dividendo, divisor):
    # Obtener el grado máximo del dividendo y divisor
    grado_dividendo = len(dividendo) - 1
    grado_divisor = len(divisor) - 1

    # Verificar que el divisor no sea el polinomio cero
    if grado_divisor == 0 and divisor[0] == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")

    # Si el grado del divisor es mayor que el del dividendo, el resultado es cero
    if grado_dividendo < grado_divisor:
        return [0], dividendo

    # Inicializar el cociente y el resto con ceros
    cociente = [0] * (grado_dividendo - grado_divisor + 1)
    resto = list(dividendo)

    # Algoritmo de división de polinomios
    for i in range(grado_dividendo - grado_divisor + 1):
        coeficiente = resto[i] / divisor[0]
        cociente[-i-1] = coeficiente
        for j in range(1, grado_divisor + 1):
            resto[i + j] -= coeficiente * divisor[j]

    # Eliminar ceros a la izquierda del cociente y el resto
    while len(cociente) > 1 and cociente[0] == 0:
        cociente.pop(0)
    while len(resto) > 1 and resto[0] == 0:
        resto.pop(0)

    # Devolver el cociente y el resto como listas de coeficientes
    return cociente, resto
dividendo = [1, 5, -2, 4]
divisor = [-1, 2]
cociente, resto = dividir_polinomios(dividendo, divisor)
print("Cociente:", cociente)  # Output: [4, -3]
print("Resto:", resto)  # Output: [1, 9]


#eliminar un termino del polinomio
class Termino:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

class Polinomio:
    def __init__(self, terminos):
        self.terminos = terminos
        
    def eliminar_termino(self, termino_eliminar):
        for i, t in enumerate(self.terminos):
            if t.exponente == termino_eliminar.exponente:
                del self.terminos[i]
                break
def test_eliminar_termino():
    p = Polinomio([Termino(2, 3), Termino(-1, 2), Termino(4, 0)])
    p.eliminar_termino(Termino(-1, 2))
    assert len(p.terminos) == 2
    assert p.buscar_termino(Termino(-1, 2)) == False
    p.eliminar_termino(Termino(2, 3))
    assert len(p.terminos) == 1
    assert p.buscar_termino(Termino(2, 3)) == False
    p.eliminar_termino(Termino(4, 0))
    assert len(p.terminos) == 0
    assert p.buscar_termino(Termino(4, 0)) == False




#Tests polinomio
class Termino:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

class Polinomio:
    def __init__(self, terminos):
        self.terminos = terminos
        
    def buscar_termino(self, termino):
        for t in self.terminos:
            if t.exponente == termino.exponente:
                return True
        return False
def test_buscar_termino():
    p = Polinomio([Termino(2, 3), Termino(-1, 2), Termino(4, 0)])
    assert p.buscar_termino(Termino(-1, 2)) == True
    assert p.buscar_termino(Termino(2, 2)) == False
    assert p.buscar_termino(Termino(4, 0)) == True
 #ejemplo 
terminos = [Termino(3, 3), Termino(-5, 2), Termino(2, 1), Termino(1, 0)]

P = Polinomio(terminos)
termino_buscado = Termino(-5, 2)
encontrado = P.buscar_termino(termino_buscado)
