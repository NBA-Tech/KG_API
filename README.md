

# HappyFeet API

## Introduction

This is a FastAPI application that provides a RESTful API for managing contacts, students, staff, events, and settings for the happy feet app.

## Requirements

To run this application, you need to install the required dependencies. You can do this by running the following command from the requirements directory:

```
pip install -r requirements.txt
```

## Environment Variables

You need to update the `.env` file with the environment variables provided by the dev team. This file should contain the following variables:

* `DATABASE_URI`
* `FIREBASE_CREDS_PATH`
* `STORAGE_BUCKET_ID`

## Running the Application

To run the application, navigate to the root directory of the project and run the following command:

```
uvicorn api.main:app --reload
```

This will start the development server with automatic reloading.

## Creating a New Virtual Environment

To create a new virtual environment, you can use the following steps:

1. Open a terminal or command prompt.
2. Navigate to the root directory of the project.
3. Run the following command to create a new virtual environment:
```
python -m venv venv
```
This will create a new virtual environment named `venv`.

4. Activate the virtual environment:
```
source venv/bin/activate
```
On Windows, use `venv\Scripts\activate` instead.

5. Install the required dependencies:
```
pip install -r requirements.txt
```
6. Update the `.env` file with the environment variables.
7. Run the application:
```
uvicorn api.main:app --reload
```

## Accessing the API

Once the application is running, you can access the API by navigating to `http://localhost:8000` in your web browser. You can also use a tool like `curl` or a REST client to send requests to the API.

## API Endpoints

The API provides the following endpoints:

* `/api/v1/contacts`: Manage contacts
* `/api/v1/students`: Manage students
* `/api/v1/staff`: Manage staff
* `/api/v1/events`: Manage events
* `/api/v1/settings`: Manage settings

You can find more information about each endpoint by accessing the API documentation at `http://localhost:8000/docs`.