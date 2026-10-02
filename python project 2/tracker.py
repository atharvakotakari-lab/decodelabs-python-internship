total = 0.0

print("=== DecodeLabs Expense Tracker ===")
print("Enter your expenses one by one. Type 'quit' to finish and view the total.\n")

while True:
    user_input = input("Enter expense amount (or 'quit'): ").strip()
    
    if user_input.lower() == 'quit':
        break
        
    try:
        expense = float(user_input)
        
        if expense < 0:
            print("⚠️ Error: Expense cannot be negative. Try again.")
            continue
            
        total += expense
        print(f"-> Added: ${expense:.2f} | Current Total: ${total:.2f}")
        
    except ValueError:
        print("⚠️ Invalid Data: Please enter a valid numerical amount or 'quit'.")

print("\n================================")
print(f"FINAL TOTAL SPENT: ${total:.2f}")
print("================================")