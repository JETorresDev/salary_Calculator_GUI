"""
Individual exercise related to chapter 9
Program: salaryCalcGUI.py
3/18/2025

**NOTE: the module breezypythongui.py MUST be in the same directory of this file for the app to run properly

GUI app that calculates the salary based on users individual hourly wage and hours worked"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class Header (class name will change from project to project)
class SalaryCalc(EasyFrame):
    
    # Definition of our classes constructor method
    def __init__(self):
        """Comment specific to project"""
        # CALL to the EasyFrame class constructor from breezypythongui.py
        EasyFrame.__init__(self, title = "Salary Calculator 2.0", width = 360, height = 280, resizable = False, background = "skyblue1")

        # Add labels and Initialize variables
        self.addLabel(text="Hourly wage :", row= 0, column= 0, background= "skyblue1", font= Font(size= 9, family= "verdana", weight= "bold"))
        self.addLabel(text="Total hours worked this week :", row= 1, column= 0, background= "skyblue1", font= Font(size= 9, family= "verdana", weight= "bold"))
        self.wage = self.addFloatField(value= 0.00, row= 0, column= 1, width= 10, sticky= "NW")
        self.totalHours = self.addFloatField(value= 0.00, row= 1, column= 1, width= 10, sticky= "NW")

        # Keyboard event. Allows user to press enter to trigger the compute() method and get their calculation.
        self.totalHours.bind("<Return>", lambda event: self.compute())

        # Add button that triggers the compute() method
        self.button = self.addButton(text= "Calculate", row= 3, column= 0, columnspan= 2, command= self.compute)
        self.button["background"]= "seagreen1"
        self.button["font"] = Font(size= 11, family= "verdana", weight= "bold")
        
    # Definition of the compute() method which is the event handling method
    def compute(self):
        """Collects the input hours and hourly wage integers then calculates the earnings to output a result"""
        rate = self.wage.getNumber()
        hours = self.totalHours.getNumber()
        earnings = rate * hours

        # adds widget to window displaying output of total earnings
        self.result= self.addLabel(text= "Your total earnings for this week are:\n\n$%0.2f" % earnings, row=2, column=0, columnspan= 2, background = "skyblue1", sticky= "N", font= Font(size= 11, family= "Verdana", weight= "bold"))

# End of class block

# Global definition of the main() function
def main():
    """Instantiate an object from the class into mainloop()"""
    SalaryCalc().mainloop()

# Global call to main() for program entry
if __name__ == "__main__":
    main()