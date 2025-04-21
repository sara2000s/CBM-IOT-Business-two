import pandas as pd
import random

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت هزینه‌ها
INSURANCE_FRAUD_COST = 5000  # هزینه هر تقلب بیمه‌ای (دلار)
ADMIN_OVERHEAD_COST_REDUCTION = 2000  # کاهش هزینه‌های اداری به ازای هر تراکنش امن (دلار)
GAS_COST_PER_TRANSACTION = 50  # هزینه گس برای هر تراکنش امن (دلار)

# تابع شبیه‌سازی تقلب بیمه‌ای
def simulate_fraud(row):
    fraud_chance = random.uniform(0, 1)  # احتمال تقلب بیمه‌ای بین 0 و 1
    if fraud_chance < 0.2:  # فرض کنیم احتمال تقلب بیمه‌ای 20% باشد
        return "Fraud", INSURANCE_FRAUD_COST
    else:
        return "No Fraud", ADMIN_OVERHEAD_COST_REDUCTION - GAS_COST_PER_TRANSACTION

# تحلیل کاهش تقلب و صرفه‌جویی‌ها
def analyze_fraud_reduction_with_costs(file_path):
    try:
        # خواندن داده‌ها از فایل CSV
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        total_fraud_cases = 0
        total_no_fraud_cases = 0
        total_fraud_cost = 0
        total_savings = 0
        total_gas_cost = 0

        print("Analyzing fraud reduction and costs...")
        
        # پردازش هر سطر از داده‌ها
        for index, row in data.iterrows():
            status, cost = simulate_fraud(row)
            if status == "Fraud":
                total_fraud_cases += 1
                total_fraud_cost += cost
                print(f"Row {index + 1}: FRAUD DETECTED (Cost: ${cost})")
            else:
                total_no_fraud_cases += 1
                total_savings += cost + GAS_COST_PER_TRANSACTION
                total_gas_cost += GAS_COST_PER_TRANSACTION
                print(f"Row {index + 1}: NO FRAUD (Savings: ${cost})")

        # محاسبات نهایی
        fraud_rate = (total_fraud_cases / len(data)) * 100
        net_savings = total_savings - total_fraud_cost

        print("\nFraud Reduction and Cost Analysis Report:")
        print(f"Total Rows: {len(data)}")
        print(f"Fraud Cases: {total_fraud_cases}")
        print(f"Fraud Rate: {fraud_rate:.2f}%")
        print(f"Total Fraud Cost: ${total_fraud_cost:.2f}")
        print(f"No Fraud Cases: {total_no_fraud_cases}")
        print(f"Total Administrative Savings: ${total_savings:.2f}")
        print(f"Total Gas Costs: ${total_gas_cost:.2f}")
        print(f"Net Savings: ${net_savings:.2f}")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_fraud_reduction_with_costs(file_path)
