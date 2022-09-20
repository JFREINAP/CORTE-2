#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n
def primer_paso (n):
    factorial = 1
    while (n > 1):
        factorial *= n
        n -= 1
    p_01 = factorial
    p_02= 2** n
    if p_01 >p_02:
        return True
    else:
        return False
    k=primer_paso(n+1)
assert primer_paso(5)==True


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?

def f_fibonacci(n):
    a = 1
    b = 0
    for i in range(0, n + 1):
        b = b + a
        a = b - a
        print(a, end=',')


f_fibonacci(12)


## Ejercicio objetos.
# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller
# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)


class Taller:
    def __init__(self, fecha, costo, modelo, año, dueño):
        self.fecha = fecha
        self.costo = costo
        self.modelo = modelo
        self.año = año
        self.dueño = dueño
        self.vehiculo=self
    def caja(self, din):
        dinerocaja=199000000
        dinerocaja+=din
        listavacia=[]
        if din >= self.costo:
            tot = din - self.costo
            print("se ha eliminado el vehiculo")
            dinerocaja-=tot
            listavacia.append(tot)
    def empleados (self, nombree, cargoe, salarioe, vehiculoe, documentoe):
        self.nombree=nombree
        self.cargoe=cargoe
        self.salarioe=salarioe
        self.vehiculoe=vehiculoe
        self.documentoe=documentoe
    def procesos(self,despedirocontratar,nombre1,cargo1,salario1,vehiculo1,documento1):
        listavacia1= []
        if procesos=='despedir':
            ident=input('documento del empleado')
            for i in listavacia1:
                if i==ident:
                    listavacia1.remove[i]

'vehiculos'

carro1 = Taller('24-5-02', 45000000, 'Nissan', 1993, 'Miguel Rodriguez')
carro2 = Taller('31-10-01', 6660000, 'Ford', 1960, 'Cristofer Cruz')
carro1.caja(46000000)

