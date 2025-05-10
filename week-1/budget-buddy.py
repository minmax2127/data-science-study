from tabulate import tabulate
import os
import math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Table:   
    table = []
    headers = ["ID", "Item/Source", "Category", "Amount"]
    categories = []

    def Calculate_Total(self):
        total = 0.00
        for row in self.table:
            total += row[3]
        return total

    def Show_Table(self, table_to_print) :
        if len(table_to_print) == 0:
            print("no data available:(")
        else:
            show_table = tabulate(table_to_print, headers=self.headers)
            print(show_table)

    def Add_Item(self, item, category, amount):
        self.table.append([len(self.table) + 1, item, category, amount])

    def Get_Item_Index_By_Id(self, id):
        index = 0
        for row in self.table:
            if row[0] == id:
                return index
            index += 1
        return len(self.table) + 1000
    
    def Get_Item_By_Id(self, id):
        try:
            return self.table[self.Get_Item_Index_By_Id(id)]
        except IndexError:
            return None
        
    def Edit_Item(self, index, key, value):
        self.table[index][key] = value

    def Delete_Item(self, id):
        if self.Get_Item_By_Id(id) == None:
            print("Not found!")
        else:
            self.table.remove(self.Get_Item_By_Id(id)) 

    def Display_Operation(self, operation):
        print("-------------------")
        print("  " + operation)
        print("-------------------")
        

    def Get_Categories(self):
        self.categories = []
        for row in self.table:
            self.categories.append(row[2])
        self.categories = list(set(self.categories))
        return self.categories




