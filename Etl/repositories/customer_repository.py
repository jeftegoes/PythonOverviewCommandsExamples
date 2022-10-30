from entities.customer import Customer


class CustomerRepository:
    def __init__(self) -> None:
        self.list_customers: list[Customer] = []
