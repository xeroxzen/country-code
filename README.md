## PyCountryCode documentation!

### What it is?
I have always loved knowing stuff. I love knowledge, it is my first love before anything else. In every kind of setup I find myself in I am always participating because I almost always have an idea about most things. This love of knowledge also made it easy for me to know more country telephone codes.

However, the truth is I couldn't cram them all the country codes and retrieve them from my mind every time it became necessary. I knew by heart those of the most popular countries that includes Russia (+7), UK (+44), USA (+1), Australia (+61) and of course Zimbabwe amongst many others.

### Why?
Someone wanted to know what code +52 was for which country, I didn't know, I was embarrassed at myself. I challenged myself by writing this package so I and anyone else can use to get the country calling code of any country and also to get a country after passing in a calling code you know but are not sure about the country of origin.

### Inspiration
I wanted to write something that others could find useful.


### Installation
```sh
$ pip install pycountrycode
```
### Use as per environment
```sh
Terminal
$ pip3 install pycountrycode
$ python3
>>> 
```

```sh
Windows Command Prompt
C:\Users\Andile Xeroxzen> pip install pycountrycode
C:\Users\Andile Xeroxzen> python
>>> 
```

### Importing the 'get_code' function
```python
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
'+972'
>>> get_code('Mal')
'Undefined country'
```

### Importing the 'get_country' function.
```python
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
>>> get_country('+3')
'Undefined country code'
>>> get_country('+2')
'Undefined country code'
>>> get_country('+27')
'South Africa'
```
### Package Information
```python
>>> import pycountrycode
>>> pycountrycode.__author__
'Andile Jaden Mbele'
>>> pycountrycode.__email__
'andilembele020@gmail.com'
>>> pycountrycode.__github__
'www.github.com/xeroxzen/pycountrycode'
>>> pycountrycode.__package__
'pycountrycode'
>>>
```

### Also
```python
>>> from pycountrycode.countrycode import get_code, get_country
>>> get_code('Botswana')
'+267'
>>> get_country('+33')
'France'
>>> 
```

