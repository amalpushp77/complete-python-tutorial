# Operator overloading
'''  Operators

Binary Operators

Operator           Method
+                       object.__add__(self, other)
-                        object.__sub__(self, other)
*                        object.__mul__(self, other)
//                       object.__floordiv__(self, other)
/                        object.__div__(self, other)
%                      object.__mod__(self, other)
**                      object.__pow__(self, other[, modulo])
<<                     object.__lshift__(self, other)
>>                     object.__rshift__(self, other)
&                       object.__and__(self, other)
^                       object.__xor__(self, other)
|                        object.__or__(self, other)

Assignment Operators:

Operator          Method
+=                     object.__iadd__(self, other)
-=                      object.__isub__(self, other)
*=                      object.__imul__(self, other)
/=                      object.__idiv__(self, other)
//=                     object.__ifloordiv__(self, other)
%=                    object.__imod__(self, other)
**=                     object.__ipow__(self, other[, modulo])
<<=                   object.__ilshift__(self, other)
>>=                   object.__irshift__(self, other)
&=                     object.__iand__(self, other)
^=                      object.__ixor__(self, other)
|=                      object.__ior__(self, other)

Unary Operators:

Operator          Method
-                       object.__neg__(self)
+                      object.__pos__(self)
abs()                object.__abs__(self)
~                      object.__invert__(self)
complex()        object.__complex__(self)
int()                  object.__int__(self)
long()               object.__long__(self)
float()               object.__float__(self)
oct()                object.__oct__(self)
hex()               object.__hex__(self)

Comparison Operators

Operator          Method
<                      object.__lt__(self, other)
<=                    object.__le__(self, other)
==                    object.__eq__(self, other)
!=                     object.__ne__(self, other)
>=                    object.__ge__(self, other)
>                      object.__gt__(self, other)
'''


class ComplexOverloading:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def __add__(self, other):
        return complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        # (a+jb)(c+jd)
        # real = a*c - b*d
        # img = (b*c + a*d)j
        return complex((self.real * other.real) - (self.img * other.img),
                       (self.img * other.real) + (self.real * other.img))

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img


c1 = ComplexOverloading(2, -5)
c2 = ComplexOverloading(3, 2)

print('Add:', c1 + c2)
print('Sub:', c1 - c2)
print('Mul:', c1 * c2)
print('Equal:', c1 == c2)
print('Commutative:', (c1 * c2) == (c2 * c1))
