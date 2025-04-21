import pandas as pd  

class OperationalCostEstimator:  
    def __init__(self, transaction_fee_per_tx_usd, node_maintenance_cost_per_node_usd):  
        """  
        :param transaction_fee_per_tx_usd: هزینه گس/تراکنش بر حسب دلار برای هر تراکنش در بلاک‌چین  
        :param node_maintenance_cost_per_node_usd: هزینه نگهداری سالانه هر گره بلاک‌چین (دلار)  
        """  
        self.transaction_fee_per_tx_usd = transaction_fee_per_tx_usd  
        self.node_maintenance_cost_per_node_usd = node_maintenance_cost_per_node_usd  

    def estimate_costs(self, file_path):  
        try:  
            df = pd.read_csv(file_path)  
            print(f"فایل '{file_path}' با موفقیت بارگذاری شد. تعداد ردیف‌ها: {len(df)}")  
        except Exception as e:  
            print(f"خطا در خواندن فایل: {e}")  
            return  

        # تعداد تراکنش‌ها را برابر تعداد ردیف‌ها فرض می‌کنیم  
        num_transactions = len(df)  
        print(f"تعداد تراکنش‌ها (ردیف‌های داده): {num_transactions}")  

        # تعداد دستگاه‌های یکتا براساس device_id (در صورت وجود)  
        if 'device_id' in df.columns:  
            num_devices = df['device_id'].nunique()  
            print(f"تعداد دستگاه‌های یکتا (IoMT): {num_devices}")  
        else:  
            num_devices = 100  # مقدار پیش‌فرض در صورت نبود ستون  
            print(f"ستون 'device_id' یافت نشد. فرض تعداد دستگاه‌ها: {num_devices}")  

        # تعداد گره‌های بلاک‌چین فرض: 1 گره هر 20 دستگاه  
        num_nodes = max(1, num_devices // 20)  
        print(f"تعداد گره‌های بلاک‌چین تخمینی: {num_nodes}")  

        # محاسبه هزینه تراکنش‌ها (دلار)  
        transaction_fees_cost_usd = num_transactions * self.transaction_fee_per_tx_usd  
        
        # هزینه نگهداری گره‌ها (دلار)  
        node_maintenance_cost_usd = num_nodes * self.node_maintenance_cost_per_node_usd  

        total_operational_cost_usd = transaction_fees_cost_usd + node_maintenance_cost_usd  

        print("\n--- خلاصه هزینه‌های عملیاتی بلاک‌چین و IoMT (دلار) ---")  
        print(f"هزینه تراکنش‌ها ({num_transactions} تراکنش): ${transaction_fees_cost_usd:,.2f}")  
        print(f"هزینه نگهداری {num_nodes} گره بلاک‌چین: ${node_maintenance_cost_usd:,.2f}")  
        print(f"کل هزینه عملیاتی: ${total_operational_cost_usd:,.2f}\n")  

        return {  
            'num_transactions': num_transactions,  
            'num_nodes': num_nodes,  
            'transaction_fees_cost_usd': transaction_fees_cost_usd,  
            'node_maintenance_cost_usd': node_maintenance_cost_usd,  
            'total_operational_cost_usd': total_operational_cost_usd  
        }  

if __name__ == "__main__":  
    file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

    transaction_fee_per_tx_usd = 0.50   # هزینه متوسط گس/تراکنش بر حسب دلار  
    node_maintenance_cost_per_node_usd = 2000  # هزینه نگهداری سالانه هر گره (دلار)  

    estimator = OperationalCostEstimator(transaction_fee_per_tx_usd, node_maintenance_cost_per_node_usd)  
    cost_summary = estimator.estimate_costs(file_path)  