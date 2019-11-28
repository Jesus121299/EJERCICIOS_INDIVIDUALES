# -*- codig: utf-8 -*-
import re

patch = "ejerciciounidad5.txt"

try:
    archivo=open(patch,'r')
except:
    print("el archivo no se pudo ejecutar")
    quit()

texto=""
for linea in archivo:
    texto += linea
#Ejercicio 1
variables= r'([A-Za-z-_]+\s*[=|;])'
resultvar = re.findall(variables,texto)
print("\n Las variables que estan declaradas son:\n", resultvar)

#Ejercicio 2
entero = r'[+,-]?[0-9]+'
decimal = r'[[0-9]*[.]]?[0-9]+'
resultente = re.findall(entero,texto)
resultdeci = re.findall(decimal,texto)
print("\n Los numeros enteros del archivo son:\n", resultente)
print("\nLos numeros decimales del archivo son:\n", resultdeci)

#Ejercicio 3
aritmetica = r'[A-Za-z|0-9]+[+*/%-]+[A-Za-z|0-9|]'
aritmeticaresul = re.findall(aritmetica, texto)
print("Los operadores aritmeticos del archivo son: \n", aritmeticaresul)

#Ejercicio 4
relacional = r'[A-Za-z|0-9]+\s*[|<|>|!=|<=|>=]+\s*[A-Za-z|0-9]+'
relacionalresul = re.findall(relacional, texto)
print("\n Los operadores relacionales identificados son: \n", relacionalresul)

#Ejercicio 5
reservadas = r'\b(false|def|if|raise|none|del|import|return|true|elif|int|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
resultadoreser = re.findall(reservadas, texto)
print("\n LAS PALABRAS RESERVADAS SON: ", resultadoreser)
print ("")
