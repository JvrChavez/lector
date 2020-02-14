#!/usr/bin/python3
import lector
import argparse

def contarclavesystops(lista_palabras,topes):
  dpc=dict()
  dps=dict()
  for palabra in lista_palabras:
    p=palabra.lower().strip(',.')
    if p in topes:
      if p in dps:
        dps[p]+=1
      else:
        dps[p]=1
    else:
      if p in dpc:
        dpc[p]+=1
      else:
        dpc[p]=1
  return dpc,dps

def creartotales(texto):
  dp = dict()
  for palabra in texto:
      p = palabra.lower().strip(",.")
      if p in dp:
         dp[p]+= 1
      else: 
        dp[p] = 1
  return dp

def sumar(dp):
  suma=0
  for(k,v) in dp.items():
    suma+=v
  return suma
  
def sumarunicas(dp):
  suma=0
  for x in dp:
    suma+=1
  return suma

def imprimir(totales,claves,stops):
  print('numero de palabras',totales)
  print('palabras clave',claves)
  print('palabras stopwords',stops)
  
def imprimirunicas(totales,claves,stops):
  print('numero de palabras unicas',totales)
  print('palabras clave unicas',claves)
  print('palabras stopwords unicas',stops)

def main(archivo):
  texto=lector.leer_archivo(archivo)
  texto=texto.split(' ')
  totales=creartotales(texto)
  sumtotales=sumar(totales)
  topes=lector.leer_stop('spanish_stopwords.txt')
  claves,stops=contarclavesystops(texto,topes)
  sumclaves=sumar(claves)
  sumstops=sumar(stops)
  sumtotalesunicas=sumarunicas(totales)
  sumaclavesunicas=sumarunicas(claves)
  sumastopsunicas=sumarunicas(stops)
  imprimir(sumtotales,sumclaves,sumstops)
  print('--------------------------------------')
  imprimirunicas(sumtotalesunicas,sumaclavesunicas,sumastopsunicas)
  
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo', help='nombre de archivo', required=True)
  args=parser.parse_args()
  archivo=args.archivo
  main(archivo)