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
        #check if numpy arrays are different sizes
        if self.config.shape != other.config.shape:
            return False
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
        #throw if index does not lie within dimensions of array
        if not 0 <= i < self.config.shape[0]:
            raise IndexError(f"Error: Index {i} exceeds the dimension of the bitstring of length: {self.config.shape}")
        current_bit = self.config[i]
        if current_bit == 0:
            self.config[i] = 1
        elif current_bit == 1:
            self.config[i] = 0
        else:
            #this will throw if someone the bitsring does not contain a 0 or 1
            raise ValueError(f"Error: Bit is not a 1 or 0. At index {i}, the value is {self.config[i]}")
 
    def int(self):
        decimal_number = 0
        length = len(self.config)
        for i in range(length):
            decimal_number += self.config[length - i - 1] * (2 ** i)
        return decimal_number

    def set_config(self, s:list):
        try:
            temp = np.array(s)
            for index in temp:
                #check if there are any values not 0 or 1
                if index != 0 and index != 1:
                    raise ValueError(f"Error: {index} must be 0 or 1.")

            self.config = temp
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

        #check if the dimensions of the bitstring can hold the binary_representation, otherwise throw error
        if self.N < binary_representation.__len__():
            raise ValueError(f"Error: dimension does not match {self.N} and {binary_representation.__len__()}.")
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

