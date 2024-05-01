## Overview

This Flask application contains the newsletter subscription management functionality. This application has been built using **Python 3.8 & pip 24**.

## Installation Instructions

### Installation

Pull down the source code from this Git repository:

```sh
$ git clone https://github.com/hazique/newsletter-subscription-mgr.git
```

Create a new virtual environment:

```sh
$ cd newsletter-subscription-mgr
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages specified in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

### Database Initialization

This Flask application needs a SQLite database to store data.  The database should be initialized using:

```
(venv) $ flask init_db
```

### Running the Flask Application

Run development server to serve the Flask application:

```sh
(venv) $ python -m flask run
```

The repository contains a Postman collection (newsletter-subscription-mgr.postman_collection.json) for testing requests. Please install [Postman](https://www.postman.com/downloads/) to run those requests. Also, the tests initialize an app instance. Running the tests successfully means the app behaves the way it is supposed to. Instructions on running the tests are mentioned below.

## Key Python Modules Used

* **Flask**: micro-framework for web application development which includes the following dependencies:
  * Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server
* **pytest**: framework for testing Python projects
* **Flask-SQLAlchemy** - ORM (Object Relational Mapper) for Flask
* **coverage** - analyzes code coverage


## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ coverage run -m pytest
```


## Design Decisions
1. Python-Flask for ease of configuration and availability of a wide range of extensions for development.
2. Using Flask-Restful to create routes as resources and bundle endpoints as if it were a namespace into a single Python class.
3. Using SQLlite as DB for local development to allow any developer to start contributing without need for a complicated DB setup.
4. Using separate config class to start the application is Dev, Test and Prod environments.
5. Ease of testing.

## Tradeoffs
1. Flask handle requests synchronously. In order to handle requests asynchronously and scale, we would need to run the application in an ASGI server.
2. To make the application feature rich, we'd have to use third party modules. This can lead to security vulnerabilities.
3. This demo project does not contain user authentication as it wasn't in the scope of the assignment.