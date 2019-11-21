# Import local modules
import common
from dataCollection import fetchTickerData
#import models
# import importlib; importlib.reload(dataCollection.fetchTickerData)
# Import PyPi modules
import requests
import json
import numpy as np
import pandas as pd
import os

# Global variables
apiKey = "c382831b6e3949d78318256f6d44d1e7" # Set API key
currentWD = os.getcwd()

# Initial request TODO move to function(s)
requestInstrument = requests.get("https://apiservice.borsdata.se/v1/instruments?authKey=" + apiKey)
dataInstruments = requestInstrument.json()

requestCountries = requests.get("https://apiservice.borsdata.se/v1/countries?authKey=" + apiKey)
dataCountries = requestCountries.json()

requestMarkets = requests.get("https://apiservice.borsdata.se/v1/markets?authKey=" + apiKey)
dataMarkets = requestMarkets.json()

requestSectors = requests.get("https://apiservice.borsdata.se/v1/sectors?authKey=" + apiKey)
dataSectors = requestSectors.json()

names_list, urlName_list, instrument_list, ticker_list, sectorId_list, marketId_list, countryId_list, \
insId_list = common.instrumentDictionary(dataInstruments) # Fetch all ticker data


sectorId_list_transl = []
for value in sectorId_list:
    temp = common.getSector(value)
    sectorId_list_transl.append(temp)

marketId_list_transl = []
for value in marketId_list:
    temp = common.getMarket(value)
    marketId_list_transl.append(temp)

countryId_list_transl = []
for value in countryId_list:
    temp = common.getCountry(value)
    countryId_list_transl.append(temp)

# Create data folder
try:
    os.mkdir(currentWD + "\\data")
except OSError:
    print("already exists")

pd.DataFrame({'Name':names_list, 'Ticker':ticker_list, 'Sector':sectorId_list_transl, 'Market':marketId_list_transl, 'Country':countryId_list_transl}).to_csv(path_or_buf=currentWD + "\\data\\Tickers.csv", sep=",",
                                          index=False, decimal=".", encoding="utf-8")

# User defined place of where files are
# TODO Add checks for input file
# TickerfileLocation = input("Please provide file location. \n e.g:  C:/Users/Augus/PycharmProjects/BorsData/testTickers.csv ")
TickerfileLocation = "C:/Users/Augus/PycharmProjects/BorsData/data/Tickers.csv"
tickerReadSet = pd.read_csv(filepath_or_buffer=TickerfileLocation)


tickerObjectList = []
i = 0
for item in tickerReadSet['Ticker']: # TODO make this a method to store all instruments locally
    i = i + 1
    print('Reading item', i, ",", item)
    try:
        tempObject = fetchTickerData(item, ticker_list=ticker_list, insId_list=insId_list, apiKey=apiKey)
        tickerObjectList.append(tempObject)
    except OSError:
        print(item, 'failed collection')
    try:
        os.mkdir(currentWD + "\\data\\" + item)
        print(item, 'folder created')
    except OSError:
        print(item, 'folder already exists')
    try:
        tempObject.priceData.to_csv(path_or_buf=currentWD + "\\data\\" + item + "\\" + item + "price.csv", sep=",",
                                      header=True, index=False, decimal=".")
        print(item, 'price data created')
    except OSError:
        print(item, "couldn't write price data")
    try:
        tempObject.quarterData.to_csv(path_or_buf=currentWD + "\\data\\" + item + "\\" + item + "Quarter.csv", sep=",",
                                      header=True, index=False, decimal=".")
        print(item, 'quarter data created')
    except OSError:
        print(item, "couldn't write quarter data")
    try:
        tempObject.yearData.to_csv(path_or_buf=currentWD + "\\data\\" + item + "\\" + item + "Year.csv", sep=",",
                                      header=True, index=False, decimal=".")
        print(item, 'year data created')
    except OSError:
        print(item, "couldn't write year data")






# For each in names list call ticker
# TODO add option to exclude data in fetchTickerData, general filter




# For each file in list selected do this

def readFiles(tickerList=tickerReadSet,
              selectedTickers=["ATRE", "AZN", "BILL"],
              selectedSectors="all",
              selectedCountries="all",
              selectedMarket="all"): # Ticker, Sector or Market
    readDatasets = {}
    if selectedMarket == "all" and selectedCountries == "all" and selectedSectors == "all" and selectedTickers == "all":
        for ticker in tickerList["Ticker"]:
            year = pd.read_csv(filepath_or_buffer="C:/Users/Augus/PycharmProjects/BorsData/data/" + ticker + "/" + ticker + "Year" + ".csv")
            quarter = pd.read_csv(filepath_or_buffer="C:/Users/Augus/PycharmProjects/BorsData/data/" + ticker + "/" + ticker + "Quarter" + ".csv")
            price = pd.read_csv(filepath_or_buffer="C:/Users/Augus/PycharmProjects/BorsData/data/" + ticker + "/" + ticker + "price" + ".csv")
            readDatasets[ticker+"_year"]=year
            readDatasets[ticker + "_quarter"]=quarter
            readDatasets[ticker + "_price"]=price
    else:
        indecesTickers = np.array(None)
        indecesSectors=np.array(None)
        indecesCountries=np.array(None)
        indecesMarkets=np.array(None)

        if selectedTickers != "all":
            bool=tickerList['Ticker'].isin(selectedTickers)
            indecesTickers = np.where(bool== True)

        if selectedSectors != "all":
            bool=tickerList['Sector'].isin(selectedTickers)
            indecesSectors = np.where(bool==True)

        if selectedCountries != "all":
            bool=tickerList['Country'].isin(selectedTickers)
            indecesCountries=np.where(bool==True)

        if selectedMarket != "all":
            bool=tickerList['Market'].isin(selectedTickers)
            indecesMarkets=np.where(bool==True)

        keptIndices=np.concatenate((indecesTickers, indecesSectors, indecesCountries, indecesMarkets), axis=None)
        keptIndices=keptIndices[keptIndices != np.array(None)]
        keptIndices=np.unique(keptIndices)
        tickerSubsetSelected=tickerList.iloc[keptIndices]

        for ticker in tickerSubsetSelected["Ticker"]:
            year = pd.read_csv(filepath_or_buffer="C:/Users/Augus/PycharmProjects/BorsData/data/" + ticker + "/" + ticker + "Year" + ".csv")
            quarter = pd.read_csv(filepath_or_buffer="C:/Users/Augus/PycharmProjects/BorsData/data/" + ticker + "/" + ticker + "Quarter" + ".csv")
            price = pd.read_csv(filepath_or_buffer="C:/Users/Augus/PycharmProjects/BorsData/data/" + ticker + "/" + ticker + "price" + ".csv")
            readDatasets[ticker+"_year"]=year
            readDatasets[ticker + "_quarter"]=quarter
            readDatasets[ticker + "_price"]=price

    return readDatasets



test=readFiles()

test.keys()






