import pandas as pd  

class SmartContractExecutionCostEstimator:  
    def __init__(self, gas_cost_per_execution_usd, compliance_monitoring_cost_usd):  
        """  
        :param gas_cost_per_execution_usd: هزینه گس برای هر اجرای قرارداد هوشمند (دلار)  
        :param compliance_monitoring_cost_usd: هزینه سالانه یا دوره‌ای نظارت بر انطباق (دلار)  
        """  
        self.gas_cost_per_execution_usd = gas_cost_per_execution_usd  
        self.compliance_monitoring_cost_usd = compliance_monitoring_cost_usd  

    def estimate_costs(self, file_path):  
        try:  
            df = pd.read_csv(file_path)  
            print(f"فایل '{file_path}' با موفقیت بارگذاری شد. تعداد ردیف‌ها: {len(df)}")  
        except Exception as e:  
            print(f"خطا در خواندن فایل: {e}")  
            return  

        # تعداد اجرای قرارداد هوشمند فرضا برابر تعداد ردیف‌ها است  
        num_executions = len(df)  
        print(f"تعداد اجرای قراردادهای هوشمند (تعداد تراکنش‌ها): {num_executions}")  

        # محاسبه هزینه‌های گس (Gas Costs)  
        gas_cost_total = num_executions * self.gas_cost_per_execution_usd  

        # هزینه‌های نظارت بر انطباق (Compliance Monitoring) به صورت ثابت  
        compliance_cost_total = self.compliance_monitoring_cost_usd  

        total_smart_contract_cost = gas_cost_total + compliance_cost_total  

        print("\n--- خلاصه هزینه‌های اجرای قراردادهای هوشمند (USD) ---")  
        print(f"هزینه گس برای {num_executions} اجرای قرارداد: ${gas_cost_total:,.2f}")  
        print(f"هزینه نظارت بر انطباق: ${compliance_cost_total:,.2f}")  
        print(f"کل هزینه‌های اجرای قرارداد هوشمند: ${total_smart_contract_cost:,.2f}\n")  

        return {  
            'num_executions': num_executions,  
            'gas_cost_total_usd': gas_cost_total,  
            'compliance_monitoring_cost_usd': compliance_cost_total,  
            'total_smart_contract_cost_usd': total_smart_contract_cost  
        }  

if __name__ == "__main__":  
    file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

    gas_cost_per_execution_usd = 0.75  # هزینه گس برای هر اجرای قرارداد (دلار)  
    compliance_monitoring_cost_usd = 5000  # هزینه نظارت سالانه بر انطباق (دلار)  

    estimator = SmartContractExecutionCostEstimator(gas_cost_per_execution_usd, compliance_monitoring_cost_usd)  
    cost_summary = estimator.estimate_costs(file_path)  