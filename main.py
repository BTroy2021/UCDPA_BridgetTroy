import pandas as pd

from sqlalchemy import create_engine

fdi_csv = pd.read_csv(r'C:\Users\Bridg\Desktop\FDI.csv', encoding='utf-8')

print(fdi_csv.head())
print(fdi_csv.shape)

migration = pd.read_csv(r'C:\Users\Bridg\Desktop\CIDA\pythonProjectFDI\API_Edit.csv')

engine = create_engine('sqlite:///:memory:')

migration.to_sql('data_table', engine)

print(migration.head())

fdi_migration = fdi_csv.merge(migration, on='Country Name', how="left")

print(fdi_migration.head())

print(fdi_migration)
