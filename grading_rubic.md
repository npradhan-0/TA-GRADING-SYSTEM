# Grading Rubic
The students were asked to write a document with some requirements.

 Students should include:

1. Five different valid integers -- 4 points each. No more than 20 points (Do not count those in email addresses, prices, and phone numbers)
2. Five different decimal numbers -- 4 points each. No more than 20 points (Do not count those in prices)
3. Five different email addresses -- 4 points each. No more than 20 points
4. Five different valid prices -- 4 points each. No more than 20 points
5. Five different valid phone numbers -- 4 points each. No more than 20 points

For example, a student has 6 integers,0 double numbers, 1 email address, 2 prices, and 10 phone numbers.
His grade should be 20 + 0 + 4 + 4*2 + 20 = 52

## Hints:
You can use Python regular expressions to specify the patterns and find the matches. You have to figure out the correct patterns for each category.

## Integers 
Integers are whole numbers. They can be positive or negative.

The following are valid integers:
```
1234
9
-78
```
The following are not valid integers:
```
1a2b3c
nine
3.4
hello
2.5.7
Integers that are included in the email addresses, prices, and phone numbers.
```
## Decimals
The decimals have a whole number and a fractional part separated by a decimal point.

The following are valid decimals:
```
5.6
- 7.00
1.678943578976543
```

The following are not valid decimals:
```
3
-9
4.9.8
decimals in prices
```
## Email address
Capturing all the rules for what makes a valid email address is complex,
so we will use a simplified definition of a valid email address. 
This definition generally works just fine for extracting email addresses from documents.

The first part of the email address is the username portion, 
and it must not contain whitespace or the @ symbol. 
The username portion is followed by the @ symbol. 
After the @ symbol is the domain, which does not contain any whitespace or the @ symbol. 
The domain contains two or more non-empty components which are separated by periods. 
The final component must consist of only letters from the English alphabet.
The following are valid email addresses:
```
nsommer@wooster.edu
n.sommer@cs.wooster.edu
yippee_skippy@yee-haw.wheeeee
fun-times@Taylor.hall.wooster.edu
```
The following are not valid email addresses:
```
n@sommer@wooster.edu
n sommer@wooster.edu
nsommer@wooster..edu
nsommer@wooster.edu-org
```
## Price
Here, a valid price is a numeric value using the US dollar sign. 
The number of cents is optional, but there must be two digits if 
the cents are shown. For prices above $999.99, there may optionally 
be a comma separating thousands, millions, etc.

The following are valid prices:
```
$1
$20
$1.99
$10.00
$1500.50
$2,000.99
$1,234,567.89
```
The following are not valid prices:
```
$1.9
$10,23.4
```
## Phone Number
Here, a phone number is a valid US phone number with the area code (you don't have to check whether the area code is real or not). 
The final 7 digits must be separated by a hyphen, while the area code 
may be in parentheses or separated from the rest of the number by a hyphen. 
There may or may not be a single space between the closing parentheses and the fourth number.

The following are valid phone numbers:
```
(330) 263-2000
(330)263-2000
123-456-7890
```
The following are not valid phone numbers:
```
(123)4567890
456-7890
330 263-2000
```

