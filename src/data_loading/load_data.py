def load_all_data():
    customers = pd.read_csv(path + 'customers.csv')
    orders = pd.read_csv(path + 'orders.csv')
    order_items = pd.read_csv(path + 'order_items.csv')
    products = pd.read_csv(path + 'products.csv')
    payments = pd.read_csv(path + 'order_payments.csv')
    
    return customers, orders, order_items, products, payments
def explore(df, name):
    print(f"\n==================== BẢNG: {name.upper()} ====================")
   
    print(df.head())
    
    print(" Thông tin cấu trúc (info):")
    df.info() 
    
    print(" Thống kê mô tả (describe):")
    print(df.describe())
    
    print(" Kiểm tra giá trị thiếu (isnull):")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "Dữ liệu đầy đủ, không thiếu.")
    print("-" * 60)
