import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

dates = []
openRecords = []
HighRecords = []
LowRecords = []

#downloaded data from https://www.google.com/finance/historical?cid=304466804484872&startdate=Jun+15%2C+2016&enddate=Jun+30%2C+2016&num=30&ei=WbVaWdHkN4fjjAG2l6OwCA
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            #print(', '.join(row))
            dat1 = row[0].split("-")[1]
            dat2 = row[0].split("-")[2];
            dat=dat1+"."+dat2
            dates.append(float(dat))
            openRecords.append(float(row[1]))
            HighRecords.append(float(row[2]))
            LowRecords.append(float(row[3]))
    return


def show_plot(dates, openRecords,HighRecords,LowRecords):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    linear_mod.fit(dates, openRecords)  # fitting the data points in the model
    plt.plot(dates, linear_mod.predict(dates), color='blue', linewidth=3)  # plotting the line made by linear regression

    HighRecords = np.reshape(HighRecords, (len(HighRecords), 1))
    linear_mod.fit(dates, HighRecords)  # fitting the data points in the model
    plt.plot(dates, linear_mod.predict(dates), color='black', linewidth=3)  # plotting the line made by linear regression

    LowRecords = np.reshape(LowRecords, (len(LowRecords), 1))
    linear_mod.fit(dates, LowRecords)  # fitting the data points in the model
    plt.plot(dates, linear_mod.predict(dates), color='green', linewidth=3)  # plotting the line made by linear regression

    plt.show()
    return



get_data('^GDAXI.csv')  # calling get_data method by passing the csv file to it
print
dates
print
open
print
"\n"

show_plot(dates, openRecords,HighRecords,LowRecords)

