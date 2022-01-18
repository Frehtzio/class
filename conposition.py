class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]} #esto es para todos # si alguna funcion lo toca o modifica afectara a todos los hijos
  material="prueba"
  def __init__(self,name):
    self.name = name

  def add_item(self,name, material, amount):
    Clothing.stock['name'].append(name)
    Clothing.stock['material'].append(material)
    Clothing.stock['amount'].append(amount)
    print(Clothing.stock) 
  def Stock_by_Material(self, material):
    self.count=0
    n=0
  
    for key,value in Clothing.stock.items():
      if key == "amount":
          for v in value:
            
            self.count += value[n] #en vez de esto vale esto v
            n+=1
            if material == "Cotton": # el resto de funciones incluyendo tambien las variables dentro de funciones  no le afectara a los hijos, hermanos y padres 
              self.count += 1
          return n
    
    

class shirt(Clothing):
  material="Cotton"
class pants(shirt): #se puede usar al hermano como padre
  material="Cotton"
  
polo = shirt("Polo") # name esto es llama intance
prueba = Clothing("prueba") #prueva
sweatpants = pants("Sweatpants") #name
polo.add_item(polo.name, polo.material, 4) 
prueba.add_item(prueba.name, prueba.material, 4) 
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
print(polo.stock)
#current_stock = polo.Stock_by_Material("Cotton")
#print(current_stock)
polo.Stock_by_Material("Cotton")
sweatpants.Stock_by_Material("Coss")
c =prueba.Stock_by_Material("Coss")
#print(c) 



print(polo.count)
print(sweatpants.count)
print(prueba.count)
