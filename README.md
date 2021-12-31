# Landman

This app is a modern approach to a land management application, which generally is designed to be used by the energy industry. This approach uses commonly used frontend and backend frameworks (React.js and Python's Django module, respectively) to create a simplified data management solution.

At this time, the application has not been officially released, and should be treated as a pre-alpha state.

## Debugging

This app uses Docker containerization for the database, frontend (React.js), and backend (Django)

To Debug the app, from the main application directory, run:

> docker-compose pull; docker-compose up -d

Once the containers have been started, you can seed initial data by opening the CLI for the backend container from Docker and running

> python3 manage.py loaddata fixtures/landman/\*.json

## Testing

Tests are split up into separate files for each model and/or view method, and are found in /backend/tests/. When adding a new test class, be sure to import the tests into /backend/tests/\_\_init\_\_.py

To run tests locally, run the following from the backend path:

> python3 manage.py test
