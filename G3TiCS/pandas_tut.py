#GitHub Doc

import pandas as pd 
#import G3TiCS/pennData500.csv 

scores = pd.DataFrame( #Sets up a basic data frame 
    [
        [85, 91, 78, 92],
        [88, 76, 95, 89],
        [90, 87, 84, 93]
    ],
    index=["Alex", "Sam", "Jordan"],
    columns=["Assignment 1", "Assignment 2",
             "Assignment 3", "Assignment 4"]
)

print(scores) 

print("    ----     ") #This is a divider to make the printed information more seperatied 

data = pd.read_csv("G3TiCS/pennData500.csv") #Imports the cvs file, converts it to a dataframe, and names it data 
print(" ") 

print(data.head()) #Prints the head and tail of the data 

print("    ----     ")

print(data.tail()) 

print("    ----     ")

print(data.shape) #Prints the shape of the data 

print("    ----     ")

print(data.columns) #Prints the column labels 

print("    ----     ")

print(data.dtypes) #Prints the column labels and what type of data they contain 

print("    ----     ") 

print(data.describe()) #Prints some basic information about the numeric data, such as average and minimum 

print("    ----     ") 

print(data["Age"].mean()) #Manually prints some basic information about Age 
print(data["Age"].median()) 
print(data["Age"].min()) 
print(data["Age"].max()) 

print("    ----     ") 

print(data["Year"]) #Prints (the head and tail) of just the Year column 

print("    ----     ") 

print(data[["Name", "Pathway"]]) #Prints just the Name and Pathway columns 

print("    ----     ") 

filtered_data = data[data["Credits Completed"] > 50] #Filters the data and prints just the rows where the student has completed more than 50 credits 

print(filtered_data) 

print("    ----     ") 

filtered_data = data[data["Pathway"] == "Computer Science"] #Filters and prints just the rows where the student is in the CS Pathway 

print(filtered_data) 

print("    ----     ") 

filtered_data = data[data["GPA"] > 4.0] #Filters the data so that it's just the students who have a GPA of over 4.0 
print(filtered_data[["Name", "Year"]]) #Prints the Name and Year of the students from the filtered data 
print(filtered_data.shape) #Prints the shape of the filtered data 

print("    ----     ") 

print(data.shape) #Prints the shape of the data set 

print("    ----     ") 

print(data["Age"]) #Prints the age column and then various basic information about the data 
print(data["Age"].mean()) 
print(data["Age"].median()) 
print(data["Age"].min()) 
print(data["Age"].max()) 

print("    ----     ") 

filtered_data = data[data["Year"] == "Sophomore"] #Filters the data for just Sophomores and prints the data shape 
print(filtered_data.shape) 

print("    ----     ") 

print(data[["Age", "Credits Completed"]]) #Prints just the age and credits completed columns 

print("    ----     ") 

CS_filter = data[data["Pathway"] == "Computer Science"] #Filters the data for CS pathway students and prints the data shape 
print(CS_filter.shape) 
business_filter = data[data["Pathway"] == "Business"] #Filters the buisness pathway students and prints the shape of the data 
print(business_filter.shape) 