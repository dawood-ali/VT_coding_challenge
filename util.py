import pandas as pd

#This function fetches the dataset. It takes a string (csv_path) which can be a url or a path to the dataset.
#It returns a pandas DataFrame of the data.
def get_dataset(csv_path:str) -> pd.DataFrame:

    return pd.read_csv(csv_path)

#This function takes a row in the dataframe as an argument and applies the current validation rules on it to return an array of strings of all the rules
#the row has failed on.
def validate(row) -> list[str]:

    reasons = []

    #no make has been provided
    if pd.isnull(row.make):
        reasons.append('hasMake')

    #no model has been provided
    if pd.isnull(row.model):
        reasons.append('hasModel')
    
    #no year has been provided
    if pd.isnull(row.year):
        reasons.append('hasYear')

    #no Condition of the vehicle has been provided.
    if pd.isnull(row.Condition):
        reasons.append('hasCondition')
    
    #Improper length of the Vin of the vehicle
    if len(row.vin) != 17:
        reasons.append('hasVin')

    #Vehicle year doesn't match the desired range (between 1990 and 2024 inclusive of both boundaries)
    if not (row.year >= 1990 and row.year <= 2024):
        reasons.append('validYear')

    return reasons

#This function takes a dataframe and the transformation instructions to apply to the dataframe, these transformation instructions are given in the form of a list
#of dictionaries, where every dictionary has the format of {'column': column_name, 'condition': {'old_val1': 'new_val1', 'old_val2': 'new_val2',...}}
#e.g look at TRANSFORMATION_INFORMATION global variable
def transform_columns(df:pd.DataFrame, transformation_info:list[dict[str, any]]) -> pd.DataFrame:

    #loop over all transformations and apply them one by one.
    for transformation in transformation_info:

        col_name = transformation['column']

        condition = transformation['condition']

        df[col_name].replace(condition,inplace=True)
    
    return df

#This function applies the validation rules as 'func' (see validate above as an example) to the provided dataframe 'df' and returns the true set that follow
#all the validation rules as a dataframe, and the rejected set that have failed at least ONE rule as a dataframe
def validate_dataset(df:pd.DataFrame, func: any) -> tuple[pd.DataFrame, pd.DataFrame]:

    #add a new column 'failed' for every row that is an array of strings of the validation rules the dataset has failed on. The function 'validate'
    #is applied to every row in the dataframe to determine whether the entry in the dataframe is valid or not.
    df['failed'] = df.apply(func, axis = 1)

    #get the indices of the rows that follow all validation rules (these are rows that would have 0 entries in the 'failed' column array)
    true_indices = df["failed"].str.len() == 0

    #obtain the rows using the true_indices, return all columns except the failed column since all entries will have a value of [] in the failed column
    true_set = df.loc[true_indices,df.columns != 'failed']

    #get the rejected rows by using the complement of the indices that follow the validation rules, return only the two required columns 'vin' and 'failed'
    rejected_set = df.loc[~true_indices,["vin","failed"]]

    return true_set, rejected_set
