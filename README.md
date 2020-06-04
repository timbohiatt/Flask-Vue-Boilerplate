### Boilerplate: Flask and Vue

### Getting Started

Welcome to my Flask and Vue Boilerplate.

When I have a new Web Application to build I go to this template as a starting point. It has almost everything I need to have API's Running within Minutes.

##### Whats Included:

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

- **Celery**

- **Redis**

- **MySQL Database**

### GET IT RUNNING

#### **Prerequisites** 

##### Install Docker and Compose

In order to use this boilerplate you must have `docker` and `docker-compose` installed on your machine. To do this follow the instructions provided by this [link](https://docs.docker.com/get-docker/) to install docker and then use this [link](https://docs.docker.com/compose/install/) to install docker-compose.

#### **Running the Application**

Running the application is simple thanks to the `docker-compose.yml` file. All you need to do is run:

```
docker-compose build
```

followed by

```
docker-compose up
```

It is also possible to run:

```
docker-compose up --build
```

if you want to squash the two commands into one. Stopping the application by running:

```
docker-compose down
```

or if you want to remove the volumes as well:

```
docker-compose down -v
```