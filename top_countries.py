import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_waste_import_data(filepath='data/processed/waste_imports_by_category.csv'):
    """
    Load waste import data from CSV.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pandas.DataFrame
    """
    return pd.read_csv(filepath)

def get_top_countries_by_hs4(data=None, n=5):
    """
    Get top n countries by trade value for each HS4 code.
    
    Parameters:
    -----------
    data : pandas.DataFrame, optional
        DataFrame with waste import data
    n : int, optional
        Number of top countries to return for each HS4 code
        
    Returns:
    --------
    dict: Dictionary with HS4 codes as keys and DataFrames of top countries as values
    """    
    if data is None:
        data = load_waste_import_data()
    
    # Get unique HS4 codes
    hs4_codes = data['HS4'].unique()
    
    # Create dictionary to store results
    top_countries = {}
    
    # For each HS4 code, find the top n countries
    for code in hs4_codes:
        # Filter data for the current HS4 code
        code_data = data[data['HS4'] == code]
        
        # Group by country and sum trade values
        country_totals = code_data.groupby('Partner_Country')['Tradevalue_USD'].sum().reset_index()
        
        # Sort by trade value in descending order and take top n
        top_n = country_totals.sort_values('Tradevalue_USD', ascending=False).head(n)
        
        # Store in dictionary
        top_countries[code] = top_n
    
    return top_countries

def display_top_countries(top_countries_dict, hs4_descriptions=None):
    """
    Display the top countries for each HS4 code in a readable format.
    
    Parameters:
    -----------
    top_countries_dict : dict
        Dictionary with HS4 codes as keys and DataFrames of top countries as values
    hs4_descriptions : dict, optional
        Dictionary mapping HS4 codes to their descriptions
    """
    for code, countries_df in top_countries_dict.items():
        if hs4_descriptions is not None and code in hs4_descriptions:
            print(f"\nHS4 Code {code} - {hs4_descriptions[code]}")
        else:
            print(f"\nHS4 Code {code}")
        
        print("Top countries by trade value:")
        for i, (_, row) in enumerate(countries_df.iterrows(), 1):
            country = row['Partner_Country']
            value = row['Tradevalue_USD']
            print(f"{i}. {country}: ${value:,.0f}")
        print("-" * 40)

def get_hs4_descriptions():
    """
    Return a dictionary of HS4 code descriptions.
    
    Returns:
    --------
    dict: Dictionary with HS4 codes as keys and descriptions as values
    """
    return {
        6309: 'Textile products', 
        8548: 'Electrical and electronic waste and scrap', 
        7404: 'Copper waste and scrap',
        7602: 'Aluminum waste and scrap',
        3915: 'Waste, parings, and scrap of plastics'
    }

def plot_top_countries(top_countries_dict, hs4_code, figsize=(10, 6), hs4_descriptions=None):
    """
    Create a bar chart of top countries for a specific HS4 code.
    
    Parameters:
    -----------
    top_countries_dict : dict
        Dictionary with HS4 codes as keys and DataFrames of top countries as values
    hs4_code : int
        The HS4 code to plot
    figsize : tuple, optional
        Figure size as (width, height) in inches
    hs4_descriptions : dict, optional
        Dictionary mapping HS4 codes to their descriptions
        
    Returns:
    --------
    fig, ax : matplotlib figure and axes objects
    """
    
    if hs4_code not in top_countries_dict:
        print(f"HS4 code {hs4_code} not found in data")
        return None, None
    
    df = top_countries_dict[hs4_code]
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot horizontal bars
    ax.barh(df['Partner_Country'], df['Tradevalue_USD'])
    
    # Use description if available
    title = f'Top Countries by Trade Value - HS4 Code {hs4_code}'
    if hs4_descriptions and hs4_code in hs4_descriptions:
        title += f' ({hs4_descriptions[hs4_code]})'
    
    # Formatting
    ax.set_xlabel('Trade Value (USD)')
    ax.set_title(title)
    ax.get_xaxis().set_ticks([])
    
    # Add value labels
    for i, v in enumerate(df['Tradevalue_USD']):
        ax.text(v + 0.01*max(df['Tradevalue_USD']), i, f"${v:,.0f}", va='center')
    
    plt.tight_layout()
    return fig, ax

# This code only runs when the script is executed directly
if __name__ == "__main__":
    # Load data
    waste_data = load_waste_import_data()
    
    # Get top 5 countries for each HS4 code
    top_countries = get_top_countries_by_hs4(waste_data)
    
    # Get HS4 descriptions
    hs4_descriptions = get_hs4_descriptions()
    
    # Display the results
    display_top_countries(top_countries, hs4_descriptions)