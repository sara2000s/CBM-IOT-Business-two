import pandas as pd
import hashlib
import random
import time

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت هزینه‌ها
DATA_BREACH_COST = 10000  # هزینه هر نقض داده (دلار)
COMPLIANCE_COST_REDUCTION = 5000  # کاهش هزینه انطباق به ازای هر داده امن (دلار)
GAS_COST_PER_TRANSACTION = 2  # هزینه گس به ازای هر تراکنش (دلار)

# تابع هش کردن داده‌ها با الگوریتم SHA-256
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# تابع شبیه‌سازی نقض داده‌ها و امنیت
def simulate_data_security(row):
    breach_chance = random.uniform(0, 1)  # احتمال نقض داده‌ها بین 0 و 1
    if breach_chance < 0.1:  # فرض کنیم نقض داده‌ها 10% احتمال دارد
        return "Breach", hash_data(str(row))  # داده‌ها هش می‌شوند اما نقض رخ می‌دهد
    else:
        return "Secure", hash_data(str(row))  # داده‌ها امن هستند

# تحلیل امنیت و هزینه‌ها
def analyze_security_and_costs(file_path):
    try:
        # خواندن داده‌ها از فایل CSV
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        breaches = 0
        secure_data = 0
        total_breach_cost = 0
        total_savings = 0
        total_gas_cost = 0

        print("Analyzing data security and costs...")
        
        # پردازش هر سطر از داده‌ها
        for index, row in data.iterrows():
            status, hashed_data = simulate_data_security(str(row))
            if status == "Breach":
                breaches += 1
                total_breach_cost += DATA_BREACH_COST
                print(f"Row {index + 1}: DATA BREACH (Hashed: {hashed_data})")
            else:
                secure_data += 1
                total_savings += COMPLIANCE_COST_REDUCTION
                total_gas_cost += GAS_COST_PER_TRANSACTION
                print(f"Row {index + 1}: SECURE DATA (Hashed: {hashed_data})")

        # محاسبات نهایی
        breach_rate = (breaches / len(data)) * 100
        net_savings = total_savings - (total_breach_cost + total_gas_cost)

        print("\nSecurity and Cost Analysis Report:")
        print(f"Total Rows: {len(data)}")
        print(f"Data Breaches: {breaches}")
        print(f"Data Breach Rate: {breach_rate:.2f}%")
        print(f"Total Breach Cost: ${total_breach_cost:.2f}")
        print(f"Secure Data Rows: {secure_data}")
        print(f"Total Compliance Savings: ${total_savings:.2f}")
        print(f"Total Gas Costs: ${total_gas_cost:.2f}")
        print(f"Net Savings: ${net_savings:.2f}")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_security_and_costs(file_path)
