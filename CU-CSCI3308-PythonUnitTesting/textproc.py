# -*- coding: utf-8 -*-

#Muntaha Pasha
#Chakrya Ros
#CSCI 3308
#Lab 11

"""
A simple module with various Text Processing Capabilities

"""

# Imports

import re

# Exceptions

class TextProcError(Exception):
    """
    Base Class for TextProc Exceptions

    """

    def __init__(self, msg):
        """
        TextProcError Constructor

        :param msg: error message
        :return: TextProcError instance

        """

        super().__init__(msg)

# Public Classes

class Processor:
    """
    Class for Processing Strings

    """

    def __init__(self, text):
        """
        Test Processor Constructor

        :param str text: text string to process
        :return: Processor instance

        """

        if type(text) is not str:
            raise TextProcError("Processors require strings")

        self.text = text

    def __len__(self):
        """
        Length of text

        :return: Length

        """

        return len(self.text)

    def count(self):
        """
        Count number of characters in text

        :return: Length

        """

        return len(self)

    def count_alpha(self):
        """
        Count number of alphabetic characters in text

        :return: Number of alphabetic characters

        """
        #find error
        alpha = re.compile(r'[a-zA-Z]')
        return len(alpha.findall(self.text))

    def count_numeric(self):
        """
        Count number of numeric characters in text

        :return: Number of numeric characters

        """

        alpha = re.compile(r'[1-9]')
        return len(alpha.findall(self.text))

    def count_numeric(self):
        """
        Count number of numeric characters in text

        :return: Number of numeric characters

        """

        alpha = re.compile(r'[1-9]')
        return len(alpha.findall(self.text))

    def count_vowels(self):
        """
        Count number of vowels in text

        :return: Number of vowels

        """
        #find error
        vowels = re.compile(r'[aeoiu]', re.IGNORECASE)
        return len(vowels.findall(self.text))

    def is_phonenumber(self):
        """
        Check if text is a valid US phone number

        :return: True or False

        """
        #find error
        #phonenum = re.compile(r'^[0-9]{3}[\-.]?[0-9]{3}[\-.]?[0-9]{4}$')
        phonenum = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
        if phonenum.match(self.text) is None:
            return False
        else:
            return True
