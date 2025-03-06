# import pandas as pd
# pd.DataFrame()

class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

dhruvApplication = RailwayForm()
dhruvApplication.name = "Dhruv"
dhruvApplication.train = "Rajdhani Express"
dhruvApplication.printData()