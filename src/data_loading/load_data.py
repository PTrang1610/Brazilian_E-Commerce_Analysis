import pandas as pd
DATA_PATH = "data/raw/"
def load_all_data():
    print(f"--- Loading data from: {DATA_PATH} ---")
    
    # Reading CSV files
    customers = pd.read_csv(DATA_PATH + 'customers.csv')
    orders = pd.read_csv(DATA_PATH + 'orders.csv')
    order_items = pd.read_csv(DATA_PATH + 'order_items.csv')
    products = pd.read_csv(DATA_PATH + 'products.csv')
    payments = pd.read_csv(DATA_PATH + 'order_payments.csv')

    return customers, orders, order_items, products, payments

def explore(df, name):
    print(f"\n==================== DATASET: {name.upper()} ====================")
    
    # 1. Preview the first 5 rows
    print("First 5 rows (head):")
    print(df.head())
    
    # 2. Check data types and non-null counts
    print("Data structure and types (info):")
    df.info() 
    
    # 3. Statistical summary
    print("Statistical summary (describe):")
    print(df.describe())
    
    # 4. Check for missing values
    print("Missing values: ", df.isnull().sum())
    print("-" * 65)
