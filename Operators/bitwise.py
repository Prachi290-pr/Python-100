# Used to compare binary numbers

# AND  &
print(2 & 1)   # 010 & 001  => 000

# OR  |
print(2 | 1)   # 010 | 001 => 011

# XOR  ^
print(2 ^ 1)   # 010 ^ 001 => 011

# NOT  ~
print(~2)      # ~2  =>   -(2+1) =>    -3

# LEFT SHIFT
print(5 << 1)     # 101
# move bits to the left. 1010    =>   10
# [ Multiply by 2^n ]  5 * 2^1   =>   10

# RIGHT SHIFT
print(5 >> 1)    # 101
# move bits to the right    010_   =>  2
# [ Divide by 2^n ]    5 / 2       =>  2