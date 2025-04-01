#Creacion de la superclase "Animal
class Animal:
  #Definir el metodo "sonido"
  def sonido (self)
    pass
    
# Creacion de la subclase 1, juntyo con su metodo y atributo
class Perro (Animal):
  
  #Se asigna el mismo metodo de la superclase "Animal"
  def sonido (self):
    return "Guau"
    
#Creacion de la subclase 2, junto con su metodo y atributo 
class Gato (Animal):
  #Se asigna erl mismo metodo de la superclase "Animal"
  def sonido(self):
    return "Miau"

#Creacion de la funcion "Hacer sonido"
hacer_sonido(animal:Animal):
  print (animal.sonido())

#Creacion de los objetos 
perro=Perro()
gato=Gato()

#Salida de los objetos
hacer_sonido(perro)
hacer_sonido(gato)
