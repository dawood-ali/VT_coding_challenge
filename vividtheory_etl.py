
from util import *

PATH_TO_DATASET = "https://heyauto.blob.core.windows.net/test/DataEngineer-Challenge.csv"

TRANSFORMATION_INFORMATION =  [
    {
        'column': 'Condition',
        'condition':  {'U':'Used', 'N': 'New'}
    }
]

#NOTE: refer to util.py for all the helper functions used.
if __name__ == "__main__":

    #Get the dataset as a pandas dataframe from the provided url/path to .csv file.
    input_vehicles = get_dataset(PATH_TO_DATASET)

    #Apply the desired transformations on the columns specified in the global variable TRANSFORMATION_INFORMATION
    transformed_df = transform_columns(input_vehicles,transformation_info=TRANSFORMATION_INFORMATION)

    #Apply the desired transformations on the columns specified in the global variable TRANSFORMATION_INFORMATION
    true_set, rejected_set = validate_dataset(transformed_df, validate)

    #Ensure that all rows are going to be displayed and that the failed array can show all validation rules that the row failed on.
    pd.options.display.max_colwidth = 200
    pd.set_option('display.max_rows', None)

    print("\nTrue Data:\n")

    print(true_set)

    print("\n----------------\n")

    print("\nRejected Data:\n")

    print(rejected_set)


    exit