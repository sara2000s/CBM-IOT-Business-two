import pandas as pd
import random

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت
COST_PER_DUPLICATE_TEST = 100  # هزینه هر آزمایش تکراری (دلار)
COST_REDUCTION_FROM_RECYCLING = 5000  # صرفه‌جویی از بازیافت هر دستگاه (دلار)
NUM_DEVICES_RECYCLED = 100  # تعداد دستگاه‌های قابل بازیافت

# تابع شبیه‌سازی کاهش تکرار آزمایش‌ها
def simulate_duplicate_test_reduction(row):
    reuse_chance = random.uniform(0, 1)  # احتمال استفاده مجدد از داده‌های پزشکی
    if reuse_chance > 0.6:  # فرض کنیم 60% احتمال استفاده مجدد وجود دارد
        return "Reduced", COST_PER_DUPLICATE_TEST
    else:
        return "Not Reduced", 0

# تحلیل مدل کسب‌وکار چرخه‌ای
def analyze_circular_business_model(file_path):
    try:
        # خواندن داده‌ها از فایل CSV
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        total_tests = len(data)
        reduced_tests = 0
        total_savings_from_tests = 0
        total_savings_from_recycling = NUM_DEVICES_RECYCLED * COST_REDUCTION_FROM_RECYCLING

        print("Analyzing circular business model impact...")
        
        # پردازش هر سطر از داده‌ها
        for index, row in data.iterrows():
            status, savings = simulate_duplicate_test_reduction(row)
            if status == "Reduced":
                reduced_tests += 1
                total_savings_from_tests += savings
                print(f"Row {index + 1}: DUPLICATE TEST REDUCED (Savings: ${savings})")
            else:
                print(f"Row {index + 1}: NO REDUCTION")

        # محاسبات نهایی
        reduction_rate = (reduced_tests / total_tests) * 100
        total_savings = total_savings_from_tests + total_savings_from_recycling

        print("\nCircular Business Model Analysis Report:")
        print(f"Total Tests: {total_tests}")
        print(f"Reduced Duplicate Tests: {reduced_tests}")
        print(f"Reduction Rate: {reduction_rate:.2f}%")
        print(f"Total Savings from Reduced Tests: ${total_savings_from_tests:.2f}")
        print(f"Total Savings from Recycling Devices: ${total_savings_from_recycling:.2f}")
        print(f"Total Savings: ${total_savings:.2f}")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_circular_business_model(file_path)
