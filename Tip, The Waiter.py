def total_calc(bill_amount, tip_perc):
    # Define Function to Calculate the Tip on the Bill
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please Pay ${total} for your bill.")
    
# Specific only Bill_amount
# Default Value of tip percentage is used
x = int(input("Enter the Bill Amount: "))
y = int(input("Enter the Tip Amount: "))
total_calc(x, y)
