import pandas as pd
import random
import time

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# تابعی برای  تأخیر در تراکنش
def simulate_transaction(row):
    delay = random.uniform(0.1, 2.0)  #  تأخیر بین 0.1 تا 2 ثانیه
    time.sleep(delay)  #  تأخیر
    failed = random.choice([True, False])  #  موفق یا ناموفق بودن تراکنش
    return delay, failed

# تابع برای تحلیل داده‌ها
def analyze_data(file_path):
    try:
        # خواندن داده‌ها از فایل CSV
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        total_transactions = len(data)
        failed_transactions = 0
        total_delay = 0.0

        print("Processing transactions...")
        
        # پردازش هر سطر از داده‌ها
        for index, row in data.iterrows():
            delay, failed = simulate_transaction(row)
            total_delay += delay
            if failed:
                failed_transactions += 1
                print(f"Transaction {index + 1}: FAILED (Delay: {delay:.2f} seconds)")
            else:
                print(f"Transaction {index + 1}: SUCCESS (Delay: {delay:.2f} seconds)")

        # محاسبات نهایی
        average_delay = total_delay / total_transactions
        failure_rate = (failed_transactions / total_transactions) * 100

        print("\nAnalysis Report:")
        print(f"Total Transactions: {total_transactions}")
        print(f"Failed Transactions: {failed_transactions}")
        print(f"Failure Rate: {failure_rate:.2f}%")
        print(f"Average Delay: {average_delay:.2f} seconds")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل
analyze_data(file_path)
