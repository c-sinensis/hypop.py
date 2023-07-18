# hypop.py
Hyperoperations Calculator, Version 1.0
Zachary Saar

This program consists of a function that calculates the hyperoperation of degree N between two operands A and B (i.e. using Goodstein's notation, G(N,A,B)).
N, A, and B must be positive integers (no successor function, where N=0).

Future implementation ideas:
- Float/decimal operands
- Negative operands
- Inverse operations (logarithm and root)
- Optimization


Notes:
- I don't recommend using operand values that are beyond ~5 if N >= 4, because of the nature of these calculations G(4,3,4) yields a 13-digit product.
- Increase the N value at your own risk, this is a recursive function and it gets fairly resource-intensive fairly quickly.
