# AWS-Projects
AWS tutorials and practice projects showcasing serverless applications
A simple AWS Lambda project that calculates base^exponent, stores results in DynamoDB, and displays them via a JavaScript frontend. Based on a tutorial, with modifications for learning and customization

Power of Math Project
This project is a simple calculator that computes the power of a number (base^exponent) using AWS Lambda and stores the results in DynamoDB. The frontend is built with HTML and JavaScript, hosted via AWS Amplify or any static web host.
Overview
Users enter a base number and an exponent.
The frontend sends the numbers to an AWS Lambda function via API Gateway.
The Lambda function calculates the result, stores it in DynamoDB, and returns the result to the user.
CORS headers are included so the frontend can interact with the Lambda function securely.
Tutorial Reference
This project was created while following an AWS tutorial to learn the basics of:
AWS Lambda functions
API Gateway integration
DynamoDB database operations
Connecting a frontend with backend AWS services
Note: The code is not entirely original. It was based on the tutorial, but I modified it to my liking for learning and customization purposes.
Folder Structure
aws-projects/
  ├─ lambda/
  │   └─ power_of_math.py       # AWS Lambda function
  ├─ frontend/
  │   └─ index.html             # Frontend HTML + JS
  ├─ README.md                  # This file
  └─ .gitignore                 # Files to ignore in GitHub
How to Use
Deploy the Lambda function to AWS.
Connect it to API Gateway.
Update the frontend index.html with your API Gateway URL.
Open index.html in a browser, enter numbers, and click CALCULATE.
Notes
Replace the placeholder DynamoDB table name in the Lambda code with your actual table.
Replace the API Gateway URL in the frontend with your own.
This project is intended for learning purposes and does not contain sensitive credentials.
Tutorial Link
The tutorial that was followed: https://www.youtube.com/watch?v=7m_q1ldzw0U&t=815s
