print("************Primer punto Conversión de tipos de datos*******************")

cantidad = 10
velocidad = 10.5
numeros = "456"

# Se convierte un entero a cadena
conversion_E_a_C = str(cantidad)

# se convierte decimal a cadena
conversion_D_a_C = str(velocidad)

# se convierte cadena a entero
conversion_C_a_E = int(numeros)

# se convierte cadena a decimal
conversion_C_a_D = float(numeros)

print(f"Entero a cadena: {conversion_E_a_C}")
print(f"Decimal a cadena: {conversion_D_a_C}")
print(f"Cadena a entero: {conversion_C_a_E}")
print(f"Cadena a decimal: {conversion_C_a_D}")

print("\n◙◙◙◙◙◙ segundo punto Multilíneas de cadenas◙◙◙◙◙◙◙")
multilinea = """Dios es amor
tus metas deben ser un hecho
nunca te rindas."""

print(multilinea)

print("\n****Tercer punto: Función len(), con esta funcion se cuenta la longitud que tiene la cadena***")
saludo = "  hola, chanchito feliz  "
longitud = len(saludo)
print(f"La longitud de la cadena es: {longitud}")

print("\n****Obtener los primeros 6 caracteres de una cadena.****")
n = 6
primeros_n_carac = saludo[:n]
print(f"Primeros {n} caracteres: {primeros_n_carac}")

print("\n**** Obtener los caracteres de en medio de una cadena****")

mitad = saludo[len(saludo)//2 - n//2 : len(saludo)//2 + n//2]
print(f"Caracteres de en medio: {mitad}")

print("\n****Obtener los últimos n caracteres de una cadena****")

ultimos_n_carac = saludo[-n:]
print(f"Últimos {n} caracteres: {ultimos_n_carac}")

print("\n****Con la Función upper() se cambia la cadena a mayuscula****")
saludo_mayuscula = saludo.upper()
print(f"Cadena en mayúsculas: {saludo_mayuscula}")

print ("\n****con la Función lower() se cambia la cadena a minuscula*****")
saludo_minuscula = saludo.lower()
print(f"Cadena en minúsculas: {saludo_minuscula}")

print("\n***con la Función strip() se quitan los espacions al principio y al final de la cadena***")
saludo_sin_espacios = saludo.strip()
print(f"Cadena sin espacios: '{saludo_sin_espacios}'")

print("\n***con la Función replace() se reemplaza la palabra que se quiera en la base****")
saludo_reemplazado = saludo.replace("chanchito", "marrano")
print(f"Cadena reemplazada: {saludo_reemplazado}")

print("\n***con esta Función split() podemos dividir la cadena que se asigno a la variable***")
saludo_dividido = saludo.split(", ")
print(f"Cadena dividida: {saludo_dividido}")

print("\n**** con el Formato de cadenas F-String se puede ingresar \n el valor de la variable directamente en la cadena****")
nombre = "andres"
edad = 27
cadena_modificada = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(cadena_modificada)


















