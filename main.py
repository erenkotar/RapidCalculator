from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
import math

from calculator import *

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Selam Hocam, doc'a git bi zahmet",
        "endpoints": {
            "real_payment_value": "/real_payment_value?total_amount=...&month_number=...&inflation_rate=...",
            "real_profit_values": "/real_profit_value?start_value=...&end_value=...&day_number=...&inflation_rate=..."
        }
    }

@app.get("/real_payment_value")
def calculate_real_value(
    total_amount: float = Query(..., gt=0, description="Total amount (> 0)"),
    month_number: int = Query(..., gt=0, description="Number of months (> 0)"),
    inflation_rate: float = Query(..., ge=0, description="Annual inflation rate (>= 0)")
):
    result = real_payment_value(
        total_amount=total_amount,
        month_number=month_number,
        inflation_rate=inflation_rate
    )
    return {"real_value": round(result, 2)}

@app.get("/real_profit_value")
def calculate_real_value(
    start_value: float = Query(..., gt=0, description="Start value (> 0)"),
    end_value: float = Query(..., gt=0, description="End value (> 0)"),
    day_number: int = Query(..., gt=0, description="Number of days (> 0)"),
    inflation_rate: float = Query(..., ge=0, description="Annual inflation rate (>= 0)")
):
    result = real_profit_value(
        start_value=start_value,
        end_value=end_value,
        days=day_number,
        inflation_rate=inflation_rate
    )
    return {"real_value": round(result, 2)}