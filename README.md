# Serverless-Registration-WebApp-on-Amazon-Web-Services-AWS-
Registration and Greeting App
Overview
This project is a web application that combines a registration form and a greeting app. It also includes a view counter to track the number of visits to the page.

Features
Registration Form: Users can register by providing their name, email, phone number, and password.

Greeting App: Displays a personalized greeting message after the user submits their name.

View Counter: Tracks and displays the number of views on the page.

Technologies Used
HTML: Structure of the web pages.

CSS: Styling of the web pages.

JavaScript: Client-side functionality for form submission, greeting message, and view counter.

AWS Lambda: Serverless backend for handling registration and view count updates.

DynamoDB: Database for storing registration details and view counts.

Setup
Clone the repository:

bash
git clone https://github.com/your-username/manav.git

cd manav

Deploy the AWS Lambda functions and DynamoDB tables as described in the lambda_functions directory.

Update the API_INVOKE_URL in script.js with your API Gateway endpoint.

Open index.html in your browser to see the app in action.

Usage
Fill out the registration form and click "Submit" to register.

After submitting your name, a personalized greeting message will be displayed.

The view counter will automatically update and display the number of views on the page.

License
This project is licensed under the MIT License.
