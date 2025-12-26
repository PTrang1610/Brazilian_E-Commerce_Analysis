import pandas as pd
import numpy as np
from pathlib import Path

def key():
    print("KEY")
    keys_info = """
    BẢNG                PRIMARY KEY              FOREIGN KEY
    ─────────────────────────────────────────────────────────────────────
    orders              order_id                 customer_id → customers
    customers           customer_id              -
    order_items         order_id + item_id       order_id → orders
                                                 product_id → products
                                                 seller_id → sellers
    products            product_id               -
    sellers             seller_id                -
    order_payments      order_id + seq           order_id → orders
    order_reviews       review_id                order_id → orders
    """
    print(keys_info)
def join_all(customers, orders, order_items, products, payments):
    print("JOIN")    
    #orders LEFT JOIN customers
    print("\n1️  orders ← customers")
    df = orders.merge(customers, on='customer_id', how='left')
    print(f"   Shape: {df.shape}")
    
    #LEFT JOIN order_items
    print("\n2️  ← order_items")
    df = df.merge(order_items, on='order_id', how='left')
    print(f"   Shape: {df.shape}")
    
    #LEFT JOIN products
    print("\n3️  ← products")
    df = df.merge(products, on='product_id', how='left')
    print(f"   Shape: {df.shape}")
    
    #Aggregate payments trước khi JOIN
    print("\n4️  ← payments (aggregated)")
    payments_agg = payments.groupby('order_id').agg({
        'payment_type': lambda x: ', '.join(x.unique()),
        'payment_installments': 'max',
        'payment_value': 'sum'
    }).reset_index()
    payments_agg.columns = ['order_id', 'payment_types', 'max_installments', 'total_payment']
    
    df = df.merge(payments_agg, on='order_id', how='left')
    print(f"   Shape: {df.shape}")
        
    return df

def XuatFileMerge(df):
    OUTPUT_PATH = Path('data/processed')
    output_file = OUTPUT_PATH / 'merged_full.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')

