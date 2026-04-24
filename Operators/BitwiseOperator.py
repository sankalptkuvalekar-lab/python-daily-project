"""

Operator  Name	                     Description	                                                                     Example	Try it
& 	      AND	                  Sets each bit to 1 if both bits are 1	                                                  x & y	
|	      OR	                  Sets each bit to 1 if one of two bits is 1	                                          x | y	
^	      XOR	                  Sets each bit to 1 if only one of two bits is 1	                                       x ^ y	
~	      NOT	                   Inverts all the bits	                                                                      ~x	
<<	      Zero fill left shift	  Shift left by pushing zeros in from the right and let the leftmost bits fall off	        x << 2	
>>	      Signed right shift	  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

"""


# AND &

print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================


"""

# OR |

print(6 | 3)



"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================


"""

# xor ^

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)


# not ~

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100
"""

# <<. zero fill left shift

print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
"""

# >> zero fill right shift

print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
 """

