import pandas as pd
import json

with open('country_categories.json', 'r', encoding='utf-8') as f:
    country_categories = json.load(f)

data_full = pd.read_csv('data/processed/import_by_countries.csv')

# I'll remove all the unnecessary countries.
# If Ghana imports less than 1000$ worth of used clothes it's almost nothing
data = data_full[data_full['Tradevalue_USD'] > 1000].copy()

def get_region(country):
    """Map a country to its region category"""
    for region, countries in country_categories.items():
        if country in countries:
            return region
    return "Uncategorised"

data['Region'] = data['Partner_Country'].apply(get_region)

data_region = data.groupby('Region', as_index=True)['Tradevalue_USD'].sum()

# :) Just so you know, there's in a Unknown country who exported used_clothes to Ghana
# b = data[data['Region'] == 'Uncategorised']
# print(b)

if __name__ == '__main__':
    print(data)
    data_region.to_csv('data/processed/import_by_region.csv')
else:
    # When imported as a module, make data available
    pass  # data is already defined in the global scope