import csv

def init_traitement():
    updated_data = []
    noms_vu = set()

    with open("arrets.csv") as csvfile :
        reader = csv.reader(csvfile, delimiter = ";")
        for row in reader:
            nom = row[1]
            
            if(row[6]) == 'Y' and nom not in noms_vu:
                temp = []
                temp.append(nom)#nom
                """temp.append(row[2])#commune
                temp.append(row[3])#pays"""

                temp.append(row[5].split(", "))#coo séparés et mis dans une liste
                updated_data.append(temp)#que les y
                noms_vu.add(nom)

    return updated_data

print(init_traitement())