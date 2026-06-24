import pandas as pd
import re

try:
    df = pd.read_csv('all_books.csv')
except FileNotFoundError:
    pass

def clean_price(val):
    match = re.search(r'[\d\.]+', str(val))
    return float(match.group()) if match else None

df['Price'] = df['Price'].apply(clean_price)
df = df.dropna(subset=['Price'])

min_price = df.loc[df['Price'].idxmin()]
print("Cheapest book:", min_price['Price'])

median_price = df['Price'].median()
print("Median price:", median_price)

max_price = df.loc[df['Price'].idxmax()]
print("Most expensive book:", max_price['Price'])

df.to_csv('cleaned_books.csv', index=False)