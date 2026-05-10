import Grafo as gr
import math
import random

"""
Algortimos de generación de grafos

-Malla
-Erdös y Rényi
-Gilbert
-Geográfico Simple
-Barbási-Albert
-Dorogovstev-Mendes
"""

def calculo_distancias(pi,pf):
    return math.sqrt(sum((a - b)**2 for a, b in zip(pi, pf)))

def malla(grafo,filas,columnas):
        
    """
    Genera un grafo malla con las dimensiones especificadas.
    Args:
        filas: numero de filas del grafo
        columnas: numero de columnas del grafo
        
    Returns:
        Grafo malla
    """
    
    for i in range(filas):
        for j in range(columnas-1):
            origen=f"{i}_{j}"
            destino=f"{i}_{j+1}"
            if i<=filas-2:
                origendiaginv=destino
                destinodiaginv=f"{i+1}_{j}"
                destinodiag=f"{i+1}_{j+1}"
                grafo.agregar_arista(origen,destinodiaginv, peso=random.randint(1,30))
                grafo.agregar_arista(origendiaginv,destinodiaginv, peso=random.randint(1,30))
                grafo.agregar_arista(origen,destinodiag, peso=random.randint(1,30))

            if j==columnas-2:
                origenvert=f"{i}_{j+1}"
                if i<filas-1:
                    destinovert=f"{i+1}_{j+1}"
                    grafo.agregar_arista(origenvert,destinovert, peso=random.randint(1,30))

            grafo.agregar_arista(origen,destino, peso=random.randint(1,30) )
    
    return grafo

def ErdosRenyi(grafo,num_nodos,num_aristas):

    """
    Genera un grafo Erdös y Rényi con los nodos especificadas.
    Crea n nodos y formar al azar m distintas aristas entre pares 
    Args:
        num_nodos: numero de nodos del grafo
        num_aristas: numero de aristas del grafo
        
    Returns:
        Grafo de Erdös y Rényi
    """
    nodoslist=[i for i in range(num_nodos)]
    for i in range(num_nodos):
        grafo.agregar_nodo(i)
    num=0
    while num<num_aristas:
        origen=nodoslist[random.randint(0,num_nodos-1)]
        destino=nodoslist[random.randint(0,num_nodos-1)]
        if origen!=destino and not grafo.existe_arista(origen,destino):
            grafo.agregar_arista(origen,destino, peso=random.randint(1,30))
            num=num+1
    
    return grafo

def Gilbert(grafo,num_nodos,p):

    """
        Genera el grafo Gilbert con nodos especificos y probabilidad de conectarse a otro nodo 
        Crea n nodos y poner una arista entre cada par independiente y uniformemente con probabilidad p
        Args:
            num_nodos: numero de nodos 
            p: la probabilidad de conectarse
        Returns:
            Grafo Gilbert 
    """
    nodoslist=[i for i in range(num_nodos)]
    for i in range(num_nodos):
        grafo.agregar_nodo(i)

    for i in nodoslist:
        for j in nodoslist:
            if i!=j and random.random()<=p and not grafo.existe_arista(i,j):
                grafo.agregar_arista(i,j,peso=random.randint(1,30))

    return grafo

def Geo_simple(grafo,num_nodos,r):
    """
    Genera el Grafo geográfico simple con nodos espesificos y r
    Colocar n nodos en un rectángulo unitario con coordenadas y colocar una arista 
    entre nodos con distancia =< r 
    Args:
        num_nodos: n cantindad de nodos 
        r : la distacia maxima entre los nodos
    Returns:
            Grafo geográfico simple
    """

    posiciones_nodos=[]
    i=0
    while i<=num_nodos-1:
        a=random.random()
        b=random.random()
        if [a,b] not in posiciones_nodos:
            posiciones_nodos.append([a,b])
            i=i+1

    for i in posiciones_nodos:
        distancias=[]
        for j in posiciones_nodos:
            distancia=calculo_distancias(i,j)
            nodo_origen=f"{i[0]}_{i[1]}"
            grafo.agregar_nodo(nodo_origen)
            nodo_destino=f"{j[0]}_{j[1]}"
            grafo.agregar_nodo(nodo_destino)
            if distancia>0.0 and distancia<=r and not grafo.existe_arista(nodo_origen,nodo_destino):
                grafo.agregar_arista(nodo_origen,nodo_destino, peso=random.randint(1,30))

    return grafo

def Barabasi_Albert(grafo,num_nodos,num_aristas):

    """
    Genera el grafo de Barabási-Albert
    Colocar n nodos uno por uno, asignando a cada uno d aristas a nodos distintos de tal manera que la probabilidad 
    de que el vértice nuevo se conecte a un vértice existente sea proporcional a la cantidad de aristas existentes
    Args:
        num_nodos : Cantidad de nodos del grafo
        num_aristas: numero maximo de aristas por nodo 
    Returns:
        Grafo de Barabási-Albert
    """

    nodos_list=[i for i in range(num_nodos)]
    for i in nodos_list:
        grafo.agregar_nodo(i)
        nodos_creados=nodos_list[0:nodos_list.index(i)]
        for j in nodos_creados:
            aristas_disponibles=grafo.nodo_grado(j)
            if random.random()<=(1-(aristas_disponibles/num_aristas)) and not grafo.existe_arista(i,j):
                grafo.agregar_arista(i,j,peso=random.randint(1,30))
    return grafo


def Dorogovstev_Mendes(grafo,num_nodos):

    """
    Genera el Grafo Dorogovtsev-Mendes
    Crear 3 nodos y 3 aristas formando un triángulo. 
    Después, para cada nodo adicional, se selecciona una arista al azar y se 
    crean aristas entre el nodo nuevo y los extremos de la arista seleccionada
    Args:
        num_nodos: Cantidad de nodos a generar
    Returns:
        Grafo de Dorogovtsev-Mendes
    """
    
    nodos_list=[i for i in range(num_nodos)]
    for i in range(num_nodos):
        grafo.agregar_nodo(i)

    grafo.agregar_arista(0,1, peso=random.randint(1,30))
    grafo.agregar_arista(1,2, peso=random.randint(1,30))
    grafo.agregar_arista(0,2, peso=random.randint(1,30))

    for i in range(3,num_nodos):
        lista_aristas=grafo.obtener_aristas()
        seleccion=random.choice(lista_aristas)
        nodos_seleccion=seleccion.obtener_nodo()
        nodo_a=nodos_seleccion[0].obtener_valor()
        nodo_b=nodos_seleccion[1].obtener_valor()

        if not grafo.existe_arista(i,nodo_a):
            grafo.agregar_arista(i,nodo_a, peso=random.randint(1,30))
        if not grafo.existe_arista(i,nodo_b):
            grafo.agregar_arista(i,nodo_b, peso=random.randint(1,30))
        
        
    return grafo


