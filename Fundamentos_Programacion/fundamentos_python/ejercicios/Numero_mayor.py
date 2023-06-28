#Determinar el número mayor dado 3 números.
#Declaracion de variables
  # Declaración de variables
  

num_1=int(input('Ingrese el número 1: '))
num_2=int(input('Ingrese el número 2: '))
num_3=int(input('Ingrese el número 3: '))

  # Verificar el número más grande
if num_1>=num_2 and num_1>=num_3:
  print(f'El numero mas grande es: {num_1}')
elif num_2>=num_1 and num_2>=num_3:
  print(f'El numero mas grande es: {num_2}')
else:
  print(f'El numero mas grande es: {num_3}')