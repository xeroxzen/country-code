# PyCountryCode documentation!

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

### Importing the 'getCode' function
```sh
>>> from pycountrycode.countrycode import getCode
>>> getCode('Zimbabwe')
'+263'
>>> getCode('New Zealand')
'+64'
>>> getCode('Peru')
'+51'
>>> getCode('Madagascar')
'+261'
>>> getCode('Russia')
'+7'
>>> getCode('Australia')
'+61'
>>> getCode('Israel')
'+972'
>>> getCode('Mal')
'Undefined country'
```

### Importing the 'getCountry' function.
```sh
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
>>> getCountry('+3')
'Undefined country code'
>>> getCountry('+2')
'Undefined country code'
>>> getCountry('+27')
'South Africa'
```
### Package Information
```sh
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
```sh
>>> from pycountrycode.countrycode import getCode, getCountry
>>> getCode('Botswana')
'+267'
>>> getCountry('+33')
'France'
>>> 
```

