import pandas as pd

df2 = pd.read_csv(r'C:\Users\AkashR\Desktop\DataReconciliationTest\data\input\app.csv', dtype=object)
df1 = pd.read_csv(r'C:\Users\AkashR\Desktop\DataReconciliationTest\data\input\archer.csv', dtype=object)
primary_keys = ["primary_key_column","name"]
print(df1)
print(df2)
def keep_primary_key_matching_records(df1, df2, primary_keys):
    archer_df1 = df1[df1[primary_keys].isin(df2[primary_keys])]
    app_df = df2[df2[primary_keys].isin(df1[primary_keys])]
    print(archer_df1)
    print(app_df)
keep_primary_key_matching_records(df1,df2,primary_keys)

