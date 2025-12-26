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

def XuatFileMerge():
    OUTPUT_PATH = Path('data/processed')
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    
    #File 1: Full dataset (CSV)
    output_file = OUTPUT_PATH / 'merged_full.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\n Đã xuất: {output_file}")
    print(f"  Kích thước: {output_file.stat().st_size / 1024**2:.2f} MB")
    print(f"  Shape: {df.shape}")
    
    #File 2: Full dataset
    output_parquet = OUTPUT_PATH / 'merged_full.parquet'
    df.to_parquet(output_parquet, index=False)
    print(f"\n Đã xuất: {output_parquet}")
    print(f"  Kích thước: {output_parquet.stat().st_size / 1024**2:.2f} MB")
    
    # File 3: Essential columns only
    essential_cols = [
        'order_id', 'order_status', 'order_purchase_timestamp',
        'customer_id', 'customer_city', 'customer_state',
        'product_id', 'product_category_name',
        'price', 'freight_value',
        'seller_id', 'seller_city', 'seller_state',
        'review_score', 'payment_types', 'total_payment'
    ]
    
    # Lọc các cột thực sự tồn tại
    essential_cols = [col for col in essential_cols if col in df.columns]
    df_essential = df[essential_cols]
    
    output_essential = OUTPUT_PATH / 'merged_essential.csv'
    df_essential.to_csv(output_essential, index=False, encoding='utf-8-sig')
    print(f"\n Đã xuất: {output_essential}")
    print(f"  Kích thước: {output_essential.stat().st_size / 1024**2:.2f} MB")
    print(f"  Shape: {df_essential.shape}")
