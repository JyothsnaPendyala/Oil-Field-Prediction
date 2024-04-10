import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
import io
from PIL import Image
#from data_preprocess import data_preprocess
from data_analysis import analyse_data

def visualize_data():
    data, categorical_features, numerical_features = analyse_data()
    print(data.columns)
    data_num = data.drop(list(categorical_features),axis=1)
    #data_num = data[numerical_features]
    data_num_corr = data_num.corr()
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x = data_num_corr.columns,
            y = data_num_corr.index,
            z = np.array(data_num_corr),
            text=data_num_corr.values,
            texttemplate='%{text:.2f}',
            colorscale = 'YlGnBu'   
        )
    )
    fig.update_layout(template='plotly_dark')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    #fig.show()
    fig.write_image(f"Heatmap.jpg")
    for categorical_feature in categorical_features:
        fig = px.histogram(data, x=categorical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        #a.append(fig)
        # fig.show()
        if '/' in categorical_feature:
            categorical_feature = categorical_feature.replace('/','_')
        fig.write_image(f"histogram_{categorical_feature}.jpg")
    for numerical_feature in numerical_features:
        fig = px.box(data, y=numerical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False,zeroline=True,zerolinewidth=4)
        #a.append(fig)
        #fig.show()
        fig.write_image(f"boxplot_{numerical_feature}.jpg")
    return data


visualize_data()
