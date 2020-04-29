# Write your code here


class Coffee:
    def __init__(self, code, water, milk, beans, price):
        self.id = code
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price
        self.cups = 1


class CoffeeMachine:
    required_water = 200
    required_milk = 50
    required_beans = 15

    def __init__(self):
        self.total_water = 400
        self.total_milk = 540
        self.total_beans = 120
        self.total_cups = 9
        self.total_money = 550
        self.state = None
        self.fill_state = None

        self.espresso = Coffee("1", 250, 0, 16, 4)
        self.latte = Coffee("2", 350, 75, 20, 7)
        self.cappuccino = Coffee("3", 200, 100, 12, 6)
        self.states = ["buy", "fill", "take", "remaining"]

    def buy_coffee(self, action):
        selection = None
        if action == self.espresso.id:
            selection = self.espresso
        elif action == self.latte.id:
            selection = self.latte
        elif action == self.cappuccino.id:
            selection = self.cappuccino

        if selection:
            if self.can_make_coffee(selection):
                self.make_coffee(selection)

        self.reset()

    def can_make_coffee(self, coffee):
        if self.total_water < coffee.water:
            print("Sorry, not enough water!")
            return False

        if self.total_milk < coffee.milk:
            print("Sorry, not enough milk!")
            return False

        if self.total_beans < coffee.beans:
            print("Sorry, not enough beans!")
            return False

        if self.total_cups < coffee.cups:
            print("Sorry, not enough cups!")
            return False

        return True

    def make_coffee(self, coffee):
        self.total_water -= coffee.water
        self.total_milk -= coffee.milk
        self.total_beans -= coffee.beans
        self.total_cups -= coffee.cups
        self.total_money += coffee.price

        print("I have enough resources, making you a coffee!")

    def fill(self, action):
        action = int(action)
        if self.fill_state == "water":
            self.fill_water(action)
        elif self.fill_state == "milk":
            self.fill_milk(action)
        elif self.fill_state == "beans":
            self.fill_beans(action)
        elif self.fill_state == "cups":
            self.fill_cups(action)

    def start_fill(self):
        self.state = "fill"
        self.fill_state = "water"

    def fill_water(self, quantity):
        self.total_water += quantity
        self.fill_state = "milk"

    def fill_milk(self, quantity):
        self.total_milk += quantity
        self.fill_state = "beans"

    def fill_beans(self, quantity):
        self.total_beans += quantity
        self.fill_state = "cups"

    def fill_cups(self, quantity):
        self.total_cups += quantity
        self.reset()

    def take_money(self):
        print('I gave you %d' % self.total_money)
        self.total_money = 0
        self.reset()

    def status(self):
        print()
        print("The coffee machine has:")
        print("%d of water" % self.total_water)
        print("%d of milk" % self.total_milk)
        print("%d of coffee beans" % self.total_beans)
        print("%d of disposable cups" % self.total_cups)
        print("$%d of money" % self.total_money)

        self.reset()

    def reset(self):
        self.state = None
        self.fill_state = None

    def is_valid(self, action):
        return action in self.states

    def execute(self, action):

        if self.state is None:
            if not self.is_valid(action):
                return

            if action == "take":
                self.take_money()
            elif action == "remaining":
                self.status()
            elif action == "fill":
                self.start_fill()
            else:
                self.state = action
        elif self.state == "buy":
            self.buy_coffee(action)
        elif self.state == "fill":
            self.fill(action)

    def message(self):
        if self.state is None:
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latter, 3 - cappuccino, back - to main menu:")
        elif self.state == "fill":
            print("Write how many ml of water do you want to add:")
        elif self.state == "fill_milk":
            print("Write how many ml of milk do you want to add:")
        elif self.state == "fill_beans":
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "fill_cups":
            print("Write how many disposable cups of coffee do you want to add:")


machine = CoffeeMachine()
while True:
    machine.message()
    order = input()
    if order == "exit":
        break
    machine.execute(order)
    print()
