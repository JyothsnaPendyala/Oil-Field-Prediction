from data_extraction import extract_data

def analyse_data():
    data = extract_data()
    print("Analysis on Data:")
    print(data.describe())
    print(data.info())
    print("Features in the data:", data.columns)
    print(data.isnull().sum())
    for feature in data.columns:
        if data[feature].isnull().sum() > 0:
            print(f"Missing values are found in {feature}. Number of missing values are {data[feature].isnull().sum()}")
    if data.duplicated().sum() > 0:
        print("Duplicate Values are present")
    else:
        print("No Duplicate values")
    for column in data.columns:
        print(column,data[column].nunique())
    categorical_features = data.select_dtypes("object").columns
    numerical_features = data.select_dtypes("number").columns
    print("Categorical: ",categorical_features)
    print("Numerical: ",numerical_features)
    # for categorical_feature in categorical_features:
    #     print(i[categorical_feature].value_counts())
    return data, categorical_features, numerical_features

analyse_data()