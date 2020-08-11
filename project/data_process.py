#!/usr/bin/env python3
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import datetime
import subprocess
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime

PATH='/home/vdelaluz/git/distributed-computing/project/'
PATH1='/home/vdelaluz/public_html/gicc/static/cursos/2020-II/datapirates/'
today = datetime.today().strftime('%Y-%m-%d')
#with open("db.json", "w") as write_file:
#    json.dump(config, write_file)

with open(PATH+'/config/'+'db.json') as json_file:
    config = json.load(json_file)

    date_process = []
    tweet_process = []
    dollar_process = []
    date_process_5 = []
    tweet_process_5 = []
    dollar_process_5 = []

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor2= cnx.cursor()
    query = ("SELECT date,tweet,dollar FROM tipo_cambio_tweets ORDER BY date")
    query2= ("SELECT date,tweet,dollar FROM tipo_cambio_tweets ORDER BY date DESC LIMIT 5")
    cursor.execute(query)
    for (date, tweet,dollar) in cursor:
        #print(f"{date}\t{tweet}\t{dollar}")
        date_process.append(date)
        tweet_process.append(int(tweet))
        dollar_process.append(int(dollar))
    cursor2.execute(query2)
    for (date, tweet,dollar) in cursor2:
        #print(f"{date}\t{tweet}\t{dollar}")
        date_process_5.append(date)
        tweet_process_5.append(int(tweet))
        dollar_process_5.append(int(dollar))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
    cnx.close()



arr = np.array(tweet_process)
arr = np.true_divide(arr, 100)
plt.plot(arr,linestyle = "--",marker="o",color='blue')
plt.plot(dollar_process,linestyle = "--",marker="o",color='green')
plt.title('Correlation between dollar and #DonaldTrump hashtag')
plt.xlabel('Timeline')
plt.ylabel('Total tweets dividen by 100 and dollar to mexican pesos')
x  = np.arange(0, len(date_process), 1)
plt.xticks(x,date_process, rotation='vertical')
blue_patch = mpatches.Patch(color='blue',label = 'Tweets')
green_patch = mpatches.Patch(color='green',label = 'Dollar')
plt.legend(handles = [blue_patch,green_patch])
#plt.grid(True)
plt.savefig(PATH+'/graficas/'+'alldata'+'.png')
plt.savefig(PATH1+'alldata'+'.png')
plt.close()

date_process_5.reverse()
arr1 = np.array(tweet_process_5)
arr1 = np.true_divide(arr1, 100)
plt.plot(arr1,linestyle = "--",marker="o",color='blue')
plt.plot(dollar_process_5,linestyle = "--",marker="o",color='green')
plt.title('Correlation between dollar and #DonaldTrump hashtag')
plt.xlabel('Timeline')
plt.ylabel('Total tweets dividen by 100 and dollar to mexican pesos')
x  = np.arange(0, len(date_process_5), 1)
plt.xticks(x,date_process_5, rotation='vertical')
blue_patch = mpatches.Patch(color='blue',label = 'Tweets')
green_patch = mpatches.Patch(color='green',label = 'Dollar')
plt.legend(handles = [blue_patch,green_patch])
plt.grid(True)
plt.savefig(PATH+'/graficas/'+'5days'+'.png')
plt.savefig(PATH1+'5days'+'.png')
plt.close()
