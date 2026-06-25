import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load data once
df = pd.read_csv("dataset_clean.csv")

# 2. Summary Statistics
print(f"Total samples: {len(df)}")

# Using a list to describe specific columns all at once
cols_of_interest = ["gain", "ugf", "pm"]
print("\nKey Feature Statistics:")
print(df[cols_of_interest].describe())

# 3. Visualizing Distributions
df.hist(figsize=(12, 10), bins=20)
plt.tight_layout() # Prevents label overlapping
plt.show()

# 4. Correlation Analysis
# Note: df.corr() only works on numeric columns; 
# numeric_only=True prevents errors if you have text columns.
corr = df.corr(numeric_only=True)

print("\nCorrelation with Target Metrics:")
print(corr[cols_of_interest])

# 5. Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
