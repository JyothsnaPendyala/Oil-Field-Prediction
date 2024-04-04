from data_analysis import analyse_data

def data_preprocess():
    data = analyse_data()
    df = []
    for i in data:
        i = i.drop(['Country','Region','Field name','Reservoir unit','Basin name','Operator company','Reservoir period',
                    'Tectonic regime','Reservoir status','Lithology','Hydrocarbon type','Structural setting'],axis=1)
        print(i.head())
        df.append(i)
    return df

data_preprocess()