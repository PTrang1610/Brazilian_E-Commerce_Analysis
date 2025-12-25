import pandas as pd

def load_all_data():
   
    print(f"--- Loading data from: {path} ---")
    
    # Reading CSV files
    customers = pd.read_csv(path + 'customers.csv')
    orders = pd.read_csv(path + 'orders.csv')
    order_items = pd.read_csv(path + 'order_items.csv')
    products = pd.read_csv(path + 'products.csv')
    payments = pd.read_csv(path + 'order_payments.csv')
    
    return customers, orders, order_items, products, payments

def explore(df, name):
    print(f"\n==================== DATASET: {name.upper()} ====================")
    
    # 1. Preview the first 5 rows
    print(" First 5 rows (head):")
    print(df.head())
    
    # 2. Check data types and non-null counts
    print(" Data structure and types (info):")
    df.info() 
    
    # 3. Statistical summary
    print(" Statistical summary (describe):")
    print(df.describe())
    
    # 4. Check for missing values
    print(" Missing values check (isnull):")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("No missing values found. Dataset is complete.")
    
    print("-" * 65)
