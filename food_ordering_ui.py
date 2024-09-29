import data
import functions

def show_main_menu():
    my_order = []
    while True:
        print("Jayasri's diner")  # Display your name
        print("____")
        print('N for a new order')
        print("C to change the current order")
        print('X for close orders and print the check')
        print("R to reset the order")
        print('Q for quit')
        user_menu_choice = input('Your input: ')
        
        if user_menu_choice in 'Qq':
            break
        elif user_menu_choice in 'Xx':
            print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total')
            print_check(my_order)
        elif user_menu_choice in 'Cc':
            my_order = change_order(my_order)  # Change items in the order
        elif user_menu_choice in 'Nn':
            print('New order')
            while input('Add a dish? y/n: ') in 'Yy':
                item_code, quantity = input("Enter item code and quantity (e.g., E1 2): ").split()
                if functions.process_customer_request(data.menu_dict, item_code, quantity):
                    my_order.append((item_code, quantity))
                print('your order: ', my_order)
        elif user_menu_choice in 'Rr':
            my_order = []  # Reset the order

def print_check(my_order):
    print("\nYour order:")
    print('your check')

def change_order(my_order):
    print("Change the order:")

if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()
