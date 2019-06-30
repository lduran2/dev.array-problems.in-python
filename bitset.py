#!/usr/bin/env python3
r'''
./bitset.py
This is a set of Boolean bits.
* by: Leomar Duran <https://github.com/lduran2>
* date: 2019-06-30T03:30ZQ
* for: https://dev.to/javinpaul/50-data-structure-and-algorithms-\
       problems-from-coding-interviews-4lh2
'''

import collections
import logging

class BitSet:
    r'''
    A set of boolean values.
    '''
    def __init__(self):
        r'''
        Creates a new bit set.
        '''
        self.data = 0
        self.size = 0

    def add(self, index):
        r'''
        Sets the bit at the specified index.
        '''
        self.data |= (1 << index)
        self.size = max(self.size, (index + 1))

    def get(self, index):
        r'''
        Returns the value of the bit at the specified index.
        '''
        return (0 != (self.data & (1 << index)))

    def __len__(self):
        r'''
        Returns the total number of bits (set and clear) in this bit
        set.  That is equivalent to one more than the index of the
        most significant bit.
        '''
        return self.size

    def __iter__(self):
        r'''
        Returns an iterator on this bit set.
        '''
        return BitSet._Iter(self)

    def __str__(self):
        r'''
        Returns a string representation of this bit set.
        '''
        return r''.join(['[', r', '.join([str(bit) for bit in self]), ']'])

    class _Iter:
        r'''
        An iterator on a bit set.  The iterator returns the indices of
        set bits, going from least significant bit to most significant
        bit, skipping each clear bit.
        '''
        def __init__(self, bitset):
            r'''
            Creates an iterator on a bit set.
            '''
            self.bitset = bitset
            self.index = 0

        def __iter__(self):
            r'''
            Returns itself as does iter(iter([])).
            '''
            return self

        def __next__(self):
            r'''
            Returns the next set bit.
            '''
            logging.debug(r'size: %d', self.index)
            for bit in range(self.index, self.bitset.size):
                found = self.bitset.get(bit)
                logging.debug(r'    %d=%s', bit, found)
                if (found):
                    self.index = (bit + 1)
                    return bit
            raise StopIteration


def main():
    #logging.basicConfig(level=logging.DEBUG)
    bitset = BitSet()

    #for bit in range(0, len(bitset)):


    bitset.add(5)
    bitset.add(9)
    bitset.add(2)

    a = [1, 2, 3, 4]
    b = iter(a)
    c = iter(b)
    next(b)
    print(next(b))
    print(next(c))
    print()

    #print(iter(iter(iter(bitset))))

    for bit in bitset:
        print(bit)
    # for bit in range(len(bitset)):
        # (bitset.get(bit))
    print(bitset)
    print(bitset)
    print('two iterators')
    l = bitset
    it1 = iter(l)
    it2 = iter(l)
    next(it1)
    next(it1)
    print(next(it1))
    print(next(it2))

    #(next(it1))
    #(next(it2))
    #next(it2)
    #(next(it1))
    #(next(it2))

main()
