import Grafo as gr
import Algengraph as gen
import random

def generar_grafos_malla(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.malla(GR,filas=i[0],columnas=i[1])
        nodordm=GR.obtener_nodo_aleatorio()
        raiz=nodordm.obtener_valor()
        testBFS=GR.BFS(raiz)
        testDFSr=GR.DfsR(raiz)
        testDFSi=GR.DfsIte(raiz)
        nombreGrafo='Malla'+str(i[0]*i[1])
        nombreGrafoBFS='BFS'+nombreGrafo
        nombreGrafoDFSr='DFSr'+nombreGrafo
        nombreGrafoDFSi='DFSi'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        testBFS.generar_archivoGRAPH(nombreGrafoBFS)
        testDFSr.generar_archivoGRAPH(nombreGrafoDFSr)
        testDFSi.generar_archivoGRAPH(nombreGrafoDFSi)

def generar_grafos_ErdosRenyi(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.ErdosRenyi(GR,num_nodos=i[0],num_aristas=i[1])
        nodordm=GR.obtener_nodo_aleatorio()
        raiz=nodordm.obtener_valor()
        testBFS=GR.BFS(raiz)
        testDFSr=GR.DfsR(raiz)
        testDFSi=GR.DfsIte(raiz)
        nombreGrafo='Erdos'+str(i[0])
        nombreGrafoBFS='BFS'+nombreGrafo
        nombreGrafoDFSr='DFSr'+nombreGrafo
        nombreGrafoDFSi='DFSi'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        testBFS.generar_archivoGRAPH(nombreGrafoBFS)
        testDFSr.generar_archivoGRAPH(nombreGrafoDFSr)
        testDFSi.generar_archivoGRAPH(nombreGrafoDFSi)

def generar_grafos_Gilbert(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Gilbert(GR,num_nodos=i[0],p=i[1])
        nodordm=GR.obtener_nodo_aleatorio()
        raiz=nodordm.obtener_valor()
        testBFS=GR.BFS(raiz)
        testDFSr=GR.DfsR(raiz)
        testDFSi=GR.DfsIte(raiz)
        nombreGrafo='Gilbert'+str(i[0])
        nombreGrafoBFS='BFS'+nombreGrafo
        nombreGrafoDFSr='DFSr'+nombreGrafo
        nombreGrafoDFSi='DFSi'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        testBFS.generar_archivoGRAPH(nombreGrafoBFS)
        testDFSr.generar_archivoGRAPH(nombreGrafoDFSr)
        testDFSi.generar_archivoGRAPH(nombreGrafoDFSi)

def generar_grafos_GeoSimple(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Geo_simple(GR,num_nodos=i[0], r=i[1])
        nodordm=GR.obtener_nodo_aleatorio()
        raiz=nodordm.obtener_valor()
        testBFS=GR.BFS(raiz)
        testDFSr=GR.DfsR(raiz)
        testDFSi=GR.DfsIte(raiz)
        nombreGrafo='GeoSimple'+str(i[0])
        nombreGrafoBFS='BFS'+nombreGrafo
        nombreGrafoDFSr='DFSr'+nombreGrafo
        nombreGrafoDFSi='DFSi'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        testBFS.generar_archivoGRAPH(nombreGrafoBFS)
        testDFSr.generar_archivoGRAPH(nombreGrafoDFSr)
        testDFSi.generar_archivoGRAPH(nombreGrafoDFSi)

def generar_grafos_Barabasi(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.ErdosRenyi(GR,num_nodos=i[0],num_aristas=i[1])
        nodordm=GR.obtener_nodo_aleatorio()
        raiz=nodordm.obtener_valor()
        testBFS=GR.BFS(raiz)
        testDFSr=GR.DfsR(raiz)
        testDFSi=GR.DfsIte(raiz)
        nombreGrafo='Barabasi'+str(i[0])
        nombreGrafoBFS='BFS'+nombreGrafo
        nombreGrafoDFSr='DFSr'+nombreGrafo
        nombreGrafoDFSi='DFSi'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        testBFS.generar_archivoGRAPH(nombreGrafoBFS)
        testDFSr.generar_archivoGRAPH(nombreGrafoDFSr)
        testDFSi.generar_archivoGRAPH(nombreGrafoDFSi)

def generar_grafos_Dorogovstev(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Dorogovstev_Mendes(GR,num_nodos=i)
        nodordm=GR.obtener_nodo_aleatorio()
        raiz=nodordm.obtener_valor()
        testBFS=GR.BFS(raiz)
        testDFSr=GR.DfsR(raiz)
        testDFSi=GR.DfsIte(raiz)
        nombreGrafo='Dorogovstev'+str(i)
        nombreGrafoBFS='BFS'+nombreGrafo
        nombreGrafoDFSr='DFSr'+nombreGrafo
        nombreGrafoDFSi='DFSi'+nombreGrafo
        GR.generar_archivoGRAPH(nombreGrafo)
        testBFS.generar_archivoGRAPH(nombreGrafoBFS)
        testDFSr.generar_archivoGRAPH(nombreGrafoDFSr)
        testDFSi.generar_archivoGRAPH(nombreGrafoDFSi)

generar_grafos_malla([[7,8],[15,12],[25,20]])
generar_grafos_ErdosRenyi([[50,215],[160,620],[500,1050]])
generar_grafos_Gilbert([[50,0.10],[160,0.02],[500,0.02]])
generar_grafos_GeoSimple([[50,0.25],[160,0.15],[500,0.15]])
generar_grafos_Barabasi([[50,215],[160,620],[500,1050]])
generar_grafos_Dorogovstev([50,160,500])
