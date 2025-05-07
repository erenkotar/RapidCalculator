import numpy as np

def real_payment_value(total_amount: float, month_number: int, inflation_rate: float) -> float:    
    monthly_inflation = (1 + inflation_rate / 100) ** (1 / 12) - 1
    print(monthly_inflation)
    monthly_payment = total_amount / month_number
    total_amount_real = np.array([1/((monthly_inflation+1)**i)*monthly_payment for i in range(month_number)]).sum()
    print(f"Real value of payment: ${total_amount_real:.2f}")
    return total_amount_real

def real_profit_value(start_value:float, end_value:float, days:int, inflation_rate: float) -> float:
    daily_inflation = (1 + inflation_rate / 100) ** (1 / 365) - 1
    end_value_real = end_value / ((1 + daily_inflation) ** days)
    real_profit = end_value_real - start_value
    real_profit_perc = real_profit / start_value *100
    print(f"Real profit: ${real_profit:.2f}, %{real_profit_perc:.2f}, ")
    return real_profit, real_profit_perc

if __name__ == "__main__":
    None