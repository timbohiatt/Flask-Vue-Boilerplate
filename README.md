### Boilerplate: Flask and Vue

### Getting Started

Welcome to my Flask and Vue Boilerplate.

When I have a new Web Application to build I go to this template as a starting point. It has almost everything I need to have API's Running within Minutes.

##### Whats Inclued:

- **Flask**

  - Configures for primary use as an API Provider.
  - Configured with SQL Alchemy for ORM
  - Configured with Flask-Migrate for managing DB Updates.
  - Configured with Flask Marshmellow for ORM Schema Serialization.
  - Configured with Celery Launcher for Background Tasks
  - Configured with Flask Mail, for sending Emails. [mail server required]
  - Configured with UnitTest installed and setup to run on launch.
  - Configured with Flask Blueprints
  - Flask CLI
    - With CLI code for Database Destruction on Local Build.
    - With CLI code for Loading Initial Data from Config Files.
    - With CLI code for Running Unit Tests
  - Initial POST and GET Routes for User Management _[For Reference]_
  - Initial User Model _[For Reference]_
  - Unit Testing for User Model [For Reference]

- **VueJS**
  - Configured with Nuxt
  - Configured with Vue Router
  - Configured with Vuex
  - Configured with Axios
    - With Links back to Flask Backend.
  - Configured with Vuetify for Frontend Framework
  - Configured with Jest for Testing Framework
  - Configured with ESLint for Linting Code.
  -

### GET IT RUNNING

#### **Prerequisites** 

##### Create Application DB

In order to use the Flask API Backend out of the box you will be required to have already configured a MySQL Database and provide the Database Information and Credentials to a `.env` within the `api/.env` space. 

This Application DB will be used by your core application should you choose to store any Data. The Flask Application will communicate with this DB via an [ORM](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) process using [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/). 

**Steps to Complete:**

- Create a MySQL DB. 
- Create a DB User. 
- Set DB User to have the Role DB Administrator on your newly created DB.
- Populated `DB_USER, DB_PASS, DB_NAME` within your `api/.env` file. 



#### Running Flask [API Backend]

To get up and running with this boilerplate you simply need to configure the .env file with the appropriate configuration for your app.

Under normal circumstances you should not include the .env file within your git repository. It can often contain sensitive information.

**Step 1** Create [MySQL](https://www.mysql.com/) DB and User. Provide User permissions as DBA.

**Step 2** Create a [virutal environment](https://virtualenv.pypa.io/en/latest/) within the api folder.

- Run: `virtualenv venv`

**Step 3** Activate the Virtual Environment.

- Run: `source venv/bin/activate`

**Step 4** Pip Install the Requirements File.

**Setp 5** Create `.env` file within API Directory `api/`

This file should contain the following options:

 APP_NAME=<INSERT APP NAME>
​ APP_PORT=<INSERT APP PORT> \* Recommend 5000
​ APP_ENV=LCL

 DB_NAME=<INSERT DB NAME>
​ DB_USER=<INSTERT DB USERNAME>
​ DB_PASS=<INSTERT DB PASSWORD>
​ DB_HOST=<INSERT DB HOST> \* If not proivded. Assumes LOCALHOST

**Step 6** Kick off the App

- Run: `sh boot-app.sh`
  - Running `boot-app.sh` will do the following by default. 
    - It will destroy, tear down and delete all data and structures within your existing MySQL DB. 
    - It will create all new deployment scripts based on code revisions within the `models.py` file. Building out any ORM Objects from SQLAlchemy into MySQL objects in the DB. 
    - It will run all Automated Tests within the `api/tests` directory. 

**Notes:**

- **Environment Variables in .env files**. 
  - **APP_ENV is set to LCL.** The Database of the application will be completly rebuilt with every restart of the core application. Should you wish to maintain the data in the DB when rebooting the application during development you should change this vairable to another string. For example DEV
  - **APP_PORT** this is the port that the Flask Application will run on. It should also match the PORT included in your API String in the .env file for your VUE Frontend or any other tool, for example Postman, used for testing API calls. We reccomend 5000 as the default. The APP_PORT variable is referenced in multiple locations through out the codebase and should only be modified within the .env file to ensure consistency across the application.
- **Other Databases** should you wish to use a DB that is not MySQL this is totall possible. Flask Doesn't restrict. However this application has been configured for MySQL. In order to change the DB type you will need to explore the `config.py` file within the API directory and modify the `DB_URI` under Database Vairables section of the `Config` class to remove the `mysql+pymysql://` URI component.  
- **Unit Testing** is enabled by default when you run the command `sh boot-app.sh`. The Boilerplate utilises [Python Unittest](https://docs.python.org/3/library/unittest.html) for Unit Testing. If you look at this shell script you can see that it calls [flask cli](https://flask.palletsprojects.com/en/1.1.x/cli/) command `flask run-unit-tests` this in turn will run all tests that are configured within the `api/tests/` directory. You can disable these from running by removing this line. You can also run the tests manually executing `flask run-unit-tests` directly in the command line. By default there are some example tests for the User Model. Testing User Object creation in the DB and Querying by ID. You can write additional tests by examining those examples of by reading the documentation on [Python Unittest](https://docs.python.org/3/library/unittest.html).



#### Vue [Frontend]
