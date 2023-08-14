#--------------------------------------------------------------------------------------------------------------------------
#Student Name: Jenesis Fabia
#Course: CIT 134A
#Term/Year: Fall 2022
#Date: 10/2/2022
#Project Number: 2
#--------------------------------------------------------------------------------------------------------------------------

# Main Program
import Project2Functions #imports Project2Functions file to main program

def main():
    Project2Functions.display_title()
    again = 'y'
    while again == 'y' or again == 'Y':
        items_total = Project2Functions.get_all_items_total()   
        print('All items total: ${:.2f}'.format(items_total)) # Cost of items  
        print()
        sales_tax_rate = int(input("Sales tax rate (%): "))
        while sales_tax_rate < 6 or sales_tax_rate > 10:
            print("Tax rate should be from 6 to 10")
            sales_tax_rate = int(input("Sales tax rate (%): "))
        promotion_code = int(input("Promotion Code: "))
        while promotion_code != 123 and promotion_code != 456 and promotion_code != 789 and promotion_code != 0:
            print("Invalid promotion code. Try again")
            promotion_code = int(input("Promotion Code: "))
        print()
        discount_amount = Project2Functions.get_discount(items_total , promotion_code)
        subtotal = items_total - discount_amount
        sales_tax = Project2Functions.get_sales_tax(subtotal , sales_tax_rate)
        grand_total = subtotal + sales_tax
        # Output of Users Input
        print('Discount amount: ${:.2f}'.format(discount_amount)) # Discount from promotion code
        print('Subtotal: ${:.2f}'.format(subtotal)) # Subtotal after All items total and promotion code
        print('Sales tax amount: ${:.2f}'.format(sales_tax)) # Tax
        print('Grand total: ${:.2f}'.format(grand_total)) # The final price
        print()
        again = input("Continue? y/Y/n/N: ")

main()        
    
