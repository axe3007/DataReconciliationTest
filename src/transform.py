import pandas as pd


def keep_primary_key_matching_records(df1, df2, primary_keys):
    df1 = pd.merge(df1, df2, on=primary_keys, how='inner', suffixes=('_left', '_right'))
    print(df1)


def remove_leading_trailing_spaces(df1, df2):
    """
    This function removes any leading or trailing spaces from all columns in both dataframes.
    """
    for col in df1.columns:
        if df1[col].dtype == 'object':
            df1[col] = df1[col].str.strip()
        if df2[col].dtype == 'object':
            df2[col] = df2[col].str.strip()
    return df1, df2


def remove_unicode_characters(df1, df2):
    """
    This function removes any Unicode characters from all columns in both dataframes.
    """
    for col in df1.columns:
        if df1[col].dtype == 'object':
            df1[col] = df1[col].str.encode('ascii', 'ignore').str.decode('ascii')
        if df2[col].dtype == 'object':
            df2[col] = df2[col].str.encode('ascii', 'ignore').str.decode('ascii')
    return df1, df2

#to do add date format


def format_date(df1,df2, format):
    """
    A function that automatically detects the date column and converts the dates to a specific date format.

    Parameters:
    df (pandas.DataFrame): The input dataframe.
    format (str): The format to which the dates will be converted.

    Returns:
    pandas.DataFrame: The converted dataframe.
    """
    for column in df1.columns:
        if pd.api.types.is_datetime64_any_dtype(df1[column]):
            df1[column] = pd.to_datetime(df1[column]).dt.strftime(format)
        if pd.api.types.is_datetime64_any_dtype(df2[column]):
            df2[column] = pd.to_datetime(df2[column]).dt.strftime(format)
    return df1, df2


#add delimeter filter

def remove_leading_trailing_delimiters(df1,df2, delimiters):
    """
    Remove a given list of delimiters from a DataFrame.
    """
    for delimiter in delimiters:
        dataframe = df1.apply(lambda x: x.str.replace(delimiter, ''))
    for delimiter in delimiters:
        dataframe = df2.apply(lambda x: x.str.replace(delimiter, ''))
    return df1, df2


def add_trailing_space_to_primary_key_records(df1, df2, primary_keys):
    """
    This function adds a trailing space to the values in the specified primary key columns of both dataframes.
    """
    for col in primary_keys:
        df1[col] = df1[col].astype(str).str.rstrip() + ' '
        df2[col] = df2[col].astype(str).str.rstrip() + ' '
    return df1, df2



