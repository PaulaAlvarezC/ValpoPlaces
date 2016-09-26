import json
import sqlite3


BD = sqlite3.connect('vackr.db') #Conexion a Base de datos
Cur = BD.cursor()

# ---------------------------- Para insertar json Perros-Valparaiso en la tabla Foto-------------------------------
with open('C:\Users\Pau\Desktop\Final Valckr\Valckr\perrosvalpo.json') as data_file:
    data = json.load(data_file)
    #print data # Imprimir datos murales.json
for i in range(50):

    Titulo = data["photos"]["photo"][i]["title"]
    Url = data["photos"]["photo"][i]["url_z"]
    Owner = data["photos"]["photo"][i]["owner"]
    Date = data["photos"]["photo"][i]["datetaken"]
    Tags = data["photos"]["photo"][i]["tags"]
    ID_Tag = 1

    for ins in [(Titulo, Url, Owner, Date, Tags, ID_Tag),
                ]:
        Cur.execute('INSERT into directorios_foto (Titulo, Url, Owner, dateupload, Tags, ID_Tag_id)  VALUES (?,?,?,?,?,?)', ins)



Cur.close() #Cerrar el cursor
BD.commit()  #Guardar cambios en Base de Datos
BD.close() # Cerrar la base de datos