import pandas as pd  
import random  
import time  

# مسیر فایل CSV  
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

# تنظیم هزینه‌ها (قابل تغییر)  
cost_per_failed_transaction_usd = 1000      # هزینه هر تراکنش ناموفق (دلار)  
cost_per_second_delay_usd = 10              # هزینه هر ثانیه تأخیر (دلار)  

# تابعی برای شبیه‌سازی تأخیر و موفق یا ناموفق بودن تراکنش  
def simulate_transaction(row):  
    delay = random.uniform(0.1, 2.0)  # تأخیر بین 0.1 تا 2 ثانیه  
    time.sleep(delay)                 # ایجاد تأخیر (شبیه‌سازی زمان پردازش)  
    failed = random.choice([True, False])  # تراکنش موفق یا ناموفق  
    return delay, failed  

# تابع برای تحلیل داده‌ها همراه با محاسبه هزینه‌ها  
def analyze_data(file_path):  
    try:  
        print("Loading data...")  
        data = pd.read_csv(file_path)  
        
        if data.empty:  
            print("The CSV file is empty.")  
            return  
        
        total_transactions = len(data)  
        failed_transactions = 0  
        total_delay = 0.0  

        print("Processing transactions...")  
        
        # پردازش هر تراکنش  
        for index, row in data.iterrows():  
            delay, failed = simulate_transaction(row)  
            total_delay += delay  
            if failed:  
                failed_transactions += 1  
                print(f"Transaction {index + 1}: FAILED (Delay: {delay:.2f} seconds)")  
            else:  
                print(f"Transaction {index + 1}: SUCCESS (Delay: {delay:.2f} seconds)")  
        
        average_delay = total_delay / total_transactions  
        failure_rate = (failed_transactions / total_transactions) * 100  

        # محاسبه هزینه‌ها  
        total_lost_revenue = failed_transactions * cost_per_failed_transaction_usd  
        total_delay_cost = total_delay * cost_per_second_delay_usd  
        total_cost = total_lost_revenue + total_delay_cost  

        # گزارش نهایی  
        print("\n--- Analysis Report ---")  
        print(f"Total Transactions: {total_transactions}")  
        print(f"Failed Transactions: {failed_transactions}")  
        print(f"Failure Rate: {failure_rate:.2f}%")  
        print(f"Average Delay: {average_delay:.2f} seconds")  
        print("\n--- Cost Estimation (USD) ---")  
        print(f"Lost Revenue due to Failed Transactions: ${total_lost_revenue:,.2f}")  
        print(f"Operational Cost due to Delay: ${total_delay_cost:,.2f}")  
        print(f"Total Estimated Cost: ${total_cost:,.2f}")  

    except FileNotFoundError:  
        print(f"Error: File not found at path {file_path}")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  

# اجرای تحلیل  
analyze_data(file_path)  