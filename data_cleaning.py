import pandas as pd

data = pd.read_csv('data/raw/micro_data_trade_2022.csv')

def create_waste_csv_by_category(hs4):
    data_textile = data[data['HS4'] == hs4].copy()

    data_textile_import = data_textile[data_textile['Tradeflow'] == 'Import'].copy()
    data_textile_import['Tradevalue_USD'] = data_textile_import['Tradevalue_USD'].astype(int).copy()

    data_cleaned = data_textile_import.drop(columns=[
        "Year", "Month", "Tradeflow", "HS2", "Description_HS2", "HS4", "Description_HS4", "HS10", "Description_HS10", "Tradevalue_Cedis"
    ])
    print(data_cleaned.head())
    # grouped_data = data_cleaned.groupby('Partner_Country', as_index=True)['Tradevalue_USD'].sum()

    # grouped_data.to_csv(f'data/raw/import_by_countries-{hs4}.csv')
    # print('Done')

create_waste_csv_by_category(6309)
create_waste_csv_by_category(8548)
create_waste_csv_by_category(7404)
create_waste_csv_by_category(7602)
create_waste_csv_by_category(3915)