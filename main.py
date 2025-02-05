import pandas as pd


country_categories = {
    "European_Union": [
        "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
        "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
        "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
        "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"
    ],
    
    "UK": ["United Kingdom"],
    
    "West_Not_EU": [
        "United States", "Canada", "Australia", "New Zealand", "Norway", "Switzerland", "Iceland"
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


data_textile = data[data['HS2'] == 63]

data_textile_import = data_textile[data_textile['Tradeflow'] == 'Import']
data_textile_export = data_textile[data_textile['Tradeflow'] == 'Import']

data_textile.drop(columns=['Tradevalue_Cedis'], inplace=True)

data_textile_import.to_csv('data/textile_trade_import_2022.csv', index=False)
data_textile_export.to_csv('data/textile_trade_export_2022.csv', index=False)

data_textile_import_eu = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['European_Union'])]
data_textile_import_uk = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['UK'])]
data_textile_import_west = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['West_Not_EU'])]
data_textile_import_africa = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['African'])]
data_textile_import_others = data_textile_import[data_textile_import['Partner_Country'].isin(country_categories['Others'])]
data_textile_import_eu.to_csv('data/textile_trade_import_eu_2022.csv', index=False)
data_textile_import_uk.to_csv('data/textile_trade_import_uk_2022.csv', index=False)
data_textile_import_west.to_csv('data/textile_trade_import_west_2022.csv', index=False)
data_textile_import_africa.to_csv('data/textile_trade_import_africa_2022.csv', index=False)
data_textile_import_others.to_csv('data/textile_trade_import_others_2022.csv', index=False)


import_list = [data_textile_import_eu, data_textile_import_uk, data_textile_import_west, data_textile_import_africa, data_textile_import_others]
import_list_name = ['EU', 'UK', 'West', 'Africa', 'Others']

ind = 0
for i in import_list:
    sum_value = i['Tradevalue_USD'].sum()
    print(import_list_name[ind], 'USD')
    print(int(sum_value))
    ind += 1