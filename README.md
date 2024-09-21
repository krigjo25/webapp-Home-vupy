# krigjo25 | Home

## About this project

### Requirements
Please install the dependencies through the requirements.txt

```fish
pip install -r requirements.txt
```

### Purpose
The puropose of this website is to use it as a biography of whom i am,  what's been done through my journey.

### Description

####    HTML
####    CSS


During this project i've learned alot about RWD what should be prefered to be used during projects,

####    Javascript

-   Created a automatic Slider function for the webpage

####    Flask

Github:
Implemented a API which fetches repositories data from GITHUB.


While creating the modal i encounted a challange to store the information which was recieved by the API
I choosed to use SQLite, as there is no need for a huge database or a rational one.

During this project i refreshed memories by using what has been learned on the cs50x course.

####    Database

As a database i chose SQLite as it doesnt require server to operate nor a license to use, as i do not expect heavy traffic in the datase it suits well for minor projects.


### Tests

####    How to run the tests

To run the test, from the root of the repo
```fish
pytest -v
pytest --html=reports.html
```
####    Requests
Tests are based on the [GITHUB REST API](https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28)

**test_connection**
During the connection test with the reposory i found out that i could expect
agruments in the fields in the api, as a consequence of using Github REST API,
it's reasonable to believe that if the request is Ok i will recieve the same output
in expected and actual. Therefore it would be best practise to use the actual
dictionary to pass values into the expected json, as the requests returns an
json file if the code is 200, and to hide "sensitive information about a user.

**moc_requests**
By mocking the url from [GITHUB REST API](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository) i expect to find my repositories avialable


####    Databases

Tests are based on the [documentation for unit tests](https://python-basics-tutorial.readthedocs.io/en/24.1.0/test/sqlite.html)
**test_insertion**
**test_update**


In order to visualize the test, i created a test report. So its easier to view the test of the programs.
##  Credits

[flask, flask_session - by the pallets project]()
[pytest, sqlite, os - Python built in responsories]()
[dotenv - ]()

### License
see license file


## Project summary

### Modal
While creating the application i encountered some challanges with futures such as API,  database manangement

### Github API

I wanted to create an request to the API so i could automate the process to update the database with new projects.

> I created multiple functions to handle multiple requests, so i could fetch the desired data from Github. And i wanted to automate the process, so the server searches after given updates in Github once a month or when there is a new project available at Github. 
> Some tests was created in the process to confirm the autentity for the functions, to make the process easier. If necessary in the future it is possible to convert the database into another database management system
>


### SQLite database management system
#### Purpose of SQLite

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

> **Testing the Exceptions**


Sincerely,
@krigjo25
