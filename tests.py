"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Juliet George
Date:   August 10, 2020
"""

import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")
    result = currency.before_space("233 EUROS")
    introcs.assert_equals("233", result)
    result = currency.before_space("EUROS  233")
    introcs.assert_equals("EUROS", result)
    result = currency.before_space(" USD")
    introcs.assert_equals("", result)
    result = currency.before_space("55 USD ")
    introcs.assert_equals("55", result)

def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")
    result = currency.after_space("233 USD")
    introcs.assert_equals("USD", result)
    result = currency.after_space("233  USD")
    introcs.assert_equals(" USD",result)
    result = currency.after_space("EURO ")
    introcs.assert_equals("", result)
    result = currency.after_space(" USD 255")
    introcs.assert_equals("USD 255",result)

def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)
    result = currency.first_inside_quotes('A "" D "E F" G')
    introcs.assert_equals('', result)
    result = currency.first_inside_quotes('"123"')
    introcs.assert_equals('123', result)

def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")
    result = currency.get_src('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    result = currency.get_src('{"success": true, "src":"2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
    result = currency.get_src('{"success":false,"src": "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    result = currency.get_dst('{"success": true, "src":"2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    result = currency.get_dst('{"success":false,"src":"","dst": "","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
    result = currency.get_dst('{"success":false,"src": "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")
    result = currency.has_error('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_true(result)
    result = currency.has_error('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)
    result = currency.has_error('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(result)
    result = currency.has_error('{"success": false,"src":"","dst":"","error": "Source currency code is invalid."}')
    introcs.assert_true(result)

def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}',result)
    result = currency.service_response('EUR','USD',-3.5)
    introcs.assert_equals('{"success": true, "src": "-3.5 Euros", "dst": "-3.9485247747366623 United States Dollars", "error": ""}',result)
    result = currency.service_response('EURO','USD',-3.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency EURO is not present."}',result)
    result = currency.service_response('EUR','USDOLLARS',-3.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency USDOLLARS is not present."}',result)

def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")
    result = currency.iscurrency('USD')
    introcs.assert_true(True, result)
    result = currency.iscurrency('USDOLLARS')
    introcs.assert_false(False, result)

def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")
    result = currency.exchange('EUR','USD',2.5)
    introcs.assert_floats_equal(2.8203748390976155,result)
    result = currency.exchange('EUR','USD',-2.5)
    introcs.assert_floats_equal(-2.8203748390976155,result)

test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")
