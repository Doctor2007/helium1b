import pandas as pd
import matplotlib.pyplot as plt
import json

with open('country_categories.json', 'r', encoding='utf-8') as f:
    country_categories = json.load(f)

data_countries = pd.read_csv('data/processed/import_by_countries.csv')
data_region = pd.read_csv('data/processed/import_by_region.csv')
data_region_important = data_region[data_region['Region'] != 'Uncategorised']

def graph_by_data(data, x, y):
    plt.figure(figsize=(10,6))
    plt.bar(data[x], data[y], color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.xlabel(x)
    plt.ylabel(f'Total {y} (USD)')
    plt.title(f'Total {y} by {x}')
    plt.show()

# data, x, y
graph_by_data(data_region_important, 'Region', 'Tradevalue_USD')





# def region_by_sum():
#     summary_data = []
#     ind = 0
#     for i in import_list:
#         sum_value = i['Tradevalue_USD'].sum()
#         summary_data.append({'Region': import_list_name[ind], 'Tradevalue_USD': int(sum_value)})
#         ind += 1

#     summary_df = pd.DataFrame(summary_data).set_index(None)
#     summary_df.to_csv(f'data/processed/1.csv')

#     plt.bar(summary_df['Region'], summary_df['Tradevalue_USD'], color=['blue', 'orange', 'green', 'red', 'purple'])
#     plt.xlabel('Region')
#     plt.ylabel('Total Trade Value (USD)')
#     plt.title('Total Trade Value by Region')
#     plt.show()

# def region_leaders(region):
#     if region == 'World':
#         data = data_textile_import
#     else:
#         i = import_list_name.index(region)
#         data = import_list[i]
    
#     grouped_df = data.groupby('Partner_Country', as_index=False)['Tradevalue_USD'].sum()
#     grouped_df['Tradevalue_USD'] = round(grouped_df['Tradevalue_USD'])
#     grouped_df = grouped_df.sort_values(by='Tradevalue_USD', ascending=False)
#     grouped_head = grouped_df.head(5)

#     plt.bar(grouped_head['Partner_Country'], grouped_head['Tradevalue_USD'], color=['blue', 'orange', 'green', 'red', 'purple'])
#     plt.xlabel('Region')
#     plt.ylabel('Total Trade Value (USD)')
#     plt.title('Total Trade Value by Region')
#     plt.show()




# if __name__ == '__main__':
    # region_leaders('World')
    # region_leaders('West')
    # region_by_sum()
    # print(data_textile_export['HS10'].unique())