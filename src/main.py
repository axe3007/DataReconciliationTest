import pandas as pd
from config.config import ARCHER_FILE_PATH, APP_FILE_PATH, OUTPUT_FILE_PATH
from apply_transformations import apply_transformations

df1 = pd.read_csv(ARCHER_FILE_PATH, dtype=object)
df2 = pd.read_csv(APP_FILE_PATH, dtype=object)
print(df1)
print(df2)
if __name__ == '__main__':
    apply_transformations(df1, df2)
    comparison_result = df1.compare(df2, result_names=("archer", "app"))
    comparison_result.to_csv(OUTPUT_FILE_PATH, index=False)
    print(f"Report saved to {OUTPUT_FILE_PATH}")


