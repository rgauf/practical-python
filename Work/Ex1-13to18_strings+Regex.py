# Ex 1.13-18 strings
# for 1.17 -- f-strings -- see Ex1.7_mortgages

#Ex 1.13-15 string manipulation and searching
print(' >> set up the string')
text = 'AAPL,IBM,MSFT,YHOO,SCO'
print(text)
print(text[0])
print(text[-2])
text += 'GOOG'
print(text)
text = text.replace('COGO','CO,GO')
print(text)
text = 'HPQ,' + text
print(text)

print(' >> string pieces')
print('IBM' in text)
print('MM' in text)
print('M,M' in text)
print(text.find('IBM'))
print(text.find('MM'))
print(text.find('M,M'))
print(text.find('S'))
print(text.rfind('S'))
print(text.count('S',14,23))
print(text.count('S',14,24))
print(text[14:23])
print(text[14:23+1])

print(' >> adjust string')
print(text.lower())
print(text.title())
print(text.isalpha())
print(text.replace(',','').isalpha())
print(text.split(','))

# Ex1.18 regex
# regex search and replace in strings.  MUST ALWAYS "import re", isn't a default pkg
import re
text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
print(' >> regex examples for:', text)
# Find if there is a date >> digits slash digits slash digits
if (re.search(r'\d+/\d+/\d+',text)):
    print('ok')
    print(re.search(r'\d+/\d+/\d+',text))
# Find all occurrences of a date
print(re.findall(r'\d+/\d+/\d+', text))
# >>> ['3/27/2018', '3/28/2018']
# Replace all occurrences of a date, reformatted as part 3 dash part 1 dash part 2
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# >>> 'Today is 2018-3-27. Tomorrow is 2018-3-28.'
