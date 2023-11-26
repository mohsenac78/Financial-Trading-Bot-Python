def ClassificationSymboles (Classification_Result):
    
    # Check Classification_Result list
    # print(Classification_Result)

    Update_list = list()
    symbole_list= ['EURUSD','USDCHF','GBPUSD','USDJPY','USDCAD','AUDUSD','EURJPY','NZDUSD','GBPCHF' ]
    key_words_0 = ['From','Till']
    key_words_1 = ['Buy','Sell']
    key_words_2 = ['Take','Stop']

    for items in Classification_Result:
        for subitems in items:
            # print(subitems)
            if subitems[0] in symbole_list:
                Update_list.append([f'{subitems[0]}'])
                # Update_list.append([f'{subitems[2]} {subitems[3]} {subitems[4]}'])
        
            elif subitems[0] in key_words_0 or subitems[0] in key_words_1:
                Update_list.append([f'{subitems[0]} {subitems[1]}'])
                Update_list.append([f'{subitems[2]}'])

            elif subitems[0] in key_words_2:
                Update_list.append([f'{subitems[0]} {subitems[1]} {subitems[2]}'])
                Update_list.append([f'{subitems[3]}'])
    
    # Check Update_list
    # print(Update_list)

    Mainlist=list()
    for [items] in Update_list:
        Mainlist.append(items)
    
    # Check Mainlist
    # print(Mainlist)

    Mainlist2=list()
    SubList=list()

    for items in Mainlist:

        if items in symbole_list and len(SubList)>1:

            Mainlist2.append(SubList)
            SubList = list()

        SubList.append(items) 

    Mainlist2.append(SubList)
    
    # Check Mainlist2
    # print(Mainlist2)

    return Mainlist2