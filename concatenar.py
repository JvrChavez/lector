#!/usr/bin/python3
import argparse

def leer(archivo):
  try:
    with open(archivo,"r") as fc:
      texto = fc.read() 
  except:
    texto=""
  return texto

def crear(texto,archivo):
  nuevo=open(archivo,'w+',encoding='utf-8')
  nuevo.write(texto)
  nuevo.close()

def main(archivo,output):
  size=len(archivo)
  if (size>0):
    contador=0
    total=''
    while (contador!=size):
      texto=leer(archivo[contador])
      total=total+'\n'+texto
      contador+=1
    crear(total,output)
  else:
    print('No ingresaste los suficientes archivos para la accion')
   
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo', help='nombre de archivo de entrada', action='append',required=True)
  parser.add_argument('-o','--output',dest='output',help='nombre del archivo de salida',required=True)
  args=parser.parse_args()
  archivo=args.archivo
  output=args.output
  main(archivo,output)