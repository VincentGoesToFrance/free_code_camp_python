#check_funds
# ausgabe nicht komplett
# self.category = category

class Category:
    
    ledger = [] # Hauptbuch
    category = None

    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        self.category_str = ""
        category_length = 30 - len(self.category)
        if category_length % 2 == 0:
            self.category_str = (int(category_length/2)) * "*" + self.category + (int(category_length/2)) * "*" + "\n"
        else:
            category_length += 1
            self.category_str = (int(category_length/2)) * "*" + self.category + (int(category_length/2 -1)) * "*" + "\n"

        for x, obj in enumerate(self.ledger):
            #formatting:
            if x == 0:
                format_1 = f"{self.ledger[x]['description']}"
            else:
                format_1 = f"{self.ledger[x]['description']}"
            string_1 = ""
            if len(format_1) <= 23:
                string_1 = format_1 + int(23-len(format_1))*" "
            else:
                for i in range(23):
                    string_1 += format_1[i]
            test_2 = self.ledger[x]["amount"]
            formatting = "{test_2:.2f}".format(test_2 = test_2)
            string_2 = ""
            
            if len(formatting) <= 7:
                string_2 = int(7 - len(formatting)) * " " + formatting
            else:
                for i in range(7):
                    string_2 += formatting[i]
                print(string_2)
            string_3 = string_1 + string_2 + "\n"
            self.category_str += string_3    

        self.category_str += "Total: " + str(self.get_balance()) 
        return self.category_str

    #einzahlung
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    #auszahlung
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,  'description': description})
            return True
        else: 
            return False

    #get_balance
    def get_balance(self):
        total = 0
        for x,obj in enumerate(self.ledger):
            total += self.ledger[x]["amount"]
        return total
            
    #überweisung 
    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,  'description': f"Transfer to {Category.category}"})
            Category.deposit(amount,f"Transfer from {self.category}")
            return True
        else:
            print("You got not enough money")
            return False

# namensvergabe scheiße
def create_spend_chart(categories: list[Category]):

    bar_chart = ""
    bar_rows = ["Percentage spent by category\n", "100| ", " 90| ", " 80| ", " 70| ", " 60| "," 50| ", " 40| ", " 30| ", " 20| ", " 10| ", "  0| ", "    -"]
    string_1 = "o  "
    string_2 = "   "
    string_3 = "     "
    length = 0
    table_rows = []
    category_list = []

    total_category_withdrawls = 0
    category_withdrawls = 0
    category_total_list = []

    for category in categories:
        total_category_withdrawls = 0
        for total_category in category.ledger:
            if total_category["description"] != "deposit" and total_category["description"].startswith("Transfer") != True:
                total_category_withdrawls += total_category["amount"]
                category_withdrawls += total_category["amount"]
        category_total_list.append([abs(total_category_withdrawls),category.category])
    category_withdrawls = abs(category_withdrawls)

    for category in category_total_list:
        initial = category[0]
        total = category_withdrawls
        percentage = int(int(initial * 100 / total) / 10) * 10
        category_list.append((percentage, category[1]))


    for i in range(len(category_list)):
        if category_list[i][0] > 90:
            bar_rows[1] += string_1
        else:
            bar_rows[1] += string_2
        if category_list[i][0] > 80:
            bar_rows[2] += string_1
        else:
            bar_rows[2] += string_2
        if category_list[i][0] > 70:
            bar_rows[3] += string_1
        else:
            bar_rows[3] += string_2
        if category_list[i][0] > 60:
            bar_rows[4] += string_1
        else:
            bar_rows[4] += string_2
        if category_list[i][0] > 50:
            bar_rows[5] += string_1
        else:
            bar_rows[5] += string_2
        if category_list[i][0] > 40:
            bar_rows[6] += string_1
        else:
            bar_rows[6] += string_2
        if category_list[i][0] > 30:
            bar_rows[7] += string_1
        else:
            bar_rows[7] += string_2
        if category_list[i][0] > 20:
            bar_rows[8] += string_1
        else:
            bar_rows[8] += string_2
        if category_list[i][0] > 10:
            bar_rows[9] += string_1
        else:
            bar_rows[9] += string_2
        if category_list[i][0] > 0:
            bar_rows[10] += string_1
        else:
            bar_rows[10] += string_2
        if category_list[i][0] == 0:
            bar_rows[11] += string_1
        else:
            bar_rows[11] += string_1
        if i == len(category_list)-1:
            for j in range(1,12):
                bar_rows[j] += "\n"

    bar_rows[12] += len(category_list) * "---" + "\n"

    for i in range(len(category_list)):
        if length == 0 or length < len(category_list[i][1]):
            length = len(category_list[i][1])

    for i in range(length):
        table_rows.append(string_3)

    for i in range(len(category_list)):
        for j in range(len(table_rows)):
            if len(category_list[i][1])-1 >= j:
                table_rows[j] += category_list[i][1][j] + "  "
            else:
                table_rows[j] += "   "

    print(table_rows[12])
    for i in range(len(table_rows)):
        if i != len(table_rows)-1:
            table_rows[i] += "\n"


    bar_chart_part_1 = "".join(bar_rows)
    bar_chart_part_2 = "".join(table_rows)
    bar_chart = bar_chart_part_1 + bar_chart_part_2

    return bar_chart

#food = Category('Food')
#food.deposit(100, 'deposit')
#food.withdraw(60, 'groceries')
#food.withdraw(15.89, 'groceries')
#food.withdraw(15.00, 'restaurant and more food for dessert')
#clothing = Category('Clothing')
#clothing.deposit(100, "deposit")
#clothing.withdraw(20, "restaurant")
#food.transfer(20, clothing)
#print(clothing)
#print(food)
#auto = Category("Auto")
#auto.deposit(100, "deposit")
#auto.withdraw(10, "abc")
#print(create_spend_chart([food,clothing, auto]))
#print(repr(f'{create_spend_chart([food,clothing, auto])}'))

food = Category("Food")
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon')
entertainment = Category("Entertainment")
food.transfer(20, entertainment)
print(create_spend_chart([food, entertainment]))