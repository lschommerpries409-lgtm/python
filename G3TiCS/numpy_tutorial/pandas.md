# Topics in Computer Science
## Data Science — Introduction to Pandas

### Driving Question
How can we use Pandas to organize and analyze real-world data?

---

## Before You Begin

Last class, you worked with NumPy arrays.

You created a 2D array similar to:

```python
import numpy as np

scores = np.array([
    [85, 91, 78, 92],
    [88, 76, 95, 89],
    [90, 87, 84, 93]
])
```

Think about:
- What does each row represent? 
- What does each column represent?
- How do you know?
The problem is that the array itself doesn't tell us.

Today we're going to look at a Python library designed to make
real-world tabular data easier to work with.


## Part 1 — Meet Pandas
Pandas is a Python library used for working with datasets.

You must first install pandas

Open Terminal and type in
```bash
pip3 install pandas
```

Import it using:
```python
import pandas as pd
```

The primary data structure we will use is called a DataFrame.

## Part 2: Your first Dataframe

Run the following code:

```python

import pandas as pd

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

```

#### Question 1
How is this DataFrame similar to the NumPy array you created last class?
* Your answer: It contains the same data in a similar nested list format. 

#### Question 2
How is it different?
* Your answer: It also includes titles that specify what the data is. 

## Part 3 — Reading a CSV

