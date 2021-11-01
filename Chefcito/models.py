import numpy as np
from numpy.lib.function_base import delete


class Item:
    def __init__(self,nombre_item:str, cantidad_item:int,key_item = None) -> None:
        self.nombre_item = nombre_item
        self.cantidad_item = cantidad_item
        self.key_item = key_item


class Receta():

    def __init__(self,name_receta:str,key_receta= None,puntuacion=None) -> None:
       self.key_receta= key_receta
       self.name_receta = name_receta
       self.ingredientes = []
       self.puntuacion=puntuacion

    def _search_ingrediente(self,nombre_ingrediente:str):
        
        for ingrediente in self.ingredientes:
            if ingrediente.nombre_item == nombre_ingrediente:
                return ingrediente
        print("%s not found in receta"%nombre_ingrediente)
        return None
    
    def add_ingrediente(self,nombre_ingrediente:str,cantidad_ingrediente:int):
        ingrediente_searched = self.search_ingrediente(nombre_ingrediente=nombre_ingrediente)
      
        if ingrediente_searched:
            print("%s already exist"%nombre_ingrediente)
        else:
            mi_ingrediente = Item(nombre_item=nombre_ingrediente,cantidad_item=cantidad_ingrediente)
            self.ingredientes.append(mi_ingrediente)
            print("El ingrediente %s fue agregado"%nombre_ingrediente)

    def delete_ingrediente(self,nombre_ingrediente:str):
        ingrediente_searched = self.search_ingrediente(nombre_ingrediente=nombre_ingrediente)
      
        if ingrediente_searched:
            self.ingredientes.remove(ingrediente_searched)
            print("El ingrediente %s se ha eliminado"%nombre_ingrediente)
        else:
            print("El ingrediente %s no existe"%nombre_ingrediente)
    
    def show_items(self):
        for ingr in self.ingredientes:
            print("ingrdiente: %s cantidad: %d"%(ingr.nombre_item, ingr.cantidad_item))


class MiHeladera():
    
    def __init__(self) -> None:
        self.mi_heladera = []
    
    def _search_item(self,name:str):
        
        for item in self.mi_heladera:
            if item.nombre_item == name:
                return item
        print("%s not found in heladera"%name)
        return None

    
    def add_item(self,item:Item):

        item_searched = self.search_item(name=item.nombre_item)
        if item_searched:
            item_searched.cantidad_item += item.cantidad_item
        else:
            self.mi_heladera.append(item)
            print("%s se agrego en la heladera"%item.nombre_item)

    def delete_item(self,nombre_item:str,quantity:int):
        item_searched = self.search_item(name=nombre_item)
        if item_searched and item_searched.cantidad_item >=quantity:
            item_searched.cantidad_item -= quantity
        else:
            print("No hay mas %s"% nombre_item)

    # list items
        

class MiLibroDeRecetas():
    def __init__(self) -> None:
        self.libro = []
        self.cantidad_recetas=0
    
    def _search_receta(self,name_receta):
        for receta in self.libro:
            if receta.name_receta == name_receta:
                return receta
        print("%s not found in heladera"%name_receta)
        return None
        
    def add_receta(self,receta:Receta):
        
        receta_searched = self.search_receta(name_receta=receta.name_receta)
        if receta_searched:
            print("receta ya existe")
        else: 
            self.libro.append(receta)

    def delete_receta(self,name_receta):
        receta_searched = self.search_receta(name_receta=name_receta)
        if receta_searched:
            self.libro.remove(receta_searched)
        else:
            print("receta no existe")

    def use_receta(self,name_receta:str,mi_heladera:MiHeladera):
        receta_searched = self.search_receta(name_receta=name_receta)
        flag_no_item=0
        missing_items=[]
        
        for ingred in receta_searched.ingredientes:
            item_searched = mi_heladera.search_item(ingred.nombre_item)

            if not item_searched:
                missing_items.append([ingred.nombre_item,ingred.cantidad_item])
                flag_no_item=1
            elif item_searched.cantidad_item < ingred.cantidad_item:
                flag_no_item=1
                missing_items.append([ingred.nombre_item,ingred.cantidad_item-item_searched.cantidad_item])
                

        if flag_no_item:
            print("missing ingredients:",missing_items)
            return
        for ingred in receta_searched.ingredientes:
            mi_heladera.delete_item(nombre_item=ingred.nombre_item, quantity=ingred.cantidad_item)

    # list recepies
        
print(" ")
print("creando items")

mi_item = Item(nombre_item='Tomate',cantidad_item=3)
mi_item2 = Item(nombre_item='Lechuga',cantidad_item=5)
mi_item3 = Item(nombre_item='fideos',cantidad_item=8)
mi_item4 = Item(nombre_item='crema',cantidad_item=5)
mi_item5 = Item(nombre_item='champignon',cantidad_item=8)

print(" ")
print("agregando items")
mi_heladera = MiHeladera()
mi_heladera.add_item(mi_item)
mi_heladera.add_item(mi_item2)
mi_heladera.add_item(mi_item3)
mi_heladera.add_item(mi_item4)
mi_heladera.add_item(mi_item5)

print(" ")
print("creando receta")
mi_libro=MiLibroDeRecetas()
print(" ")
mi_receta= Receta("fideos con crema")
mi_receta.add_ingrediente(nombre_ingrediente='fideos',cantidad_ingrediente=1)
mi_receta.add_ingrediente(nombre_ingrediente='crema',cantidad_ingrediente=1)
mi_receta.add_ingrediente(nombre_ingrediente='champignon',cantidad_ingrediente=4)
mi_receta.add_ingrediente(nombre_ingrediente='cebolla de verdeo',cantidad_ingrediente=2)
mi_receta.add_ingrediente(nombre_ingrediente='queso rallado',cantidad_ingrediente=1)
print(" ")
print("guardando receta")
mi_libro.add_receta(mi_receta)
print(" ")
print("mostrar items de receta")
mi_receta.show_items()
print(" ")
print("usar receta")
mi_libro.use_receta("fideos con crema",mi_heladera)
