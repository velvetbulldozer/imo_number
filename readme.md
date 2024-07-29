# Functions to create and validate IMO numbers

A couple of functions to validate **IMO numbers**. The IMO number of the International Maritime Organization is a generic term covering two distinct meanings. The IMO ship identification number is a unique ship identifier; the IMO company and registered owner identification number is used to identify uniquely each company and/or registered owner managing ships of at least 100 gross tons (gt). The schemes are managed in parallel, but IMO company/owner numbers may also be obtained by managers of vessels not having IMO ship numbers. IMO numbers were introduced to improve maritime safety and reduce fraud and pollution, under the International Convention for the Safety of Life at Sea (SOLAS).

The IMO ship number scheme has been mandatory, for SOLAS signatories, for passenger and cargo ships above a certain size since 1996, and voluntarily applicable to various other vessels since 2013/2017 number identifies a ship and does not change when the ship's owner, country of registry (flag state) or name changes, unlike the official numbers used in some countries, e.g. the UK.

# Validate IMO numbers

An IMO number is made of the three letters "IMO" followed by a seven-digit number. This consists of a six-digit sequential unique number followed by a check digit. The integrity of an IMO number can be verified using its check digit. The checksum of an IMO ship identification number is calculated by multiplying each of the first six digits by a factor of 7 to 2 corresponding to their position from right to left. The rightmost digit of this sum is the check digit.

source: [Wikipedia, IMO number](https://en.wikipedia.org/wiki/IMO_number#IMO_number_of_a_vessel "Info on IMO numbers and their checksum")

# Validate Company IMO numbers

The checksum of an IMO company and registered owner identification number is calculated somewhat differently. The first six digits are multiplied by the respective weights: ''8'', ''6'', ''4'', ''2'', ''9'', and ''7'' and then summed. From this sum modulo 11 is taken. The result of which is subtracted from 11. And modulo 10 of this difference results in the check digit.'

credits to wikipedia user for Company IMO checksum: [Wikipedia, user Gotolulu](https://en.wikipedia.org/wiki/User:Gotolulu "Checksum Company IMO number first published by Gotolulu")

source: [Wikipedia, Company IMO number](https://en.wikipedia.org/wiki/IMO_number#IMO_number_of_a_company "Info on Company IMO numbers and their checksum by user Gotolulu")

# Functions in this repos

- Ability to create however many valid IMO numbers based on the checksum. Output is a list of strings or integers.
- Ability to validate an IMO number.
- Ability to validate a Company IMO number.
