from datetime import datetime

def solution(A, D, N):
    # Initialize variables
    balance = 0
    monthly_fee = 5
    payments_in_month = {}
    total_income = 0
    total_expenditure = 0
    months = range(1, 13)
    
    # Process transactions
    for i in range(N):
        # Parse date
        date = datetime.strptime(D[i], '%Y-%m-%d')
        month = date.month
        
        # Update payments in month
        if month in payments_in_month:
            payments_in_month[month] += 1
        else:
            payments_in_month[month] = 1
        
        # Update balance and income/expenditure
        balance += A[i]
        if A[i] > 0:
            total_income += A[i]
        else:
            total_expenditure -= A[i]
    
    # Calculate fees
    fees = 0
    for month in months:
        if month in payments_in_month and payments_in_month[month] >= 3 and total_income >= 100:
            fees += monthly_fee
        else:
            fees += monthly_fee
    
    # Calculate final balance
    final_balance = balance - fees
    
    return final_balance


A1 = [100, 100, 100, -10]
D1 = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]
print(solution(A1, D1, len(A1)))  # Output: 230

A2 = [180, -50, -25, -25]
D2 = ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]
print(solution(A2, D2, len(A2)))  # Output: 25

A3 = [1, -1, 0, -105, 1]
D3 = ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]
print(solution(A3, D3, len(A3)))  # Output: -164

A4 = [100, 100, -10, -20, -30]
D4 = ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]
print(solution(A4, D4, len(A4)))  # Output: 80

A5 = [-60, 60, -40, -2]