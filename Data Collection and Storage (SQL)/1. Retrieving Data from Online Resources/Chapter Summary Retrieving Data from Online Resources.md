# Chapter Summary: Retrieving Data from Online Resources

## What's Web Mining?

Sometimes you might not be given enough data to conduct a thorough analysis. In such cases, it's necessary to do further research. This allows you to take more factors into account, identify more patterns, and reach unexpected conclusions. Analysts can enrich their data by supplementing it with data from the internet. First they track down resources that might be relevant, then they retrieve all the necessary data. This process is called **web mining**, ****or **parsing.** 

## Things an Analyst Needs to Know About the Internet. Browsers. HTML. HTTP

The internet is a network of computers exchanging data. It has rules for *exchanging and representing information on the internet (taking into account the way computers display it).* To make this happen, several things were invented:

1. A language for creating documents: **HTML**
2. Software applications for viewing such documents: **browsers**
3. General rules for transferring documents: **HTTP**

## Transfer Protocols

For the process of exchanging data to work, there need to be certain rules that govern how one computer sends data to another. Data exchange on the internet is based upon the "request-response" principle: a browser generates a request, then the server analyzes it and sends back a reply. The rules for formulating requests and responses are determined by what's known as a transfer protocol—in this case, HTTP.

The majority of websites today use a security-enhanced data transfer protocol called **HTTPS**. This protocol ensures that all communication between your browser and a website is encrypted.

When you access a website, your browser sends an HTTP request to the server. The server, in turn, formulates a reply: the HTML code for the relevant page. A request formed by a browser may include the following:

