import pandas as pd  

class HardwareCostEstimator:  
    def __init__(self, iot_device_cost_usd, blockchain_node_cost_usd, integration_device_cost_usd):  
        self.iot_device_cost_usd = iot_device_cost_usd  
        self.blockchain_node_cost_usd = blockchain_node_cost_usd  
        self.integration_device_cost_usd = integration_device_cost_usd  

    def estimate_costs(self, file_path):  
        try:  
            df = pd.read_csv(file_path)  
            print(f"File '{file_path}' loaded successfully. Number of rows: {len(df)}")  
        except Exception as e:  
            print(f"Error reading file: {e}")  
            return  

        # فرض کنیم ستون 'device_id' تعیین‌کننده دستگاه‌های یکتا IoMT است  
        if 'device_id' in df.columns:  
            num_iot_devices = df['device_id'].nunique()  
            print(f"Number of unique IoMT devices: {num_iot_devices}")  
        else:  
            num_iot_devices = 100  # مقدار پیش‌فرض درصورت نبود ستون  
            print(f"'device_id' column not found. Using default number of IoMT devices: {num_iot_devices}")  

        # تعداد گره‌های بلاک‌چین، فرض یک گره برای هر 20 دستگاه  
        num_blockchain_nodes = max(1, num_iot_devices // 20)  

        # دستگاه‌های یکپارچه‌سازی برابر ده درصد تعداد دستگاه‌ها (حداقل یک)  
        num_integration_devices = max(1, num_iot_devices // 10)  

        # محاسبه هزینه‌ها به دلار  
        cost_iot_devices = num_iot_devices * self.iot_device_cost_usd  
        cost_blockchain_nodes = num_blockchain_nodes * self.blockchain_node_cost_usd  
        cost_integration_devices = num_integration_devices * self.integration_device_cost_usd  

        total_cost = cost_iot_devices + cost_blockchain_nodes + cost_integration_devices  

        print("\nHardware Cost Summary (USD):")  
        print(f"IoMT Devices ({num_iot_devices} devices): ${cost_iot_devices:,.2f}")  
        print(f"Blockchain Nodes ({num_blockchain_nodes} nodes): ${cost_blockchain_nodes:,.2f}")  
        print(f"Integration Devices ({num_integration_devices} devices): ${cost_integration_devices:,.2f}")  
        print(f"Total Hardware Cost: ${total_cost:,.2f}\n")  

        return {  
            'num_iot_devices': num_iot_devices,  
            'num_blockchain_nodes': num_blockchain_nodes,  
            'num_integration_devices': num_integration_devices,  
            'cost_iot_devices_usd': cost_iot_devices,  
            'cost_blockchain_nodes_usd': cost_blockchain_nodes,  
            'cost_integration_devices_usd': cost_integration_devices,  
            'total_cost_usd': total_cost  
        }  

if __name__ == "__main__":  
    file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

    # هزینه‌ها به دلار  
    iot_device_unit_cost_usd = 500       # Cost per IoMT device (USD)  
    blockchain_node_unit_cost_usd = 2000 # Cost per blockchain node (USD)  
    integration_device_unit_cost_usd = 300 # Cost per integration device (USD)  

    estimator = HardwareCostEstimator(iot_device_unit_cost_usd, blockchain_node_unit_cost_usd, integration_device_unit_cost_usd)  
    cost_summary = estimator.estimate_costs(file_path)  