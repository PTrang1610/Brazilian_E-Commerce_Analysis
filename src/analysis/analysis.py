def run_analysis(df):
    print("===== DATA ANALYSIS =====")

    # Tổng quan
    total_orders = df["order_id"].nunique()
    total_revenue = df["payment_value"].sum()
    avg_order_value = total_revenue / total_orders

    print("Total orders:", total_orders)
    print("Total revenue:", total_revenue)
    print("Average order value:", avg_order_value)

    # Trạng thái đơn hàng
    print("\nOrder status distribution:")
    print(df["order_status"].value_counts())

    # Doanh thu theo tháng
    df["month"] = df["order_purchase_timestamp"].dt.month
    print("\nRevenue by month:")
    print(df.groupby("month")["payment_value"].sum())

    # Danh mục sản phẩm
    print("\nTop 10 product categories:")
    print(df["product_category_name"].value_counts().head(10))

    # Phương thức thanh toán
    print("\nPayment methods:")
    print(df["payment_type"].value_counts())