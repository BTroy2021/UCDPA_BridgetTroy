import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sqlalchemy import create_engine

fdi_csv = pd.read_csv(r'C:\Users\Bridg\Desktop\FDI.csv', encoding='utf-8')

US_only = fdi_csv.iloc[251, np.r_[16:62]]

US_only1 = US_only.iloc[::5]

US_only1int = US_only1.astype(float)

FDI_Final = pd.DataFrame(US_only1int)

FDI_Final.columns = ['FDI %']

FDI_Final.index.name = 'Year'

print(FDI_Final)

migration = pd.read_csv(r'C:\Users\Bridg\Desktop\CIDA\pythonProjectFDI\API_Edit.csv')

engine = create_engine('sqlite:///:memory:')

migration.to_sql('data_table', engine)

migration.dropna(axis=1, how='all', inplace=True)

USMigration_narrow = migration.iloc[251, np.r_[6:16]]

USMigration_int = USMigration_narrow.astype(float)

USMig_Final = (USMigration_int / 1000000)

USMig_Final.columns = ['Migration in Mill']

USMig_Final.index.name = 'Year'

print(USMig_Final)

FDI_Migration = US_only1int.to_frame().merge(USMig_Final, on='Year', how='left', suffixes=('_FDI', '_mig'))
print(FDI_Migration)

FDI_Migration.rename(columns={'251_FDI': 'FDI inflows as a % of Total GDP', '251_mig': 'Migration in Millions'},
                     inplace=True)

print(FDI_Migration)
BarUS = FDI_Migration.plot.bar(y=['FDI inflows as a % of Total GDP', 'Migration in Millions'], rot=45)
plt.xlabel('Year')
plt.ylabel('Net Migration x 1 Million')
plt. title('United States Net Migration and FDI Inflows Over Time')

plt.show()

ax = FDI_Migration[['FDI inflows as a % of Total GDP', 'Migration in Millions']].plot(
    linestyle='-', marker='o')

plt.show()

