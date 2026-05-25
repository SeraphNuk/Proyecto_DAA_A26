import Grafo as gr
import Algengraph as gen
import random

def generar_grafos_malla(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.malla(GR,filas=i[0],columnas=i[1])
        MallaKruskal=GR.Kruskal()
        MallaPrim=GR.Prim()
        MallaKruskalInv=GR.Kruskal_Inverso()

        nombreGrafo='Malla'+str(i[0]*i[1])
        nombreKruskal='Kruskal'+nombreGrafo
        nombreKruskalInv='KuskalInv'+nombreGrafo
        nombrePrim='Prim'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        MallaKruskal.generar_archivoGRAPH(nombreKruskal)
        MallaKruskalInv.generar_archivoGRAPH(nombreKruskalInv)
        MallaPrim.generar_archivoGRAPH(nombrePrim)



def generar_grafos_ErdosRenyi(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.ErdosRenyi(GR,num_nodos=i[0],num_aristas=i[1])
        ErdosKruskal=GR.Kruskal()
        ErdosPrim=GR.Prim()
        ErdosKruskalInv=GR.Kruskal_Inverso()

        nombreGrafo='Erdos'+str(i[0])
        nombreKruskal='Kruskal'+nombreGrafo
        nombreKruskalInv='KuskalInv'+nombreGrafo
        nombrePrim='Prim'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        ErdosKruskal.generar_archivoGRAPH(nombreKruskal)
        ErdosKruskalInv.generar_archivoGRAPH(nombreKruskalInv)
        ErdosPrim.generar_archivoGRAPH(nombrePrim)

def generar_grafos_Gilbert(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Gilbert(GR,num_nodos=i[0],p=i[1])
        GilbertKruskal=GR.Kruskal()
        GilbertPrim=GR.Prim()
        GilbertKruskalInv=GR.Kruskal_Inverso()

        nombreGrafo='Gilbert'+str(i[0])
        nombreKruskal='Kruskal'+nombreGrafo
        nombreKruskalInv='KuskalInv'+nombreGrafo
        nombrePrim='Prim'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        GilbertKruskal.generar_archivoGRAPH(nombreKruskal)
        GilbertKruskalInv.generar_archivoGRAPH(nombreKruskalInv)
        GilbertPrim.generar_archivoGRAPH(nombrePrim)

def generar_grafos_GeoSimple(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Geo_simple(GR,num_nodos=i[0], r=i[1])
        GeoKruskal=GR.Kruskal()
        GeoPrim=GR.Prim()
        GeoKruskalInv=GR.Kruskal_Inverso()

        nombreGrafo='GeoSimple'+str(i[0])
        nombreKruskal='Kruskal'+nombreGrafo
        nombreKruskalInv='KuskalInv'+nombreGrafo
        nombrePrim='Prim'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        GeoKruskal.generar_archivoGRAPH(nombreKruskal)
        GeoKruskalInv.generar_archivoGRAPH(nombreKruskalInv)
        GeoPrim.generar_archivoGRAPH(nombrePrim)

def generar_grafos_Barabasi(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.ErdosRenyi(GR,num_nodos=i[0],num_aristas=i[1])
        BarabasiKruskal=GR.Kruskal()
        BarabasiPrim=GR.Prim()
        BarabasiKruskalInv=GR.Kruskal_Inverso()

        nombreGrafo='Barabasi'+str(i[0])
        nombreKruskal='Kruskal'+nombreGrafo
        nombreKruskalInv='KuskalInv'+nombreGrafo
        nombrePrim='Prim'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        BarabasiKruskal.generar_archivoGRAPH(nombreKruskal)
        BarabasiKruskalInv.generar_archivoGRAPH(nombreKruskalInv)
        BarabasiPrim.generar_archivoGRAPH(nombrePrim)

def generar_grafos_Dorogovstev(sizes):
    for i in sizes:
        GR=gr.Grafo()
        GR=gen.Dorogovstev_Mendes(GR,num_nodos=i)
        DorogovstevKruskal=GR.Kruskal()
        DorogovstevPrim=GR.Prim()
        DorogovstevKruskalInv=GR.Kruskal_Inverso()

        nombreGrafo='Dorogovstev'+str(i)
        nombreKruskal='Kruskal'+nombreGrafo
        nombreKruskalInv='KuskalInv'+nombreGrafo
        nombrePrim='Prim'+nombreGrafo

        GR.generar_archivoGRAPH(nombreGrafo)
        DorogovstevKruskal.generar_archivoGRAPH(nombreKruskal)
        DorogovstevKruskalInv.generar_archivoGRAPH(nombreKruskalInv)
        DorogovstevPrim.generar_archivoGRAPH(nombrePrim)


#generar_grafos_malla([[10,10],[25,20]])
#generar_grafos_ErdosRenyi([[50,215],[500,1050]])
#generar_grafos_Gilbert([[50,0.10],[500,0.02]])
#generar_grafos_GeoSimple([[50,0.25],[500,0.15]])
generar_grafos_Barabasi([[500,10000]])
#generar_grafos_Dorogovstev([50,500])


