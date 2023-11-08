import pandas as pd

# Function to convert the input data into the right format and preprocess it
def preprocess_input(json_data, transformer):
    # Convert json_data to a DataFrame
    input_df = pd.DataFrame([json_data])

    # Manually add missing columns with NaNs where the transformer expects them
    for col in transformer.named_transformers_['cat'].get_feature_names_out():
        if col.split('_')[0] not in input_df.columns:
            input_df[col.split('_')[0]] = None

    # Fill missing values and ensure correct data type
    input_df['Description'].fillna('', inplace=True)
    if 'VAT CODE' in input_df columns:
        input_df.drop('VAT CODE', axis=1, inplace=True)

    # Check if 'Month' column exists and handle different formats
    if 'Month' in input_df.columns:
        # Check if the month data is already in MM format (numeric)
        if input_df['Month'].dtype == 'int64' or input_df['Month'].str.isnumeric().all():
            # Ensure it's in the correct numeric range for months
            input_df['Month'] = pd.to_numeric(input_df['Month']).clip(1, 12)
        else:
            # Convert Month to numerical format as it's expected in the original training
            month_mapping = {v: i for i, v in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 
                                                         'July', 'August', 'September', 'October', 'November', 'December'], start=1)}
            input_df['Month'] = input_df['Month'].map(month_mapping)

    # Use the transformer to preprocess the input data
    X = transformer.transform(input_df)

    return X
