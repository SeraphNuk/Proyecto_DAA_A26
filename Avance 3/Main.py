import Grafo as gr
import Algengraph as gen
import random

def generar_grafos_malla(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.malla(GR,filas=i[0],columnas=i[1])
        raiz=GR.obtener_nodo_aleatorio()
        MallaDijkstra=GR.Dijkstra(raiz)
        nombreGrafo='Malla'+str(i[0]*i[1])
        nombreArbol='ArbolCamMin'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        MallaDijkstra.generar_archivoGRAPH(nombreArbol)


def generar_grafos_ErdosRenyi(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.ErdosRenyi(GR,num_nodos=i[0],num_aristas=i[1])
        raiz=GR.obtener_nodo_aleatorio()
        ErdosDijkstra=GR.Dijkstra(raiz)
        nombreGrafo='Erdos'+str(i[0])
        nombreArbol='ArbolCamMin'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        ErdosDijkstra.generar_archivoGRAPH(nombreArbol)

def generar_grafos_Gilbert(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Gilbert(GR,num_nodos=i[0],p=i[1])
        raiz=GR.obtener_nodo_aleatorio()
        GilbertDijkstra=GR.Dijkstra(raiz)
        nombreGrafo='Gilbert'+str(i[0])
        nombreArbol='ArbolCamMin'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        GilbertDijkstra.generar_archivoGRAPH(nombreArbol)

def generar_grafos_GeoSimple(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Geo_simple(GR,num_nodos=i[0], r=i[1])
        raiz=GR.obtener_nodo_aleatorio()
        GeoDijkstra=GR.Dijkstra(raiz)
        nombreGrafo='GeoSimple'+str(i[0])
        nombreArbol='ArbolCamMin'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        GeoDijkstra.generar_archivoGRAPH(nombreArbol)

def generar_grafos_Barabasi(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.ErdosRenyi(GR,num_nodos=i[0],num_aristas=i[1])
        raiz=GR.obtener_nodo_aleatorio()
        BarabasiDijkstra=GR.Dijkstra(raiz)
        
        nombreGrafo='Barabasi'+str(i[0])
        nombreArbol='ArbolCamMin'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        BarabasiDijkstra.generar_archivoGRAPH(nombreArbol)

def generar_grafos_Dorogovstev(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Dorogovstev_Mendes(GR,num_nodos=i)
        raiz=GR.obtener_nodo_aleatorio()
        DorogovstevDijkstra=GR.Dijkstra(raiz)

        nombreGrafo='Dorogovstev'+str(i)
        nombreArbol='ArbolCamMin'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        DorogovstevDijkstra.generar_archivoGRAPH(nombreArbol)


#generar_grafos_malla([[10,10],[25,20]])
generar_grafos_ErdosRenyi([[50,215],[500,1050]])
#generar_grafos_Gilbert([[50,0.10],[500,0.02]])
#generar_grafos_GeoSimple([[50,0.25],[500,0.15]])
#generar_grafos_Barabasi([[50,215],[500,1050]])
#generar_grafos_Dorogovstev([50,500])


