#!/usr/bin/env python3

# Limitless number of arguments function
def var_args(name, *args):
    print(name)
    print(args)

# Limitless number of arguments with key words
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["title"], kwargs["age"])

var_args("Arya", "la la la", "seemingly", 1, None, True)
var_kwargs("Arya", title = "Arya", age = 30)
