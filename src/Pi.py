#! encoding: UTF-8
import Modulo
t_uplas=(10,100,1000,10000,100000,1000000)
l=[]
for i in range(len(t_uplas)):
  s=Modulo.aproxpi (1,t_uplas[i])
  print "La aproximación del número pi es: %11.10f" %s
  l=l+[s]
print l
   

#El máximo de elementos de la t-upla para este ordenador es 7.
#Para el elemento 8.
#Sí, es pòsible definir los valores de la t-upla en notación científica.
#La extensión .pyc nos almacena el programa de forma que podamos ejecutarlo en cualquier sistema operativo.