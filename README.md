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

#### Flask [Backend]

To get up and running with this boilerplate you simply need to configure the .env file with the appropriate configuration for your app.

Under normal circumstances you should not include the .env file within your git repository. It can often contain sensitive information.

**Step 1** Create a virutal environment within the api folder.

**Step 2** Pip Install the Requirements File.

**Step 3** SH Run the boot-app.sh script.

#### Vue [Frontend]
