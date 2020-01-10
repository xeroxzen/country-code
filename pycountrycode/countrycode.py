#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Top-level package for Country Call Code Finder."""

#from sys import argv
import argparse

#import the module containing all the country data.
#Country data not put together within this file for purposes of avoiding clutter

#sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from . countryData import CountryCallingCode
# from countryData import CountryCallingCode

#Details about the author. It'll be a shame to write a module and ship it without
#putting down digital signature.

TTY = False
DATA = CountryCallingCode

#This for loop is for inverting my original country data
#so it can be used for checking a phone code for an unknown state
#country = {value:key for key, value in calling_code.items()} #another way
country = dict((v,k) for k,v in CountryCallingCode.items())

def parse_arguments(arg):
	#handles commandline input
	PROGRAM = "pycountrycode"
	DESCRIPTION = "Displays country code of the specified country."

	parser = argparse.ArgumentParser(
		prog=PROGRAM, description=DESCRIPTION,
		usage='%(prog)s [country]'
	)
	parser.add_argument('country', help="Displays the contry code of a country.",
						nargs='+')
	args = parser.parser_args(arg)
	country_data_list = ' '.join(args.country)
	return country_data_list


def get_list_of_countries():
	return DATA

#first function to determine the phone code of the requested country
def code(state):
	"""
	#Import code to get the telephone code by passing the country name
	
	>>> from pycountrycode import code
	>>> code('Zimbabwe')
	'+263'
	>>> code('New Zealand')
	'+64'
	>>> code('Peru')
	'+51'
	>>> code('Madagascar')
	'+261'
	>>> code('Russia')
	'+7'
	>>> code('Australia')
	'+61'
	>>> code('Israel')
	'+972 '
	>>>
	"""
	phoneCarrier = get_list_of_countries()
	usr_state = state
	if TTY:
		try:
			if usr_state.istitle():
				print('The country code of %s is %s' .format
					(usr_state, phoneCarrier[usr_state]))
			else:
				usr_state = usr_state.title()
				print("The country calling code of %s is %s" .format
					(usr_state, phoneCarrier[usr_state]))
		except:
			print("Please enter a valid country name.")
	else:
		try:
			if usr_state.istitle():
				return phoneCarrier[usr_state]
			else:
				usr_state = usr_state.title()
				return phoneCarrier[usr_state]
		except:
			return 0
	#print(CountryCallingCode.get(name))

#second function to determine the country of the unknown phone code.
def phoneCode(callCode):
	"""
	#Import phoneCode to get country name using the telephone code
	
	>>> from pycountrycode import phoneCode
	>>> phoneCode('+52')
	'Mexico'
	>>> phoneCode('+56')
	'Easter Island'
	>>> phoneCode('+1')
	'United States of America'
	>>> phoneCode('+7')
	'Russia'
	>>> phoneCode('+44')
	'Britain'
	>>> phoneCode('+86')
	'China'
	>>>
	"""
	phoneCarrier = country
	phone = callCode
	if TTY:
		try:
			if phone.istitle():
				print('The country code of %s is %s' .format
					(phone, phoneCarrier[phone]))
			else:
				phone = phone.title()
				print("The country calling code of %s is %s" .format
					(phone, phoneCarrier[phone]))
		except:
			print("Please enter a valid country name.")
	else:
		try:
			if phone.istitle():
				return phoneCarrier[phone]
			else:
				phone = phone.title()
				return phoneCarrier[phone]
		except:
			return 0

#calling my first function.
if __name__ == code:
	code()

#calling my second function.
if __name__ == phoneCode:
	phoneCode()
