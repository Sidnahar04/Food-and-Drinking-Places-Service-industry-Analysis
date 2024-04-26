# Food and Drinking Places Service Industry Analysis

This project aims to address this critical gap by developing a robust methodology to determine the most promising areas in Canada for launching businesses based on key financial metrics. The primary objective is to provide aspiring entrepreneurs and established businesses alike with actionable insights into potential locations that offer the highest prospects for profitability and sustainability.

## Problem Statement
In the dynamic landscape of Canadian business, entrepreneurs face the daunting challenge of selecting the most lucrative locations to establish their ventures. The decision-making process involves a multitude of factors, including operating expenses, operating revenues, sales wages, and commissions. However, the lack of a comprehensive analysis tool leaves many entrepreneurs navigating this decision through trial and error, often resulting in suboptimal outcomes.

### Key Objectives
1.	Conduct a detailed analysis of financial performance metrics for food service businesses across Canada to provide stakeholders with industry insights.
2.	Utilize data analysis to identify trends and regional variations in operating revenue, expenses, and profit margins.
3.	Investigate factors such as operating expenditure and revenue potential to guide stakeholders in selecting optimal business locations and types.

Project Strategy

![image](https://github.com/Sidnahar04/Food-and-Drinking-Places-Service-industry-Analysis/assets/68987629/279228a1-1147-46f0-9050-399923e04327)

### Data Collection
Retrieve dataset from Stat Canda: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2110017101

Annual sample survey gathering economic data for Canada's Food Services and Drinking Places industry. Aggregated with other sources for national and provincial economic estimates. Used by businesses, governments, investors, and associations to monitor industry growth, and performance, and make informed comparisons. Administered as part of the Integrated Business Statistics Program (IBSP) to streamline reporting across industries and improve data coherence. Part of the Service Industries Program, providing financial statistics for over thirty service industry groupings.


## Exploratory Data Analysis

1. Analysis of Financial Metrics across Canada

![image](https://github.com/Sidnahar04/Food-and-Drinking-Places-Service-industry-Analysis/assets/68987629/c4e0b22f-346d-4c18-a5f5-04a78abf1998)

Interpretations

It compares various financial metrics across different types of businesses and regions for the years 2012 and 2022. Currently, the image is showing for 2020 to 2022

The dashboard interface features a user-friendly design with filters conveniently positioned on the left-hand side.

These filters allow users to customize their data analysis according to three main criteria:

•	Year: Users can select the specific year or range of years they want to analyze, providing flexibility in examining trends over time.

•	Financial Metrics: This filter enables users to choose from a variety of financial indicators or metrics to focus on, such as revenue, profit, expenses, or any other relevant financial data.

•	Type of Business: Users can narrow down their analysis by selecting the type of business they are interested in, which could include categories like retail, manufacturing, services, etc.

The primary visualization tools on the dashboard are a graph and a heatmap. These tools allow users to visually compare and analyze the selected data intuitively:

•	Graph: The graph provides a visual representation of the selected data, allowing users to observe trends, patterns, and relationships over the chosen time period and across different financial metrics. Users can customize the graph to display data for specific provinces or regions of Canada.

•	Heatmap: The heatmap offers a different perspective by displaying data in a color-coded grid format. This allows users to quickly identify areas of high or low performance across different provinces and financial metrics. The color intensity indicates the magnitude of the data values, making it easy to spot outliers or areas of interest.

2. Dashboard 2 – Analysis of salaries, wages and commissions across Canada

![image](https://github.com/Sidnahar04/Food-and-Drinking-Places-Service-industry-Analysis/assets/68987629/54f3a608-05a0-4736-bc12-3a9be68ed2ca)

Interpretations - It includes the following two graphs:

•	Analysis of Salary, Wages and Commission expenses across Canada for each business type

o	Highest and Lowest: The province with the highest average salary, wages, and commission expenses appears to be Ontario, followed by Alberta and British Columbia. The province with the lowest average salary, wages, and commission expenses appears to be Prince Edward Island, followed by Newfoundland and Labrador and New Brunswick.

o	Eastern vs. Western Canada: The chart suggests that the average salary, wages, and commission expenses tend to be higher in Western Canada compared to Eastern Canada. There could be several reasons for this, such as the cost of living, the types of industries that are prevalent in each region, or government regulations.

•	Tree Structure to view overall info of data - The visualization aims to provide stakeholders or the audience with clear insights into:

o	Regional variations in compensation.

o	How different industries contribute to the overall financial landscape in Canada.

o	Potential areas for further investigation or improvement in terms of compensation policies or economic development strategies.

3.	Year Wise contribution of Provinces towards financial metrics

![image](https://github.com/Sidnahar04/Food-and-Drinking-Places-Service-industry-Analysis/assets/68987629/eb841483-9f01-436e-8168-99fdff48b04c)

Interpretations

•	Operating Expenses: Quebec seems to have the highest operating expenses throughout the years listed (2012-2022), with a significant decrease in 2020 (23.11%) compared to 2019 (31.42%). Ontario and Alberta follow with consistently lower operating expenses throughout the period.

•	Operating Revenue: British Columbia seems to have the highest operating revenue throughout most of the years listed, with a significant increase in 2020 (35.68%) compared to 2019 (25.33%). Ontario and Alberta have consistently lower operating revenue compared to British Columbia.

•	Salaries, Wages, Commissions and Benefits: Ontario has the highest contribution to salaries, wages, commissions and benefits throughout most of the years listed, though Alberta is close behind. Quebec seems to have had a significant drop in 2020 (16.11%) compared to 2019 (20.01%).

## Model Deployment

1.	Preparation of the Model:
   
    •	Train and optimize your linear regression model using the desired dataset.
  	
    •	Serialize the trained model using a library pickle to save it to disk.
  	
2.	Set Up Flask Application:
   
    •	Create a new directory for your Flask application.
  	
    •	Set up the basic structure of your Flask app, including creating an app.py file for your application logic.
  	
3.	Creating Flask Routes:

    •	Define routes in your Flask app to handle requests from clients.
  	
    •	Create a route for model inference where input data is sent to the model for prediction.
  	
4.	Load the Model:
    •	Load the trained linear regression model into your Flask application.
  	
    •	You can load the model in the Flask application startup or within the route where it's needed.
  	
5.	Parse Input Data:
   
    •	Parse the input data sent from the client within the Flask route.
  	
    •	Ensure that the input data is in the correct format expected by the model.
  	
6.	Perform Prediction:

    •	Use the loaded model to perform predictions on the input data.
  	
    •	Pass the input data to the model and obtain the predicted output.
7.	Return Predictions:

    •	Return the predicted output to the client as a response to the request.
  	
    •	Format the response in JSON or any other appropriate format.
8.	Run the Flask App:
   
    •	Run the Flask application using the Flask development server and running it on local machine.

#### Web Application Flow
![image](https://github.com/Sidnahar04/Food-and-Drinking-Places-Service-industry-Analysis/assets/68987629/1974797f-57d2-4ff0-a7c2-d41330168e6a)


## Tools & Technologies Used

Power BI: Used for data visualization and creating interactive dashboards to present machine learning insights.

Python: Utilized for data preprocessing, model development, evaluation, and integration with machine learning libraries of scikit-learn.

Flask: Employed for deploying machine learning models as web services or APIs, facilitating real-time predictions and integration with web and mobile applications.




   









