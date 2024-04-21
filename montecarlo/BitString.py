import numpy as np
class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        return np.array2string(self.config)

    def __eq__(self, other): 
        #if every element between the two arrays is the same at all indexes, they are the same
        return (self.config == other.config).all()
    
    def __len__(self):
        return self.N

    def on(self):
        count = 0
        for element in self.config:
            if element == 1:
                count += 1
        return count
    
    def off(self):
        count = 0
        for element in self.config:
            if element == 0:
                count += 1
        return count
    
    def flip_site(self,i):
        current_bit = self.config[i]
        if current_bit == 0:
            self.config[i] = 1
        elif current_bit == 1:
            self.config[i] = 0
        else:
            raise ValueError(f"Error: Bit is not a 1 or 0. At index {i}, the value is {self.config[i]}")
 
    def int(self):
        decimal_number = 0
        length = len(self.config)
        for i in range(length):
            decimal_number += self.config[length - i - 1] * (2 ** i)
        return decimal_number

    def set_config(self, s:list[int]):
        try:
            self.config = np.array(s)
        except Exception as e:
            raise ValueError(f"Error: set_config failed {e}")
        
    def set_int_config(self, dec:int):
        #convert decimal to integer
        binary_representation = ''
        while dec > 0:
            remainder = dec % 2
            binary_representation = str(remainder) + binary_representation
            dec //= 2
        if not binary_representation:
            binary_representation = '0'

        #convert string to array

        #in order to add padding zeroes, create the correct dimension array of all zeroes
        temp = np.zeros(self.N, dtype=int)
        #index should start with the correct amount of padding zeroes in the front to ensure dimensions match
        index = self.N - len(binary_representation)
        #assign each digit in the string to an element of the array
        for digit in binary_representation:
            temp[index] = int(digit)
            index += 1
        #assign the internal array to this temporary array
        self.config = temp

