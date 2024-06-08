### Exercises
There were lots of lab exercises this week. My thoughts are:
- very important to read through code and understand it
  - the code that needed fixing required not only syntactic fixes but also a bit of thinking as to whether the code was actually achieving its purpose
  - that is why it's very important to have well-written code with good variable names and logical flow
  - at the last minute, I caught the fact that the word exercise was written as exersise - fun little detail that didn't become apparent to me until I was about to move on to the next exercise
- exercise 3
  - was fun trying to solve it with list comprehensions
    - depending on the problem, these can be move readable or similar (and technically they are slightly faster although it's a negligible different for an exercise like this)
    - not sure if there's a way to get the pyramid exercise done with a nested list comprehension but it would be a fun exercise to try that out
    - happy with the method I found to get the pyramid correct but I'm curious what other methods people think of
- types
  - so used to using fstrings that when I was concatenating a string and a number, I forgot to convert the int to a str beforehand
  - it's quite important that this wouldn't be allowed and I'm glad python doesn't automatically cast the int to a str
- terminology
  - calling - invoking a function or method e.g. print() would be calling the print function
  - method - member functions tied to a specific class (ie. .upper() is a method on string objects)
  - arguments - inputs to a function that you pass in e.g. in def foo(bar), the function foo would have bar as an argument
