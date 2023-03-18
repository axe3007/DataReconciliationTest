import json

with open(r'C:\Users\AkashR\Desktop\DataReconciliationTest\config\transformations.json', 'r') as f:
    TRANSFORMATIONS = json.load(f)['transformations']

ARCHER_FILE_PATH = r'C:\Users\AkashR\Desktop\DataReconciliationTest\data\input\archer.csv'
APP_FILE_PATH = r'C:\Users\AkashR\Desktop\DataReconciliationTest\data\input\app.csv'
OUTPUT_FILE_PATH = r'C:\Users\AkashR\Desktop\DataReconciliationTest\data\output\report.csv'

