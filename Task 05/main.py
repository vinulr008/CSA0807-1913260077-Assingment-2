def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


def calculate_bill(items, gst_rate=0.05):
    total = sum(items)
    gst = total * gst_rate
    return total, gst


def customer_order(customer, item, quantity=1):
    return f"{customer} ordered {quantity} {item}(s)"


print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))

print(add_item_buggy.__defaults__)

customer1 = add_item("Tea", [])
customer1 = add_item("Vada", customer1)

customer2 = add_item("Coffee", [])
customer3 = add_item("Juice", [])

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)

print(customer_order("Arun", "Tea"))
print(customer_order(customer="Bala", item="Coffee", quantity=2))

total, gst = calculate_bill([20, 30, 40])

print("Total:", total)
print("GST:", gst)
print("Final amount:", total + gst)


college_name = "SIMATS"


def show_local():
    message = "Local variable"
    print(message)
    print(college_name)


def change_global():
    global college_name
    college_name = "SIMATS Engineering"


show_local()
change_global()

print(college_name)


def outer_function():
    count = 0

    def inner_function():
        nonlocal count
        count += 1
        return count

    print(inner_function())
    print(inner_function())


outer_function()
