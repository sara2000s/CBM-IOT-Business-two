import pandas as pd
import random

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت هزینه‌ها
HOSPITALIZATION_COST_PER_PATIENT = 3000  # هزینه بستری شدن به ازای هر بیمار (دلار)
REMOTE_MONITORING_COST = 500  # هزینه نظارت از راه دور به ازای هر بیمار (دلار)
GAS_COST_PER_TRANSACTION = 50  # هزینه گس برای هر بیمار (دلار)
OTHER_OPERATIONAL_COSTS = 200  # هزینه عملیاتی اضافی به ازای هر بیمار (دلار)

# مقادیر ثابت صرفه‌جویی‌ها
ANNUAL_FRAUD_SAVINGS = 500000  # صرفه‌جویی سالانه ناشی از کاهش تقلب
ANNUAL_HOSPITALIZATION_SAVINGS = 200000  # صرفه‌جویی سالانه ناشی از کاهش بستری شدن
TOTAL_ANNUAL_SAVINGS = ANNUAL_FRAUD_SAVINGS + ANNUAL_HOSPITALIZATION_SAVINGS  # مجموع صرفه‌جویی سالانه

# تابع شبیه‌سازی کاهش بستری شدن
def simulate_hospitalization(row):
    monitoring_effectiveness = random.uniform(0, 1)  # احتمال کاهش بستری شدن بین 0 و 1
    if monitoring_effectiveness > 0.7:  # فرض کنیم نظارت از راه دور با احتمال 70% مؤثر است
        return "Reduced", HOSPITALIZATION_COST_PER_PATIENT - REMOTE_MONITORING_COST - GAS_COST_PER_TRANSACTION - OTHER_OPERATIONAL_COSTS
    else:
        return "No Reduction", -REMOTE_MONITORING_COST - GAS_COST_PER_TRANSACTION - OTHER_OPERATIONAL_COSTS

# تحلیل کاهش هزینه‌ها
def analyze_hospitalization_costs_with_details(file_path):
    try:
        # خواندن داده‌ها از فایل CSV
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        total_patients = len(data)
        reduced_cases = 0
        total_savings = 0
        total_monitoring_cost = 0
        total_gas_cost = 0
        total_operational_costs = 0

        print("Analyzing hospitalization costs with additional details...")
        
        # پردازش هر سطر از داده‌ها
        for index, row in data.iterrows():
            status, savings = simulate_hospitalization(row)
            total_monitoring_cost += REMOTE_MONITORING_COST
            total_gas_cost += GAS_COST_PER_TRANSACTION
            total_operational_costs += OTHER_OPERATIONAL_COSTS
            if status == "Reduced":
                reduced_cases += 1
                total_savings += savings
                print(f"Row {index + 1}: HOSPITALIZATION REDUCED (Savings: ${savings})")
            else:
                total_savings += savings
                print(f"Row {index + 1}: NO REDUCTION (Cost: ${-savings})")

        # محاسبات نهایی
        reduction_rate = (reduced_cases / total_patients) * 100
        net_savings = total_savings

        print("\nHospitalization Cost Analysis Report with Additional Costs:")
        print(f"Total Patients: {total_patients}")
        print(f"Reduced Hospitalization Cases: {reduced_cases}")
        print(f"Reduction Rate: {reduction_rate:.2f}%")
        print(f"Total Monitoring Cost: ${total_monitoring_cost:.2f}")
        print(f"Total Gas Costs: ${total_gas_cost:.2f}")
        print(f"Total Operational Costs: ${total_operational_costs:.2f}")
        print(f"Net Savings: ${net_savings:.2f}")
        
        # نمایش صرفه‌جویی نمونه
        print("\nExample Annual Savings Report:")
        print(f"Reduced fraud due to blockchain transparency: ${ANNUAL_FRAUD_SAVINGS}")
        print(f"Remote monitoring could reduce hospital stays by 20%, saving: ${ANNUAL_HOSPITALIZATION_SAVINGS}")
        print(f"Total Annual Savings: ${TOTAL_ANNUAL_SAVINGS}")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_hospitalization_costs_with_details(file_path)
