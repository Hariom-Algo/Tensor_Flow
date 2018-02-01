import datetime
def graphData(stock,MA1,MA2):
    try:
        print('Currently Pulling',stock)
        q.ApiConfig.api_key = "API-KEY"   #API Key
        sData = q.get('WIKI/'+stock+'')
    except Exception as e:
            print(str(e), 'failed to organize pulled data.')
    except Exception as e:
        print(str(e), 'failed to pull pricing data')

    try:
        sData = sData[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
        x = 0
        y = len(date)
        newAr = []
        while x < y:
            appendLine = date[x], Adj. Open[x],Adj. High[x],Adj. Low[x],Adj. Close[x],Adj. Volume[x]
            newAr.append(appendLine)
            x+=1