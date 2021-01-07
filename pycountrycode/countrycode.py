#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Top-level package for Country Call Code Finder."""

#from sys import argv
import argparse

#import the module containing all the country data.
#Country data not put together within this file for purposes of avoiding clutter

#sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from . country_data import country_calling_code
# from countryData import CountryCallingCode

#Details about the author. It'll be a shame to write a module and ship it without
#putting down digital signature.

TTY = False
DATA = country_calling_code

#This for loop is for inverting my original country data
#so it can be used for checking a phone code for an unknown state
#country = {value:key for key, value in calling_code.items()} #another way
country = dict((v,k) for k,v in country_calling_code.items())

def parse_arguments(arg):
	#handles commandline input
	PROGRAM = "pycountrycode"
	DESCRIPTION = "Displays country code of the specified country."

	parser = argparse.ArgumentParser(
		prog=PROGRAM, description=DESCRIPTION,
		usage='%(prog)s [country]'
	)
	parser.add_argument('country', help="Displays the country code of a country.",
						nargs='+')
	args = parser.parser_args(arg)
	country_data_list = ' '.join(args.country)
	return country_data_list


def get_list_of_countries():
	return DATA

#first function to determine the phone code of the requested country
def get_code(state):
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
			return 'Undefined country'
	#print(CountryCallingCode.get(name))

#second function to determine the uknown country of the passed in phone code.
def getCountry(callCode):
	"""
	#Import getCountry to get country name using the telephone code

	>>> from pycountrycode.countrycode import getCountry
	>>> getCountry('+52')
	'Mexico'
	>>> getCountry('+56')
	'Easter Island'
	>>> getCountry('+1')
	'United States of America'
	>>> getCountry('+7')
	'Russia'
	>>> getCountry('+44')
	'Britain'
	>>> getCountry('+86')
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
			return 'Undefined country code'

#calling my first function.
if __name__ == get_code:
	get_code()

#calling my second function.
if __name__ == getCountry:
	getCountry()
