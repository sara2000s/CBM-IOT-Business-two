import pandas as pd

# مسیر فایل CSV
file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"

# مقادیر ثابت
TOTAL_UPFRONT_COSTS = 330000  # هزینه‌های اولیه (دلار)
ANNUAL_OPERATIONAL_COSTS = 50000  # هزینه‌های عملیاتی سالانه (دلار)
SAVINGS_FROM_REDUCED_FRAUD = 500000  # صرفه‌جویی سالانه از کاهش تقلب (دلار)
SAVINGS_FROM_REMOTE_MONITORING = 200000  # صرفه‌جویی سالانه از نظارت از راه دور (دلار)
REVENUE_FROM_DATA_SHARING = 0  # درآمد حاصل از اشتراک‌گذاری داده (در صورت وجود)

# تابع برای محاسبه ROI
def calculate_roi(file_path):
    try:
        # بارگذاری داده‌ها (در صورت نیاز به داده‌ها)
        print("Loading data...")
        data = pd.read_csv(file_path)
        
        if data.empty:
            print("The CSV file is empty.")
            return
        
        # محاسبه مزایا و هزینه‌ها
        total_benefits = SAVINGS_FROM_REDUCED_FRAUD + SAVINGS_FROM_REMOTE_MONITORING + REVENUE_FROM_DATA_SHARING
        total_costs = TOTAL_UPFRONT_COSTS + ANNUAL_OPERATIONAL_COSTS

        # محاسبه ROI
        roi = (total_benefits / total_costs) * 100

        # نمایش نتایج
        print("\nReturn on Investment (ROI) Analysis:")
        print(f"Total Benefits (Savings + Revenue): ${total_benefits:.2f}")
        print(f"Total Costs (Upfront + Operational): ${total_costs:.2f}")
        print(f"ROI: {roi:.2f}%")

        # تفسیر
        print("\nInterpretation:")
        print(f"An ROI of {roi:.2f}% indicates that the project generates significant value beyond its costs.")

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# اجرای تحلیل ROI
calculate_roi(file_path)
