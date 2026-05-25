import Arista as ar
import Nodo as nd
import random as rdm
import math
import heapq
import itertools

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
    

    
    def Kruskal(self):
        arbol_kruskal = Grafo()
        nodos_originales = self.obtener_todos_nodos()
        
        # 1. Agregar todos los nodos al nuevo árbol
        for nodo in nodos_originales:
            arbol_kruskal.agregar_nodo(nodo.obtener_valor())

        # 2. Extraer todas las aristas (evitando duplicados en grafos no dirigidos)
        aristas = []
        aristas_vistas = set()
        
        for nodo in nodos_originales:
            u_val = nodo.obtener_valor()
            for vecino, peso in nodo.obtener_vecinos().items():
                v_val = vecino.obtener_valor()
                # Creamos un identificador único ordenado para la arista (A-B es igual a B-A)
                id_arista = tuple(sorted([u_val, v_val]))
                if id_arista not in aristas_vistas:
                    aristas_vistas.add(id_arista)
                    aristas.append((peso, u_val, v_val))
                    
        # Ordenar aristas de menor a mayor peso
        aristas.sort(key=lambda x: x[0])

        # 3. Estructura Union-Find para detectar ciclos
        padre = {nodo.obtener_valor(): nodo.obtener_valor() for nodo in nodos_originales}
        rango = {nodo.obtener_valor(): 0 for nodo in nodos_originales}

        def encontrar(i):
            if padre[i] == i:
                return i
            padre[i] = encontrar(padre[i]) # Compresión de caminos
            return padre[i]

        def unir(i, j):
            raiz_i = encontrar(i)
            raiz_j = encontrar(j)
            if raiz_i != raiz_j:
                # Unión por rango para mantener el árbol plano
                if rango[raiz_i] < rango[raiz_j]:
                    padre[raiz_i] = raiz_j
                elif rango[raiz_i] > rango[raiz_j]:
                    padre[raiz_j] = raiz_i
                else:
                    padre[raiz_j] = raiz_i
                    rango[raiz_i] += 1

        # 4. Construir el Árbol
        for peso, u, v in aristas:
            # Si no forman un ciclo, los unimos y agregamos la arista
            if encontrar(u) != encontrar(v):
                unir(u, v)
                arbol_kruskal.agregar_arista(u, v, peso)
                # En un grafo no dirigido puro, tal vez necesites agregar (v, u, peso) también
                # dependiendo de cómo esté implementado tu método agregar_arista.

        return arbol_kruskal
    
    
    def Kruskal_Inverso(self):
        nodos_originales = self.obtener_todos_nodos()
        valores_nodos = [nodo.obtener_valor() for nodo in nodos_originales]
        
        # 1. Extraer todas las aristas
        aristas = []
        aristas_vistas = set()
        
        # Simulamos una lista de adyacencia temporal para no modificar el grafo original
        # Formato: {nodo: {vecino: peso}}
        grafo_temp = {val: {} for val in valores_nodos}
        
        for nodo in nodos_originales:
            u_val = nodo.obtener_valor()
            for vecino, peso in nodo.obtener_vecinos().items():
                v_val = vecino.obtener_valor()
                grafo_temp[u_val][v_val] = peso
                
                id_arista = tuple(sorted([u_val, v_val]))
                if id_arista not in aristas_vistas:
                    aristas_vistas.add(id_arista)
                    aristas.append((peso, u_val, v_val))
                    
        # Ordenar aristas de MAYOR a menor peso
        aristas.sort(key=lambda x: x[0], reverse=True)

        # Función auxiliar: Verificar conectividad usando Búsqueda en Anchura (BFS)
        def es_conexo(lista_adyacencia):
            if not valores_nodos: return True
            visitados = set()
            cola = [valores_nodos[0]]
            visitados.add(cola[0])
            
            while cola:
                actual = cola.pop(0)
                for vecino in lista_adyacencia[actual]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        cola.append(vecino)
            return len(visitados) == len(valores_nodos)

        # 2. Proceso de eliminación (Reverse Delete)
        for peso, u, v in aristas:
            # Quitamos la arista de nuestra simulación temporal en ambas direcciones
            del grafo_temp[u][v]
            if u in grafo_temp[v]: 
                del grafo_temp[v][u]

            # Si quitarla desconecta el grafo, la volvemos a poner
            if not es_conexo(grafo_temp):
                grafo_temp[u][v] = peso
                grafo_temp[v][u] = peso

        # 3. Construir el árbol final usando el grafo temporal depurado
        arbol_kruskal_inv = Grafo()
        for val in valores_nodos:
            arbol_kruskal_inv.agregar_nodo(val)
            
        aristas_agregadas = set()
        for u, vecinos in grafo_temp.items():
            for v, peso in vecinos.items():
                id_arista = tuple(sorted([u, v]))
                if id_arista not in aristas_agregadas:
                    aristas_agregadas.add(id_arista)
                    arbol_kruskal_inv.agregar_arista(u, v, peso)

        return arbol_kruskal_inv
    
    def Prim(self):
        arbol_prim = Grafo()
        nodos_originales = self.obtener_todos_nodos()
        
        if not nodos_originales:
            return arbol_prim

        for nodo in nodos_originales:
            arbol_prim.agregar_nodo(nodo.obtener_valor())

        visitados = set()
        nodo_inicio = nodos_originales[0]
        visitados.add(nodo_inicio.obtener_valor())

        # 2. Inicializamos el contador de desempate
        contador = itertools.count() 
        cola_prioridad = []
        
        for vecino, peso in nodo_inicio.obtener_vecinos().items():
            # 3. Usamos next(contador) como segundo elemento
            heapq.heappush(cola_prioridad, (peso, next(contador), nodo_inicio, vecino))

        while cola_prioridad and len(visitados) < len(nodos_originales):
            # 4. Extraemos ignorando el contador con '_'
            peso, _, nodo_origen, nodo_destino = heapq.heappop(cola_prioridad)
            
            v_origen = nodo_origen.obtener_valor()
            v_destino = nodo_destino.obtener_valor()

            if v_destino in visitados:
                continue

            visitados.add(v_destino)
            arbol_prim.agregar_arista(v_origen, v_destino, peso)

            for vecino, p in nodo_destino.obtener_vecinos().items():
                if vecino.obtener_valor() not in visitados:
                    # 5. Volvemos a usar next(contador) aquí
                    heapq.heappush(cola_prioridad, (p, next(contador), nodo_destino, vecino))

        return arbol_prim