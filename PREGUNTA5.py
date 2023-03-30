#cada carácter deberá ser encriptado a ocho caracteres
def encriptar_mensaje(mensaje):
    caracteres_encriptados = []
    for caracter in mensaje:
        valor_ascii = ord(caracter)
        valor_binario = bin(valor_ascii)[2:].zfill(8)
        bits_divididos = [valor_binario[i:i+2] for i in range(0, 8, 2)]
        caracteres = ""
        for bit in bits_divididos:
            caracteres += {
                "00": "A", "01": "B", "10": "C", "11": "D"
            }[bit]
        caracteres_encriptados.append(caracteres)
    mensaje_encriptado = "".join(caracteres_encriptados)
    return mensaje_encriptado
def desencriptar_mensaje(mensaje_encriptado):
    caracteres_desencriptados = []
    for i in range(0, len(mensaje_encriptado), 8):
        caracteres = mensaje_encriptado[i:i+8]
        bits_divididos = ["".join(caracteres[j:j+1]) for j in range(0, 8, 2)]
        valor_binario = "".join({
            "A": "00", "B": "01", "C": "10", "D": "11"
        }[caracter] for caracter in bits_divididos)
        valor_ascii = int(valor_binario, 2)
        caracteres_desencriptados.append(chr(valor_ascii))
    mensaje_desencriptado = "".join(caracteres_desencriptados)
    return mensaje_desencriptado



#se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
import hashlib

# Generar la clave secreta
clave = b'mi_clave_secreta'

# Generar la cadena de sal
salt = b'mi_cadena_de_sal'

# Definir el número de iteraciones
iteraciones = 100000

# Definir el tamaño de la clave
tamanio_clave = 32

# Definir el algoritmo de hash
algoritmo = 'sha256'

# Generar la tabla hash para encriptar
tabla_encriptar = {}
for i in range(32, 126):
    char = chr(i)
    hash = hashlib.pbkdf2_hmac(algoritmo, clave, salt, iteraciones, tamanio_clave)
    tabla_encriptar[char] = hash.hex()

# Generar la tabla hash para desencriptar
tabla_desencriptar = {}
for char, hash in tabla_encriptar.items():
    tabla_desencriptar[hash] = char

# Imprimir las dos tablas hash
print('Tabla hash para encriptar:')
print(tabla_encriptar)
print('Tabla hash para desencriptar:')
print(tabla_desencriptar)
