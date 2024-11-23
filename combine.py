import pandas as pd

# Load the datasets
data = pd.read_csv('data.csv')
import pandas as pd
labels = pd.read_excel('lable.xlsx')


# Combine datasets
# If rows align perfectly between the two files
combined = pd.concat([data, labels], axis=1)

# Save the merged file
combined.to_csv('combined_dataset.csv', index=False)

print("Combined dataset saved as 'combined_dataset.csv'")
