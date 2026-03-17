import Grafo as gr
import Algengraph as gen

GR=gr.Grafo()
GR=gen.malla(GR,filas=7,columnas=8)
GR.generar_archivoGRAPH('Mallas56')

GR=gr.Grafo()
GR=gen.malla(GR,filas=15,columnas=12)
GR.generar_archivoGRAPH('Mallas180')

GR=gr.Grafo()
GR=gen.malla(GR,filas=25,columnas=20)
GR.generar_archivoGRAPH('Mallas500')

######################################

grafotest=gr.Grafo()
gen.ErdosRenyi(grafotest,num_nodos=50,num_aristas=215)
grafotest.generar_archivoGRAPH('Erdos50')

grafotest=gr.Grafo()
gen.ErdosRenyi(grafotest,num_nodos=160,num_aristas=620)
grafotest.generar_archivoGRAPH('Erdos160')

grafotest=gr.Grafo()
gen.ErdosRenyi(grafotest,num_nodos=500,num_aristas=1050)
grafotest.generar_archivoGRAPH('Erdos500')

#######################################

grafotest=gr.Grafo()
gen.Gilbert(grafotest,num_nodos=50,p=0.10)
grafotest.generar_archivoGRAPH('Gilbert50')

grafotest=gr.Grafo()
gen.Gilbert(grafotest,num_nodos=250,p=0.015)
grafotest.generar_archivoGRAPH('Gilbert250')

grafotest=gr.Grafo()
gen.Gilbert(grafotest,num_nodos=500,p=0.015)
grafotest.generar_archivoGRAPH('Gilbert500')

########################################

grafotest=gr.Grafo()
gen.Geo_simple(grafotest,num_nodos=50,r=0.25)
grafotest.generar_archivoGRAPH('Geo_simple50')

grafotest=gr.Grafo()
gen.Geo_simple(grafotest,num_nodos=250,r=0.15)
grafotest.generar_archivoGRAPH('Geo_simple250')

grafotest=gr.Grafo()
gen.Geo_simple(grafotest,num_nodos=500,r=0.15)
grafotest.generar_archivoGRAPH('Geo_simple500')

#########################################

grafotest=gr.Grafo()
gen.Barabasi_Albert(grafotest,num_nodos=50,num_aristas=6)
grafotest.generar_archivoGRAPH('Barabasi_Albert50')

grafotest=gr.Grafo()
gen.Barabasi_Albert(grafotest,num_nodos=250,num_aristas=6)
grafotest.generar_archivoGRAPH('Barabasi_Albert250')

grafotest=gr.Grafo()
gen.Barabasi_Albert(grafotest,num_nodos=500,num_aristas=6)
grafotest.generar_archivoGRAPH('Barabasi_Albert500')

#########################################
grafotest=gr.Grafo()
gen.Dorogovstev_Mendes(grafotest,num_nodos=50)
grafotest.generar_archivoGRAPH('Dorogovstev_Mendes50')

grafotest=gr.Grafo()
gen.Dorogovstev_Mendes(grafotest,num_nodos=250)
grafotest.generar_archivoGRAPH('Dorogovstev_Mendes250')

grafotest=gr.Grafo()
gen.Dorogovstev_Mendes(grafotest,num_nodos=500)
grafotest.generar_archivoGRAPH('Dorogovstev_Mendes500')