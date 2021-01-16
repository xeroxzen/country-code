#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Top-level package for Country Call Code Finder."""

# from sys import argv
import argparse

# import the module containing all the country data.
# Country data not put together within this file for purposes of avoiding clutter

# sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from typing import Dict, Any, Union

from .country_data import country_calling_code

# from countryData import CountryCallingCode

# Details about the author. It'll be a shame to write a module and ship it without
# putting down digital signature.

TTY = False
DATA: Dict[Union[str, Any], Union[str, Any]] = country_calling_code

# This for loop is for inverting my original country data
# so it can be used for checking a phone code for an unknown selected_country
# country = {value:key for key, value in calling_code.items()} #another way
country = dict((v, k) for k, v in country_calling_code.items())


def parse_arguments(arg):
	# handles commandline input
	program = "pycountrycode"
	description = "Displays country code of the specified country."

	parser = argparse.ArgumentParser(
		prog=program, description=description,
		usage='%(prog)s [country]'
	)
	parser.add_argument('country', help="Displays the country code of a country.", nargs='+')
	args = parser.parser_args(arg)
	country_data_list = ' '.join(args.country)
	return country_data_list


def get_list_of_countries():
	return DATA


# first function to determine the phone code of the requested country
def get_code(selected_country):
	"""
	#Import get_code to get the telephone code by passing the country name

	>>> from pycountrycode.countrycode import get_code
	>>> get_code('Zimbabwe')
	'+263'
	>>> get_code('New Zealand')
	'+64'
	>>> get_code('Peru')
	'+51'
	>>> get_code('Madagascar')
	'+261'
	>>> get_code('Russia')
	'+7'
	>>> get_code('Australia')
	'+61'
	>>> get_code('Israel')
	'+972 '
	>>>
	"""
	phone_carrier = get_list_of_countries()
	nation = selected_country
	if TTY:
		try:
			if nation.istitle():
				print('The country code of %s is %s'.format(nation, phone_carrier[nation]))
			else:
				nation = nation.title()
				print("The country calling code of %s is %s".format(nation, phone_carrier[nation]))
		except:
			print("Please enter a valid country name.")
	else:
		try:
			if nation.istitle():
				return phone_carrier[nation]
			else:
				nation = nation.title()
				return phone_carrier[nation]
		except:
			return 'Undefined country'


# print(CountryCallingCode.get(name))

# second function to determine the unknown country of the passed in phone code.
def get_country(call_code):
	"""
	#Import get_country to get country name using the telephone code

	>>> from pycountrycode.countrycode import get_country
	>>> get_country('+52')
	'Mexico'
	>>> get_country('+56')
	'Easter Island'
	>>> get_country('+1')
	'United States of America'
	>>> get_country('+7')
	'Russia'
	>>> get_country('+44')
	'Britain'
	>>> get_country('+86')
	'China'
	>>>
	"""
	phone_carrier = country
	phone = call_code
	if TTY:
		try:
			if phone.istitle():
				print('The country code of %s is %s'.format(phone, phone_carrier[phone]))
			else:
				phone = phone.title()
				print("The country calling code of %s is %s".format(phone, phone_carrier[phone]))
		except:
			print("Please enter a valid country name.")
	else:
		try:
			if phone.istitle():
				return phone_carrier[phone]
			else:
				phone = phone.title()
				return phone_carrier[phone]
		except:
			return 'Undefined country code'


# calling my first function.
if __name__ == get_code:
	get_code()

# calling my second function.
if __name__ == get_country:
	get_country()
