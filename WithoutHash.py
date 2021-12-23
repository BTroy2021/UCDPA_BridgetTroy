import pandas as pd

from sqlalchemy import create_engine

import numpy as np

import matplotlib.pyplot as plt

fdi_csv = pd.read_csv(r'C:\Users\Bridg\Desktop\FDI.csv', encoding='utf-8')

migration = pd.read_csv(r'C:\Users\Bridg\Desktop\CIDA\pythonProjectFDI\API_Edit.csv')

engine = create_engine('sqlite:///:memory:')

migration.to_sql('data_table', engine)

migration = migration.loc[:, ['Country Name', 'Country Code', '1962', '1972', '1977', '1982', '1987', '1992', '1997', '2002', '2007', '2012', '2017']]

fdi_migration = fdi_csv.merge(migration, on= ['Country Name', 'Country Code'], how='left')

print(fdi_migration.head())
print(migration.head())

print(fdi_migration)


