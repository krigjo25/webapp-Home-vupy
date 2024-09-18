# Finance

## About this project

### Purpose
The puropose of this website is to use it as a biography of whom i am,  what's been done through my journey.

### What must be learned

-   - 
-   Creating cookies analysis
-   Server analysis

### Description

####    HTML
####    CSS

Thorugh CSS RWD has been the primary Intention
####    Javascript

-   Created a automatic Slider function for the webpage
-    
####    Flask

Github:
Implemented a API which fetches repositories data from GITHUB.


While creating the modal i encounted a challange to store the information which was recieved by the API
I choosed to use SQLite, as there is no need for a huge database or a rational one.

####    SQLite

It's maybe easy to use, but the difference between the other databases it doesnt require a server to operate, nor a license to use. As i don't expect heavy Traffic in HTTP Requests it suits well for personal and educative usage.




### Tests


**test_connection**
During the connection test with the reposory i found out that i could expect
agruments in the fields in the api, as a consequence of using Github REST API,
it's reasonable to believe that if the request is Ok i will recieve the same output
in expected and actual. Therefore it would be best practise to use the actual
dictionary to pass values into the expected json, as the requests returns an
json file if the code is 200, and to hide "sensitive information about a user.

**moc_requests**
By mocking the url i expect to find my repositories avialable


**test_insertion**
**test_update**


In order to visualize the test, i created a test report. So its easier to view the test of the programs.
##  Credits

[flask, flask_session - by the pallets project]()
[pytest, sqlite, os -]()
[dotenv - ]()


## Project summary

- While creating the application i encountered some challanges in
> The modal - Storing information from APIs
>   >   the solution for the issue would be to have a database with the stored information.
>   >   The data is stored, and we do not have to call the API unless there is a update in the GITHUB
>   >   The data can be used in other projects or converted into another database management system,

>   Testing the API function - Automated testing 
> > During the tests  i had to figure out a way to store the expected results with out sharing any sensitive information about the account.
> > I chose to use the request to add the sensitive information, as later on i do not need to hard code the expected result, and then still
> > Ensure the connection to the API. 
-   During the tests of the API function i encounted a challange to test the API with out sharing any sensitive information about the account which was tested
-   -   
-   

-   During this project i've learned alot about RWD what should be prefered to be used during projects
-   During this project i refreshed memories by using what has been learned on the cs50x course.
Sincerely,
@krigjo25
