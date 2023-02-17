#!/usr/bin/python3
import argparse
#comentario default
#funcion para leer archivo
def leer_archivo( archivo ):
    try:
      with open(archivo,"r") as fc:
        texto = fc.read() 
        lineas = texto.splitlines()  
        texto_limpio = " ".join(lineas)
    except:
      texto_limpio=""
    return texto_limpio

#funcion para leer stopwords
def leer_stop(archivo_stopwords):
  try:
    with open(archivo_stopwords,"r") as fh:
      stopwords = fh.readlines()
      stopwords=[p.strip('\n') for p in stopwords]
      set_sw=set(stopwords)
  except:
      set_sw=set()
  return set_sw

#funcion para contar palabras
def contar_palabras( texto ):
    palabras = texto.split(" ") 
    dp = dict() 
    for palabra in palabras: 
        p = palabra.strip(",.")
        p=p.lower() 
        if p in dp: 
           dp[p]+= 1
        else: 
          dp[p] = 1
    
    if '' in dp:
      del(dp[''])
    return dp

##funcion de limpiar stopwords al diccionario
def limpiar(dp,words):
  print(len(dp))
  diccionario={}
  for (k,v) in dp.items():
    if k not in words:
      diccionario[k]=v
  print(len(diccionario))
  return diccionario

##funcion para imprimir diccionario
def imprime_diccionario(dp, minimo):
  lista=[ (k,v) for k,v in dp.items() if v>=minimo]
  lista_ordenada=sorted(lista, key= lambda x:x[1], reverse=True)
  for tupla in lista_ordenada:
    print(tupla[0],'= ',tupla[1])
  return

def main( archivo,minimo):
    topes=leer_stop('spanish_stopwords.txt')
    #print(topes)
    texto = leer_archivo( archivo )
    dipo   = contar_palabras( texto )
    dip  = limpiar(dipo,topes)
    #print(dip)
    #print(dip)
    imprime_diccionario(dip,minimo)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-a','--archivo',dest='archivo', help='nombre de archivo', required=True)
  parser.add_argument('-m','--minimo',dest='minimo', help='numero minimo de repeticiones', required=False, default=3, type=int)
  args=parser.parse_args()
  minimo=args.minimo
  archivo=args.archivo
  main(archivo,minimo)
