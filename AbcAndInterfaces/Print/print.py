from print_interface import PrintInterface


class Print(PrintInterface):
    def print_standard(self):
        print("Method in print class.")

    def print_name(self, name: str):
        print(f'Method in iPrint with this parameter in input: {name}.')

    def print_generic(self):
        print('Method in iPrint.')
