import qsharp

from Operations import RandomNumber

max = 50
output = max + 1
while output > max:
    bit_string = []

    for i in range(0, len(bin(max))):

        bit_string.append(RandomNumber.simulate())

    output = int(''.join(str(x) for x in bit_string), 2)

print ("The random number generated is " + str(output))