print("====CURRENCY CONVERTER====")
print("1.USD  UGX")
print("2.UGX  USD")

choice = input("choose an option:")

if choice =="1":
    amount = float(input("Enter USD:"))
    converted = amount*3700
    print(f"{amount}USD = {converted}UGX")
    
elif choice == "2":
    amount = float(input("Enter UGX:"))
    converted = amount/3700
    print(f"{amount}UGX = {converted:2f}USD")
else:
    print("Invalid choice")        
    