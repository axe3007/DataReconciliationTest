from transform import *
from config.config import TRANSFORMATIONS

def apply_transformations(df1, df2):
    for transformation in TRANSFORMATIONS:
        for operation, args in transformation.items():
            if operation == 'KEEP_PRIMARY_KEY_MATCHING_RECORDS':
                primary_keys = args['primary_keys']
                df1 = keep_primary_key_matching_records(df1, df2, primary_keys)
                df2 = keep_primary_key_matching_records(df2, df1, primary_keys)

            elif operation == 'ADD_TRAILING_SPACE_TO_PRIMARY_KEY_RECORDS':
                primary_keys = args['primary_keys']
                df1 = add_trailing_space_to_primary_key_records(df1, primary_keys)
                df2 = add_trailing_space_to_primary_key_records(df2, primary_keys)

            elif operation == 'REMOVE_LEADING_TRAILING_SPACES':
                df1 = remove_leading_trailing_spaces(df1)
                df2 = remove_leading_trailing_spaces(df2)

            elif operation == 'REMOVE_UNICODE_CHARACTERS':
                df1 = remove_unicode_characters(df1)
                df2 = remove_unicode_characters(df2)
            elif operation == 'FORMAT_DATE':
                for format in args:
                    from_format = format['from_format']
                    to_format = format['to_format']
                    df1 = format_date(df1, from_format, to_format)
                    df2 = format_date(df2, from_format, to_format)

            elif operation == 'REMOVE_LEADING_TRAILING_DELIMITERS':
                delimiters = args['delimiters']
                df1 = remove_leading_trailing_delimiters(df1, delimiters)
                df2 = remove_leading_trailing_delimiters(df2, delimiters)

