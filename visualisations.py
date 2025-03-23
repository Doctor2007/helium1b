import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    """Load and prepare the waste import data."""
    data_region = pd.read_csv('data/processed/waste_imports_by_region.csv')
    data_countries = pd.read_csv('data/processed/waste_imports_by_category.csv')
    
    data_region = data_region[data_region['Region'] != 'Uncategorised']
    
    merged_data = data_countries.merge(data_region, on='Region', suffixes=('_HS4', '_Region'))
    grouped_data = merged_data.groupby(['Region', 'HS4'])['Tradevalue_USD_HS4'].sum().unstack(fill_value=0)
    
    return grouped_data


def plot_waste_imports(grouped_percent=None, figsize=(12, 7), save_path=None):
    """
    Create a bar chart of waste imports by HS4 category in each region.
    
    Parameters:
    -----------
    grouped_percent : pandas.DataFrame, optional
        DataFrame with regions as index and HS4 codes as columns.
        If None, data will be loaded using load_data().
    figsize : tuple, optional
        Figure size as (width, height) in inches.
    save_path : str, optional
        Path to save the figure. If None, figure is not saved.
        
    Returns:
    --------
    fig, ax : matplotlib figure and axes objects
    """
    if grouped_percent is None:
        grouped_percent = load_data()
    
    # Plot settings
    regions = grouped_percent.index
    hs4_codes = grouped_percent.columns
    hs4_descriptions = {
        # 6309  Worn clothing and other worn articles
        # 7404	Copper waste and scrap
        # 3915	Waste, parings and scrap, of plastics
        # 7602	Aluminium waste and scrap
        # 8548	Electrical parts of machinery or apparatus, nes
        6309: 'Textile products', 
        8548: 'Electrical and electronic waste and scrap', 
        7404: 'Copper waste and scrap',
        7602: 'Aluminum waste and scrap',
        3915: 'Waste, parings, and scrap of plastics'
    }
    x = np.arange(len(regions))
    width = 0.15  # Width of each bar segment
    colors = plt.cm.viridis(np.linspace(0, 1, len(hs4_codes)))

    # Plot
    fig, ax = plt.subplots(figsize=figsize)

    for i, hs4 in enumerate(hs4_codes):
        ax.bar(x + i * width, grouped_percent[hs4], width, label=f'{hs4_descriptions.get(hs4, hs4)}')

    ax.set_xlabel('Region', fontsize=14, fontweight='bold')
    ax.set_ylabel('Trade Value (10 Million USD - 1)', fontsize=14, fontweight='bold')
    ax.set_title('Waste Imports by HS4 Category in Each Region', fontsize=16, fontweight='bold')
    ax.set_xticks(x + width * (len(hs4_codes) / 2))
    ax.set_xticklabels(regions, rotation=45, fontsize=12)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.legend(title="HS4 Codes", bbox_to_anchor=(1.05, 1), loc='best', fontsize=12)

    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

if __name__ == "__main__":
    data = load_data()
    fig, ax = plot_waste_imports(data)
    plt.show()