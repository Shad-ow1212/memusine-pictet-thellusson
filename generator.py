import csv

def parse_coo(coo): #met les coo en float
    temp = coo.split(", ")
    x = float(temp[0])
    y = float(temp[1])

    return x, y

def init_traitement():
    updated_data = []
    noms_vu = set()

    with open("arrets.csv") as csvfile :
        reader = csv.reader(csvfile, delimiter = ";")
        for row in reader:
            nom = row[1]
            
            if(row[6]) == 'Y':
                temp = []
                if nom not in noms_vu: #si arret nouveau
                    temp.append(nom)#nom
                    """temp.append(row[2])#commune
                    temp.append(row[3])#pays"""

                    temp.append(parse_coo(row[5]))#coo
                    noms_vu.add(nom) #update les arrets deja vu
                    updated_data.append(temp) #ajoute temp a updated_data
                else: #si arret deja vu
                    for i in updated_data:
                        if i[0] == row[1]:
                            i.append(parse_coo(row[5])) #ajoute uniquement les coo
            
    for i in updated_data: #Fait la moyenne des coord normalement
        if len(i) > 2:
            moyenne_x = 0
            moyenne_y = 0
            diviseur = len( i ) - 1 
            for j in range (diviseur, 0 ,-1):
                moyenne_x += i[ j ] [ 0 ]
                moyenne_y += i[ j ] [ 1 ]
                i.pop()
            
                
            moyenne_x, moyenne_y = moyenne_x / diviseur ,  moyenne_y / diviseur
            moyenne_x = round(moyenne_x, 5)
            moyenne_y = round(moyenne_y, 5)

            i.append( (moyenne_x , moyenne_y) )


                    
    return updated_data

data = init_traitement()
for d in data:
    print(d)