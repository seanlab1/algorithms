"""
Given an array of integers, every element appears
three times except for one, which appears exactly once.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
Solution:
32 bits for each integer.
Consider 1 bit in it, the sum of each integer's corresponding bit
(except for the single number)
should be 0 if mod by 3. Hence, we sum the bits of all
integers and mod by 3,
the remaining should be the exact bit of the single number.
In this way, you get the 32 bits of the single number.
"""
## one once
from algorithms.bit import single_number2
a=[4,1,2,1,2]
b=[2,2,1]

print(single_number2(a))

print(single_number2(b))