
operation_history = []
def show_menu():
    print("""
Dostępne operacje: 
dz - dzielenie
m - mnożenie
d - dodawanie
o - odejmowanie 
   """)

def get_user_data():
    good_value = False
    while not good_value:
        try:
            first_number = float(input("Podaj pierwszą liczbe: "))
            second_number = float(input("Podaj drugą liczbe: "))
            print(f"Podałeś {first_number} i {second_number}")
            good_value = True
        except ValueError:
            print("Podana wartość musi być liczbą")
    return first_number , second_number

def add(a,b):
    addition = a + b
    result = f"{a} + {b} = {addition}"
    operation_history.append(result)
    print(result)
def div(a,b):
    if b == 0:
        print("Nie można dzielić przez zero!")
    else:
        divide = a / b
        result = f"{a} / {b} = {divide}"
        operation_history.append(result)
        print(result)
def multi(a,b):
    multiply = a * b
    result = f"{a} * {b} = {multiply}"
    operation_history.append(result)
    print(result)
def subs(a,b):
    subtraction = a - b
    result = f"{a} - {b} = {subtraction}"
    operation_history.append(result)
    print(result)
def save_file(a):
    file_path = "C:/Users/Oliwia/Desktop/operationHistory.txt"
    with open(file_path, "w") as file:
        file.write(a)
def operation_system():
    end_program = False
    while not end_program:
        numbers = get_user_data()
        first_number = numbers[0]
        second_number = numbers[1]
        show_menu()

        user_operation = input("Jaką operacje chcesz wykonać ? ").lower()

        if user_operation == "dz":
           div(first_number, second_number)
        elif user_operation == "m":
            multi(first_number,second_number)
        elif user_operation == "d":
            add(first_number, second_number)
        elif user_operation == "o":
            subs(first_number, second_number)
        else:
            print("Nieznana operacja!")

        try:
            more_calc = int(input("Czy chcesz wykonać nowe obliczenie ? \n 1 - Tak \n 2 - Nie \n"))
            if more_calc == 2:
                print("Historia obliczeń: ")
                for operation in operation_history:
                    print(operation)
                res = '\n'.join(operation_history)
                save_file(res)
                end_program = True
        except ValueError:
            print("Nieprawidłowa odpowiedź, kończę program.")
            end_program = True


operation_system()
