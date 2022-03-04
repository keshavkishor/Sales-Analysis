# Sales-Analysis
Sales Analysis of a store using Python Libraries and Google Colab

We use Python Pandas and Python Matplotlib to analyse and answer business questions regarding a year's worth of sales data. Hundreds of thousands of electronics store purchases are broken out by month, product kind, price, purchasing address, and other factors.

We begin by clearing up our information. The tasks to be completed during this segment are:

1. Remove all NaN values from the DataFrame.
2. Rows are removed based on a criterion.
3. Modify the column types (to numeric, to datetime, astype).

We'll move on to the data exploration portion once we've cleaned up our data a bit. In this section, we'll look at five high-level business issues that our data can answer:

1. What month did you have the most sales? How much money did you make that month?
2. Which city has the most product sales?
3. When should we show advertisements to increase the chances of customers purchasing the product?
4. What are the most common products sold together?
5. What was the most popular product? Why do you believe it was the most popular?

To answer these problems, we'll go over a variety of pandas and matplotlib methods. They are as follows:

1. Creating a new DataFrame by concatenating numerous csvs (pd.concat)
2. Columns are being added
3. Making new columns by parsing cells as strings (.str)
4. Using the .apply() method
5. Performing aggregate analysis using groupby
6. To display our findings, we created bar charts and line graphs.
7. Adding labels to our graphs


RESULTS

 What month did you have the most sales?
![Sales Vs Months](https://user-images.githubusercontent.com/87081613/156742774-aef57d01-acff-40ee-8c20-352e46f5fd38.png)







Which city has the most product sales?
![Sales Vs Cities](https://user-images.githubusercontent.com/87081613/156742895-7a7e503d-0e9b-46f4-b96e-df24faa0abd8.png)












When should we show advertisements to increase the chances of customers purchasing the product?
![Order Vs Hour](https://user-images.githubusercontent.com/87081613/156742992-c28a30e4-59c2-4946-8baf-d833686eead0.png)













What are the most common products sold together?
<img width="1440" alt="Screenshot 2022-03-04 at 3 36 10 PM" src="https://user-images.githubusercontent.com/87081613/156743207-c54477e4-c4ea-4320-9322-be27cac640d4.png">















What was the most popular product?
![Qunatity Vs Product Name](https://user-images.githubusercontent.com/87081613/156743292-21faa974-9580-4820-95b1-73a0eecb0700.png)

