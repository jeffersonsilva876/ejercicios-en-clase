# Tuplas – Listas - Diccionarios
usuario = ("jeffs","1234","jeff@gmail.com")
materias = ["Python","c++","pseint"]
estudiante = {"nombre":"jefferson","edad":20,"fac2":"faci"}
print(usuario[0],materias[1],estudiante['nombre'])
print(usuario[0:2],estudiante.keys(),estudiante.values())
materias.append('Programacion Movil')
estudiante["sexo"],estudiante["edad"]="M", 21
print(materias,estudiante)
tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,":",c)
# Recorridos diccionario con items
for c, v in estudiante.items(): print(c,":",v)

