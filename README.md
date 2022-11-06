# Python overview, commands and examples <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Python overview](#1-python-overview)
  - [1.1. Brief History of Python](#11-brief-history-of-python)
  - [1.2. Why Choose Python?](#12-why-choose-python)
  - [1.3. What can you do with Python?](#13-what-can-you-do-with-python)
- [2. Python Object and Data Structure Basics](#2-python-object-and-data-structure-basics)
  - [2.1. Basic Data Types](#21-basic-data-types)
  - [2.2. Numbers](#22-numbers)
  - [2.3. Variable Assignments](#23-variable-assignments)
    - [2.3.1. Dynamic Typing](#231-dynamic-typing)
  - [2.4. Strings](#24-strings)
    - [2.4.1. String Formatting for Printing](#241-string-formatting-for-printing)
  - [2.5. List and Dictionaries](#25-list-and-dictionaries)
    - [2.5.1. List](#251-list)
    - [2.5.2. Dictionaries](#252-dictionaries)
    - [2.5.3. Dictionaries or List?](#253-dictionaries-or-list)
  - [2.6. Tuples](#26-tuples)
  - [2.7. Sets](#27-sets)
  - [2.8. Booleans](#28-booleans)
  - [2.9. Files](#29-files)
  - [2.10. Resume](#210-resume)
- [3. Python Statements](#3-python-statements)
  - [3.1. If, Elif, Else Statements](#31-if-elif-else-statements)
  - [3.2. For Loops](#32-for-loops)
  - [3.3. While Loops](#33-while-loops)
  - [3.4. List Comprehensions](#34-list-comprehensions)
- [4. Methods and Functions](#4-methods-and-functions)
  - [4.1. Function](#41-function)
- [5. Object Oriented Programming](#5-object-oriented-programming)
- [6. Modules and Packages](#6-modules-and-packages)
  - [6.1. Pip](#61-pip)
  - [6.2. Own Modules and Packages](#62-own-modules-and-packages)
- [7. Errors and Exception Handling](#7-errors-and-exception-handling)
- [8. Decorators](#8-decorators)
- [9. Generators](#9-generators)
- [10. Web Scraping](#10-web-scraping)
  - [10.1. Rules of Web Scraping](#101-rules-of-web-scraping)
  - [10.2. Limitations of Web Scraping](#102-limitations-of-web-scraping)
  - [10.3. Basic HTML and CSS](#103-basic-html-and-css)
  - [10.4. How to scrape](#104-how-to-scrape)
- [11. Commands](#11-commands)

# 1. Python overview

## 1.1. Brief History of Python

- Created in 1990 by Guido van Rossum.
- Python 3 released in 2008.
- Specifically designed as an easy to use language.
- High focus on readability of code.
- Focuses on optimizing developer time, rather than a computer's processing time.
- Great documentation online:
  - [Python documentation](https://docs.python.org/3/)

## 1.2. Why Choose Python?

- Designed for clear, logical code that is easy to read and learn.
- Lots of existing libraries and frameworks written in Python allowing users to apply Python to a wide variety of tasks.

## 1.3. What can you do with Python?

- Automate simple tasks.
- Searching for files and editing them.
- Scraping information from a website.
- Reading and editing excel files.
- Work with PDFs.
- Automate emails and text messages.
- Fill out forms.
- Data Science and Machine Learning:
  - Analyze large data files
  - Create visualizations
  - Perform machine learning tasks
  - Create and run predictive algorithms
- Create websites:
  - Use web frameworks such as Django and Flask to handle the backend of a website and user data.
  - Create interactive dashboards for users.

# 2. Python Object and Data Structure Basics

## 2.1. Basic Data Types

|      Name      | Type  |                             Description                             |
| :------------: | :---: | :-----------------------------------------------------------------: |
|    Integers    |  int  |                  Whole numbers, such as: 3 300 200                  |
| Floating point | float |             Numbers with a decimal point: 2.3 4.6 100.0             |
|    Strings     |  str  |   Ordered sequence of characters: "hello" 'Sammy' "2000" "楽しい"   |
|     Lists      | list  |           Ordered sequence of objects: [10,"hello",200.3]           |
|  Dictionaries  | dict  | Unordered Key:Value pairs: {"mykey" : "value" , "name" : "Frankie"} |
|     Tuples     |  tup  |      Ordered immutable sequence of objects: (10,"hello",200.3)      |
|      Sets      |  set  |          Unordered collection of unique objects: {"a","b"}          |
|    Booleans    | bool  |               Logical value indicating True or False                |

## 2.2. Numbers

- There are two main number types we will work with:
  - Integers which are whole numbers.
  - Floating Point numbers which are numbers with a decimal.
- What's the difference between floating point and an integer?
  - An integer has no decimals in it, a floating point number can display digits past the decimal point.
- Why doesn't 0.1+0.2-0.3 equal 0.0 ?
  - This has to do with floating point accuracy and computer's abilities to represent numbers in memory.

## 2.3. Variable Assignments

- We just saw how to work with numbers, but what do these numbers represent?
- It would be nice to assign these data types a variable name to easily reference them later on in our code!
- For example:
  - `my_customer = 2`
- Rules for variable names:
  - Names can not start with a number.
  - There can be no spaces in the name, use \_ instead.
  - Can't use any of these symbols :'",<>/?|\()!@#$%^&\*~-+
- Rules for variable names:
  - It's considered best practice (PEP8) that names are lowercase.
  - Avoid using words that have special meaning in Python like "list" and "str".

### 2.3.1. Dynamic Typing

- Python uses Dynamic Typing.
- This means you can reassign variables to different data types.
- This makes Python very flexible in assigning data types, this is different than other languages that are "Statically-Typed".
- Work in python
  ```
  my_customer = 2
  my_customer = [ "Sammy" ,  "Frankie" ]
  ```
- Don't work in other languages E.g. C#, Java, C++

  ```
  int my_customer = 1;
  my_customer = "Sammy" ;  //RESULTS IN ERROR
  ```

- Pros of Dynamic Typing:
  - Very easy to work with
  - Faster development time
- Cons of Dynamic Typing:
  - May result in bugs for unexpected data types!
  - You need to be aware of type()

## 2.4. Strings

- Strings are sequences of characters, using the syntax of either single quotes or double quotes:
  - 'hello'
  - "Hello"
  - " I don't do that "
- Because strings are ordered sequences it means we can using indexing and slicing to grab sub-sections of the string.
- Indexing notation uses `[ ]` notation after the string (or variable assigned the string).
- Indexing allows you to grab a single character from the string...
- These actions use `[ ]` square brackets and a number index to indicate
- positions of what you wish to grab:

```
Character:     h     e     l      l    o
Index:         0     1     2      3    4
Reverse Index: 0    -4    -3     -2   -1
```

- Slicing allows you to grab a subsection of multiple characters, a "slice" of the string.
- This has the following syntax: `[start:stop:step]`
  - **start** is a numerical index for the slice start
  - **stop** is the index you will go up to (but not include)
  - **step** is the size of the "jump" you take.

### 2.4.1. String Formatting for Printing

- Often you will want to "inject" a variable into your string for printing.
- For example:
  ```
  my_name = "Jefté"
  print("Hello " + my_name)
  ```
- There are multiple ways to format strings for printing variables in them.
- This is known as string interpolation.
- Below two methods for this:
  - `.format() method`
  - `f-strings (formatted string literals)`

## 2.5. List and Dictionaries

### 2.5.1. List

- Lists are ordered sequences that can hold a variety of object types.
- They use [] brackets and commas to separate objects in the list.
  - `[1,2,3,4,5]`
- Lists support indexing and slicing.
- Lists can be nested and also have a variety of useful methods that can be called off of them.

### 2.5.2. Dictionaries

- Dictionaries are unordered mappings for storing objects.
- Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead.
- This key-value pair allows users to quickly grab objects without needing to know an index location.
- Dictionaries use curly braces and colons to signify the keys and their associated values.
  - `{'key1':'value1','key2':'value2'}`

### 2.5.3. Dictionaries or List?

- So when to choose a list and when to choose a dictionary?
  - Dictionaries: Objects retrieved by key name.
    - Unordered and can not be sorted.
  - Lists: Objects retrieved by location.
    - Ordered Sequence can be indexed or sliced.

## 2.6. Tuples

- Tuples are very similar to lists.
  - However they have one key difference - immutability.
- Once an element is inside a tuple, it can not be reassigned.
- Tuples use parenthesis: `(1,2,3)`

## 2.7. Sets

- Sets are unordered collections of unique elements.
- Meaning there can only be one representative of the same object.

## 2.8. Booleans

- Booleans are operators that allow you to convey `True` or `False` statements.
- These are very important later on when we deal with control flow and logic!

## 2.9. Files

- Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
- open file in current directory.
  - `f = open("test.txt")`
  - `f = open("C:/Python38/README.txt")`
- We can specify the mode while opening a file.
- We can also specify if we want to open the file in text mode or binary mode.
- The default is reading in text mode.
  - In this mode, we get strings when reading from the file.

| Mode | Description                                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------------------------- |
| r    | Opens a file for reading. (default)                                                                               |
| w    | Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.             |
| x    | Opens a file for exclusive creation. If the file already exists, the operation fails.                             |
| a    | Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist. |
| t    | Opens in text mode. (default)                                                                                     |
| b    | Opens in binary mode.                                                                                             |
| +    | Opens a file for updating (reading and writing)                                                                   |

## 2.10. Resume

- Numbers: Store numerical information and come in two forms:
  - Integers - Whole Numbers.
  - Floating Point - Numbers with a decimal.
- Strings: Ordered sequence of characters.
- Lists: Ordered sequence of objects (mutable).
- Tuples: Ordered sequence of objects (immutable).
- Dictionary: Key-Value pairing that is unordered.

# 3. Python Statements

## 3.1. If, Elif, Else Statements

- We often only want certain code to execute when a particular condition has been met.
- For example, `if my dog is hungry (some condition), then I will feed the dog (some action)`.
- To control this flow of logic we use some keywords:
  - `if`
  - `elif`
  - `else`
- Control Flow syntax makes use of colons and indentation (whitespace).
- This indentation system is crucial to Python and is what sets it apart from other programming languages.

- Syntax of an `if` statement:

  ```
  if some_condition:
    # execute some code
  ```

- Syntax of an `if/else` statement:

  ```
  if some_condition:
    # execute some code
  else:
    # do something else
  ```

- Syntax of an if/else statement:

  ```
    if some_condition:
      # execute some code
    elif some_other_condition:
      # do something different
    else:
      # do something else
  ```

## 3.2. For Loops

- Many objects in Python are "iterable", meaning we can iterate over every element in the object.
- Such as every element in a list or every character in a string.
- We can use for loops to execute a block of code for every iteration.
- The term iterable means you can "iterate" over the object.
- For example you can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary.

  ```
    my_iterable = [1,2,3]
    for item_name in my_iterable:
      print(item_name)
    >> 1
    >> 2
    >> 3
  ```

## 3.3. While Loops

- While loops will continue to execute a block of code while some condition remains `True`.
- For example: `while` my pool is not full, keep filling my pool with water.
- Other example: `while` my dogs are still hungry, keep feeding my dogs.
- Syntax of a while loop:
  ```
    while some_boolean_condition:
      #do something
  ```
- You can combine with an else if you want
  ```
    while some_boolean_condition:
      #do something
    else:
      #do something different
  ```

## 3.4. List Comprehensions

- List Comprehensions are a unique way of quickly creating a list with Python.
- If you find yourself using a for loop along with .append() to create a list, List Comprehensions are a good alternative!

# 4. Methods and Functions

## 4.1. Function

- Creating a function requires a very specific syntax, including the `def` keyword, correct indentation, and proper structure.

  ```
    def name_of_function(name):
      '''
      Docstring explains function.
      '''
      print("Hello "+name)

  >> name_of_function("Jefté")
  >> Hello Jefté
  ```

- Typically we use the `return` keyword to send back the result of the function, instead of just printing it out.
- `return` allows us to assign the output of the function to a new variable.

  ```
    def add_function(num1,num2):
      return num1+num2

  >> result = add_function(1,2)
  >>
  >> print(result)
  >> 3
  ```

# 5. Object Oriented Programming

- Object Oriented Programming (OOP) allows programmers to create their own objects that have methods and attributes.
- Recall that after defining a string,list, dictionary, or other objects, you were able to call methods off of them with the .method_name() syntax.
- These methods act as functions that use information about the object, as well as the object itself to return results, or change the current object.

  ```
    class NameOfClass():
      def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

      def some_method(self):
        # perform some action
        print(self.param1)
  ```

# 6. Modules and Packages

## 6.1. Pip

- PyPI is a repository for open-source third-party Python packages.
- It's similar to RubyGems in the Ruby world, PHP's Packagist, CPAN for Perl, and NPM for Node.js
- So far we've really only used libraries that come internally with Python.
- There are many other libraries available that people have open-sourced and shared on PyPi.
- We can use `pip install` at the command line to install these packages.
- By installing Python from python.org or through the Anaconda distribution you also installed `pip`
- `pip` is a simple way to download packages at your command line directly from the PyPi repository.

## 6.2. Own Modules and Packages

- An often confusing part of Python is a mysterious line of code: `if __name__ == "__main__":`
  - Sometimes when you are importing from a module, you would like to know whether a modules function is being used as an import, or if you are using the original .py file of that module.

# 7. Errors and Exception Handling

- Errors are bound to happen in your code!
- Especially when someone else ends up using it in an unexpected way.
- We can use error handling to attempt to plan for possible errors.
- For example, a user may try to write to a file that was only opened in `mode='r'`
- Currently if there is any type of error in your code, the entire script will stop.
- We can use Error Handling to let the script continue with other code, even if there is an error.
- We use three keywords for this:
  - `try`: This is the block of code to be attempted (may lead to an error)
  - `except`: Block of code will execute in case there is an error in try block
  - `finally`: A final block of code to be executed, regardless of an error.

# 8. Decorators

- Decorators allow you to "decorate" a function, let's discuss what that word means in this context.
- Python has `decorators` that allow you to tack on extra functionality to an already existing function.
- They use the `@` operator and are then placed on top of the original function.

# 9. Generators

- Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.
- This type of function is a generator in Python, allowing us to generate a sequence of values over time.
- The main difference in syntax will be the use of a yield statement.
- When a generator function is compiled they become an object that supports an iteration protocol.
- That means when they are called in your code they don't actually return a value and then exit.
- Generator functions will automatically suspend and resume their execution and state around the last point of value generation.
- The advantage is that instead of having to compute an entire series of values up front, the generator computes one value waits until the next value is called for.
- For example, the range() function doesn't produce an list in memory for all the values from start to stop.
- Instead it just keeps track of the last number and the step size, to provide a flow of numbers.
- If a user did need the list, they have to transform the generator to a list with list(range(0,10)).

# 10. Web Scraping

- Web scraping is a general term for techniques involving automating the gathering of data from a website.
- When a browser loads a website, the user gets to see what is known as the "front-end" of the website

## 10.1. Rules of Web Scraping

- Always try to get permission before scraping!
- If you make too many scraping attempts or requests your IP Address could get blocked!
- Some sites automatically block scraping software.

## 10.2. Limitations of Web Scraping

- In general every website is unique, which means every web scraping script is unique.
- A slight change or update to a website may completely break your web scraping script.

## 10.3. Basic HTML and CSS

- When viewing a website, the browser doesn't show you all the source code behind the website, instead it shows you the HTML and some CSS and JS that the website sends to your browser.
- HTML is used to create the basic structure and content of a webpage.
- CSS is used for the design and style of a web page, where elements are placed and how it looks.
- JavaScript is used to define the interactive elements of a webpage.
- For effective basic web scraping we only need to have a basic understanding of HTML and CSS.
- Python can view these HTML and CSS elements programmatically, and then extract information from the website.
- HTML is Hypertext Markup Language and is present on every website on the internet.
- You can right-click on a website and select "View Page Source" to get an example.
- Let's see a small example of HTML and CSS code:

  ```
  style.css file:
  #para2 {​
      color: red;​
  }

  <!DOCTYPE html>
  <html>
    <head>
      <link rel="stylesheet" href="styles.css">
      <title>Some Title</title>
      </head>
      <body>
          <p id='para2'> Some Text </p>
      <body>
  </html>
  ```

## 10.4. How to scrape

- To web scrape with Python we can use the BeautifulSoup and requests libraries.​
- These are external libraries outside of Python so you need to install them with either conda or pip at your command line.
- Directly at your command line use:​
  - `pip install requests​`
  - `pip install lxml​`
  - `pip install bs4​`
  - Or for Anaconda distributions, use conda install instead of pip install.

# 11. Commands

- Execute python script .py
  - python `<py_file>`
- Execute test with PyTest
  - pytest -v
  - python -m pytest -v
- Install others packages/components
  - pip install -u `<package_name>`
