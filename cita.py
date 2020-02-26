#!/usr/bin/python3
import lector
import contar_palabras
import argparse

def obtener_cita(lista,inicio,cuenta):
  size=len(lista)
  if( (inicio+cuenta)<size):
    cita=lista[inicio:(inicio+cuenta)]
  else:
    cita=''
  return cita

def limpiar(texto):
  lim=[]
  for x in texto:
    limpia=x.lower().strip(',.-...;?!:')
    if x!=(''):
      lim.append(x)
  return lim

def main(archivo,inicio,cuenta):
  texto=lector.leer_archivo(archivo)
  texto=texto.split(' ')
  texto=limpiar(texto)
  cita=obtener_cita(texto,inicio,cuenta)
  #print('cita:',cita)
  topes=lector.leer_stop('spanish_stopwords.txt')
  totales=contar_palabras.creartotales(cita)
  claves,stops=contar_palabras.contarclavesystops(cita,topes)
  sumtotales=contar_palabras.sumar(totales)
  sumclaves=contar_palabras.sumar(claves)
  sumstops=contar_palabras.sumar(stops)
  contar_palabras.imprimir(sumtotales,sumclaves,sumstops)
  
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo', help='nombre de archivo', required=True)
  parser.add_argument('-i','--inicio',dest='inicio',help='numero de inicio',required=True,type=int)
  parser.add_argument('-c','--cuenta',dest='cuenta',help='numero que cuenta',required=True,type=int)
  args=parser.parse_args()
  archivo=args.archivo
  inicio=args.inicio
  cuenta=args.cuenta
  main(archivo,inicio,cuenta)
