vat_rate = int(input("What's the VAT rate? Enter in whole number. "))
vat_rate = vat_rate / 100

option = input("Would you like to *add* or *remove* VAT? ")
original_price = float(input("What's the original price? "))
if option == "add":
    ex_vat_price = original_price
    vat_price = original_price * (1 + vat_rate)
    vat = vat_price - ex_vat_price
else:
    vat_price = original_price
    ex_vat_price = vat_price / (1 + vat_rate)
    vat = vat_price - ex_vat_price

print("Price before VAT is: ", ex_vat_price)
print("VAT charged: ", vat)
print("Price after VAT is: ", vat_price)