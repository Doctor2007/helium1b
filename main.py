import pandas as pd
import matplotlib.pyplot as plt

country_categories = {
    "European_Union": [
        "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
        "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
        "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
        "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"
    ],
    
    "West_Not_EU": [
        "United States of America", "United Kingdom", "Canada", "Australia", "New Zealand", "Norway", "Switzerland", "Iceland"
    ],
    
    "African": [
        "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", 
        "Central African Republic", "Chad", "Comoros", "Democratic Republic of the Congo", "Djibouti", 
        "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", 
        "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", 
        "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", 
        "Nigeria", "Republic of the Congo", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", 
        "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", 
        "Uganda", "Zambia", "Zimbabwe"
    ],
    
    "Others": [
        "Argentina", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Belarus", "Bhutan", "Bolivia", 
        "Bosnia and Herzegovina", "Brazil", "Brunei", "Cambodia", "Chile", "China", "Colombia", "Costa Rica", 
        "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Fiji", "Georgia", "Guatemala", "Honduras", 
        "Iceland", "India", "Indonesia", "Iran", "Iraq", "Israel", "Jamaica", "Japan", "Jordan", "Kazakhstan", 
        "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mexico", "Moldova", "Mongolia", 
        "Montenegro", "Myanmar", "Nepal", "Nicaragua", "North Korea", "North Macedonia", "Oman", "Pakistan", 
        "Panama", "Paraguay", "Peru", "Philippines", "Qatar", "Russia", "Saudi Arabia", "Serbia", "Singapore", 
        "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", 
        "Turkmenistan", "Ukraine", "United Arab Emirates", "Uruguay", "Uzbekistan", "Venezuela", "Viet Nam", "Yemen"
    ]
}



data = pd.read_csv('data/micro_data_trade_2022.csv')


data_textile = data[data['HS4'] == 6309]

data_textile_import = data_textile[data_textile['Tradeflow'] == 'Import']
data_textile_export = data_textile[data_textile['Tradeflow'] == 'Import']

# data_textile_import.to_csv('data/textile_trade_import_2022.csv', index=False)
# data_textile_export.to_csv('data/textile_trade_export_2022.csv', index=False)

data_textile_import_eu = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['European_Union'])]
data_textile_import_west = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['West_Not_EU'])]
data_textile_import_africa = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['African'])]
data_textile_import_others = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['Others'])]


import_list = [data_textile_import_eu, data_textile_import_west, data_textile_import_africa, data_textile_import_others]
import_list_name = ['EU', 'West', 'Africa', 'Others']

def region_by_sum():
    summary_data = []
    ind = 0
    for i in import_list:
        sum_value = i['Tradevalue_USD'].sum()
        summary_data.append({'Region': import_list_name[ind], 'Tradevalue_USD': int(sum_value)})
        ind += 1

    summary_df = pd.DataFrame(summary_data)

    plt.bar(summary_df['Region'], summary_df['Tradevalue_USD'], color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.xlabel('Region')
    plt.ylabel('Total Trade Value (USD)')
    plt.title('Total Trade Value by Region')
    plt.show()

def region_leaders(region):
    if region == 'World':
        data = data_textile_import
    else:
        i = import_list_name.index(region)
        data = import_list[i]
    
    grouped_df = data.groupby('Partner_Country', as_index=False)['Tradevalue_USD'].sum()
    grouped_df['Tradevalue_USD'] = round(grouped_df['Tradevalue_USD'])
    grouped_df = grouped_df.sort_values(by='Tradevalue_USD', ascending=False)
    grouped_head = grouped_df.head(5)

    plt.bar(grouped_head['Partner_Country'], grouped_head['Tradevalue_USD'], color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.xlabel('Region')
    plt.ylabel('Total Trade Value (USD)')
    plt.title('Total Trade Value by Region')
    plt.show()

# region_leaders('World')
# region_leaders(region)
region_by_sum()