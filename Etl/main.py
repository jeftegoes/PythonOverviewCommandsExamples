from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

file_book = list(open("books.csv", "r", encoding="utf-8"))

list_books: list[Book] = []


def format_str_price_to_float(price: str) -> float:
    try:
        return float(price.replace("R$ ", "").replace(",", "."))
    except:
        return 0


def verif_if_customer_exists(customer_id: int, customer_repository: CustomerRepository) -> bool:
    for customer in customer_repository.list_customers:
        if (customer.id == customer_id):
            return True

    return False


def get_customer(customer_id: int, customer_repository: CustomerRepository) -> Customer:
    for customer in customer_repository.list_customers:
        if (customer.id == customer_id):
            return customer

    return Customer(-1, "Client not found!")


def principal_menu() -> int:
    try:
        print("1 - Cadastrar cliente")
        print("2 - Fazer pedido")
        print("3 - Relatório de Pedidos")
        print("4 - Relatório de Clientes")
        print("5 - Relatório de Livros")
        print("0 - Sair")
        return int(input("Informe a opção do menu: "))
    except:
        print("A opção informada é inválida, o programa vai ser encerrado...")
        return 0


for book in file_book[1:]:
    list_book = book.split(";")
    book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                list_book[4], format_str_price_to_float(list_book[5]))
    list_books.append(book)

customer_repository = CustomerRepository()
order_repository = OrderRepository()

while True:
    menu_option = principal_menu()
    if (menu_option == 0):
        break

    if menu_option == 1:
        id = int(input("Informe o código do cliente: "))
        nome = input("Informe o nome do cliente: ")
        customer = Customer(id, nome)
        customer_repository.list_customers.append(customer)
    if menu_option == 2:
        id = int(input("Informe o código do pedido: "))
        customer_id = int(input("Informe o código do cliente: "))
        today = date.today()
        if (not verif_if_customer_exists(customer_id, customer_repository)):
            print("Cliente não existe!")
            continue

        customer = get_customer(customer_id, customer_repository)
        order = Order(id, customer, today)
        order_repository.list_orders.append(order)
    if menu_option == 3:
        formatText = "{0:<10} {1:<20}\n"
        menu = ("***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        print(menu)
    if menu_option == 4:
        formatText = "{0:<10} {1:<20}\n"
        menu = ("***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        print(menu)
    if menu_option == 5:
        formatText = "{0:<10} {1:<20} {1:<20} {1:<20} {1:<20} {1:<20}\n"
        menu = ("***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Ttítulo", "ISBN",
                                  "Autor", "Assunto", "Valor", "Estoque")

        for book in list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        print(menu)
