import datetime
import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
from datetime import datetime
    
def insertar(data_query):
    try:
        cnx=mysql.connector.connect(**config)
        cursor=cnx.cursor()
        query=("INSERT INTO tipo_cambio_tweets(date,tweet,dollar) VALUES(%s,%s,%s) ")
        cursor.execute(query,data_query)
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("algo esta mal con tu usuario o contrasena")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("la base de datos no existe")
        else:
            print(err)
    else:
        cnx.close()

if __name__ == "__main__":
    PATH='/home/saul/victor/'

    with open(PATH+'/config/'+'db.json') as json_file:
        config=json.load(json_file)
    
    for filename in glob.glob(PATH+"*.json"):
        print(filename)
        real_file =filename[18:]
        with open(real_file,'r') as f:
            datos=json.load(f)
        date= datos['date']
        tweets=datos['tweet']
        dolar=datos['dollar']
        data_query=(date,tweets,dolar)
        insertar(data_query)
    
