import db

MENU_PROMPT = """ 
       
       --The Food App--

Please enter a value to continue:
1) Add a new food
2) See all food
3) Find a food by name
4) Find the best category by food name
5) Exit
Your Selection: """


def menu():
    conn = db.connect()
    db.create_tables(conn)

    while (num := input(MENU_PROMPT)) != "5":
        print("You selected: ",num)
        if num == "1":
            add_food_function(conn)

        elif num == "2":
            get_all_foods_function(conn)

        elif num == "3":
            get_foods_by_name_function(conn)

        elif num == "4":
            get_best_category_by_name_function(conn)

        else:
            print("Invalid Input, Please try with a valid input!")


def get_all_foods_function(conn):
    foods = db.get_all_foods(conn)
    for food in foods:
        print(f"{food[1]} {food[2]} {food[3]}/100")

def get_foods_by_name_function(conn):
    name = input("Enter food name to find: ")
    foods = db.get_foods_by_name(conn, name)
    for food in foods:
        print(f"{food[1]} {food[2]} {food[3]}/100")

def get_best_category_by_name_function(conn):
    name = input("Enter a food name: ")
    best_cat = db.get_best_category_by_name(conn, name)
    print(f'The best category of "{best_cat[1]}" is: {best_cat[2]}')


menu()


def add_food_function(conn):
    name = input("Enter food name: ")
    category = input("Enter a category: ")
    rating = int(input("Enter your rating: "))
    db.add_food(conn, name, category, rating)

