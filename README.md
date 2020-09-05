# Querying-a-RESTFUL-API
This application is utilizes python to to query a RESTFUL API. The resulting application is a currency converter.


# File Structure

## Test file

The test.py is a unit test script that contains several procedures that test all the functions in the currency module. This file imports introcs and currency modules.
https://github.com/Jules-Boogie/Querying-a-RESTFUL-API/blob/master/tests.py

## Currency 

The currency.py file provides string parsing functions that process the results from querying an online currency service. The functions use assert statements to enforce preconditions for parameters. 
https://github.com/Jules-Boogie/Querying-a-RESTFUL-API/blob/master/currency.py

## Exchange 

The exchangeit.py module is a script that when run, prompts the user to enter an original currency, money amount, and the new currency to convert to.
The user's input is then passed into the exchange function from the currency module and the returned value is saved in a python object.
https://github.com/Jules-Boogie/Querying-a-RESTFUL-API/blob/master/exchangeit.py

## Tools Used
Python 
RestFul API
IntroCS Module
