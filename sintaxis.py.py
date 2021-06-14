num=20
nombre="ana"
print(num,type(num))
print(nombre,type,(nombre))

def mensaje(msg):
    print(msg)

    
mensaje("mi primermensaje en python")
mensaje("mi segundo programa en python")

class sintaxis:
    instancia=0 #atributo de clase 
    #_init_metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    #e inicializar los atributos de la clase . felf es un objeto que representa la clase creada
    def __init__(self,dato="llamando al constructor"):
        self.frase=dato #atributo de instancia
        sintaxis.instancia=sintaxis.instancia+1
        
        
    def usovariables(self):
        edad, _peso = 50, 70.5
        
        nombres = "Daniel Vera"
        Tipo_sexo = "M"
        civil= true
        #tuplas
        usuario = ("dchiki","1234","chiki@gmail.com")
        materias= []
        
        materias = ["Programacion Web","PHP","POO"]
        materias [1]="python"
        materias.append("Go")
        #print(materias,aux,materias[1])
        
        docente={}
        docente = {"nombre":"Daniel","edad":50,"activo": True}
        edad=docente["edad"]
        docente["edad"]=51
        docente["carrera"]="15"
        #print(docente,edad,docente["edad"])
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(usuario,usuario[0],usuario[0:2],nombre[-1])
        
        print(materias,materias[2:],materias,[3],materias,[-1],materias[-2:])
        # #presentacion con format
        # print("""Mi nombre es {}, tengo {}     
        #       años""".format(nombres,edad))
       
                    
# int("sintaxis antes de instancia es:{}".format(sintaxis.instancia))
ejer1=sintaxis() #instancia de la clasesintaxis y crea el objeto
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2=sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es:{}".format(sintaxis.instancia))
# print(ejer2.frase)

    
    
