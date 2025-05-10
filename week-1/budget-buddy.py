from tabulate import tabulate
import os

# clears the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Class that performs the table operations (Adding, Editing, Deleting, Filtering, etc.)
class Table:  
    # initialize the object 
    def __init__(self, title, table, headers, x, categories = []):
        self.title = title  # title of the table
        self.table = table  # data to be displayed; contains rows
        self.headers = headers # the label of each column
        self.x = x          # refers to the item/source name
        self.categories = categories  # list of categories in a table

    # calculates total amount
    def Calculate_Total(self):
        total = 0
        for row in self.table:
            total += row[3]
        return total

    # displays the table in grid
    def Show_Table(self) :
        print("\n\t" + self.title + " Table\n")

        # if no data
        if len(self.table) == 0:
            print("no data available:(")

        # if there is data
        else:
            # appends an additional row to show total
            self.table.append([None, None, None, self.Calculate_Total()]) 
            show_table = tabulate(self.table, headers=self.headers, tablefmt="grid")
            print(show_table) # display table
            self.table.remove(self.table[-1])
        print()

    # asks input from user about the item to be added
    def Add_Item(self):  
        # will continuously ask user to input a new values if the values inputted are invalid
        while True: 
            print()
            try: 
                item = input(str(self.x) + ": ")
                category = input("Category: ")
                amount = float(input("Amount: "))

                # if amount is valid, add item to the table
                self.table.append([len(self.table) + 1, item, category, amount])
                break

            except ValueError:
                print("Invalid input. Please try again!")

    # returns the index of an item based on its id
    def Get_Item_Index_By_Id(self, id):
        index = 0
        # iterates through every row on the table and returns the index of the row that matches the id given
        for row in self.table:
            if row[0] == id:
                return index
            index += 1
        return len(self.table) + 1000 # returns "decoy" value if id does not have a match
    
    # asks input from user about the item to be editted
    def Edit_Item(self):
        while True:
            try:
                id = int(input("Id: "))
                item_index = self.Get_Item_Index_By_Id(id)
                if item_index > len(self.table):
                    print("ID not found!")
                    continue
                print(self.table[item_index])

                key = 0
                while True:
                    choice = input("Edit [x] " + self.headers[1] + ", [c] category, [a] amount: ")
                    if choice != 'x' and choice != 'c' and choice != 'a':
                        print("Invalid choice!")
                        continue
                    
                    if choice == 'x':
                        key = 1
                    elif choice == 'c':
                        key = 2
                    else:
                        key = 3
                    
                    break

                value = ""
                while True:
                    try:
                        value = input("Input new value: ")
                        if key == 3:
                            value = float(value)
                        break
                    except ValueError:
                        print("Invalid value!")

                self.table[item_index][key] = value

                break
            except ValueError:
                print("Invalid ID!")
                continue

    # takes user input for the id then deletes it
    def Delete_Item(self):
        while True:
            id = int(input("Id: "))
            if self.Get_Item_Index_By_Id(id) > len(self.table):
                print("Not found!")
                continue
            else:
                self.table.remove(self.table[self.Get_Item_Index_By_Id(id)]) 
                break

    # returns categories
    def Get_Categories(self):
        self.categories = []
        for row in self.table:
            self.categories.append(row[2])
        self.categories = list(set(self.categories))
        return self.categories
    
    # displays filtered table based on category
    def Show_Filtered_Table(self, category):
        filtered_table = []
        sum = 0.00
        for row in self.table:
            # if category matches, add to temp list then increment to total sum
            if row[2].lower() == category.lower():
                filtered_table.append(row)
                sum += row[3]

        print("\n\t" + self.title + " (By " + str(category) + ")\n")

        # if no row in the filtered table
        if len(filtered_table) == 0:
            print("no data available:(")
        else:
            # append a row that will show the total
            total_row = [None, None, None, sum]
            filtered_table.append(total_row)
            show_table = tabulate(filtered_table, headers=self.headers, tablefmt="grid")
            print(show_table) # print row
        print()

   
class Options: # creates options and validates user input
    def Validate_Answer(self, options, title):
        while True:
            print()
            try: 
                print(title)
                for i in range(len(options)):
                    print("[" + str(i + 1) + "] " + options[i])
                print("[0] Back to Menu")

                choice = int(input("\nChoice: "))
                if choice >= 0 and choice <= len(options):
                    return choice
                else:
                    print("Invalid answer! Please try again.")
            except ValueError:
                print("Invalid answer!")

# for visual purposes, display text with borders
def display_operation(txt):
    print("\n******************************")
    print("\t " + str(txt))
    print("******************************")

# show the two tables: budget and expense table
def Show_Tables(budget, expense):
    clear_screen()

    display_operation("YOUR BUDGET BUDDY")
    budget.Show_Table()
    expense.Show_Table()

    print("Total Budget: " + str(budget.Calculate_Total())) 
    print("Total Expense: " + str(expense.Calculate_Total())) 
    print("\n  CURRENT SAVINGS: " + str(budget.Calculate_Total() - expense.Calculate_Total()) + "\n")



### Main Function ###

budgets = [
    [1, "Papa", "Allowance", 150], 
    [2, "Mama", "Allowance", 100], 
    [3, "DOST", "Scholarship", 120]
]

expenses = [
    [1, "Phone", "Laptop", 37000], 
]

budget_table = Table("Budget", budgets, ["ID", "Source", "Category", "Amount"], "Source")
expense_table = Table("Expense", expenses, ["ID", "Item", "Category", "Amount"], "Item")
options = Options()

table_obj = budget_table

clear_screen()

while True:
    Show_Tables(budget_table, expense_table)
    
    # main menu
    menu_choice = options.Validate_Answer(
        ["Add", "Edit", "Delete", "View by Category"], 
        "What would you like to do? : "
    )

    if menu_choice == 1 or menu_choice == 2 or menu_choice == 3: # add, edit, delete
        if menu_choice == 1:
            display_operation("Add")
        elif menu_choice == 2:
            display_operation("Edit")
        elif menu_choice == 3:
            display_operation("Delete")
        
        choice = options.Validate_Answer(
            ["Budget", "Expense"], 
            ""
        )

        ### Determine if budget or expense
        if choice == 1: # budget
            table_obj = budget_table
        elif choice == 2: # expense
            table_obj = expense_table
        else:
            continue
        
        ### Determine what operation
        if menu_choice == 1: # add
            table_obj.Add_Item()

        elif menu_choice == 2: # edit
            table_obj.Edit_Item()
        
        elif menu_choice == 3: # delete
            table_obj.Delete_Item()

    
    elif menu_choice == 4: # show filtered table
        display_operation("View by category")
        print("Categories")
        
        # display all categories of data saved
        categories = budget_table.Get_Categories() + expense_table.Get_Categories()
        print(categories)
        
        # asks user to add a category
        chosen_category = input("Input category: ")
        
        # shows the filtered table based on category
        budget_table.Show_Filtered_Table(chosen_category)
        expense_table.Show_Filtered_Table(chosen_category)

        inputEnter = input("[ENTER] to proceed...")
