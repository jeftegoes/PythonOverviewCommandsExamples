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
- [Commands](#commands)

# 1. Python overview

## 1.1. Brief History of Python

- Created in 1990 by Guido van Rossum.
- Python 3 released in 2008.
- Specifically designed as an easy to use language.
- High focus on readability of code.
- Focuses on optimizing developer time, rather than a computer’s processing time.
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
  my_customer = [ “Sammy” ,  “Frankie” ]
  ```
- Don't work in other languages E.g. C#, Java, C++

  ```
  int my_customer = 1;
  my_customer = “Sammy” ;  //RESULTS IN ERROR
  ```

- Pros of Dynamic Typing:
  - Very easy to work with
  - Faster development time
- Cons of Dynamic Typing:
  - May result in bugs for unexpected data types!
  - You need to be aware of type()

## 2.4. Strings

# Commands