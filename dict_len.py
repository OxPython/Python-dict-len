'''
Created on Jul 2, 2014

@author: viejoemer

How to determine the number of items that are in a dictionary in python?

¿Cómo saber el numero de items que hay en un diccionario en python?

The method len() gives the total length of the dictionary. 
This would be equal to the number of items in the dictionary.
'''

#dict with three values and keys
d = {"one":1, "two":2, "three":3}
print(d)

#Determine the number of items
length = len(d)
print(length)