import Arista as ar
import Nodo as nd

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
    
    def agregar_arista(self,origen,destino):
        nodo_origen=self.agregar_nodo(origen)
        nodo_destino=self.agregar_nodo(destino)
        arista=ar.Arista(nodo_origen, nodo_destino,self.dirigido)

        self.aristas.append(arista)

        nodo_origen.agregar_vecino(nodo_destino)

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

    