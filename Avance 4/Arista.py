class Arista:
    def __init__(self, origen, destino, dirigida=False, peso= 1):

        self.origen=origen
        self.destino=destino
        self.dirigida=dirigida
        self.peso=peso

    def obtener_nodo(self):
        return(self.origen,self.destino)
    
    def es_dirigida(self):
        return(self.dirigida)
    
    def peso_arista(self):
        return(self.peso)
    
    def cambiar_peso(self,nuevo_peso):
        self.peso=nuevo_peso
    
    def __str__(self):
        direccion= "->" if self.dirigida else "--"
        etiqueta= f"[label= \"{self.peso}\"]"
        return f"{self.origen.obtener_valor()} {direccion} {self.destino.obtener_valor()} {etiqueta}"
    