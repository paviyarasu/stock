from pandas_datareader import data as wb
stock_list = ['FRETAIL','AXISBANK','YESBANK']
for stock in stock_list:
    data = wb.DataReader(stock + '.NS', data_source='yahoo', start='2020-01-01')
    data.to_excel(stock + '.xlsx')
