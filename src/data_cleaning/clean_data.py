import pandas as pd
import numpy as np


def clean_customers(df):
    print("\n--- Cleaning Customers ---")
    df = df.copy()

    # Remove duplicate customers
    before = len(df)
    df = df.drop_duplicates(subset=['customer_id'])
    after = len(df)
    if before > after:
        print(f"Removed {before - after} duplicate customers")

    # Handle missing values
    df = df.dropna(subset=['customer_id', 'customer_unique_id'])

    print(f"Customers cleaned: {len(df):,} records")
    return df


def clean_orders(df):
    print("\n--- Cleaning Orders ---")
    df = df.copy()

    # Convert datetime columns
    datetime_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for col in datetime_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Remove duplicate orders
    before = len(df)
    df = df.drop_duplicates(subset=['order_id'])
    after = len(df)
    if before > after:
        print(f"Removed {before - after} duplicate orders")

    # Remove missing critical fields
    df = df.dropna(subset=['order_id', 'customer_id', 'order_status'])

    # Keep valid order status only
    valid_status = [
        'delivered',
        'shipped',
        'processing',
        'invoiced',
        'canceled',
        'unavailable',
        'approved',
        'created'
    ]
    df = df[df['order_status'].isin(valid_status)]

    print(f"Orders cleaned: {len(df):,} records")
    return df


def clean_order_items(df):
    print("\n--- Cleaning Order Items ---")
    df = df.copy()

    # Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before > after:
        print(f"Removed {before - after} duplicate order items")

    # Remove missing critical fields
    df = df.dropna(subset=['order_id', 'product_id'])

    # Remove invalid prices
    if 'price' in df.columns:
        df = df[df['price'] > 0]

    # Remove invalid freight values
    if 'freight_value' in df.columns:
        df = df[df['freight_value'] >= 0]

    print(f"Order Items cleaned: {len(df):,} records")
    return df


def clean_products(df):
    print("\n--- Cleaning Products ---")
    df = df.copy()

    # Remove duplicate products
    before = len(df)
    df = df.drop_duplicates(subset=['product_id'])
    after = len(df)
    if before > after:
        print(f"Removed {before - after} duplicate products")

    # Fill missing category name
    if 'product_category_name' in df.columns:
        missing = df['product_category_name'].isnull().sum()
        if missing > 0:
            df['product_category_name'] = df['product_category_name'].fillna('unknown')
            print("Filled missing product_category_name with 'unknown'")

    # Remove invalid numeric values
    numeric_cols = [
        'product_weight_g',
        'product_length_cm',
        'product_height_cm',
        'product_width_cm'
    ]
    for col in numeric_cols:
        if col in df.columns:
            df = df[(df[col] > 0) | (df[col].isnull())]

    print(f"Products cleaned: {len(df):,} records")
    return df


def clean_payments(df):
    print("\n--- Cleaning Payments ---")
    df = df.copy()

    # Remove duplicate payments
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    if before > after:
        print(f"Removed {before - after} duplicate payments")

    # Remove missing critical fields
    df = df.dropna(subset=['order_id', 'payment_type'])

    # Remove invalid payment values
    if 'payment_value' in df.columns:
        df = df[df['payment_value'] >= 0]

    # Normalize payment_type
    df['payment_type'] = df['payment_type'].str.lower().str.strip()

    print(f"Payments cleaned: {len(df):,} records")
    return df
