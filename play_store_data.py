# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')


# Correct way to load your CSV file:
file_path = ("/Users/siddheshkalgaonkar/Desktop/learnbay_Data_Analyst/Madhuri/google_playstore_dataset/googleplaystore.csv")  # Or use a raw string: r"path"
try:
    data = pd.read_csv(file_path)
    print(data.head())  # Print the first few rows to verify it loaded correctly
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    data = None  # Ensure data is defined
except Exception as e: # Catch other potential errors (e.g., bad CSV format)
    print(f"An error occurred while reading the CSV: {e}")
    data = None


if data is not None:
    print(data.describe())

#last 5 rows
print(data.tail())

#how many rows and cols
print(" rows and cols :",data.shape)

###### displat boxplot
data.boxplot()
plt.show()

data.hist()
plt.show()



##################### Data Cleaning part ###############################
print(data.info())

###checking the null  value
print("********* checking  null  value *********")
print(data.isnull().sum())

print("***************************************")
print("******** checking how many outliers are there *********")
filtered_data = data[data['Rating'] > 5]
print(filtered_data)

data.drop([10472], inplace=True)
print(data[10470:10475])

data.boxplot()
plt.show()

data.hist()
plt.show()


print("****** remove columns 90% empty *********")
Threshold = len(data) * 0.1
print(Threshold)
data.dropna( thresh=Threshold, axis=1, inplace=True)
print(data.isnull().sum())

print("******** Data Manipulation *******")

def input_median(series):
    return series.fillna(series.median)
data.Rating = data['Rating'].transform(input_median)
print(data.isnull().sum())

print("************* Data Visualization ****************")
def clean_and_convert(series):
    """Cleans and converts a pandas Series to numeric."""
    series = series.astype(str).str.replace(r'[^\d.]+', '', regex=True) #remove all non numeric characters.
    return pd.to_numeric(series, errors='coerce')

# Clean and convert the 'Installs' and 'Reviews' columns
data['Installs'] = clean_and_convert(data['Installs'])
data['Price'] = clean_and_convert(data['Price'])
data['Reviews'] = clean_and_convert(data['Reviews'])

grp = data.groupby('Category')
x = grp['Installs'].agg(np.mean)
y = grp['Price'].agg(np.sum)
z = grp['Reviews'].agg(np.mean)

print(x)
print(y)
print(z)

plt.figure(figsize=(16,5))
plt.plot(x , 'ro')
plt.xticks(rotation=90)
plt.title('Category vs Installs')
plt.xlabel('Category ------------------>')
plt.ylabel('Installs ------------------>')
plt.show()




plt.figure(figsize=(16,5))
plt.plot(y, 'r--',color='blue')
plt.xticks(rotation=90)
plt.title('Category vs Price')
plt.xlabel('Category ------------------>')
plt.ylabel('Price ------------------>')
plt.show()


plt.figure(figsize=(16,5))
plt.plot(z, 'g^',color='g')
plt.xticks(rotation=90)
plt.title('Category vs Price')
plt.xlabel('Category ------------------>')
plt.ylabel('Price ------------------>')
plt.show()
















