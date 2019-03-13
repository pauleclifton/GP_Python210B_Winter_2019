#-------------------
#!/usr/bin/env python3
#Session 08 Exercise:Sparse Array 
#Shirin Akther
#-------------------------


class SparseArray():
    """SparseArray class"""
    def __init__(self, array):
        self.array = {}
        self.length = len(array)
      
        for key, value in enumerate(array):
            if value is not 0:
                
                self.array[key] = value

                
    def __getitem__(self, key):
        if key>self.length:
            raise IndexError     
        return self.array[key]


    def __str__(self): 
        return "Sparse Array({})".format(self.array) 

    def __setitem__(self, key, value):
        self.array[key] = value

        
    def __len__(self):
        return self.length

    
    def __del__(self, key):
        del self.array[key]
        

    def append(self, value): 
        '''append a number at the end''' 
        self.length += 1 
        self.array[self.length] = value 

    
        
