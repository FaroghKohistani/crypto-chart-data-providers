import requests
                               

def get_charts_btc_average(asset_code):
    url = "https://apiv2.bitcoinaverage.com/indices/global/history/"\
    +asset_code.upper()+"GBP?period=monthly&format=json"
    headers = {'X-ba-key':'NjgxMWNiODcxMzY3NGZlZDlhNTQxMTZkMjY0OTNkODQ'}
    
    response = requests.request("GET",url, headers=headers)
    
    return response


def get_charts_coinapi(asset_code):
    url = "https://rest.coinapi.io/v1/ohlcv/"+asset_code.upper()\
    +"/GBP/history?period_id=1HRS&time_start=2016-01-01T00:00:00&limit=1" 
    headers = {'X-CoinAPI-Key':'7394CAE1-99FB-462D-B2B4-F3CD9DBEA4C0'}
    
    response = requests.request("GET",url, headers=headers)
    
    return response 
    
    
def get_charts_cryptocompare(asset_code):
    url = "https://min-api.cryptocompare.com/data/histohour"
    querystring = {"fsym":asset_code,"tsym":"GBP","limit":"1"}
    
    response = requests.request("GET", url, params = querystring)
    
    return response


def get_charts_poloniex(asset_code):
    url = "https://poloniex.com/public"
    querystring = {"command":"returnChartData","currencyPair":"BTC_"+asset_code,
                   "start":"1548529200","end":"9999999999","period":"86400"}
    
    response = requests.request("GET", url, params=querystring)
    
    return response


def get_assets_cointec():
    url = "https://api.staging.cointec.co.uk/assets/status"
    response = requests.request("GET",url)
    
    return response
