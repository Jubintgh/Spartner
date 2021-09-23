# Spartner
-Summary

Spartner is inspired by OkCupid based on the idea of finding gym friends who you can train with! The main purpose of the app is to help gym goers find friends for their sports activities based on a match algorithm. Upon sign-up users are directed to fillout a questionare that will be used by the matching algorithm to assign a score for each user that is used by the algorithm

## Application Architecture
- Coin-pal is built using a Flask back-end and a React front-end with postgreSQL as its database. additionally redux architecture was implemented for better management of the state

## Technologies

- Flask
    * Coin Pal uses Flask for its back-end. The api files, forms and database models are built on a Flask back-end. The database models also use Flask SQLAlchemy as the object-relational mapper to interact with the postgres database.
    * Coin pal uses WTForms library to validate the forms on the backend as well as to provide the CSRF protection on sensetive forms.
- React
    * Coin pal is a React application. The front-end logic which controls the display is controlled by React libraries.
- PostgreSQL
    * Coin pal uses PostgreSQL as its database and it interacts with it via Flask-SQLAlchemy


## Features
