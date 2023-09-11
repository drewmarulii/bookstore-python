from enum import Enum

class BookName(Enum):
    JAVA = 'Java'
    KOTLIN = 'Kotlin'
    GOLANG = 'Golang'
    PYTHON = 'Python'

class BookPrice(Enum):
    JAVA = 10000
    KOTLIN = 11000
    GOLANG = 12000
    PYTHON = 13000

def select_book():
    print('\nBook List')
    print(f'1) {BookName.JAVA.name}')
    print(f'2) {BookName.KOTLIN.name}')
    print(f'3) {BookName.GOLANG.name}')
    print(f'4) {BookName.PYTHON.name}')

    book = input('Choose Book: ')
    return book

def book_quantity():
    qty = input('Quantity: ')
    return qty

def get_book_price(selected_book):

    if selected_book == '1':
        book_price = BookPrice.JAVA.value
    elif selected_book == '2':
        book_price = BookPrice.KOTLIN.value
    elif selected_book == '3':
        book_price = BookPrice.GOLANG.value
    elif selected_book == '4':
        book_price = BookPrice.PYTHON.value

    return book_price

def calculate(selected_book, quantity):
    book_price = get_book_price(selected_book)
    total_price = int(quantity) * int(book_price)
    return total_price

def manage_order():
    selected_book = select_book()
    quantity = book_quantity()
    total_price = calculate(selected_book, quantity)
    order_summary(selected_book, quantity, total_price)

def order_summary(selected_book, quantity, total_price):
    if selected_book == '1':
        book_name = BookName.JAVA.value
    elif selected_book == '2':
        book_name = BookName.KOTLIN.value
    elif selected_book == '3':
        book_name = BookName.GOLANG.value
    elif selected_book == '4':
        book_name = BookName.PYTHON.value
    
    print('Order Summary:')
    print(f'You have bought {quantity}X of {book_name}. Total Price = Rp {total_price}')
    order_again()

def order_again():
    print('\nOrder Again?')
    print('1) Yes')
    print('2) No')
    choose = input('Choose Number: ')

    if choose == '1':
        manage_order()
    elif choose == '2':
        print('Thank you!') 

def main_menu():
    print('Main Menu')
    print('1) List Book')
    print('2) Exit')

    menu = input('Choose Number: ')

    if int(menu) == 1:
        manage_order()
    elif int(menu) == 2:
        print('Thank you')

main_menu()