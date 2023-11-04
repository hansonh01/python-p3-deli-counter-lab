katz_deli = []

def line(katz_deli):
    if katz_deli == []:
        print(f"The line is currently empty.")
    else:
        status = "The line is currently:"
        for num,name in enumerate(katz_deli,start=1):
            status += f" {num}. {name}"
        print(status)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")
    

def now_serving(katz_deli):
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = katz_deli.pop(0)
        print(f"Currently serving {serving_customer}.")
    
