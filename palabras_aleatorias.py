#!/usr/bin/python3
import lector
import argparse
from random import randrange

def limpiar(texto):
  lim=[]
  for x in texto:
    limpia=x.lower().strip(',.-...;?!:')
    if limpia!=(''):
      lim.append(limpia)
  return lim

def sortear(texto,numero):
  lista=[]
  size=len(texto)
  if (numero<size):
    i = 1
    while i <= numero:
      r=randrange(size)
      lista.append(texto[r])
      i +=1
  else:
    print('El numero es mayor al numero de palabras')
  return lista
def main(archivo,numero):
  texto=lector.leer_archivo(archivo)
  texto=texto.split(' ')
  limpio=limpiar(texto)
  lista=sortear(limpio,numero)
  print(lista)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo', help='nombre de archivo', required=True)
  parser.add_argument('-n','--numero',dest='numero',help='numero de palabras',required=True, type=int)
  args=parser.parse_args()
  archivo=args.archivo
  numero=args.numero
  main(archivo,numero)