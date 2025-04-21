import pandas as pd  

class BlockchainInfrastructureCostEstimator:  
    def __init__(self, blockchain_network_cost_per_device_usd, security_tools_cost_per_device_usd):  
        """  
        :param blockchain_network_cost_per_device_usd: هزینه زیرساخت شبکه بلاک‌چین به ازای هر دستگاه (دلار)  
        :param security_tools_cost_per_device_usd: هزینه ابزارهای امنیتی به ازای هر دستگاه (دلار)  
        """  
        self.blockchain_network_cost_per_device_usd = blockchain_network_cost_per_device_usd  
        self.security_tools_cost_per_device_usd = security_tools_cost_per_device_usd  

    def estimate_costs(self, file_path):  
        try:  
            df = pd.read_csv(file_path)  
            print(f"فایل '{file_path}' با موفقیت بارگذاری شد. تعداد ردیف‌ها: {len(df)}")  
        except Exception as e:  
            print(f"خطا در خواندن فایل: {e}")  
            return  

        # تعداد دستگاه‌های یکتا (ایده‌آل ستون device_id)  
        if 'device_id' in df.columns:  
            num_devices = df['device_id'].nunique()  
            print(f"تعداد دستگاه‌های یکتا (IoMT) در داده‌ها: {num_devices}")  
        else:  
            num_devices = 100  # مقدار پیش‌فرض  
            print(f"ستون 'device_id' یافت نشد. فرض بر تعداد دستگاه‌ها: {num_devices}")  

        # محاسبه هزینه‌ها  
        blockchain_network_cost = num_devices * self.blockchain_network_cost_per_device_usd  
        security_tools_cost = num_devices * self.security_tools_cost_per_device_usd  

        total_infrastructure_cost = blockchain_network_cost + security_tools_cost  

        print("\n--- خلاصه هزینه‌های زیرساخت بلاک‌چین (دلار) ---")  
        print(f"هزینه شبکه بلاک‌چین (برای {num_devices} دستگاه): ${blockchain_network_cost:,.2f}")  
        print(f"هزینه ابزارهای امنیتی (برای {num_devices} دستگاه): ${security_tools_cost:,.2f}")  
        print(f"کل هزینه زیرساخت بلاک‌چین: ${total_infrastructure_cost:,.2f}\n")  

        return {  
            'num_devices': num_devices,  
            'blockchain_network_cost_usd': blockchain_network_cost,  
            'security_tools_cost_usd': security_tools_cost,  
            'total_infrastructure_cost_usd': total_infrastructure_cost  
        }  

if __name__ == "__main__":  
    file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

    blockchain_network_cost_per_device_usd = 1500  
    security_tools_cost_per_device_usd = 700  

    estimator = BlockchainInfrastructureCostEstimator(  
        blockchain_network_cost_per_device_usd, security_tools_cost_per_device_usd  
    )  
    cost_summary = estimator.estimate_costs(file_path)  