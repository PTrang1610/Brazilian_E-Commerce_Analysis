# ===================== IMPORT MODULES =====================
from src.data_loading.load_data import load_all_data, explore
from src.data_cleaning.clean_data import (
    clean_customers,
    clean_orders,
    clean_order_items,
    clean_products,
    clean_payments
)
from src.data_joining.join_tables import join_all, export_merged
from src.analysis.analysis import run_analysis
from src.visualization.visualization import run_visualization


def main():
    print("===== START BRAZILIAN E-COMMERCE ANALYSIS =====\n")

    # ===================== 1. LOAD DATA =====================
    customers, orders, order_items, products, payments = load_all_data()

    # (OPTIONAL) Khám phá dữ liệu – dùng khi cần báo cáo SV1
    explore(customers, "customers")
    explore(orders, "orders")
    explore(order_items, "order_items")
    explore(products, "products")
    explore(payments, "payments")

    # ===================== 2. CLEAN DATA =====================
    customers = clean_customers(customers)
    orders = clean_orders(orders)
    order_items = clean_order_items(order_items)
    products = clean_products(products)
    payments = clean_payments(payments)

    # ===================== 3. JOIN DATA =====================
    df_merged = join_all(
        customers,
        orders,
        order_items,
        products,
        payments
    )

    # Xuất file merged (phục vụ kiểm tra / báo cáo)
    export_merged(df_merged)

    # ===================== 4. ANALYSIS =====================
    run_analysis(df_merged)

    # ===================== 5. VISUALIZATION =====================
    run_visualization(df_merged)

    print("\n===== END ANALYSIS =====")


if __name__ == "__main__":
    main()
