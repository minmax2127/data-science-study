from tabulate import tabulate
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_table(expenses, budgets):
    # takes expenses and budgets from the main function and displays it on a table
    if len(budgets) != 0:
        headers = ["ID", "Source", "Amount", "Category"]
        budget_table = tabulate(budgets, headers=headers)
        print("\n\n\t BUDGET LIST\n")
        print(budget_table)
    else:
        print("\n\tNo budget recorded!")
    
    if len(expenses) != 0:
        headers = ["ID", "Item", "Amount", "Category"]
        expenses_table = tabulate(expenses, headers=headers)
        print("\n\n\t EXPENSE LIST\n")
        print(expenses_table)
    else:
        print("\n\tNo expenses recorded!")



### MAIN FUNCTION ###
print("Hi! I am your budget buddy!")

total_money = 0.00

headers = ["ID", "Item/Source", "Category", "Amount"]
expenses= []
budgets = []




while True: # for the what would you like to do today part
    try:
        clear_screen()
        print("\nWhat would you like to do today? : ")

        # PROMPT 1: Menu Screen
        print("[1] Add")
        print("[2] Edit")
        print("[3] Delete")
        print("[4] View by category")

        choice = int(input("\nInput choice: "))

        # IF Adding, Editing, or Deleting an Item
        if choice >= 1 and choice <= 3: 

            while True:
                print("\n------------------------------------\n")

                # Display Operation
                if choice == 1:
                    print("Adding \n")
                elif choice == 2:
                    print("Editting\n")
                elif choice == 3:
                    print("Deleting\n")

                # PROMPT 2: Choose what to add/edit/delete
                print("[1] Budget")
                print("[2] Expense")
                print("[0] Back to Menu")


                if choice == 1: # For adding
                    choice = int(input("\nInput choice: "))
                    
                    # Add an Item/Source
                    if choice >= 1 and choice <= 2:

                        # Takes input for item/source
                        x = ""
                        if choice == 1:
                            x = input("\n\tSource: ")
                        else:
                            x = input("\n\tItem: ")
                        
                        category = input("\tCategory(Optional): ")
                        amount = float(input("\tAmount: "))

                        if choice == 1:
                            budgets.append([len(budgets) + 1, x, category, amount])
                        else:
                            budgets.append([len(budgets) + 1, x, category, amount])

                        display_table(expenses, budgets) # displays table

                    # Back to Menu
                    elif choice == 0:
                        break
                    
                    # Invalid character inputted
                    else:
                        print("Invalid input! Please try again!")
                        continue
                
                elif choice == 2: # For editing
                    choice = int(input("\nInput choice: "))

                    from_table = []

                    if choice == 1 or choice == 2:
                        
                        id_to_edit = input("Input ID of the row to edit: ")
                        
                        # determines the table it will take a row to edit from
                        if choice == 1: # budget table
                            budget_to_edit = budgets[id_to_edit - 1]

                            print(budget_to_edit)

                            # check what detail to edit
                            choice = input("Edit the: [s] source, [c] category, [a] amount. Input other character to cancel: ")

                            if choice != 's' and choice != 'c' and choice != 'a':
                                continue
                            else:
                                new_value = input("New value: ")
                                if choice == 's':
                                    budget_to_edit[1] = new_value
                                elif choice == 'c':
                                    budget_to_edit[2] = new_value
                                elif choice == 'a':
                                    new_value = int(new_value)
                                    budget_to_edit[3] = new_value
                                

                        else: # expenses table
                            expense_to_edit = expenses[id_to_edit - 1]

                    

                    

        else:
            print("Invalid choice! Please try again")
            continue
    except ValueError:
        print("Error! Invalid input")
