Churning is a serious issue for companies trying to grow their business. Churning is the instance when a consumer leaves the company for whatever reason, and the company loses valuable business. From Kaggle, I was able to gain access to a data set for the Telco Customer Churn. The goal for this project was to classify each customer and see why they churned, and also to find the top reasons for churning. This can be very valuable information for a company, because knowing why customers are choosing to leave will allow the company to strengthen their vulnerabilities in business. 

Because the goal was to classify the customers to see why they are churning, I chose to use logistic regression to fit the data. With the functions from the sklearn library, I formatted the data into a table so that Each row would consist of one consumer, and the columns would store important information about the customer. The following list shows what information is displayed about a customer in each column:

Gender
Senior Citizen (Yes/No)
Partner (Yes/No)
Dependents (Yes/No)
Tenure with the company
Phone Service (Yes/No)
Type of contract
Paperless Billing (Yes/No)
Payment Method
Monthly Charges
Total Charges
Churn (Yes/No)

To show how the data has been fit into a table, I print the first 5 columns of the newly formatted dataset. To do this, I use panda dataframes. I then calculate the churn rate for the company, which is the percentage of customers that choose to churn. I then find the top 10 reasons for churning and display them. Aside from that, I also calculate the churn rate for each customer service, so that the company can see which of their facilities and services have the highest chance of losing business. 