[Download Data Here](https://github.com/marsh135/python/blob/main/G3TiCS/pennData500.csv)

```python
data = pd.read_csv("pennData500.csv")
```

### Questions:
- What is a DataFrame? Nested lists of data that are labled. 
- How is it similar to the 2D NumPy array you worked with? It contains the same data, just with lables. 
- What's different? There are labels. 
- Why are column names useful? They tell you what the data is. 

## Part 4: Looking at the DataFrame
```python
print(data.head())
print(data.tail())
print(data.shape)
print(data.columns)
print(data.dtypes)
```

### Questions:
- What does .head() do? It desplays the first 5 entries of data. 
- What does .tail() do? It desplays the last 5 entries. 
- What is the shape of this data? (499,6) 
-  What is the result of .columns? It desplays the index/names of the colums of data. 
- What is the result of .dtype? It desplays each index/column name and the data type it contains. 


## Describe
```python
print(data.describe())
```

### Questions:
- What does .describe() do? It lists various information about the numerical data such as count, mean, min, max, etc. 

## Statistics
```python
print(data["COLUMN_NAME"].mean())
print(data["COLUMN_NAME"].median())
print(data["COLUMN_NAME"].min())
print(data["COLUMN_NAME"].max())
```

Replace "COLUMN_NAME" with a column name from the data and run the code above


### Questions:
- Which column did you choose? Age 
- What is the mean? 16.430861723446895 
- What is the median? 16.0 
- What is the minimum value? 14 
- What is the maximum value? 19 
- In your own words, what do these statistics tell you about the data? They tell me the average, middle, minimum, and maximum value of age for this data set. 

## Part 5: Selecting Data

One advantage of a Pandas DataFrame is that we can select specific columns from a large dataset.

To display one column:

```python
print(data["COLUMN_NAME"])
```

Replace `"COLUMN_NAME"` with the name of one of the columns in the Penn dataset.

To display multiple columns:

```
print(data[["COLUMN_1", "COLUMN_2"]])
```

Replace `"COLUMN_1"` and `"COLUMN_2"` with two columns from the dataset.

### Questions:
- Which column did you select first? Year. 
- What type of data does that column contain? String. 
- Which two columns did you select together? Name and Pathway. 
- Why might it be useful to look at only a few columns instead of the entire DataFrame? It lets you filter just the data you need. 

## Part 6: Filtering Data

Pandas can also select only the rows that meet a certain condition.

For example:

```python
filtered_data = data[data["COLUMN_NAME"] > 50]

print(filtered_data)
```

This code tells Pandas:

"Give me only the rows where COLUMN_NAME has a value greater than 50."

You will need to replace `"COLUMN_NAME"` with the name of a **quantitative** column from the Penn dataset.

You may also need to change `50` to a value that makes sense for the column you selected.

### Try It:

Create a filter using a numerical column from the Penn dataset.

```python
filtered_data = data[data["________________"] > ______]

print(filtered_data)
```

### Questions:
- Which column did you filter? Credits Completed. 
- What condition did you use? >50. 
- How many rows appear to meet your condition? 83. 
- In your own words, explain what your filter asked Pandas to find. 
    - My filter asked Pandas to find all rows where the student had completed more than 50 credits. 

## Part 7: Filtering Qualitative Data

We can also filter using qualitative data.

Instead of asking whether a number is greater than or less than something, we can ask whether a value is equal to something.

Example:

```python
filtered_data = data[data["COLUMN_NAME"] == "VALUE"]

print(filtered_data)
```

Notice the difference:

```python
> 50
```

asks a numerical question.

While:

```python
== "VALUE"
```

asks whether something is equal to a specific value.

### Try It:

Find a qualitative column in the Penn dataset.

Create a filter that displays only rows containing one particular value from that column.

```python
filtered_data = data[data["________________"] == "________________"]

print(filtered_data)
```

### Questions:
- Which qualitative variable did you use? Pathway. 
- What value did you search for? Computer Science. 
- What does the resulting DataFrame contain? It contains all the rows where the student's pathway is Computer Science. 
- Why do we use `==` instead of `=` when checking whether two values are equal? '==' checks if two values are equal, while '=' is used to set a value equal to another. 

## Part 8: Combining Selection and Filtering

We can combine what we have learned.

First, filter the data:

```python
filtered_data = data[data["COLUMN_NAME"] > 50]
```

Then select only the columns we want to see:

```python
print(filtered_data[["COLUMN_1", "COLUMN_2"]])
```

Instead of displaying every variable for every matching observation, Pandas will now display only the information we requested.

### Your Turn:

Create your own example that:

- Filters the dataset using a condition  
- Displays at least two columns from the filtered data  

Paste or write your completed code below:

```python

filtered_data = data[data["GPA"] > 4.0] 
print(filtered_data[["Name", "Year"]]) 
print(filtered_data.shape) 

```

### Questions:
- What question were you trying to answer? What's the name and year of everyone who had a GPA higher than a 4.0. 
- What did your code find? The name and year of everyone with a GPA greater than a 4.0. 
- Did the result match what you expected? Explain. Yes. There were 52 people with a GPA higher than 4.0 which matched my expectations for the number of people in this list that would have a GPA that high (out of 500 total). 

## Part 9: Data Detective

Now it is time to put everything together.

For this section, you will receive **less example code**.

Use what you have learned about Pandas to investigate the Penn dataset.

You may use:

```python
data.head()
data.tail()
data.shape
data.columns
data.dtypes
data.describe()
```

You may also use:

```python
data["COLUMN_NAME"]
data["COLUMN_NAME"].mean()
data["COLUMN_NAME"].median()
data["COLUMN_NAME"].min()
data["COLUMN_NAME"].max()
```

And filtering:

```python
data[data["COLUMN_NAME"] > VALUE]
data[data["COLUMN_NAME"] < VALUE]
data[data["COLUMN_NAME"] == "VALUE"]
```

### Challenge 1

How many **rows** and **columns** are in the Penn dataset?

Write the Pandas command you used and your answer. 

```python 
print(data.shape) 
``` 
There are 500 rows and 6 columns. 

### Challenge 2

Choose one quantitative variable.

Determine its:

- Mean  
- Median  
- Minimum  
- Maximum  

What does this information tell you about that variable? 

```python 
print(data["Age"]) 
print(data["Age"].mean()) 
print(data["Age"].median()) 
print(data["Age"].min()) 
print(data["Age"].max()) 
``` 
This information tells me that the average age is 16.430861723446895, the middle age when age is listed in ascending order is 16.0, the lowest age is 14, and the highest age is 19. 

### Challenge 3

Create a filter that returns only a portion of the dataset.

Your filter must answer a question that you can describe in plain English.

For example:

"How many observations have a value greater than _____?"

Do not use this exact question. Create your own.

Write:

- Your question  
- Your Python code  
- What you discovered 

Question: How many Sophomores are in this list? 
```python 
filtered_data = data[data["Year"] == "Sophomore"] 
print(filtered_data.shape) 
``` 
I discovered that there are 109 Sophomores in this list. 

### Challenge 4

Choose two variables that you think might be interesting to examine together.

Display only those two columns. 

### Questions:
- Which variables did you choose?
- Why did you choose them?
- Do you notice anything interesting?
- What would you want to investigate further? 

```python 
print(data[["Age", "Credits Completed"]])
``` 
- I chose Age and Credits Completed 
- I chose these variables to see if there is a correlation between Age and the number of Credits Completed 
- There doesn't seem to be a clear correlation from the portion of data displayed 
- I would want to create some filters to try and narrow down the amount of data shown in order to try and distinguish some trends. 

## Part 10: Ask Your Own Question

This is the most important part of today's assignment.

Data scientists do not just run commands.

They use data to **answer questions**.

Write one question about Penn that you believe this dataset can answer.

### My Question:

Your question: Are there more Computer Science Pathway students than Business Pathway students? 

### My Code:

Write the Pandas code necessary to help answer your question.

```python

CS_filter = data[data["Pathway"] == "Computer Science"] 
print(CS_filter.shape) 
business_filter = data[data["Pathway"] == "Business"] 
print(business_filter.shape) 

```

### My Result:

What did your program find? It found that there are more business pathway students than CS pathway students (43<65). 

### What Does It Mean?

Explain your result in a complete sentence. 
- There are more business pathway students than CS pathway students. 

Do not simply write the number produced by Python.

For example, instead of:

**"72.4"**

write something like:

**"The average value of ______ in this dataset is 72.4."**

## Part 11: What CAN'T the Data Tell Us?

A dataset can only answer questions about the information it contains.

Write one interesting question about Penn that **cannot** be answered using this dataset.

### Question:

What would you like to know?

### Missing Data:

What additional variable or data would need to be collected to answer your question?

## Final Reflection

Answer each question in 1–3 complete sentences.

### 1. NumPy vs. Pandas

What is one major difference you noticed between working with a NumPy array and working with a Pandas DataFrame?

### 2. DataFrames

Why might a DataFrame be more useful than a basic 2D array when working with a large real-world dataset?

### 3. Data Science

Return to today's Driving Question:

**How can we use Pandas to organize and analyze real-world data?**

Answer the question using something you did during today's activity as an example.

## Before You Are Finished

Make sure you have:

- [ ] Installed and imported Pandas  
- [ ] Created your first DataFrame  
- [ ] Loaded `pennData500.csv`  
- [ ] Used `.head()` and `.tail()`  
- [ ] Examined the shape, columns, and data types  
- [ ] Used `.describe()`  
- [ ] Calculated summary statistics  
- [ ] Selected individual columns  
- [ ] Filtered quantitative data  
- [ ] Filtered qualitative data  
- [ ] Completed the Data Detective challenges  
- [ ] Created and answered your own data question  
- [ ] Identified a question the dataset cannot answer  
- [ ] Completed the final reflection  

## If You Finish Early

Continue exploring the Penn dataset.

Try to discover something interesting that was **not specifically asked for in this assignment**.

You may use the Pandas documentation or search for additional Pandas commands.

Some things you might investigate:

- How can you count how many times each value appears?  
- How can you sort a DataFrame?  
- How can you find the standard deviation of a column?  
- How can you find only the rows where **two conditions** are true?

Document anything new that you discover.

Be prepared to show me what you figured out when I return.