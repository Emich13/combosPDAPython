import csv

#Función para extraer los DD en una lista (DD.csv)
#El negocio debe definir cuales son los DD a los que quiere aplicar los combos
def distribuidores():
    list_DD=[]
    with open('DD.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            e = i.pop()
            list_DD.append(e)
        return list_DD 
DD = distribuidores()

#Función para extraer los combos en una lista (combos.csv)
#Se crean codigos de combos (solo hay que tener en cuenta que no estén repetidos con los que están en PDA)
def combos():
    list_combos=[]
    with open('combos.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            e = i.pop()
            list_combos.append(e)
        return list_combos
CC = combos()

#Función para devolver cluster;combo;DD teniendo en cuenta los DD que aparecen en DD.csv y los combos de combos.csv
def cluster_dd(distri, combo):
    with open('dsc_clusters.csv') as csv_file: #dsc_clusters es el archivo maestro que tiene codigo;nombre;estado;codigoDistribuidor
        csv_reader = csv.reader(csv_file, delimiter=';')
       
        for row in csv_reader:    
            for j in combo: #recorro los combos
                for x in distri: #Recorro los distribuidores 
                    if row[3] == x :
                        a = row[0],j,row[3]
                        yield a  # Se usa yield porque return cortaba el bucle            
        return 

# Se escribe el archivo dsc_clusters_combos.csv 
data = list(cluster_dd(DD,CC))
file = 'dsc_clusters_combos.csv'

with open (file, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    for i in data:
        writer.writerow(i)

    print('Se creó con éxito el archivo:', file)