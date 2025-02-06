# krigjo25 | Home

## Video Demo: [Video demo](https://youtu.be/n-jNhiu5Nm0)

## Overview
This project was not intended to use as an assignment for CS50x, but it kills two birds with one stone. The purpose of this website is to use it as a biography of who I am,  what's been done through my journey.

The application will create a new file called app.log, where Server information will be logged to control its behavior

## Description

###    HTML
The project uses HTML to structure the content of the web pages.

###    CSS
Cascade Style Sheets has been automaticly generated using Sass complier


###    Sass
Sass was used to style the web pages. Including RWD to ensure the webpage is viewable for various devices.

###   Javascript
The JavaScript is used to add interactivity to the web site.
- Automated Slider (Non functional as im going to go over to a Instagram API later) is implemented for the carusel

####    React


###   Flask
During the planning, Flask was chosen as the web framework because of it's flexiblibility and ease of use. It provides the backend logic and API endpoints to fetch data from Github.

####   Database
SQLite is used as the Database Management System.

It is lightweight and doesn't require a server, which makes it suitable for the project.

### Requirements
Please install the dependencies through the `requirements.txt` :
```sh
pip install -r requirements.txt
```

Create a .env file
```env
#   Tokens
GITHUB_TOKEN = "Bearer <Your Github Token>"
```

### Testing Framework And Datasets

####    How to run the tests
To run the test, from the root of the repo
```sh
pytest -v
pytest --html=reports.html
```
####    Requests
Tests are based on the [GITHUB REST API](https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28) & [Heavy REST API](https://api.hevyapp.com/docs/)
Tests are based on the 

**test_connection**
During the connection test with the reposory i found out that i could expect agruments in the fields in the api, as a consequence of using
Github REST API,it's reasonable to believe that if the request is Ok
i will recieve the same output in expected and actual. Therefore it
would be best practise to use the actual dictionary to pass values
into the expected json, as the requests returns an json file if the
code is 200, and to hide "sensitive information about a user.

**moc_requests**
By mocking the url from [GITHUB REST API](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository) i expect to find my repositories avialable


####    Databases
Tests are based on the [documentation for unit tests](https://python-basics-tutorial.readthedocs.io/en/24.1.0/test/sqlite.html)
**test_insertion**
**test_update**


In order to visualize the test, i created a test report. So its easier to view the test of the programs.

##  Credits
[flask, flask_session - by the pallets project](https://pypi.org/project/Flask/)
[pytest, sqlite, os - Python built in responsories]()
[dotenv - Saurabh Kumar](https://pypi.org/user/theskumar/)

### License
See the seperate file LICENCE

## Project summary

### Modal
During the creation of the model some challanges with the API was encountered.

### Github API
While fetching the API i encountered an issue that for everytime
the program sends a GET request. The program fetches the whole repo
I choose to create an intervaler in order to just fetch once a day or when there is something new in the Repo.

Filtering by language wasn't as easy as i expected, because of some strange bug in the system, i couldn't add a custom language to the list.


## Tests
During the tests i learned alot about how to use Python's built-in pytest as unit testing network.

During the testing stage, raising exceptions durng the tests was learned.

I learned to test an API using requests and pytest repository
i learned basic database testing using Unit testing repository

#### Github API
>   **Testing the API function - Automated testing**<br>
>  During the tests  i had to figure out a way to store the expected results with out sharing any sensitive information about the account.
>  I chose to use the request to add the sensitive information, as i can expect that information to be added if the test should do succseed.
>
> **Ensure the connection to the API.**<br>
> During the tests of the API function i encounted a challange to test the API with out sharing any sensitive information about the account which was tested.

#### Database Management system SQLite3
> **Testing the Database connection**
> By testing the database connection, 
> we can ensure that the database can be connected in a requested way

> **Testing the Exceptions**
> While testing Exceptions, We can ensure the user to know what excatly went wrong under the operation
> **Testing the request**

## JavaScript

### React
Through this repository i have learned how to initialize React environment with a python based server such as Flask
Sincerely,
@krigjo25

