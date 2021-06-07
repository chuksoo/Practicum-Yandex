# Takeaway Sheet: Retrieving Data from Online Resources

## Practice

```python
# Retrieve information from a webpage using a URL
import requests

req = requests.get(URL)
print(req.text) # printing page contents
print(req.status_code) # printing status code
```

```python
# Search a string for the first substring that matches a regular expression

import re
print(re.search(pattern, string).group())
```

```python
# Split a string into substrings by pattern occurrences
# maxsplit - maximum number of splits, maxsplit=0 by default

import re
print(re.split(pattern, string, maxsplit=num_split))
```

```python
# Find a substring and replace with it repl substring
import re
print(re.sub(pattern, repl, string)) 
```

```python
# Find all matching substrings

import re
print(re.findall(pattern, string))
```

```python
# Generate a tree structure for a webpage

from bs4 import BeautifulSoup
soup = BeautifulSoup(req.text, parser)
```

```python
# Find the first 'tag' tag
# Returns a string with tag, attributes, and contents
# attrs - tag attributes dictionary

tag_content = soup.find(tag, attrs={"attr_name": "attr_value"})
print(tag_content.text) # content without tag
```

```python
# Operations with all tag tags
# attrs - tag attributes dictionary

for tag_content in soup.find_all(tag, attrs={"attr_name": "attr_value"}):
	# do something
```

## Theory

**Web mining** — the process of searching for online resources and retrieving data from them

**HTML** — ****Hypertext Markup Language*,* a language used to create webpages

**HTTP** — transfer protocol used to transmit information online

**HTTPS** — ****a ****secure version of HTTP

**HTML tag** — a hypertext markup language element

**Tag attribute** — a feature that allows fine-tuning when working with tags