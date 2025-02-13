import json
def abrirJSON():
    dicFinal={}
    with open('./infocliente.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./infocliente.json",'w') as outFile:
        json.dump(dic,outFile)

def menu():
 print ("¿Que desea realizar?")
 print ("1. Ver clientes ")
 print ("2. crear un nuevo cliente")
 print ("3. actualizar datos de un cliente ")
 print ("4. Eliminar cliente")
 print( "5. ")
 op =(input(":") )

 bol = True
 while bol == True:
     if op == "1":
        vercli = {}
        vercli = abrirJSON
        for i in range (len(vercli["usuarios"])):
         print (vercli[i]["nombre"])
     if op == "2":
        adcli = {}
        adcli = abrirJSON
        nom=(input("ingrese el nombre"))
        ap=(input("ingrese el apellido"))
        direc=(input("ingrese la direccion"))
        tel=(input("ingrese el telefono"))
        cor=(input("ingrese el correo"))
        tiem=(input("ingrese el tiempo que lleva en la empresa"))
          
        nuevousuario = {
           "nombre": nom,
           "apelido": ap,
           "Direccion": direc,
           "Telefono": tel,
           "Correo":cor,
           "Tiempo": tiem,

        }
        
        nuevousuario.append(adcli)
        guardarJSON()

     if op == "3":
      actcli = {}
      actcli = abrirJSON
      nom2=(input("ingrese el nombre"))
      ap2=(input("ingrese el apellido"))
      direc2=(input("ingrese la direccion"))
      tel2=(input("ingrese el telefono"))
      cor2=(input("ingrese el correo"))
      tiem2=(input("ingrese el tiempo que lleva en la empresa"))
          
      actu = {
            "nombre": nom2,
            "apelido": ap2,
            "Direccion": direc2,
            "Telefono": tel2,
            "Correo":cor2,
            "Tiempo": tiem2,

        }
     actu.update(actcli)
     guardarJSON()

     if op == "4":
        elcli = {}
        elcli = abrirJSON
         
        
     elcli.pop[actcli]
     guardarJSON(actcli)


     break
        