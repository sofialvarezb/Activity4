exercises=int(input("Enter the number of the exercise you want to run: "))
if exercises == 1:
  #Exercise 1 
  def addition_list(numbers):
    addition = 0
    for number in numbers:
      addition+= number
    return addition
  list = 12, 14, 16, 18, 20
  result= addition_list(list)
  print("The list is: ", list, "the result of the sum of the list is: ",result )

elif exercises == 2:
  #Exercise 2
  def calculate_average(list):
    if len(list) == 0:
        return 0 
    else:
        addition = sum(list)
        average = addition / len(list)
        return average
  number = [2, 4, 6, 8, 10]
  average = calculate_average(number)
  print("the list is: ", number, "The average of these num bers is: ",average)

elif exercises == 3:
  #Exercise 3
  def eliminate_duplicates(lists):
    list_no_duplicates = list(set(lists))
    return list_no_duplicates
  numbers =  [12, 14, 16, 14, 20, 20, 18]
  list_no_duplicates = eliminate_duplicates(numbers)
  print("the list is: ", numbers, "The list without duplicates is: ", list_no_duplicates)

elif exercises == 4:
  #Exercise 4
  def order(list):
    number = len(list)
    for i in range(number - 1):
        for _ in range(0, number - i - 1):
            if list[_] > list[_ + 1]:
                list[_], list[_ + 1] = list[_ + 1], list[_]
    return list
  numbers = [5, 1, 7 ,9, 4, 2, 0, 3, 6, 8]
  organized = order(numbers)
  print("the list is: ", numbers,"The list organized is: ", organized)

#Exercise 5
elif exercises == 5:
  def wrodLarge(listWord):
    wordLarge = ""
    longMax = 0

    for word in listWord:
        if len(word) > longMax:
            wordLarge = word
            longMax = len(word)

    return wordLarge
  list = ["apple", "table", "programming", "cat","butterfly","cu5rtain"]
  wordLarge = wrodLarge(list)
  print("the words on the list are: ",list, "The words in order from longest are: ", wordLarge) 

elif exercises == 6:
  #Exercise 6
  def product(tuple):
      product = 1
  
      for num in tuple:
          product *= num
  
      return product
  tuple = (3, 6, 9, 12, 15)
  result = product(tuple)
  print("The list is: ",tuple, "The list tuple is: ", result)

elif exercises == 7:
  #exercise 7 
  def maxminTuple(tuple):
    maxi = max(tuple)
    mini = min(tuple)
    return maxi, mini
  tupla = (10, 12, 14, 16, 18, 20)
  maxi, mini = maxminTuple(tupla)
  print("The list is: ",tupla,"The maximun number is: ", maxi)  
  print("The minimum number is : ", mini)

elif exercises == 8:
  #exercise 8
  def contar_ocurrencias_tupla(tupla):
    diccionario = {}

    for elemento in tupla:
        if elemento in diccionario:
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1

    return diccionario
tupla = (8, 6, 8, 4, 3, 7, 6)
ocurrencias = contar_ocurrencias_tupla(tupla)
print(ocurrencias) 

elif exercises == 9:
  #Exercise 9
  def encontrar_indices(tupla, elemento):
      indices = []
  
      for i in range(len(tupla)):
          if tupla[i] == elemento:
              indices.append(i)
  
      return indices
  tupla = (6, 9, 4, 8, 3, 2, 9)
  elemento = 2
  indices = encontrar_indices(tupla, elemento)
  print(indices)

  #Exercise 10
elif exercises == 10:
  def separar_cadenas_por_vocal(tupla_cadenas):
      vocales = ('a', 'e', 'i', 'o', 'u')
      cadenas_con_vocal = []
      cadenas_sin_vocal = []
  
      for cadena in tupla_cadenas:
          if cadena.lower().startswith(vocales):
              cadenas_con_vocal.append(cadena)
          else:
              cadenas_sin_vocal.append(cadena)
  
      return tuple(cadenas_con_vocal), tuple(cadenas_sin_vocal)
  tupla = ("manzana","loro","perro","Mono","elefante","gato","abdomen"," hígado","músculo","cuello","corazón","mente","alma","espíritu", "pecho","cintura","cadera","espalda","sangre","carne", "piel","hueso","Iglesia")
  con_vocal, sin_vocal = separar_cadenas_por_vocal(tupla)
  print("Cadenas con vocal:", con_vocal)  
  print("Cadenas sin vocal:", sin_vocal)  

elif exercises == 11:
#Exercise 11
  def contar_palabras(lista_palabras):
      contador = {}
  
      for palabra in lista_palabras:
          if palabra in contador:
              contador[palabra] += 1
          else:
              contador[palabra] = 1
  
      return contador
  lista = ["SOFIA","HELEN","HELEN","SOFIA","HELEN","JULIETH", "SOFIA","HELEN","LEO","SALOME","JIRETH","SALOME","CRISTIAN","MERY","ALEJO","MATIAS"]
  contador = contar_palabras(lista)
  print(contador)  
  
  
elif exercises == 12:
  def promedio_calificaciones(diccionario_estudiantes):
      total_calificaciones = 0
      total_estudiantes = len(diccionario_estudiantes)
  
      for calificaciones in diccionario_estudiantes.values():
          total_calificaciones += sum(calificaciones)
  
      promedio = total_calificaciones / total_estudiantes
  
      return promedio
  
  estudiantes = {
      "Juan": [78, 91,71],
      "María": [76,85,76],
      "Pedro": [68,99,87],}
  promedio = promedio_calificaciones(estudiantes)
  print(promedio) 
  
  
  
elif exercises == 13:
  def filtrar_diccionario(diccionario, valor):
      nuevo_diccionario = {}
  
      for clave, val in diccionario.items():
          if val == valor:
              nuevo_diccionario[clave] = val
  
      return nuevo_diccionario
  diccionario = {"SEBASTIAN": 25, "MARIA": 30, "JIMMY": 25, "CAMILA": 40}
  valor = 25
  nuevo_diccionario = filtrar_diccionario(diccionario, valor)
  print(nuevo_diccionario)  
  
 elif exercises == 14:
  
  def combinar_diccionarios(diccionario1, diccionario2):
      diccionario_combinado = {}
  
      # Combinar las claves y valores del primer diccionario
      for clave, valor in diccionario1.items():
          diccionario_combinado[clave] = valor
  
      # Sumar los valores de las claves comunes del segundo diccionario
      for clave, valor in diccionario2.items():
          if clave in diccionario_combinado:
              diccionario_combinado[clave] += valor
          else:
              diccionario_combinado[clave] = valor
  
      return diccionario_combinado
  diccionario1 = {"a": 1, "b": 2, "c": 3}
  diccionario2 = {"b": 5, "c": 4, "d": 6}
  diccionario_combinado = combinar_diccionarios(diccionario1, diccionario2)
  print(diccionario_combinado) 
  
  
elif exercises == 15:
  
  def contar_palabras(texto):
      palabras = texto.lower().split()
      contador = {}
  
      for palabra in palabras:
          if palabra in contador:
              contador[palabra] += 1
          else:
              contador[palabra] = 1
  
      return contador
  texto = "Érase una vez un rey muy presumido, que vivía en gran castillo. Un día un comerciante de un lejano país le hizo un extraño trato"
  resultado = contar_palabras(texto)
  print(resultado)