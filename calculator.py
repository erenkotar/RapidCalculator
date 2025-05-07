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
    real_profit = (end_value - start_value) / ((1 + daily_inflation) ** days)
    print(f"Real profit of investment: ${real_profit:.2f}")
    return real_profit

if __name__ == "__main__":
    None