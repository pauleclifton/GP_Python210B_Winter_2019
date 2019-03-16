'''
##########################
#Python 210
#Session 08 - Sparse Array
#Elaine Xu
#Mar 8, 2019
###########################
'''
'''
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/sparse_array.html

Oftentimes, at least in computation programming, we have large arrays of data that hold mostly zeros
These are referred to as “sparse” as the information in them is widely scattered, or sparse.
Since they are mostly zeros, it can be memory and computationally efficient to store only the value
that are non-zero.
But you want it to look like a regular array in user code.
In the real world, these are usually 2 dimensional arrays. But to keep it a bit simpler, we’ll make
a 1 dimensional sparse array in this class.

A sparse array class should present to the user the same interface as a regular list.

Internally, it can store the values in a dict, with the index as the keys, so that only the indexes
with non-zero values will be stored.
It should take a sequence of values as an initializer:
sa = SparseArray([1,2,0,0,0,0,3,0,0,4])

you should be able to tell how long it is:
len(my_array)
This will give its “virtual” length – with the zeros

It should support getting and setting particular elements via indexing:
sa[5] = 12
sa[3] = 0 # the zero won't get stored!
val = sa[13] # it should get a zero if not set

It should support deleting an element by index:
del sa[4]

It should raise an IndexError if you try to access an index beyond the end.
it should have an append() method.
Can you make it support slicing?
How else can you make it like a list?
'''
class SparseArray():
    '''generates sparse array'''
    def __init__(self, array):
        self.array = {}
        self.len = len(array)
        for i, item in enumerate(array):
            if item is not 0:
                self.array[i] = item

    def __str__(self):
        return "Sparse Array({})".format(self.array)

    def __getitem__(self, i):
        if isinstance(i, slice):
            print(i)
            if i.stop > self.len:
                raise IndexError
            self.slicearray = {}
            for ind in range(i.start, i.stop):
                if ind in self.array:
                    self.slicearray[ind] = self.array[ind]
            return self.slicearray
        else: #simple index integer
            if i in self.array:
                return self.array[i]
            elif i <= self.len:
                return 0
            else:
                raise IndexError

    def __setitem__(self, i, item):
        if item is not 0:
            self.array[i] = item
            if i > self.len:
                self.len = i

    def __delitem__(self, i):
        if i in self.array:
            del self.array[i]

    def append(self, item):
        '''append a number at the end'''
        self.len += 1
        self.array[self.len] = item


#############################################################
if __name__ == "__main__":

    my_array = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4]
    sa = SparseArray(my_array)
    print("Sparse Array:", sa.array)
    print("Array virtual length:", sa.len)

    print("\nTest:")
    print("Assign a value to 12:")
    sa[5] = 12
    print('sa[5]:', sa[5])
    print(sa)

    print("\nAssign a value to 0:")
    sa[3] = 0 # the zero won't get stored!
    #print(sa)
    print('sa[3]:', sa[3])
    print(sa)

    print("\nGet a value:")
    print('sa[10]:', sa[10]) # it should get a zero if not set

    print("\nIt should support deleting an element by index:")
    del sa[4]
    del sa[1]
    print("deleting sa[4], sa[1]")
    print(sa)

    print("\nRaise an IndexError if you try to access an index beyond the end")
    #print('sa[13]:', sa[13])

    print("\nTry append() method:")
    sa.append(4)
    print("appending 4 to the last number:", sa)

    print("\nSupport slicing")
    print('sliced array:', sa[4:6])
