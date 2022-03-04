# Sales-Analysis
Sales Analysis of a store using Python Libraries 

We use Python Pandas and Python Matplotlib to analyse and answer business questions regarding a year's worth of sales data. Hundreds of thousands of electronics store purchases are broken out by month, product kind, price, purchasing address, and other factors.

We begin by clearing up our information. The tasks to be completed during this segment are:

Remove all NaN values from the DataFrame.
Rows are removed based on a criterion.
Modify the column types (to numeric, to datetime, astype).

We'll move on to the data exploration portion once we've cleaned up our data a bit. In this section, we'll look at five high-level business issues that our data can answer:

What month did you have the most sales? How much money did you make that month?
Which city has the most product sales?
When should we show advertisements to increase the chances of customers purchasing the product?
What are the most common products sold together?
What was the most popular product? Why do you believe it was the most popular?

To answer these problems, we'll go over a variety of pandas and matplotlib methods. They are as follows:

Creating a new DataFrame by concatenating numerous csvs (pd.concat)
Columns are being added
Making new columns by parsing cells as strings (.str)
Using the .apply() method
Performing aggregate analysis using groupby
To display our findings, we created bar charts and line graphs.
Adding labels to our graphs
