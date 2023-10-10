from itertools import zip_longest


# class definition according to the problem statement
class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        have_funds = self.check_funds(amount)
        if have_funds:
            self.ledger.append({"amount": -amount, "description": description})
        return have_funds

    def get_balance(self):
        return sum((item["amount"] for item in self.ledger))

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, category):
        withdrawn = self.withdraw(amount, f"Transfer to {category.name.title()}")
        if withdrawn:
            category.deposit(amount, f"Transfer from {self.name.title()}")
        return withdrawn

    # this is my extra added method for this class for easy calculation in chart printing
    def total_withdrawal(self):
        total_withdrawal = sum(
            [
                abs(transaction["amount"])
                for transaction in self.ledger
                if transaction["amount"] < 0
            ]
        )
        return round(total_withdrawal, 2)

    # I used __str__ instead of __repr__ because it said to print out object but
    # the print looked more user friendly than programmer friendly :P
    def __str__(self):
        final_str = f"{self.name.title():*^30}\n"
        for item in self.ledger:
            description = item["description"]
            space_between = (23 - len(description)) if len(description) < 23 else 0
            final_str += description if len(description) < 24 else description[0:23]
            final_str += f"{' '*space_between}{item['amount']:>7.2f}\n"
        final_str += f"Total: {self.get_balance():.2f}"
        return final_str


def create_spend_chart(categories):
    # keep in mind when using list comprehension inside () it return a generator so you should convert it into tuple
    category_names = tuple(category.name for category in categories)
    money_spent_by_category = tuple(item.total_withdrawal() for item in categories)
    # this zip will give you a iterator but since we need to use length then we need tuple
    # and zipping the longest value as the delimiter instead of the shortest value like in zip
    char_tuple = tuple(zip_longest(*category_names, fillvalue=" "))
    total_spent = sum(money_spent_by_category)

    def percentage_spent(spent, total):
        # first part of the formula is simple percentage the second part is to get the nearest multiple of 10
        # where you do floor division on percentage and multiply that value with 10
        percentage = (spent / total) * 100
        nearest_multiple_10 = (percentage // 10) * 10
        return nearest_multiple_10

    percentage_spent_list = tuple(
        percentage_spent(item, total_spent) for item in money_spent_by_category
    )
    # developing the chart string
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        bars = ""
        for value in percentage_spent_list:
            bars += " o " if value >= i else "   "
        chart += f"{i:>3}|{bars} \n"
    # this is the horizontal line count after the bars and before the names of category
    number_of_lines = (len(percentage_spent_list) * 3) + 1
    # plus 4 because it needs to take the space occupied by numbers into account
    chart += f"{'-'*(number_of_lines):>{number_of_lines + 4}}\n"
    for index, item in enumerate(char_tuple):
        char_lines = ""
        for set_char in item:
            char_lines += f" {set_char} "
        new_line = "" if index == (len(char_tuple) - 1) else "\n"
        # if added 4 then i will only get one extra space but two was need according to the problem statement
        chart += f"{char_lines:>{number_of_lines+3}} " + new_line
    return chart


if __name__ == "__main__":
    # * my tests
    # food = Category("food")
    # clothing = Category("clothing")
    # food.deposit(1000, "initial deposit")
    # food.withdraw(10.15, "groceries")
    # food.withdraw(15.89, "restaurant and more food services")
    # food.transfer(50, clothing)
    # print(food.total_withdrawal())

    # * Tests from freecodecamp test_module.py
    # food = Category("Food")
    # entertainment = Category("Entertainment")
    # business = Category("Business")
    # food.deposit(900, "deposit")
    # entertainment.deposit(900, "deposit")
    # business.deposit(900, "deposit")
    # food.withdraw(105.55)
    # entertainment.withdraw(33.40)
    # business.withdraw(10.99)
    # print(food)
    # print(entertainment)
    # print(business)
    # print(create_spend_chart([business, food, entertainment]))

    # * tests from main.py in replit
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))
