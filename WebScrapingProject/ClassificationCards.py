# important librarys
# website = 'https://foresignal.com/en/'
# class or id
# class or id value ex : 'd-flex flex-row flex-wrap signal-row'
# website_url = input('insert website url : ')
# class_id = input('Choose "class" or "id" : ')
# class_id_value = input('insert class or id "value" : ')
# print(signaltitle(website_url,class_id,class_id_value))
# print(Output_Result)

# from extractsignaltitles import signaltitle
# Output_Result = signaltitle('https://foresignal.com/en/','class','d-flex flex-row flex-wrap signal-row')
# print(Output_Result)


def ClassificationCards (alist):
    
    # Check alist 
    # print(alist)

    symbole_list = ['EUR/USD','USD/CHF','GBP/USD','USD/JPY','USD/CAD','AUD/USD','EUR/JPY','NZD/USD','GBP/CHF' ]

    for items in alist:
        for items_2 in symbole_list:
            if items_2 in items:   
                items[0]=items[0].replace('/','')
                

    key_words = ['EURUSD','USDCHF','GBPUSD','USDJPY','USDCAD',
                 'AUDUSD','EURJPY','NZDUSD','GBPCHF' ]
    
    Mainlist = list()
    Sublist = list()

    for items in alist:

        for item in items:
            
            if item in key_words and len(Sublist)>1:

                Mainlist.append(Sublist)
                Sublist = list()
        
        Sublist.append(items)
    
    Mainlist.append(Sublist)
    
    # Check Final Mainlist 
    # print(Mainlist)
        
    return Mainlist

# print (ClassificationCards(Output_Result))