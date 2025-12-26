import pandas as pd
import numpy as np


def clean_customers(df):
    print("\n--- Cleaning Customers ---")
    df = df.copy()

    # Xóa duplicates
    before = len(df)
    df = df.drop_duplicates(subset=['customer_id'])
    after = len(df)
    if before > after:
        print(f"Đã xóa {before - after} duplicate customers")

    # Xử lý missing values
    df = df.dropna(subset=['customer_id', 'customer_unique_id'])

    print(f"Customers cleaned: {len(df):,} records")
    return df


def clean_orders(df):
    print("\n--- Cleaning Orders ---")
    df = df.copy()

    # Convert datetime columns
    datetime_cols = ['order_purchase_timestamp', 'order_approved_at',
                     'order_delivered_carrier_date', 'order_delivered_customer_date',
                     'order_estimated_delivery_date']

    for col in datetime_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Xóa duplicates
    before = len(df)
    df = df.drop_duplicates(subset=['order_id'])
    after = len(df)
    if before > after:
        print(f"Đã xóa {before - after} duplicate orders")

    # Xử lý missing values trong các cột quan trọng
    df = df.dropna(subset=['order_id', 'customer_id', 'order_status'])

    # Lọc các orders có status hợp lệ
    valid_status = ['delivered', 'shipped', 'processing', 'invoiced',
                    'canceled', 'unavailable', 'approved', 'created']
    df = df[df['order_status'].isin(valid_status)]

    print(f"Orders cleaned: {len(df):,} records")
    return df


def clean_order_items(df):
    print("\n--- Cleaning Order Items ---")
    df = df.copy()

    # Xóa duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before > after:
        print(f"Đã xóa {before - after} duplicate order items")

    # Xử lý missing values
    df = df.dropna(subset=['order_id', 'product_id'])

    # Xử lý giá trị âm hoặc 0
    if 'price' in df.columns:
        df = df[df['price'] > 0]

    if 'freight_value' in df.columns:
        df = df[df['freight_value'] >= 0]

    print(f" Order Items cleaned: {len(df):,} records")
    return df


def clean_products(df):
    print("\n--- Cleaning Products ---")
    df = df.copy()

    # Xóa duplicates
    before = len(df)
    df = df.drop_duplicates(subset=['product_id'])
    after = len(df)
    if before > after:
        print(f"Đã xóa {before - after} duplicate products")

    # Xử lý missing product_category_name
    if df['product_category_name'].isnull().sum() > 0:
        df['product_category_name'] = df['product_category_name'].fillna('unknown')
        print(f"Đã fill missing category = 'unknown'")

    # Xử lý các giá trị số âm
    numeric_cols = ['product_weight_g', 'product_length_cm',
                    'product_height_cm', 'product_width_cm']
    for col in numeric_cols:
        if col in df.columns:
            df = df[(df[col] > 0) | (df[col].isnull())]

    print(f" Products cleaned: {len(df):,} records")
    return df


def clean_payments(df):
    """Làm sạch dữ liệu payments"""
    print("\n--- Cleaning Payments ---")
    df = df.copy()

    # Xóa duplicates
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before > after:
        print(f"Đã xóa {before - after} duplicate payments")

    # Xử lý missing values
    df = df.dropna(subset=['order_id', 'payment_type'])

    # Xử lý giá trị payment âm hoặc 0
    if 'payment_value' in df.columns:
        df = df[df['payment_value'] >= 0]

    # Chuẩn hóa payment_type
    df['payment_type'] = df['payment_type'].str.lower().str.strip()

    print(f"Payments cleaned: {len(df):,} records")
    return df