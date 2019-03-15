import sys
import string

#This class will hold all the information about a single donor,
#and have attributes, properties, and methods to provide access
#to the donor-specific information. 
class Donor():
    """Donor Class"""
    def __init__(self, name):
        self.name = name
        self.donation = []

    def __name__(self):
        return self.name
    
    def add_donations(self, amount):
        self.donation.append(amount)

        
    @property
    def total_donations(self):
        """return total donation of a single donor"""
        return sum(self.donation)

    
    @property
    def num_donations(self):
        """return number of donations a donor donated"""        
        return len(self.donation)

    
    @property
    def ave_donations(self):
        return self.total_donations/self.num_donations

    
    def __str__(self):
        return f'{self.name}:{self.donation}'

    
    @property
    def thank_you_letter(self):
        """
        returns a string that is a formatted thank you note
        with the donor's name and last donation amount.
        """
        return "Dear {:s},\n\nWe greatly appreciate your generous donation of"
        " ${:,.2f}.\n\nThank you,\nThe Team".format(self._name, self._donations[-1])
    
