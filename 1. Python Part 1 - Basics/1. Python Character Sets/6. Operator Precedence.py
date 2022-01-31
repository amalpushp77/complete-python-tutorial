"""
Precedence from Highest to lowest.


Operator       Description                                                          Associativity
------------------------------------------------------------------------------------------------------------------------
( )             Parentheses (Highest precedence)                                    left-to-right
**	            Exponent            	                                            right-to-left
+x, -x, ~x	    Unary plus/minus, Bitwise NOT
* @ / // %	    Multiplication/matrix/division/floor/modulus                        left-to-right
+  –	        Addition/subtraction	                                            left-to-right
------------------------------------------------------------------------------------------------------------------------
<<  >>	        Bitwise shift left, Bitwise shift right	                            left-to-right
&	            Bitwise AND	                                                        left-to-right
^	            Bitwise exclusive OR	                                            left-to-right
|	            Bitwise inclusive OR	                                            left-to-right
------------------------------------------------------------------------------------------------------------------------
< <= > >= == !=	Comparison Operators                                                left-to-right
is,  is not     Identity Operator                                                   left-to-right
in, not in      Membership operator                                                 left-to-right
not	            Logical NOT	                                                        right-to-left
and	            Logical AND                                                         left-to-right
or	            Logical OR	                                                        left-to-right
------------------------------------------------------------------------------------------------------------------------
=               Assignment Operators                                                right-to-left
+=  -=
*=  /=
%=  &=
^=  |=
<<=  >>=
:=	            Assignment expression (Lowest precedence)                           right-to-left
------------------------------------------------------------------------------------------------------------------------
"""
a = 2
b = 3
c = 5

print(b - c / a)
print((b - c) / a)
print((b - c) // a)
print(c ** b ** a)
print(c / a / b)
print(6 / 3 / 2)
print(200 >> 2 >> 3)
print(5 < 8 << 2)
print(5 & 55 > 3)
print(not not True)
a <<= 3 == 3
print(a)

x = y = z = 7
print(x, y, z)

print(a > b > c)

