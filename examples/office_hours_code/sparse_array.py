'''
Demonstrates one solution to the Sparse Array problem
from lesson 8.
Does not include implementing list slicing
'''
class SparseArray:
    '''
    Implements a sparse array, only for lists
    only non-zero value get stored
    '''
    def __init__(self, input_list):
        # This one tracks current index in the list
        # for init purposes
        self.next_index = 0
        self.array_dict = {}
        for element in input_list:
            # Check that the element is not zero
            if element != 0:
                self.array_dict[self.next_index] = element
            self.next_index += 1

    # Return the entire list
    def __repr__(self):
        reconstructed_list = []
        for index in range(self.next_index):
            if index in self.array_dict:
                reconstructed_list.append(self.array_dict[index])
                continue
            reconstructed_list.append(0)
        return repr(reconstructed_list)

    # Return len of the list
    # emulates len()
    def __len__(self):
        return self.next_index

    # Assign element by index
    def __setitem__(self, index, value):
        self.array_dict[index] = value

    # Return element by index
    def __getitem__(self, index):
        # Check if the index value is valid
        if index >= self.next_index:
            raise IndexError
        # Return the value if index is in dictionary
        # return zero if otherwise
        if index in self.array_dict:
            return self.array_dict[index]
        return 0

    # Delete element by index
    def __delitem__(self, delete_index):
        # Check if the index value is valid
        if delete_index >= self.next_index:
            raise IndexError
        if delete_index in self.array_dict:
            del self.array_dict[delete_index]
        for index in range(delete_index + 1, self.next_index):
            if index in self.array_dict:
                self.array_dict[index -1] = self.array_dict[index]
                del self.array_dict[index]
        # Decrease next_index
        self.next_index -= 1

    # Appends element to the list
    def append(self, value):
        '''
        Implements append method
        '''
        self.array_dict[self.next_index] = value
        self.next_index += 1
         