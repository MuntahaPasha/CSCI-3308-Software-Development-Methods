#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Muntaha Pasha
# Chakrya Ros


#Bugs
#count 0, alpha 2, numberic 1, vowels has 1, phone has 2
#The bug in count alpha is that the code desn't count the capital letters.
#The Bug in count numberic is that it doesn't count the number 0
#The bug in vowels is that it is not counting i's.
#The bugs in phone numbers are that it's not counting 0's or looking for a missing last digit in the last 4 digits of the phonenumber. 

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    #question  1
    def test_string(self):
        text = "testing_string"
    #question 2
    def test_count(self):
        text = "ABCdef"
        pro = textproc.Processor(text)
        self.assertEqual(pro.count(), 6, "'text' does not match input")
    #question3
    def test_count_alpha(self):
        text = "abdFg123"
        pro = textproc.Processor(text)
        self.assertEqual(pro.count_alpha(), 5,"'text' does not match input")
    #question4
    def test_count_numeric(self):
        text = "adf123"
        pro = textproc.Processor(text)
        self.assertEqual(pro.count_numeric(), 3, "'text' does not match input")
     #question5
    def test_count_vowels(self):
        text = "cuboulderis"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 5,"'text' does not match input")
    #question6
    def test_is_phonenumber(self):
        phone_number1 = textproc.Processor("303-345-5695")
        phone_number2 = textproc.Processor("3033455554")
        phone_number3 = textproc.Processor("(303) 345-3695")
        bad_Number = textproc.Processor("so1r-mkt-29sk")
        self.assertEqual(True,phone_number1.is_phonenumber(), "expected '303-3453695' to be valid phone number")
        self.assertEqual(True, phone_number2.is_phonenumber(), "expected '3033453695' to be valid phone number")
        self.assertEqual(True, phone_number3.is_phonenumber(), "expected '(303) 345-3695' to be valid phone number")
        self.assertEqual(False, bad_Number.is_phonenumber(), "expected 'so1r-mkt-29sk' to NOT be valid phone number")

    # Add Your Test Cases Here...

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()