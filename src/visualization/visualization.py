import matplotlib.pyplot as plt
import pandas as pd

def run_visualization(df):
    print("===== DATA VISUALIZATION =====")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    fig, axes = plt.subplots(2, 2, figsize=(20, 12))
    # 1. Monthly Revenue 
    df["month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)
    monthly_revenue = df.groupby("month")["total_payment"].sum()

    axes[0, 0].bar(
        monthly_revenue.index,
        monthly_revenue.values,
        color="steelblue"
    )
    axes[0, 0].set_title("Monthly Revenue", fontsize=14)
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].set_ylabel("Revenue")
    axes[0, 0].tick_params(axis="x", rotation=90, labelsize=9)

    # ===================== Order Status Distribution (Custom Groups) =====================
    order_status = df["order_status"].value_counts()
    main_labels = ["delivered", "shipped", "canceled"]
    main_values = order_status[order_status.index.isin(main_labels)]
    others_value = order_status[~order_status.index.isin(main_labels)].sum()
    if others_value > 0:
        main_values["Others"] = others_value
    percentages = (main_values / main_values.sum() * 100).round(1)
    colors = ["#4C72B0", "#55A868", "#C44E52", "#DD8452"]
    wedges, texts = axes[0, 1].pie(
        main_values.values,
        startangle=90,
        colors=colors,
        wedgeprops={"edgecolor": "white"}
    )
    axes[0, 1].set_title("Order Status Distribution", fontsize=14)
    legend_labels = [
        f"{label} ({percentages[label]}%)"
        for label in main_values.index
    ]
    axes[0, 1].legend(
        wedges,
        legend_labels,
        title="Order Status",
        loc="center left",
        bbox_to_anchor=(1.25, 0.5),
        fontsize=10
    )
    # 3. Top 10 Product Categories
    top10_categories = df["product_category_name"].value_counts().head(10)

    axes[1, 0].barh(
        top10_categories.index,
        top10_categories.values,
        color="seagreen"
    )
    axes[1, 0].set_title("Top 10 Product Categories", fontsize=14)
    axes[1, 0].set_xlabel("Number of Products")
    axes[1, 0].invert_yaxis()
    axes[1, 0].tick_params(axis="y", labelsize=10)

    # 4. Payment Methods (1 màu – không ghi số)
    payment_methods = df["payment_types"].value_counts()
    axes[1, 1].bar(
        payment_methods.index,
        payment_methods.values,
        color="darkorange"
    )
    axes[1, 1].set_title("Payment Methods", fontsize=14)
    axes[1, 1].set_xlabel("Payment Type")
    axes[1, 1].set_ylabel("Number of Payments")
    axes[1, 1].tick_params(axis="x", rotation=90, labelsize=7)

    plt.subplots_adjust(
    left=0.13,
    right=0.88,  
    top=0.92,
    bottom=0.2,
    hspace=0.6,  
    wspace=0.8  
    )
    plt.show()
