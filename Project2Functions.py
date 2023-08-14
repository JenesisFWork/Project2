#--------------------------------------------------------------------------------------------------------------------------
#Student Name: Jenesis Fabia
#Course: CIT 134A
#Term/Year: Fall 2022
#Date: 10/2/2022
#Project Number: 2
#--------------------------------------------------------------------------------------------------------------------------

# Display a welcome message
def display_title():
    print ("Department Store Sales Tax and Grand Total Application")
    print ()
    
def get_all_items_total():
    total = 0
    cost = []
    #Tells User how to end input by pressing "0"
    print("Data Entries: Enter 0 to end your input") 
    # Users Input
    cost_of_item = float(input("Cost of item:"))
    while cost_of_item != 0:
        total = total + cost_of_item
        cost_of_item = float(input("Cost of item:"))
    return total    
    
def get_discount(total , promo_code):
    if total >= 100:
        discount = 0.10 * total
    elif promo_code == 123:
        discount = 1
    elif promo_code == 456:
        discount = 2
    elif promo_code == 789:
        discount = 3
    else:
        discount = 0
    return discount  
    
def get_sales_tax(subtotal , tax_rate):
    tax = subtotal * (tax_rate / 100)
    return tax