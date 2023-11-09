
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getPrecip(name):
    filename = name
    file1 = open(filename, "r")
    dict = {}
    great = []  
    something = file1.readline()
    for line in file1:
        currentline = line.split(",")
        nameLine = currentline[0]
        dict.update({nameLine: float(currentline[10])})
    #print(dict)
    greatest =0
    greatest_key=""
    for key in dict:
        if dict[key]>=greatest:
            greatest = dict[key]
            greatest_key= key       
    great.append(greatest_key)
    print(great)

#3
def getActualmaxtempAverage(name):
    filename = name
    file1 = open(filename, "r")
    something = file1.readline()
    average_list =[]
    sum = 0
    average = 0
    for line in file1:
        currentline = line.split(",")
        if "2014-7" in currentline[0]:
            average_list.append(currentline[3])
        else:
            continue
    for item in average_list:
        sum+=float(item)
        average = float(sum/len(average_list))
    print("average actual max temp for July 2014: " + str(average))



def actualMaxtempEqual(name):
    filename = name
    file1 = open(filename, "r")
    something = file1.readline().split(",")
    dict ={}
    days =[]
    
    for item in something:
        dict[item]= None
    #print(dict)
    for line in file1:
        currentline = line.split(",")
        counter = 0
        for key in dict:
            dict[key]=currentline[counter]
            counter+=1
        #print(dict)
        num1 = int(dict["actual_max_temp"])
        num2 = int(dict["record_max_temp"])        
        if num1==num2:
            days.append(dict["date"])
    print("days when actual max temp and record max temp were the same: " +str(days))  


def getRainOctober(name):
    filename = name
    file1 = open(filename, "r")
    something = file1.readline()
    list =[]
    sum = 0
    average = 0
    for line in file1:
        currentline = line.split(",")
        if "2014-10" in currentline[0]:
            list.append(currentline[10])
        else:
            continue
    for item in list:
        sum+=float(item)
    print("total rainfall for October 2014: " + str(sum))


def actualLow(name):
    filename = name
    file1 = open(filename, "r")
    something = file1.readline().split(",")
    dict ={}
    days =[]
    
    for item in something:
        dict[item]= None
    #print(dict)
    for line in file1:
        currentline = line.split(",")
        counter = 0
        for key in dict:
            dict[key]=currentline[counter]
            counter+=1
        #print(dict)
        if int(dict["actual_min_temp"])<60 and int(dict["actual_max_temp"])>90:
            days.append(dict["date"])
    print("days when actual max temp and record max temp were the same: " +str(days))  
    

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

def linechar():
    file1 = open('weather_data.txt', "r")
    something = file1.readline()
    axes = plt.gca()
    days =[]
    max_temp =[]
    min_temp=[]
    for line in file1:
        currentLine = line.split(",")
        days.append(currentLine[0])
        max_temp.append(int(currentLine[3]))
        min_temp.append(int(currentLine[2]))
            #max temp and min temp
    df = pd.DataFrame({'Max Temp': max_temp, 'Min Temp': min_temp, 'Days': days})
    df.plot(x= "Days", y = "Max Temp", ax = axes, style={'Max Temp': 'r'})
    df.plot(x= "Days", y = "Min Temp", ax = axes, style={'Min Temp': 'b'})

def histo():
    file1 = open('weather_data.txt', "r")
    something = file1.readline()
    axes = plt.gca()
    days =[]
    precip=[]
    for line in file1:
        currentLine = line.split(",")
        days.append(currentLine[0])
        precip.append(float(currentLine[10]))
    df = pd.DataFrame({'Precip': precip, 'Days': days})
    df.plot(kind ="hist", title="Precipitation", ax = axes)

    





    

def main():
    getPrecip("weather_data.txt")
    getActualmaxtempAverage("weather_data.txt")
    actualMaxtempEqual("weather_data.txt")
    getRainOctober("weather_data.txt")
    actualLow("weather_data.txt")
    #createChart("weather_data.txt")



if __name__ == "__main__":
    main()

# %%