- An HTTP method: determines the operation that needs to be carried out. There are several methods, the most popular being GET and POST. The former requests data from the server, while the latter sends them.
- Path: the segment of the address following the name of the site (in *[example.com/hello](http://example.com/hello)* the path is /*hello)*.
- The version of the HTTP protocol used to send the request (e.g. HTTP/1.1).
- Request headers, which are used to send additional information to the server.
- Request body. For example, the body of a POST request is the data that is sent. Not every request has a body.

The reply may include:

- The HTTP version.
- The reply's code and message (e.g. "200 OK" if everything goes smoothly, or "404 Not Found" if the requested path cannot be found).
- Headers containing additional information for the browser.
- Reply body (e.g., when you open the website, you will see the HTML code for this page in the reply body).

## Introduction to HTML

To export a list of goods from an online store's website, you'll first need to get the page's code and its content.

With HTML each object on the page has to be marked up in order to display correctly. This marking-up involves placing blocks of information within commands called "tags." These tags tell browsers how to display the information they surround.

An HTML element is composed of *tags* and the *content* contained within them. An HTML tag consists of a name surrounded by angle brackets. An element begins with an *opening tag* with the name of the tag and ends with a *closing tag* with a slash and the name of the tag. The element is referred to by the name of the tag. 

Here's the typical structure of an HTML page:

### 1. <html> ... </html>

The **<html>** tag introduces each HTML document and indicates its beginning, while **</html>**  marks its end. The **<head>** and **<body>** of the HTML document are found between these tags.

### 2. <head> ... </head>

These tags mark the document's heading. Tags introducing the document's title (**<title>)** and meta (additional) information (**<meta>**) are placed between these tags.

### 3. <body> ... </body>

The **<body>** tag marks the beginning of the body of an HTML page. All the contents of the page (headings, text paragraphs, tables, images) are placed within the body.

To make the markup clearer, developers leave comments inside special tags `<!-- -->`  in the page's code. This is very helpful for analysts, and we'll be leaving comments in code in our examples.

Analysts often parse tables. These are usually placed in *table* elements, between `<table>`   and `</table>` tags. The opening `<table>` tag marks the beginning of a table, and the closing `</table>` tag marks its end. Within this element, the contents of the table are divided into rows by `<tr>` (table row) tags, and rows, in turn, are divided into cells by `<td>` **(**table data) tags. The first row usually contains column headings instead of regular cells. They're placed between `<th>` (table heading) tags. 

Text is often placed within a *p* (paragraph) element. The beginning of the paragraph is marked by the  `<p>` tag and the end by the  `</p>` tag.

The `<div>` (division) block tag, which can wrap various elements, is quite common. *div* is useful since it can incorporate any number of elements, even of different kinds (e.g. a header with an image plus a couple of text paragraphs), and assign them common features or behavior. 

You can also put **attributes** inside the brackets to provide more information as to how the element should behave. Different types of information require different attributes.

The name of the attribute tells the browser what feature the attribute concerns, while the value specifies what should happen to the feature. Most often, you'll need to work with the `id` and `class` attributes. The *id* attribute provides a unique identifier for an element. The value of the *class* attribute is a name that several elements can share, just as multiple family members share one last name.

## Developer Tools

Every modern browser has a **web developer toolbar**, a Swiss Army knife for any developer. Here you can look at the code of an entire page or a particular element, see the style of each element on the page, and even change how they display on your computer. You can access it by pressing Control+Shift+i.

## Your First GET Request

To get data from the server, we'll use the **get()** method, and to send HTTP requests, we need the **Requests** library. We import the library:

```python
import requests
```

The *get()* method acts like a browser. We'll pass it the link as an argument. The method will send the server a GET request, then process the reply it receives and return a **response,** an object that contains the server's response to the request.

```python
req = requests.get(URL) # saving response object as req variable
```

A *response* object contains the server's reply: the status code, the contents of the request, and the code of the HTML page itself. The attributes of *response* objects make it possible to get only the data that's relevant from the server. For example, a *response* object with the *text* attribute will only return the text content of the request: 

```python
print(req.text) # the name of the attribute is placed after the response object and divided from it by period
```

The *status_code* attribute tells you whether the server responded or an error occurred.  

```python
print(req.status_code)
```

Unfortunately, not all requests come back with data. Sometimes requests return errors; each has a special code depending on its type. Here are the most common errors:

[Error codes](https://www.notion.so/a30fc411c37b4a348e4d7cdf4b71b061)

## Regular Expressions

To search for strings in big texts you will need a powerful tool, regular expressions. A **regular expression** is a rule for searching for substrings (fragments of text within strings). It is possible to create complex rules so that one regular expression returns several substrings. 

To start working with regular expressions in Python, we need to import the *re* (i.e. regular expressions) module. Two stages follow.

In the first stage, we create the pattern of the regular expression. This is an algorithm describing what should be searched for within text (e.g. all capital letters). 

Then this pattern is passed to the specific methods from `re`. These methods search for, replace, and remove symbols. In other words, the pattern identifies what to search for and how, while the method defines what to do with the matches that are found.

The following table lists the simplest regular expression patterns. You can create more intricate regular expressions by combining them.

[Regular expression syntax](https://www.notion.so/058ed9a68a954151accf719810f1e1e2)

The most common tasks for analysts include:

- finding a substring within a string
- breaking strings into substrings
- replacing parts of a string with other strings

To complete these tasks, you'll need the following `re` methods:

1. **search(pattern, string)** searches for a `pattern` in a `string`*.* Although `search()` runs through the whole string to find the pattern, it only returns the first substring it finds: 

```python
import re
print(re.search(pattern, string))
```

The `search()` method returns a **match** type object. The `span` parameter defines a range of indices matching the pattern. The match parameter indicates the value of the substring itself. 

If we don't need information about the span, we can return just the substring using the `group()` method:

```python
import re
print(re.search(pattern, string).group())
```

2. **split(pattern, string)** breaks up ****a `string` at points where the `pattern` **appears. 

```python
import re
print(re.split(pattern, string))
```

The string is split wherever the pattern is found. The number of splits can be controlled by means of the `split()` method's **maxsplit** parameter.

```python
import re
print(re.split(pattern, string, maxsplit = num_split))
```

3. **sub(pattern, repl, string)** searches for the `pattern` **substring within a **`string` **and replaces it with the ****repl** (i.e. replace) substring. **

```python
import re
print(re.sub(pattern, repl, string)) 
```

4. **findall(pattern, string)** returns a list of all substrings in a `string` that match the `pattern`*.* Compare it with the `search()` method, which only returns the first matching substring*.*

```python
import re
print(re.findall(pattern, string))
```

**findall()** method is particularly useful in that it allows you to determine the number of recurrent substrings in a string with the `len()` **function:

```python
import re
print(len(re.findall(pattern, string)))
```

## HTML Parsing

Extracting pure data values from a string containing a page's code manually can be difficult. To resolve this we will need **BeautifulSoup** library. BeautifulSoup library methods turn an HTML file into a tree structure. Then the necessary content can be found by tags and attributes. 

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')
```

The first argument presents data that will form a tree structure. The second argument is a syntactic analyzer, or parser. It defines the way a web-page turns intro the tree. There are numerous parsers, and they all make different structures out of one and the same HTML document. We have chosen **lxml** analyzer for its high speed performance. But, of course, there are other analyzers, like  html.parser, xml, and html5lib. 

After the code is turned into a tree structure, the data can be searched using various methods. The first search method is called **find()**. It runs through an HTML document and finds the first element which name was passed as an argument and returns it together with tags and its content. 

```python
tag_content = soup.find(tag)
```

To display the content without tags, you will need the **text** method. It will return the result in the form of a string:

```python
tag_content.text
```

There is still another search method, that is **find_all.** As opposed to the previous method, `find_all()` finds *all* the instances of a given element in an HTML document an returns a list:

```python
tag_content = soup.find_all(tag)
```

Let's extract only the content from paragraphs with the help of *text* method: 

```python
for tag_content in soup.find_all(tag):
    print(tag_content.text)
```

`find()` and `find_all()` methods have an extra filter for searching for page elements: the **attrs** (attributes) parameter*.* It is used for searching by classes and identifiers. Their names are specified on the web developer tools panel.

You need to pass `attrs` a dictionary with attribute names and values:

```python
soup.find(tag, attrs={"attr_name": "attr_value"})
```

# API

Sometimes you need to request information from external sources whose structure is much more complicated than that of an ordinary HTML page. To avoid having to study their structure to get data faster, analysts send GET requests to third-party applications through a special data transfer interface called an **API** (Application Programming Interface)*.* 

The requests library allows you to pass parameters to a URL. When you search for certain content on a multi-page website, you need to pass the PARAM dictionary to the keyword **params** (parameters). For example:

```python
URL = 'https://yandex.com/'
PARAM={"page": "4"}
req = requests.get(url = URL, params = PARAM)
```

This request should return the fourth page (according to the catalogue) of the website [https://yandex.com/](https://yandex.ru/). 

# JSON

When responding to your request, the server returns structured data in one of several special formats, the most common of which is **JSON** (JavaScript Object Notation)**.** It looks like a jumble of digits, letters, colons, and curly brackets. 

Here's how data in this format looks:

```json
[
  {
    "name": "General Slocum",
    "date": "June 15, 1904" 
  },
  {
    "name": "Camorta",
    "date": "May 6, 1902"
  },
  {
    "name": "Norge",
    "date": "June 28, 1904"
  }
]
```

If JSON includes several elements, they are written in square brackets `[ ... ]`, just as in lists. An individual JSON object looks like a dictionary: it's bounded by curly brackets and has `key : value` pairs. 

JSON lets you gather data within an object (a list of `key : value` pairs) and then make a string out of it to be passed in a request. The receiver turns this string back into an object. 

Python has a built-in module for working with data in JSON format:

```python
import json
```

Its method **json.loads()** converts strings that are in JSON format:

```python
x = '{"name": "General Slocum", "date": "June 15, 1904"}'
y = json.loads(x)

print('Name : {0}, date : {1}'.format(y['name'], y['date']))
```

```python
# Response
Name : General Slocum, date : June 15, 1904
```