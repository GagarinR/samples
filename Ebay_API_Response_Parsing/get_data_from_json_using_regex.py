# import regex
import json
import re
regex101 = 'https://regex101.com/r/wzlKXr/1'
with open('ebay_json.txt', encoding='utf-8') as f:
	text = f.read().encode('utf-8')
	text = str(text).replace('\\\'', "'")

pattern_title = r"'title': \[\'(.*?)\'\]"
pattern_value = r"'__value__': \'(.*?)\'"
titles = re.findall(pattern_title, text)
values = re.findall(pattern_value, text)
a = dict(zip(titles, values))
print(a)
