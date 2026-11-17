# Citizen Grievance Redressal System

A backend API built with FastAPI where citizens can register complaints
and track their resolution. Complaints are handled by officers of the
relevant department, and an admin manages the whole system.

This project is under development and is being built step by step
along with my FastAPI learning.

## Tech Stack

- Python
- FastAPI
- pydantic-settings

## Setup

    python -m venv myenv
    myenv\Scripts\activate
    pip install -r requirements.txt

Copy `.env.example` to a new file named `.env` and fill in your own values.

    fastapi dev main.py

Open http://127.0.0.1:8000/docs to see the API documentation.

## Project Structure

    main.py          app entry point
    config.py        settings loaded from .env
    routers/         endpoints split by feature

## Current Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | / | Check that the API is running |
| GET | /config | App name and token expiry from settings |
| GET | /complaints | List of complaints |
| GET | /departments | List of departments |
