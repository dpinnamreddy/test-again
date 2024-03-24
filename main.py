# main.py

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

def main():
    # Creating an instance of the Greeter class
    greeter = Greeter("Alice")

    # Calling the greet method
    greeter.greet()

if __name__ == "__main__":
    main()
