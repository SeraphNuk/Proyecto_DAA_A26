import Arista as ar
import Nodo as nd
import random as rdm
import math
import heapq

"""
Clase Grafo:

funciones---> agregar_nodo

"""
class Grafo:
    def __init__(self, dirigido=False):
        self.nodos={}
        self.aristas=[]
        self.dirigido=dirigido 
    
    def agregar_nodo(self,valor):
        if valor not in self.nodos:
            self.nodos[valor]=nd.Nodo(valor)

        return self.nodos[valor]
    
    def agregar_arista(self,origen,destino, peso=1):
        nodo_origen=self.agregar_nodo(origen)
        nodo_destino=self.agregar_nodo(destino)
        arista=ar.Arista(nodo_origen, nodo_destino,self.dirigido, peso)

        self.aristas.append(arista)

        nodo_origen.agregar_vecino(nodo_destino, peso)

        if not self.dirigido:
            nodo_destino.agregar_vecino(nodo_origen)

        return arista
    
    def obtener_nodo(self,valor):
        return self.nodos.get(valor)
    
    def obtener_aristas(self):
        return self.aristas
    
    def obtener_todos_nodos(self):
        return list(self.nodos.values())
    
    def existe_arista(self,origen,destino):
        nodo_origen=self.obtener_nodo(origen)
        nodo_destino=self.obtener_nodo(destino)

        if not nodo_origen or not nodo_destino:
            return False
        
        if self.dirigido:
            return nodo_destino in nodo_origen.obtener_vecinos()
        else:
            return (nodo_destino in nodo_origen.obtener_vecinos() or
                    nodo_origen in nodo_destino.obtener_vecinos())
        
    def __str__(self):
        tipo="Dirigido" if self.dirigido else "No dirigido"
        nodos= ", ".join(str(nodos.obtener_valor()) for nodo in self.obtener_todos_nodos())
        aristas= "\n".join(str(arista) for arista in self.obtener_aristas())

        return f"Grafo ({tipo})\nNodos: [{nodos}]\nAristas:\n{aristas}"
    
    def nodo_grado(self,valor):
        nodo=self.obtener_nodo(valor)

        if not nodo:
            return 0
        
        if self.dirigido:
            grado_salida= len(nodo.obtener_vecinos())
            grado_entrada= sum(1 for n in self.obtener_todos_nodos() if nodo in n.obtener_vecinos())
            return ("Entrada="+str(grado_entrada),"Salida="+str(grado_salida))
        else:
            return len(nodo.obtener_vecinos())
        
    def generar_archivoGRAPH(self, id):
        f= open(str(id+".dot"),"w")

        f.write(str("graph " + id+"={\n"))
        f.write(";\n".join(str(nodo.obtener_valor()) for nodo in self.obtener_todos_nodos()))
        f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.obtener_aristas()))
        f.write(";\n}")
        f.close

    def BFS(self, inicio):


        arbol=Grafo()
        nodo_raiz = self.obtener_nodo(inicio)
        if not nodo_raiz:
            return arbol
        
        queue=[nodo_raiz]
        visitados=set()

        while len(queue)>0:
            nodo_actual=queue[0]
            valor_nodo_actual=nodo_actual.obtener_valor()
            vecinos=nodo_actual.obtener_vecinos()
            for i in vecinos:
                if i not in visitados:
                    valor_vecino=i.obtener_valor()
                    if not arbol.existe_arista(valor_nodo_actual,valor_vecino):
                        arbol.agregar_arista(valor_nodo_actual,valor_vecino)
                    visitados.add(i)
                    queue.append(i)
            del queue[0]
        return arbol
    
    def DfsR(self, inicio):
        '''
        Busqueda a profundidad. Recursivamente
        Args:
            nodo: Nodo inicial
        '''
        nodo_inicio = self.obtener_nodo(inicio)
        if not nodo_inicio:
            return Grafo()
        
        visitados = set()
        ArbolDfsR = Grafo()
        
        def Dfs(nodo):
            valor = nodo.obtener_valor()
            visitados.add(valor)
            
            for vecino in nodo.obtener_vecinos():
                if vecino.obtener_valor() not in visitados:
                    ArbolDfsR.agregar_arista(valor,vecino.obtener_valor())
                    Dfs(vecino)
        Dfs(nodo_inicio)
        return ArbolDfsR

    def DfsIte(self, inicio):
        """
        Búsqueda a profundidad iterativa que construye el árbol DFS.
        
        Args:
            grafo: Objeto de la clase Grafo
            inicio: Valor del nodo inicial

        Returns:
            Grafo que representa el árbol DFS construido
        """
        nodo_inicio = self.obtener_nodo(inicio)
        if not nodo_inicio:
            return Grafo()

        visitados = set()
        pila = [nodo_inicio]
        ArbolDfsI = Grafo()
        ArbolDfsI.agregar_nodo(nodo_inicio.obtener_valor())

        while pila:
            nodo_actual = pila.pop()
            valor_actual = nodo_actual.obtener_valor()
            if valor_actual not in visitados and nodo_actual not in ArbolDfsI.obtener_todos_nodos():
                ArbolDfsI.agregar_nodo(valor_actual)
                visitados.add(valor_actual)
                for vecino in reversed(nodo_actual.obtener_vecinos()):
                    valor_vecino = vecino.obtener_valor()
                    if valor_vecino not in visitados and vecino not in pila:
                        ArbolDfsI.agregar_nodo(valor_vecino)
                        pila.append(vecino)
                        ArbolDfsI.agregar_arista(valor_actual, valor_vecino)
        return ArbolDfsI
    
    def Dijkstra(self,nodo_fuente):
        valor_inicio=nodo_fuente.obtener_valor()
        costos={nodo.obtener_valor(): float('inf') for nodo in self.obtener_todos_nodos()}
        costos[valor_inicio]=0
        #Creamos la lista de nodos padres para llevar registro de la relación entre nodos
        padres = {nodo.obtener_valor(): None for nodo in self.obtener_todos_nodos()}

        visitados=set()
        cola_prioridad = [(0, id(nodo_fuente), nodo_fuente)] # Formato: (distancia, id_unico, nodo_objeto) para evitar errores si las distancias son iguales


        while cola_prioridad:
            distancia_actual, _ ,nodo_actual = heapq.heappop(cola_prioridad)
            valor_actual = nodo_actual.obtener_valor()
            if valor_actual in visitados:
                continue

            visitados.add(valor_actual)
            nodos_adyacentes=nodo_actual.obtener_vecinos()

            for vecino, peso in nodos_adyacentes.items():
                valor_vecino = vecino.obtener_valor()
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < costos[valor_vecino]:
                    costos[valor_vecino] = nueva_distancia
                    padres[valor_vecino] = valor_actual # Registramos quién es el padre en el camino óptimo
                    heapq.heappush(cola_prioridad, (nueva_distancia, id(vecino), vecino))

        arbol_dijkstra = Grafo()

        for nodo_val,dist in costos.items():
            if dist != float('inf'):
                arbol_dijkstra.agregar_nodo(nodo_val)

        for nodo_hijo, nodo_padre in padres.items():
            if nodo_padre is not None and costos[nodo_hijo] != float('inf'):
                # Calculamos el peso exacto de esa arista restando los costos acumulados
                peso_arista = costos[nodo_hijo] - costos[nodo_padre]
                
                arbol_dijkstra.agregar_arista(nodo_padre, nodo_hijo, peso= peso_arista)

        return arbol_dijkstra
    
    def obtener_nodo_aleatorio(self):
        nodos=self.obtener_todos_nodos()
        nodo_random= rdm.choice(nodos)
        return nodo_random
