from ForeSignalScraper import Login
from ForeSignalScraper import CustomizeFoSignals
from TradingViewScaper import Price
from datetime import datetime
from collections import OrderedDict
import random
import time

Currencys_list = ['EURUSD','USDCHF','GBPUSD','USDJPY','USDCAD'
                  ,'AUDUSD','EURJPY','NZDUSD','GBPCHF']

desired_time = int(input('Please Enter Your Desired Time Range To load Websiter - input a number ex:20 : '))

FoLogin_url = 'https://foresignal.com/en/login/index'
FoWebsite_url = 'https://foresignal.com/en/'
Fouser_name = 'xabiz'
FoUser_password = 'tohid0010011'
Foclassorid = 'class'
Foclassoridvalue = 'd-flex flex-row flex-wrap signal-row'

final_list = Price(2,Currencys_list)

ForeSignalDriver = Login(FoLogin_url,Fouser_name,FoUser_password)

counter=0

final_informations = OrderedDict()

main_list = list()

FoFinalList = list()

Reference_list = list()


while True:

    FoFinalList_Start_len = len(FoFinalList)

    FoFinalList = CustomizeFoSignals(ForeSignalDriver,FoWebsite_url,Foclassorid,Foclassoridvalue)

    FoFinalList_Final_len = len(FoFinalList)

    Tradingview_price_dictionary = OrderedDict()

    delay_time = random.randrange(0,desired_time)

    tradnigview_scrape_counter = 0

    if FoFinalList_Start_len<FoFinalList_Final_len:
        
        main_list_start_len = len (main_list)

        for items in FoFinalList:
            if len(items) > 10 and items not in main_list:
                main_list.append(items)
        
        main_list_final_len = len (main_list)
        
        for item in range (0,9):
            now = datetime.now()
            final_list[0].switch_to.window(final_list[0].window_handles[item])
            Tradingview_price_dictionary[f'{Currencys_list[item]} : {now}'] = final_list[1][item].text
        # print(Tradingview_price_dictionary)

        for item_fo in main_list:
            for k,v in Tradingview_price_dictionary.items():
                if item_fo[0] in k[:6]:
                    item_fo.append(k)
                    item_fo.append(v)
                    final_informations[f'{item_fo[:11]}']=item_fo
        
        Reference_list_start_len = len(Reference_list)

        Reference_list = list(final_informations.items()) 
        
        Reference_list_final_len = len(Reference_list)

        for items in Reference_list[Reference_list_start_len:Reference_list_final_len]:
            
            print(items[1])
        
        

    time.sleep(delay_time)