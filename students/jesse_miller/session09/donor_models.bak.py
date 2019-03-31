#!/usr/bin/env python3
'''
Let's try this by following the directions.  So, this is going to be where the
donor manipulation occurs.  The goal is to compartmentalize everything so that
functions can be called by other programs if and when needed.
'''


class Donor:
    '''
    This is not being used at all.  Every time I've attempted to use these
    functions something has broken in a unique and fun way.  For example, key
    errors.
    '''

    def __init__(self, name):
        self.name = name
        self.donations = []


    def donation_add(self, new_donation):
        '''
        This should append donations to the list
        '''
        self.donations.append(new_donation)

    @property
    def donation_count(self):
        '''
        Fairly obvious, counts the number of donations
        '''
        return len(self.donations)


    @property
    def donation_total(self):
        '''
        Again, obvious, adds the donations up
        '''
        return sum(self.donations)


    @property
    def donation_average(self):
        '''
        Averages the donations
        '''
        return self.donation_total / self.donation_count


################################################################################
'''
End Donors
'''
################################################################################

class DonorCollection:
    '''
    This class will handle the donors dictionary, as well as the collections.
    Some of the things we can look forward to:
    Create a donor
    Find a donor
    List donors
    Donor reports
    Data saving and reloading.
    '''
    def __init__(self):
        '''
        Initializing and building the default dict
        '''
        self.donors_dict = {'Robert Smith': [435.56, 125.23, 357.10],
                            'JD Cronise': [123.12],
                            'Chris Stapleton': [243.87, 111.32],
                            'Dave Lombardo': [63.23, 422.87, 9432.01],
                            'Randy Blythe': [223.50, 8120.32],
                            'Devin Townsand': [431.12, 342.92, 5412.45],
                           }


    def donor_creation(self, current_donor):
        '''
        Allows for adding new donors to the db
        '''
        new_donor = Donor(current_donor)
        self.donors_dict[current_donor] = new_donor
        return new_donor


    def list_donor(self):
        '''
        Listing the contents of the db
        '''
        donor_list = []
        for donor in self.donors_dict:
            donor_list.append(donor)
        sorted_donors = sorted(donor_list)
        return sorted_donors


    def find_donor(self, current_donor):
        '''
        This will take an inputed donor name, and search for it.  If the name
        isn't found, it will then bounce the request to the creation function.
        '''
        try:
            return self.donors_dict[current_donor]
        except KeyError:
            return self.donor_creation(current_donor)


    def delete_donor(self, current_donor):
        '''
        This should allow for the removal of a donor from the dictionary
        '''
        del self.donors_dict[current_donor]
        return self.donors_dict


    def create_report(self):
        '''
        Last but not least, the report function
        '''
        reporting = []
        #pylint: disable=C0103
        #I don't like disabling the linter, but this is a silly complaint
        for k, v in self.donors_dict.items():
            reporting.append([k, (sum(v)), (len(v)), (sum(v) / len(v))])
            reporting.sort(key=lambda d: d[1], reverse=True)
        return reporting


################################################################################
'''
End DonorCollection
'''
################################################################################
