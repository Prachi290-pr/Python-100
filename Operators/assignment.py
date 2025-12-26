x = 10      # =

x += 5      # x = 15
x -= 3      # x = 12
x *= 2      # x = 24
x //= 4     # x = 6
x **= 2     # x = 36
x %= 7      # x = 1

x |= 2      # bitwise OR  x = 3     001 | 010  => 011
x &= 1      # bitwise AND  x = 1    011 X 001 => 001
x ^= 4      # bitwise XOR  x = 5    001 xor 100 => 101

x <<= 1     # left shift  x = 10
x >>= 2     # right shift  x = 2


##  Left Shift   5 << 1     101
# move bits to the left. 1010    =>   10
# [ Multiply by 2^n ]  5 * 2^1   =>   10

## Right Shift   5 >> 1     101
# move bits to the right    010_   =>  2
# [ Divide by 2^n ]    5 / 2       =>  2



# Walrus Operator
# The walrus operator := assigns a value to a variable while evaluating an expression.

x = 5
print(x)

print(x:=5)

if (n := len("Python")) > 5:
    print(n)