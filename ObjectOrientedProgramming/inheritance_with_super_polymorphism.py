class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        return f"2: Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("4: Disconnected.")


class Printer(Device):
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def print(self, pages):
        if not self.connected:
            print("5: Your printer is not connected!")
            return

        print(f"1: printing {pages} pages.")
        self.remaining_pages -= pages

    def disconnect(self):
        print("3: This is a polymorphism...")
        return super().disconnect()

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(50)
