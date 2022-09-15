'''Ejercicios de recursion'''

#TODO 1

def f_contar(s_num): # se inicia la función, esta debe tener un parametro que sirva como memoria del sistema
    if s_num < 10: # si el número actual es menor que 10, aumentar en uno y volver a correr la función
        print (s_num)
        s_num+=1
        return f_contar(s_num) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final

print(f_contar(1))

#TODO 2

def f_contar(s_num,s_obj): # se inicia la función, esta consta de dos parametros que sirva para alacenarlos en la meoria del sistema
    if s_num < s_obj: # si el numero actual es menor al objetivo, aumentar en uno y vuelve a recorrr la funcion
        print(s_num)
        s_num+=1
        return f_contar(s_num,s_obj) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final

f_contar(1,20)


#TODO 3

def f_contar(s_num,s_obj,s_pasos): # se inicia la función, esta tiene 3 parametros que se almacenan en la memoria
    if s_num < s_obj-1: # si el numero actual es menor al objetivo, aumentar en uno y vuelve a recorrr la funcion esta vez en un paso de 3 numeros
        print(s_num)
        s_num+=s_pasos #Se representa el nuemro y los pasos en que se van a recorrer
        return f_contar(s_num,s_obj,s_pasos) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final


f_contar(1,20,3)


'''TORRE DE HANOI'''

def f_torre(n,n1,n2,n3):
  if(n>0):
    f_torre(n-1,n1,n3,n2)
    print('Mueve el anillo de la torre '+str(n1)+ ' hasta la torre ' +str(n2))
    f_torre(n-1,n3,n2,n1)
n=int(input('Ingrese la cantidad de anillos '))
f_torre(n,1,2,3)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

