filing_status = int(input("enter filing status (0-single, 1-married joint, 2-married seperate, 3-head of household): "))
taxable_income = float(input("enter taxable income: "))

tax = 0.0

if filing_status == 0: #single filing 
    if taxable_income <= 8350:
        tax = taxable_income * 0.1
    elif taxable_income <= 33950:
        tax = (8350 * 0.1) + ((taxable_income - 8350)*0.15)
    elif taxable_income <= 82250:
        tax = ((8350 * 0.1) + ((33950 - 8350)*0.15)) + ((taxable_income - 33950)*0.25)
    elif taxable_income <= 171550:
        tax = (((8350 * 0.1) + ((33950 - 8350)*0.15)) + ((82250 - 33950)*0.25)) + ((taxable_income - 82250)*0.28)
    elif taxable_income <= 372950:
        tax = ((((8350 * 0.1) + ((33950 - 8350)*0.15)) + ((82250 - 33950)*0.25)) + ((171550 - 82250)*0.28)) + ((taxable_income - 171550)*0.33)
    elif taxable_income > 372950:
        tax = (((((8350 * 0.1) + ((33950 - 8350)*0.15)) + ((82250 - 33950)*0.25)) + ((171550 - 82250)*0.28)) + ((372950 - 171550)*0.33)) + ((taxable_income - 372950)*0.35)
    else:
        print('invalid input')
                       

if filing_status == 1: # married joint filing
    if taxable_income <= 16700:
        tax = taxable_income * 0.1
    elif taxable_income <= 67900:   
        tax = (16700 * 0.1) + ((taxable_income - 16700)*0.15)
    elif taxable_income <= 137050:
        tax = ((16700 * 0.1) + ((67900 - 16700)*0.15)) + ((taxable_income - 67900)*0.25)
    elif taxable_income <= 208850:
        tax = (((16700 * 0.1) + ((67900 - 16700)*0.15)) + ((137050 - 67900)*0.25)) + ((taxable_income - 137050)*0.28)
    elif taxable_income <= 372950:
        tax = ((((16700 * 0.1) + ((67900 - 16700)*0.15)) + ((137050 - 67900)*0.25)) + ((208850 - 137050)*0.28)) + ((taxable_income - 208850)*0.33)
    elif taxable_income > 372950:
        tax = (((((16700 * 0.1) + ((67900 - 16700)*0.15)) + ((137050 - 67900)*0.25)) + ((208850 - 137050)*0.28)) + ((372950 - 208850)*0.33)) + ((taxable_income - 372950)*0.35)
    else:
        print('invalid input')

if filing_status == 2:
    if taxable_income <= 8350:
        tax = taxable_income * 0.1
    elif taxable_income <= 33950:
        tax = (8350 * 0.1)+ ((taxable_income - 8350)*0.15) 
    elif taxable_income <= 68525:
        tax = ((8350 * 0.1)+ ((33950 - 8350)*0.15) )+ ((taxable_income - 33950)*0.25)
    elif taxable_income <= 104425: 
        tax = ((8350 * 0.1)+ ((33950 - 8350)*0.15) + ((68525- 33950)*0.25))+ ((taxable_income - 68525)*0.28)
    elif taxable_income <= 186475:
        tax = (((8350 * 0.1)+ ((33950 - 8350)*0.15) + ((68525- 33950)*0.25))+ ((104425 - 68525)*0.28)) + ((taxable_income-104425)*0.33)
    elif taxable_income > 186475:
        tax = ((((8350 * 0.1)+ ((33950 - 8350)*0.15) + ((68525- 33950)*0.25))+ ((104425 - 68525)*0.28)) + ((186475-104425)*0.33)) + ((taxable_income-186475)*0.35)
    else:
        print('invalid input')

if filing_status == 3: 
    if taxable_income <= 11950:
        tax =  taxable_income * 0.1
    elif taxable_income <= 45500:
        tax = (11950 * 0.1) + ((taxable_income - 11950)*0.15)
    elif taxable_income <= 117450:
        tax = ((11950 * 0.1) + ((45500 - 11950)*0.15)) + ((taxable_income - 45500)*0.25)
    elif taxable_income <= 190200:
        tax = (((11950 * 0.1) + ((45500 - 11950)*0.15)) + ((117450 - 45500)*0.25)) + ((taxable_income - 117450)*0.28)
    elif taxable_income <= 372950:
        tax = ((((11950 * 0.1) + ((45500 - 11950)*0.15)) + ((117450 - 45500)*0.25)) + ((190200 - 117450)*0.28)) + ((taxable_income - 190200)*0.33)
    elif taxable_income > 372950:
        tax = (((((11950 * 0.1) + ((45500 - 11950)*0.15)) + ((117450 - 45500)*0.25)) + ((190200 - 117450)*0.28)) + ((372950 - 190200)*0.33)) + ((taxable_income - 372950)*0.35)
    else:
        print('invalid input') 

print(f'Total tax owed: ${tax:.2f}')

