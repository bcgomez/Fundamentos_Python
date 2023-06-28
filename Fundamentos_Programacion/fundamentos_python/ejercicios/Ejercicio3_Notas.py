# Dado el código y las 5 calificaciones de un alumno, obtenidas a lo largo del semestre, construya un algoritmo que imprima el código del alumno y el promedio de sus calificaciones.'

# Encontre esta funcion matematca en internet
''''import statistics

nota1=float(input('Digite la primera nota'))
nota2=float(input('Digite la segundaa nota'))
nota3=float(input('Digite la tercera nota'))
nota4=float(input('Digite la cuarta nota'))
nota5=float(input('Digite la quinta nota'))

notas=[nota1,nota2,nota3,nota4,nota5]

promedio=statistics.mean(notas)
print(promedio)

# Teniendo en cuenta una lista con numeos finitos 

# ///////////////////////////////////////////
# Ejemplo de un programa con n numero de notas 

'''
notas=[]
Cant_Notas=0

while Cant_Notas <5:
        valor= int(input(f'Calificacion {Cant_Notas+1}: '))
        Cant_Notas+=1
        notas.append(valor)
        
print(notas)
def promedio_calificaciones(notas):
    sumar=sum(notas)
    Cant_elementos=len(notas)
    Promedio=sumar/Cant_elementos
    return Promedio

codigo=input('Digite el codigo del estudiante: ')
resultado=promedio_calificaciones(notas)
print(f'El codigo del estudiante es: {codigo}, su promedio es: {resultado}')