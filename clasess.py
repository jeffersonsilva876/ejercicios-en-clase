class For:
    def __init__(self):
        pass

    def usoFor(self):
      #ciclo repetitivo de incremento o decrementose ejecuta por verdaddero
        nombre = "jefferson"
        datos=["jefferson",21,True]
        #pos 0     1           2
        numeros=(2,5.6,4,1)
        docente = {"nombre": "jefferson","edad": 21,"fac": "faci"}
        listaNotas=[(30,40),(29,40),(50,40)]
        listaAlumnos = [{"nombre":"luis","final":21},{"nombre":"carlos","final":31},{"nombre":"miguel","final":34}]



        for i in range(5):
            print("for",i)
        for i in range(1,5):
            print("for", i)
        for i in range(2,10,2):
            print("for", i)
        for i in range(12,3,-3):
            print("for",i,end=" ")

       #Ion = len(nombre)
       #for pos in range(Ion)
       #for pos%2 == 0 and pos !=0:
       #print(pos,nombre[pos])
          # #vocal=("a","e","i","o","u")
        #for elem in datos:
        # print(elem,end=" ")
        #for elem in nombre:
       # print(elem, end=" ")


       # for pos,valor in enumerate(dato):
        #    print(pos,valor)
        #for pos, valor in docente.items():
         #   print(clave,valor,end=" ")
            # print(listaNotas)
            #for notas in listaNotas:
            #print("for externo",notas)
             #  for nota in notas:
              #     print(nota,end=" ")
             #print("saliendo del for interno")

           # print(listaNotas)
            #for notas in listaNotas:
            #acum=0
         #for nota in notas:
         #   acum=acum+nota
          #  print(acum/Ien(notas),end=" ")
          
        # listaAlumnos = [{"nombre":"trick","final":70},{"nombre":"jady","final":80},{"nombre":"dani","final":90}]
        # print("/nDiccionario de alumnos")
        # print(listaAlumnos)
        # acum=0
        # for alumnos in listaAlumnos:
        #     print(alumnos)
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor,type(valor),end=" ")
        #         if clave == "final":
                
        #           acum=acum+valor
        #     print()
            
        #     print("promedio",acum/len(listaAlumnos))
        
        listaNotas= [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for notas in notas:
                acumparcial+=notas
            cont=cont+1
            acum=acum+acumparcial
            print("totalParcial:{} promParcial:{}".format(acumparcial,acumparcial))
            print("totalGeneral:{} Promedio:{}".format(acum,acum/cont))
       
bucle = For()
bucle.usoFor()


