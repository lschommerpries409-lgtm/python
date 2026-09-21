#GitHub Doc

import pandas as pd 
#import G3TiCS/pennData500.csv 

scores = pd.DataFrame(
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
print("This is a test file for GitHub documentation purposes.  ")
print("this is a new line  .") 

print("    ----     ")

data = pd.read_csv("G3TiCS/pennData500.csv") 
print(" ") 

print(data.head()) 

print("    ----     ")

print(data.tail()) 

print("    ----     ")

print(data.shape) 

print("    ----     ")

print(data.columns) 

print("    ----     ")

print(data.dtypes) 

print("    ----     ") 

print(data.describe()) 

print("    ----     ") 

print(data["Age"].mean()) 
print(data["Age"].median()) 
print(data["Age"].min()) 
print(data["Age"].max()) 

print("    ----     ") 

print(data["Year"]) 

print("    ----     ") 

print(data[["Name", "Pathway"]]) 

print("    ----     ") 

filtered_data = data[data["Credits Completed"] > 50] 

print(filtered_data) 

print("    ----     ") 

filtered_data = data[data["Pathway"] == "Computer Science"]

print(filtered_data) 

print("    ----     ") 

filtered_data = data[data["GPA"] > 4.0] 
print(filtered_data[["Name", "Year"]]) 
print(filtered_data.shape) 

print("    ----     ") 

print(data.shape) 

print("    ----     ") 

print(data["Age"]) 
print(data["Age"].mean()) 
print(data["Age"].median()) 
print(data["Age"].min()) 
print(data["Age"].max()) 

print("    ----     ") 

filtered_data = data[data["Year"] == "Sophomore"] 
print(filtered_data.shape) 

print("    ----     ") 

print(data[["Age", "Credits Completed"]]) 

print("    ----     ") 

CS_filter = data[data["Pathway"] == "Computer Science"] 
print(CS_filter.shape) 
business_filter = data[data["Pathway"] == "Business"] 
print(business_filter.shape) 