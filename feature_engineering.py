from datavisualization import visualize_data
import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_geocoder")

def geocode_location(row):
    if pd.isnull(row['Latitude']) or pd.isnull(row['Longitude']):
        location = geolocator.geocode(row['Field name'])
        #print("loc:",location)
        if location:
            row['Latitude'] = location.latitude
            row['Longitude'] = location.longitude
    return row

def feature_engineering():
    data = visualize_data()
    data = data.apply(geocode_location, axis=1)
    data.loc[data['Field name']=='RHOURDE EL BAGUEL','Longitude'] = geolocator.geocode("Ouargla Province").longitude
    data.loc[data['Field name'] == 'ROURKE GAP', 'Longitude'] = geolocator.geocode("MINNELUSA").longitude
    data.loc[data['Field name'] == 'ROURKE GAP', 'Latitude'] = geolocator.geocode("MINNELUSA").latitude
    data.loc[data['Field name'] == 'WUBAITI', 'Longitude'] = geolocator.geocode("HUANGLONG").longitude
    data.loc[data['Field name'] == 'WUBAITI', 'Latitude'] = geolocator.geocode("HUANGLONG").latitude
    data.loc[data['Field name'] == 'HARMATTAN-ELKTON', 'Longitude'] = geolocator.geocode("TURNER VALLEY").longitude
    data.loc[data['Field name'] == 'HARMATTAN-ELKTON', 'Latitude'] = geolocator.geocode("TURNER VALLEY").latitude

    # null_data = data[data.isnull().any(axis=1)]
    
    # print("Null Data:", null_data[['Country','Region','Field name','Latitude','Longitude']])
    # print("----:",null_data[['Latitude','Longitude']].isnull().sum())
    data = data.drop(['Country','Region','Field name','Reservoir unit','Basin name','Operator company','Reservoir period',
                    'Tectonic regime','Reservoir status','Lithology','Hydrocarbon type','Structural setting'],axis=1)
    #print(data['Onshore/Offshore'].value_counts())
    data.replace({'Onshore/Offshore':{'ONSHORE':0,'OFFSHORE':1,'ONSHORE-OFFSHORE':0}},inplace=True)
    
    print(data.head())
    print(data['Onshore/Offshore'].value_counts())

    onshore_count, offshore_count =data['Onshore/Offshore'].value_counts()
    offshore = data[data['Onshore/Offshore'] == 0]
    onshore = data[data['Onshore/Offshore'] == 1]
    offshore_over = offshore.sample(onshore_count,replace=True)
    data_balanced = pd.concat([offshore_over,onshore], axis=0)
    data_balanced['Onshore/Offshore'].groupby(data_balanced['Onshore/Offshore']).count()
    print(data_balanced['Onshore/Offshore'].value_counts())
    data_balanced.to_csv('oil_field_cleansed_data.csv')

    #data_balanced.copy()

feature_engineering()