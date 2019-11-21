https://towardsdatascience.com/efficient-frontier-portfolio-optimisation-in-python-e7844051e7f



# TODO https://www.statsmodels.org/stable/examples/index.html#statespace
# Beta/correlation computations
## https://towardsdatascience.com/four-ways-to-quantify-synchrony-between-time-series-data-b99136c4a9c9



# Add filter
# Which c


def correlationCompute(tickerList = c, whichMetric = , returnBeta = , )
        '''' Computes correlation table between stocks 
            Beta_1 Is beta related to all selected stocks  
            Beta_2 is related to all stocks available
            ''''

    dataLink = "C://Users//Augus//PycharmProjects//BorsData//data"

    import os
    tickerReadSet[]

    dirs = os.listdir(dataLink)

    dirsList = []
    for item in dirs:
        temp = dataLink + "//" + item
        dirsList.append(temp)

    dataSet1 = pd.read_csv("C://Users//Augus//PycharmProjects//BorsData//data//AF B//AF BQuarter.csv")  # doctest: +SKIP
    dataSet2 = pd.read_csv("C://Users//Augus//PycharmProjects//BorsData//data//ACRI//ACRIQuarter.csv")  # doctest: +SKIP


    dataSet1['datetime'] = pd.to_datetime(dataSet1['report_End_Date']) # Convert time variable to time type
    dataSet1 = dataSet1.set_index('datetime') # Set to time , make series
    dataSet1.drop(['report_End_Date'], axis=1, inplace=True) # Drop time column

    dataSet2['datetime'] = pd.to_datetime(dataSet2['report_End_Date']) # Convert time variable to time type
    dataSet2 = dataSet2.set_index('datetime') # Set to time , make series
    dataSet2.drop(['report_End_Date'], axis=1, inplace=True) # Drop time column



    # compute returns
    dataSet1['stock_Price_Average_avgReturn'] = dataSet1['stock_Price_Average'].pct_change(periods=-1)
    dataSet2['stock_Price_Average_avgReturn'] = dataSet2['stock_Price_Average'].pct_change(periods=-1)

    returnsList = []
    # Correaltion between two
    dataSet1["cash_Flow_From_Investing_Activities"].corr(dataSet2["cash_Flow_From_Investing_Activities"])








result = pd.concat([dataSet1, dataSet2], axis=1)
test.iloc[:1]
# Need to choose variables earlier




def weightGeneration(tickerList, # 1 * Possiblestocks
                        numPortfolios # Possible permutations
                        ):
    numWeights = tickerList.shape[1]
    results = np.zeros((numPortfolios, numWeights))
    # Generate proposals:
    for i in range(numPortfolios):
        # select random weights for portfolio holdings
        weights = np.random.random(numWeights)
        # rebalance weights to sum to 1
        weights /= np.sum(weights)
        #weights=weights*100
        results[i,] = weights
    return results









    inputConstraintMatrix1,  # 1 * Possiblestocks
    inputConstraintMatrix2,  # 1 * Possiblestocks
    inputConstraintMatrix3,  # 1 * Possiblestocks


    # store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
    results[2, i] = results[0, i] / results[1, i]

    # calculate portfolio return and volatility
    portfolio_return = np.sum(stock_mean_daily_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)

    # convert results array to Pandas DataFrame
    results_frame = pd.DataFrame(results.T, columns=['ret', 'stdev', 'sharpe'])

    # create scatter plot coloured by Sharpe Ratio
    plt.scatter(results_frame.stdev, results_frame.ret, c=results_frame.sharpe, cmap='RdYlBu')
    plt.colorbar()




def optimalPortfolios():


# Maximization

# How is goal function defined?















test=dataSet2['stock_Price_Average_avgReturn'] + dataSet1['stock_Price_Average_avgReturn']










test.mean(axis = 0) # return mean








dataSet2['stock_Price_Average_avgReturn']+dataSet1['stock_Price_Average_avgReturn']





