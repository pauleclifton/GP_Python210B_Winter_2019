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

    @property
    def last_donation(self):
        if len(self.donation) > 0:
            return self.donation[-1]
        else:
            return 0

    def __str__(self):
       
       return f'{self.name}:{self.donation}' 
           
        
 #--------------------------------
 #       End of Donor class
 #------------------------------

# This class will hold all of the donor objects, as well as methods to add a new donor,
#search for a given donor,  generates reports about multiple donors.
#In other words,if the functionality involves more than one donor – it belongs in this class.
    
class DonorCollection():
    def __init__(self):
        self.donors_dict = {}
                            
                       
    def find_donor(self, name):
        if name.lower() in self.donors_dict:
            return self.donors_dict[name.lower()]
        return None


    def add_donor(self, name):
        """allows for adding new donors to the db"""
        
        new_donor = Donor(name)
        self.donors_dict[new_donor.name] = new_donor
        return new_donor

    def search_donor(self,name):
        return self.donors_dict.get(name.lower())

        

    
    @staticmethod
    def sort_key(item):
        return item[1]

    
    def donor_list(self):
        name_list = [donor.name for donor in self.donors_dict.values()]
        return '\n'.join(name_list)


#Builds the donor report and displays the name, total given, number of gifts
# and the average gift donated by the donor.

    def donor_report(self):
        report_rows = []
        for donor in self.donors_dict.values():
            name = donor.name
            donation = donor.donation
            total_donations = donor.total_donations
            num_donations = len(donation)

            avg_donation = donor.ave_donations
            report_rows.append((name, total_donations, num_donations, avg_donation))
        report_rows.sort(key=self.sort_key)
        report = []

        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Donated",
                                                                "Num gifts",
                                                                "Average Donation"))

        report.append("_" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   ${:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    
    def write_letter(self, donor):
        """
        returns a string that is a formatted thank you note
        with the donor's name and last donation amount.
        """               
        return ("Dear {:s},\n\nWe greatly appreciate your generous donation of"
        " ${:,.2f}.\n\nThank you,\nThe Team".format(donor.name, donor.last_donation))

    
    def save_letters_to_disk(self):
        
         """
        Generate letter for each donor and write to disk
        """
         for donor in self.donors_dict.values():
            print("creating letter to {:s}".format(donor.name))
            letter = self.write_letter(donor)
            filename = donor.name.replace(" ", "_") + ".txt"
            with open(filename, 'w') as outfile:
                outfile.write(letter)



 #----------------------------------------
 #       End of DonorCollection class
 #----------------------------------------


