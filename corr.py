import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
def pearson_corr(a,b):
    mean_a = np.mean(a)
    mean_b = np.mean(b)
    std_a = np.std(a)
    std_b = np.std(b)
    covariance = np.sum((a - mean_a) * (b - mean_b)) / (len(a) - 1)
    correlation = covariance / (std_a * std_b)
    return correlation


def main():
    df = pd.read_csv("output_file.csv", nrows=1000)
    #print(df) 
    df = pd.get_dummies(df, columns=["business_unit_group_name", "company_region_name_level_1","product_line_code", "product_line_name"])
    # Calculate the Pearson's correlation between each feature and the quality
    quality = df["sales_amount"]
    feature_correlations = []
    for column_name in df.columns:
        if column_name != "sales_amount":
            feature = df[column_name]
            correlation = pearson_corr(feature, quality)
            feature_correlations.append((column_name, abs(correlation)))

    # Sort the features based on their absolute correlation values  
    feature_correlations.sort(key=lambda x: x[1], reverse=True)

    # Print the features and their absolute correlation values
    #for feature, correlation in feature_correlations:
    #    print(feature, correlation)

    # Calculate the Pearson's correlation between each column
    
    correlations = {}
    for column_name1 in df.columns:
        for column_name2 in df.columns:
            if column_name1 != column_name2:
                column1 = df[column_name1]
                column2 = df[column_name2]
                correlation = pearson_corr(column1, column2)
                correlations[(column_name1, column_name2)] = correlation
    
    # Plot the correlations as a heatmap
    #plt.figure(figsize=(10, 10))
    #sns.heatmap(df.corr(), cmap="RdBu_r", annot=True)
    #plt.show()

    # List the features that have a correlation >= 0.7
    #strong_correlations = [(column1, column2) for (column1, column2), correlation in correlations.items() if abs(correlation) >= 0.7]
    #print("Features with strong correlations (>= 0.7):")
    #for column1, column2 in strong_correlations:
        #print("{} and {}".format(column1, column2))


main()