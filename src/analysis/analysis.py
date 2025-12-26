def run_analysis(df):
    print("===== DATA ANALYSIS =====")

    # Tổng quan
    total_orders = df["order_id"].nunique()
    total_revenue = df["total_payment"].sum()
    avg_order_value = total_revenue / total_orders

    print("Total orders:", total_orders)
    print("Total revenue:", round(total_revenue, 2))
    print("Average order value:", round(avg_order_value, 2))

    # Trạng thái đơn hàng
    print("\n--- Order Status Distribution ---")
    print(df["order_status"].value_counts())

    # Doanh thu theo tháng
    df["order_purchase_timestamp"] = df["order_purchase_timestamp"].astype("datetime64[ns]")
    df["month"] = df["order_purchase_timestamp"].dt.to_period("M")

    revenue_by_month = df.groupby("month")["total_payment"].sum()
    print("\n--- Revenue by Month ---")
    print(revenue_by_month)

    # Danh mục sản phẩm
    print("\n--- Top 10 Product Categories ---")
    print(df["product_category_name"].value_counts().head(10))

    # Phương thức thanh toán
    print("\n--- Payment Methods ---")
    print(df["payment_types"].value_counts())