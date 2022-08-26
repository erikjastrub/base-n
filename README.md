# base-n
Create custom numeric systems that can represent integer values.
Negative integer values can be represented at the cost of an extra character to represent integer values.

By creating a custom numeric system, you can improve the storge and memory footprint of integer values at the cost of additional (but still minimal) computation to encode and decode base-n values.

For Example:
With Hex (base16) you can represent the value 15 with the hex base 'F'.
As opposed to 2 characters, 1 character can be used to represent the integer value.
Under this premise, and exponentially with larger integer values, the character footprint of integer values can be reduced using a custom numeric system.

To create a custom numeric system, you will need to supply the bases and optionally the negative base if you would like your numeric system to represent negative values.

Examples:
hex can be recreated by supplying the numeric system with bases "0123456789ABCDEF"
denary can be represented with "0123456789" and with a negative base of "-"
binary can be represented with bases "01" 

Using this numeric system it is possible to represent the value 255 using a single character (3 characters represented with only a single character)

Final Example:
Using the bases: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

When attempting to represent the value:
99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
(128 nines)

The value will be encoded to:
5Urb1Rbm7aWzQrJUdZfQjPyycQqz6ZTpaqWj4ng2G3GU8nh1AAGV34y7fIt5hPTHMyImpjLD

which is only 72 characters as opposed to the 128 characters (56% less characters)
This saving grows exponentially and can be heightened by supplying more bases

This should demonstrate the storage, memory and networking improvements that can be made when using a custom numeric system

