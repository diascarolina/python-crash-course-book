# Chapter 8 Functions

"The variable `username` in the definition of `greet_user()` is an example of a **parameter**, a piece of information the function needs to do its job. The value "jesse" in `greet_user(jesse)` is an example of an **argument**. An argument is a piece of information that's passed from a function call to a function. [...] In this case, the argument "jesse" was passed to the function `greet_user()`, and the value was assigned to the parameter `username`."

`greet_user(jesse)` -> parameter(argument)

"When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly."

Positional vs. keyword arguments.

In conditional tests, _None_ evaluates to _False_.

Shallow copy: `list_name[:]`

[Python Docs - Shallow and deep copy operations](https://docs.python.org/3/library/copy.html#:~:text=The%20difference%20between,shared%20between%20copies.)

"It's more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you're working with large lists."

### Passing an Arbritary Number of Arguments

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

The asterisk in the parameter name `*toppings` tells Python to make an empty tuple called `toppings` and pack whatever values it receives into this tuple. The `print()` call in the function body produces output showing that Python can handle a function call with one value and a call with three values. It treats the different calls similarly. Note that Python packs the
arguments into a tuple, even if the function receives only one value.

This syntax works no matter how many arguments the function receives.

### Mixing Positional and Arbitrary Arguments

If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter `*toppings`:
```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**Note:** You'll often see the generic parameter `*args`, which collects arbitrary positional arguments like this.

### Using Arbitrary Keyword Arguments

Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)
```

The definition of `build_profile()` expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. The double asterisks before the parameter `**user_info` cause Python to create an empty dictionary called `user_info` and pack whatever name-value pairs it receives into this dictionary. Within the function, you can access the key-value pairs in `user_info` just as you would for any dictionary.

You can mix positional, keyword, and arbitrary values in many different ways when writing your own functions. It’s useful to know that all these argument types exist because you’ll see them often when you start reading other people’s code.

**Note:** You'll often see the parameter name `**kwars` used to collect non-specific keyword arguments.

