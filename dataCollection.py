import requests
from common import idConv
from time import sleep
import numpy as np
import pandas as pd
class fetchTickerData:
    # Initializer / Instance Attributes
    def __init__(self, tickerName, ticker_list, insId_list, apiKey):
        self.name = tickerName

        """Price data """
        tempPriceData = requests.get("https://apiservice.borsdata.se/v1/instruments/" + idConv(
            tickerName, ticker_list, insId_list) + "/stockprices?authKey=" + apiKey).json()
        tickerPriceData = []
        # print(tempPriceData["stockPricesList"])
        for item in tempPriceData["stockPricesList"]:
            tempPrice = [item["d"], item["c"], item["o"], item["h"], item["l"]]
            tickerPriceData.append(tempPrice)
        tickerPriceDataFrame = pd.DataFrame(data=tickerPriceData,
                                         columns=("Time", "Close", "Open", "High", "Low"))
        self.priceData = tickerPriceDataFrame
        sleep(1)
        """ Year Data """
        tempYear = requests.get("https://apiservice.borsdata.se/v1/instruments/" + idConv(tickerName, ticker_list, insId_list) +
                                "/reports/year?authKey=" + apiKey).json()
        yearData = []
        sleep(1)
        #print(tempYear["reports"])
        for item in tempYear["reports"]:
            yearTemp = [item["report_End_Date"], item["revenues"], item["gross_Income"],
                        item["operating_Income"], item["profit_Before_Tax"],
                        item["profit_To_Equity_Holders"], item["earnings_Per_Share"],
                        item["number_Of_Shares"], item["dividend"], item["intangible_Assets"],
                        item["tangible_Assets"], item["financial_Assets"], item["non_Current_Assets"],
                        item["cash_And_Equivalents"], item["current_Assets"], item["total_Assets"],
                        item["total_Equity"], item["non_Current_Liabilities"],
                        item["current_Liabilities"], item["total_Liabilities_And_Equity"],
                        item["net_Debt"], item["cash_Flow_From_Operating_Activities"],
                        item["cash_Flow_From_Investing_Activities"],
                        item["cash_Flow_From_Financing_Activities"], item["cash_Flow_For_The_Year"],
                        item["free_Cash_Flow"], item["stock_Price_Average"], item["stock_Price_High"],
                        item["stock_Price_Low"]]
            yearData.append(yearTemp)
        yearDataFrame = pd.DataFrame(data=yearData,
                                         columns=("report_End_Date", "revenues", "gross_Income", "operating_Income",
                                                  "profit_Before_Tax", "profit_To_Equity_Holders", "earnings_Per_Share",
                                                  "number_Of_Shares", "dividend", "intangible_Assets",
                                                  "tangible_Assets",
                                                  "financial_Assets", "non_Current_Assets", "cash_And_Equivalents",
                                                  "current_Assets", "total_Assets", "total_Equity",
                                                  "non_Current_Liabilities",
                                                  "current_Liabilities", "total_Liabilities_And_Equity", "net_Debt",
                                                  "cash_Flow_From_Operating_Activities",
                                                  "cash_Flow_From_Investing_Activities",
                                                  "cash_Flow_From_Financing_Activities", "cash_Flow_For_The_Year",
                                                  "free_Cash_Flow", "stock_Price_Average", "stock_Price_High",
                                                  "stock_Price_Low"))
        self.yearData = yearDataFrame
            # tempRr12 = requests.get("https://apiservice.borsdata.se/v1/instruments/" + idConv(tickerName) + "/reports/r12?authKey=" + apiKey).json()
            # tempRr12["reports"][0].keys()
            # tempRr12["reports"][0]["report_Start_Date"]
            # tempRr12["reports"][0]["report_End_Date"]
        print("Year data read")
        """Quarter data"""
        tempQuarter = requests.get("https://apiservice.borsdata.se/v1/instruments/" + idConv(tickerName, ticker_list, insId_list) +
                                   "/reports/quarter?authKey=" + apiKey).json()
        quarterData = []
        # print(tempQuarter["reports"])
        for item in tempQuarter["reports"]:
            quarterTemp = [item["report_End_Date"], item["revenues"], item["gross_Income"],
                               item["operating_Income"], item["profit_Before_Tax"],
                               item["profit_To_Equity_Holders"], item["earnings_Per_Share"],
                               item["number_Of_Shares"], item["dividend"], item["intangible_Assets"],
                               item["tangible_Assets"], item["financial_Assets"], item["non_Current_Assets"],
                               item["cash_And_Equivalents"], item["current_Assets"], item["total_Assets"],
                               item["total_Equity"], item["non_Current_Liabilities"],
                               item["current_Liabilities"], item["total_Liabilities_And_Equity"],
                               item["net_Debt"], item["cash_Flow_From_Operating_Activities"],
                               item["cash_Flow_From_Investing_Activities"],
                               item["cash_Flow_From_Financing_Activities"], item["cash_Flow_For_The_Year"],
                               item["free_Cash_Flow"], item["stock_Price_Average"], item["stock_Price_High"],
                               item["stock_Price_Low"]]
            quarterData.append(quarterTemp)
        quarterDataFrame = pd.DataFrame(data=quarterData,
                                            columns=("report_End_Date", "revenues", "gross_Income", "operating_Income",
                                                     "profit_Before_Tax", "profit_To_Equity_Holders",
                                                     "earnings_Per_Share",
                                                     "number_Of_Shares", "dividend", "intangible_Assets",
                                                     "tangible_Assets",
                                                     "financial_Assets", "non_Current_Assets", "cash_And_Equivalents",
                                                     "current_Assets", "total_Assets", "total_Equity",
                                                     "non_Current_Liabilities",
                                                     "current_Liabilities", "total_Liabilities_And_Equity", "net_Debt",
                                                     "cash_Flow_From_Operating_Activities",
                                                     "cash_Flow_From_Investing_Activities",
                                                     "cash_Flow_From_Financing_Activities", "cash_Flow_For_The_Year",
                                                     "free_Cash_Flow", "stock_Price_Average", "stock_Price_High",
                                                     "stock_Price_Low"))
        print("Quarter data read")
        self.quarterData = quarterDataFrame