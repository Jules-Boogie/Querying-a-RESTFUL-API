"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Juliet George
Date:   August 10, 2020
"""

import currency

originalCurr = input('3-letter code for original currency: ')
newCurr = input('3-letter code for the new currency: ')
old_amount = float(input('Amount of the original currency: '))

new_amount = round(currency.exchange(originalCurr,newCurr,old_amount),3)

result = 'You can exchange '+str(old_amount)+ ' '+originalCurr+' for '+str(new_amount)+' '+newCurr+'.'
print(result)
