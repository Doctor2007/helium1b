import pandas as pd
import json

# Load country categories from JSON
with open('country_categories.json', 'r', encoding='utf-8') as f:
    country_categories = json.load(f)

# Load trade data
data = pd.read_csv('data/raw/micro_data_trade_2022.csv')


def get_region(country):
    """Map a country to its region category"""
    for region, countries in country_categories.items():
        if country in countries:
            return region
    return "Uncategorised"


def waste_by_category(hs4):
    """Process waste import data by HS4 category"""
    data_product = data[data['HS4'] == hs4].copy()

    data_product_import = data_product[data_product['Tradeflow'] == 'Import'].copy()
    data_product_import['Tradevalue_USD'] = data_product_import['Tradevalue_USD'].astype(int)
    data_cleaned = data_product_import[['Partner_Country', 'Tradevalue_USD']].copy()

    grouped_data = data_cleaned.groupby('Partner_Country', as_index=False)['Tradevalue_USD'].sum()

    grouped_data['Region'] = grouped_data['Partner_Country'].apply(get_region)
    grouped_data['HS4'] = hs4

    print(f'Done processing HS4: {hs4}')
    print(grouped_data.head())  # Display first few rows for verification

    return grouped_data


# List of waste-related HS4 codes
def hs4_codes():
    hs_codes = [8548, 7404, 7602, 3915, 6309]
    return hs_codes

hs_codes = hs4_codes()

dfs = [waste_by_category(hs4) for hs4 in hs_codes]

final_df = pd.concat(dfs, ignore_index=True)
# Filter out low-value imports (e.g., < $1000)
final_df = final_df[final_df['Tradevalue_USD'] > 1000]

data_region = final_df.groupby('Region', as_index=False)['Tradevalue_USD'].sum()

unknown_countries = final_df[final_df['Region'] == 'Uncategorised']

print("\nRegions Summary:")
print(data_region)

print("\nUnknown Countries:")
print(unknown_countries)

# Save output if needed
final_df.to_csv("data/processed/waste_imports_by_category.csv", index=False)
data_region.to_csv("data/processed/waste_imports_by_region.csv", index=False)
