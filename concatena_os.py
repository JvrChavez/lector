#!/usr/bin/python3
import os
import lector
import concatenar
import argparse

def archivos(folder,inicio,tipo):
  lista_archivos=os.listdir(folder)
  lista_archivos.sort()
  listado_filtrado=[]
  for archivo in lista_archivos:
    if archivo.endswith(tipo):
      if inicio or len(inicio)>0:
        if archivo.startswith(inicio):
          listado_filtrado.append(archivo)
      else:
        listado_filtrado.append(archivo)
  return listado_filtrado
  
def concatena(listado,folder):
  lista_textos=[]
  for archivo in listado:
    texto=lector.leer_archivo(os.path.join(folder,archivo))
    lista_textos.append(texto)
  textote='\n\n'.join(lista_textos)
  return textote
  
def main(folder,inicio,tipo,output):
  lista=archivos(folder,inicio,tipo)
  textote=concatena(lista,folder)
  concatenar.crear(textote,output)
        

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-f','--folder',dest='folder', help='nombre del folder',required=True)
  parser.add_argument('-i','--inicio',dest='inicio',help='nombre que inicia el archivo',required=False)
  parser.add_argument('-t','--tipo',dest='tipo',help='tipo de archivo',required=True)
  parser.add_argument('-o','--output',dest='output',help='archivo a crear',required=True)
  args=parser.parse_args()
  folder=args.folder
  inicio=args.inicio
  output=args.output
  tipo=args.tipo
  main(folder,inicio,tipo,output)