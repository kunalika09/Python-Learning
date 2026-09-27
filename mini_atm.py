#MINI ATM
account = {
    "name":"kunalika",
    "balance":"203567",
    "pin":"8397",
    "type":"business account"
}
print("===MINI ATM===")
pin = input("Enter your pin:")
if pin == account["pin"]:
      while True:
            print("*** ATM MENU ***")
            print("1.Check Balance:")
            print("2.Deposit Money:")
            print("3.Withdraw Money:")
            print("4.Account Details:")
            print("5.Exit:")
            choice = input("Enter your choice:")
            if choice == "1":
                  print("Your balance is:", account["balance"])
            elif choice == "2":
                  amount = input("Enter your amount:")
                  if amount>0:
                        account["balance"]=account["balance"]+amount
                        print("Money deposited successfully.")
                        print("Collect your cash.")
                        print("New balance",account["balance"])
            elif choice =="4":
                  print("\nAccount Name", account["name"])
                  print("\nAccount Balance", account["balance"])
                  print("\nAccount type", account["type"])
            elif choice =="5":
                  print("Invalid choice")
            else:
            print("Invalid pin")
            print("Access Denied")
                  
