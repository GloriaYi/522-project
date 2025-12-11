#-------
# eda.py
#------
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def compute_feature_correlations(df, feature_cols):
    """
    Computes a numeric correlation matrix for selected features.
    
    Parameters
    ----------
    df : pd.DataFrame
    feature_cols : list of str
    
    Returns
    -------
    pd.DataFrame
        Correlation matrix
    """
    corr_matrix = df[feature_cols].corr()
    corr_long = corr_matrix.reset_index().melt(id_vars="index")
    corr_long.columns = ["Feature 1", "Feature 2", "Correlation"]
    return corr_matrix, corr_long

def plot_correlation_heatmap(corr_matrix, save_path):
    """
    Plot and save a correlation heatmap given a correlation matrix.
    
    Parameters
    ----------
    corr_matrix : a correlation matrix
    save_path : str
        File path (including filename) where the heatmap image will be saved.

    Returns
    -------
    None
        This function is executed for its side effects: producing a file.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="viridis",
        square=True,
        cbar_kws={"label": "Correlation"},
    )
    plt.title("Correlation heatmap")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

