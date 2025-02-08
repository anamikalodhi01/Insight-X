import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/msme_dataset.csv")

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values with mean
df.fillna(df.mean(), inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_msme_dataset.csv", index=False)

# Plot MSME loan trends
plt.figure(figsize=(10,5))
sns.lineplot(x=df['year'], y=df['loan_approval_rate'])
plt.title("MSME Loan Approval Rate Over the Years")
plt.xlabel("Year")
plt.ylabel("Loan Approval Rate")
plt.show()
