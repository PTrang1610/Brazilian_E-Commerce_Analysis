import matplotlib.pyplot as plt
import pandas as pd  
def run_visualization(df):
    print("===== DATA VISUALIZATION =====")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
# 1. Doanh thu theo tháng
    df["month"] = df["order_purchase_timestamp"].dt.month
    monthly_revenue=df.groupby("month")["payment_value"].sum()  
    plt.figure(figsize=(10,6))
    monthly_revenue.plot(kind='bar', color='skyblue')
    bars=plt.bar(monthly_revenue.index, monthly_revenue.values)
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=90)
    for bar in bars:
        y = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y:,.0f}",
            ha="center",
            va="bottom"
        )
    plt.tight_layout()
    plt.show()
# 2. Trạng thái đơn hàng(tròn)
    order_status=df["order_status"].value_counts()
    plt.figure(figsize=(8,8))
    plt.pie(
        order_status.values,labels=order_status.index, autopct=lambda p: f"{p:.1f}%\n({int(p*order_status.sum()/100)})",
        startangle=90
    )
    plt.title("Order Status")
    plt.tight_layout()
    plt.show()
# 3. Top danh mục sản phẩm(10)
    top10_categories=df["product_category_name"].value_counts().head(10)
    plt.figure(figsize=(10,6))
    bars=plt.barh(top10_categories.index, top10_categories.values, color='green')
    plt.title("Top 10 Product Categories")
    plt.xlabel("Number of Products")
    plt.ylabel("Product Category")
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f"{width}",
            ha="left",
            va="center"
        )
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
# 4. Phương thức thanh toán
    payment_methods=df["payment_type"].value_counts()
    plt.figure(figsize=(8,6))
    bars=plt.bar(payment_methods.index, payment_methods.values, color='orange')
    plt.title("Payment Methods")
    plt.xlabel("Payment Type")
    plt.ylabel("Number of Payments")
    for bar in bars:
        y = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            y,
            f"{y}",
            ha="center",
            va="bottom"
        )
    plt.tight_layout()
    plt.show()
