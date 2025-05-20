# krigjo25 | Home
The project was inteded to create as a personal home page, show my what i have done so far
and not as a CS50x assignment, but it killed two birds with one stone.

## Description
[Visual representation of the directory tree](./model/directoryTree.md)
[Future Projects](https://github.com/users/krigjo25/projects/17)

###    Frontend
In the frontend the project is equipped with
* HTML as the content of the webpage
* sass has been used to automatically generate css files for the project.
* Basic Javascrip adds interactivity for the project. ( Automated slider)

The project uses HTML to structure the content of the web pages.

###   Backend
The project is equipped with technologies such as
-   Flask serves as API for the project.

#### [Visual representation](./model/system-architecture.md) of the Web Architecture

#### [Visual representation](./model/endpoints.md) of the Endpoints

#### [Visual representation](./model/apis.md) of the API Classes

#### [Visual representation](./model/utils.md) of the Utils Classes

#### Database
[Visual representation](./model/database.md) of the Database Classes
As a consequence of the project not requires a server to handle database functionallity, SQLite was choosen to keep the records.

### Installation and Configurations

1. Clone the repository:
```sh
#   Using HTTPS
git clone https://github.com/krigjo25/webapp-home-flask.git

#   Using SSH
ssh git@github.com:krigjo25/webapp-home-flask.git

#   Using Github CLI
gh repo clone krigjo25/webapp-home-flask
```

2. Navigate to the project directory
```sh
cd webapp-home-flask
```

3. Install the projects dependencies using pip:
```sh
pip install -r requirements.txt
```
4. Run the project
```sh
flask run --debug  # Running flask in developer and debug mode
```
*** Configuration ***
To configure access to Github create a '.env' file in the project's root directory and add your github token

```env
#   Github Access Token
GITHUB_TOKEN = "Bearer <Your Github Token>"
```

## Testing Framework And Datasets

####    Test Execution
[Visual representation](./model/testmodel.md) of the test cases
To run the tests, use the following commands from the project's root directory

```sh
pytest -v

#   This command will output a report of the tests.
pytest --html=reports.html
```

#####    API Testing
[Visual representation](./model/apis.md) of the apis classes
[Visual representation](./model/testmodel.md) of the test
API tests are conducted using:

- The [GITHUB REST API](https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28)
- The [Heavy REST API](https://api.hevyapp.com/docs/)
- Tests are based on the 

**Connection test (`test_connection`)**
This test validates the connection to the specified APIs.
Given the structure of the Github REST API, successful
connection tests involve comparing identical expected and
actual outputs. The actual response dictionary is therefore
used to define the expected JSON, ensuring that no sensitive
user data is unitetentionally included in the test.

**Repository Availability Test (`mock_request`)**
The test ensures the availability of repositories.
It achives this by mocking the relevant URL from
the GitHub REST API: [Get A Repos](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository)

#####    Databases
[Visual representation](./model/database.md) of the database
Database tests are designed according to the principles
outlined in this unit testing documentation: [test/sqlite.html](https://python-basics-tutorial.readthedocs.io/en/24.1.0/test/sqlite.html)

* **Insertion Test (`test_insertion`)**: This test verifies the correct insertion of data into the database.
* **Update Test (`test_update`)**: This test validates the accurate updating of data within the database.

A test report is generated to provide a clear visualization of the test results.

##   Credits
**Libraries:**

* Flask and Flask-Session:
    * Developed by: The Pallets Project
    * URL: [https://pypi.org/project/](https://pypi.org/project/)
    * Purpose: Web framework and session management

* python-dotenv:
    * Developed by: Saurabh Kumar
    * URL: [https://pypi.org/user/theskumar/](https://pypi.org/user/theskumar/)
    * Purpose: Library for loading environment variables

**Built-in Python Modules:**

* sqlite: Database management
* os: Operating system interactions

**Testing:**

* pytest: Python testing framework

###   License
The project's licensing information can be found in the separate [LICENSE](./license) file.


##  Summary
During the project i some challanges were faced to solve.

###   Model Implementation
During the implementation of the data model, i had to learn how to create a model, 
- I wanted to describe a class and describe its relationship between its subclasses and its functionallity
- 
###   GitHub API Integration
during the implementation of the API Itegration, it was observed that every GET request returned the complete data. 
In order to optimize this process, a scheduling mechanism was implemented to limit data fetching to once per day or when changes in the repository are detected.

the ideal possibility is to create a database

###   Testing
The testing phase provided valuable learning experiences in utilizing Python's built-in `pytest` framework for unit testing.

Key skills acquired during testing include exception handling, API testing using `requests` and `pytest`, and basic database testing.

####   GitHub API Testing
* **Automated API Function Testing:**
    * Challenge: Securely storing expected test results without exposing sensitive account information.
    * Solution: Utilizing the API request itself to retrieve and validate sensitive information, ensuring its presence in successful test cases.
  
* **API Connection Testing:**
    * Challenge: Testing API connectivity without revealing sensitive information associated with the test account.

####   SQLite3 Database Management System Testing
* **Database Connection Testing:**
    * Objective: Validate the ability to establish database connections as required.
* **Exception Testing:**
    * Objective: Verify that appropriate exceptions are raised to inform users of operation failures.


have a glorious rest of your day,
[@krigjo25](https://github.com/krigjo25)