class Budget(Table):
    budgets = [
        [1, "Papa", "Allowance", 1500],
        [2, "Mama", "Allowance", 1000],
        [3, "DOST", "Scholarship", 8000],
        [3, "Savings", "Own", 5000],
    ]
    total_budget = 0.0
    headers = ["ID", "Source", "Category", "Amount"]
    table = budgets
    

    def Show_Table(self):
        print("\n\tBUDGET LIST\n")
        super().Show_Table(self.budgets)
        self.total_budget = super().Calculate_Total()
        print("\nTOTAL BUDGET: " + str(self.total_budget) + "\n")

    def Input_Item(self):
        super().Display_Operation("ADD BUDGET")
        print("\n\n")
        source = input("Source: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        self.Add_Item(source, category, amount)

    def Edit_Item(self):
        super().Display_Operation("EDIT BUDGET")
        id = int(input("Id: "))
        item_index = super().Get_Item_Index_By_Id(id)
        item = self.budgets[item_index]

        # ask what to edit
        print(item)
        key_to_edit = input("Edit [s] source, [c] category, [a] amount ? : ")
        
        if key_to_edit == 's' or key_to_edit == 'c' or key_to_edit == 'a':
            new_value = input("New Value: ")

            if key_to_edit == 's':
                super().Edit_Item(item_index, 1, new_value)
            elif key_to_edit == 'c':
                super().Edit_Item(item_index, 2, new_value)
            elif key_to_edit == 'a':
                super().Edit_Item(item_index, 3, float(new_value))

        else:
            print("~Invalid choice~")

    def Delete_Item(self):
        super().Display_Operation("DELETE BUDGET")
        id = int(input("Id: "))
        super().Delete_Item(id)

    def Filter_By_Category(self, category):
        filtered_table = []

        for row in self.table:
            if row[2].lower() == category.lower():
                filtered_table.append(row)

        super().Show_Table(filtered_table)


class Expense(Table):
    expenses = [
        [1, "Phone", "Tech Device", 15000],
        [2, "Laptop", "Tech Device", 37000],
        [3, "Food", "Basic Needs", 200],
    ]
    total_expenses = 0.0
    headers = ["ID", "Item", "Category", "Amount"]
    table = expenses
    

    def Show_Table(self):
        print("\n\tEXPENSE LIST\n")
        super().Show_Table(self.expenses)
        self.total_expenses = super().Calculate_Total()
        print("\nTOTAL EXPENSES: " + str(self.total_expenses) + "\n")

    def Input_Item(self):
        super().Display_Operation("ADD EXPENSE")
        print("\n\n")
        item = input("Item: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        self.Add_Item(item, category, amount)

    def Edit_Item(self):
        super().Display_Operation("EDIT EXPENSE")
        id = int(input("Id: "))
        item_index = super().Get_Item_Index_By_Id(id)
        item = self.expenses[item_index]

        # ask what to edit
        print(item)
        key_to_edit = input("Edit [i] item, [c] category, [a] amount ? : ")
        
        if key_to_edit == 'i' or key_to_edit == 'c' or key_to_edit == 'a':
            new_value = input("New Value: ")

            if key_to_edit == 'i':
                super().Edit_Item(item_index, 1, new_value)
            elif key_to_edit == 'c':
                super().Edit_Item(item_index, 2, new_value)
            elif key_to_edit == 'a':
                super().Edit_Item(item_index, 3, float(new_value))

        else:
            print("~Invalid choice~")

    def Delete_Item(self):
        super().Display_Operation("DELETE EXPENSE")
        id = int(input("Id: "))
        super().Delete_Item(id)

    def Filter_By_Category(self, category):
        filtered_table = []

        for row in self.table:
            if row[2].lower() == category.lower():
                filtered_table.append(row)

        super().Show_Table(filtered_table)
        
class Options:
    def Validate_Answer(self, options, title):
        while True:
            try: 
                print(title)
                for i in range(len(options)):
                    print("[" + str(i + 1) + "] " + options[i])
                print("[0] Back to Menu")

                choice = int(input("Choice: "))
                if choice >= 0 and choice <= len(options):
                    return choice
                else:
                    print("Invalid answer! Please try again.")
            except ValueError:
                print("Invalid answer!")


def Show_Tables(budget, expense):

    clear_screen()
    budget.Show_Table()
    expense.Show_Table()

    print("Total Budget: " + str(budget.total_budget)) 
    print("Total Expense: " + str(expense.total_expenses)) 
    print("\n  CURRENT SAVINGS: " + str(budget.total_budget - expense.total_expenses) + "\n")



# Main Function
clear_screen()
print("BUDGET TRACKER CLI APP")
print("-----------------------")

budget = Budget()
expense = Expense()
options = Options()

table_obj = budget

clear_screen()

while True:
    Show_Tables(budget, expense)
    # main menu
    menu_choice = options.Validate_Answer(
        ["Add", "Edit", "Delete", "View by Category"], 
        "What would you like to do? : "
    )

    if menu_choice == 1 or menu_choice == 2 or menu_choice == 3: # add, edit, delete
        choice = options.Validate_Answer(
            ["Budget", "Expense"], 
            ""
        )

        if choice == 1: # budget
            table_obj = budget
        elif choice == 2: # expense
            table_obj = expense

        if menu_choice == 1: # add
            table_obj.Input_Item()

        elif menu_choice == 2: # edit
            table_obj.Edit_Item()

        elif menu_choice == 3: # delete
            table_obj.Delete_Item()

    elif menu_choice == 4: # view by category
        print("Categories: ")
        categories = budget.Get_Categories() + expense.Get_Categories()
        print(categories)
        
        chosen_category = input("Input category: ")
        
        budget.Filter_By_Category(chosen_category)
        expense.Filter_By_Category(chosen_category)

        inputEnter = input("[ENTER] to proceed")













'''
while True:
    clear_screen then show table
    [1] Add
    [2] Edit
    [3] Delete
    [4] View by category
    [0] End program

    if 1: Add
        clear_screen then show table
        [1] Budget
        [2] Expense
        [0] Back to Menu

        if 1 or 2:
            Determine what class to access
            use class function to get input - Add_Row()
            add to table
        Back to menu

    else if 2:
        clear_screen then show table
        [1] Budget
        [2] Expense
        [0] Back to Menu

        if 1 or 2:
            Determine what class to access
            use class function to edit a row - Edit_Row()
        Back to menu
    
    else if 3:
        clear_screen then show table
        [1] Budget
        [2] Expense
        [0] Back to Menu

        if 1 or 2:
            Determine what class to access
            use class function to delete a row - Delete_Row()
        Back to menu

    else if 4:
        clear_screen then show table
        display categories
        take input for category
        filter table  - Filter_Table()
'''