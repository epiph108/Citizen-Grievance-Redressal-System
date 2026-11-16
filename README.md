# Citizen Grievance Redressal System

A backend API built with FastAPI where citizens can register complaints
and track their resolution. Complaints are handled by officers of the
relevant department, and an admin manages the whole system.

This project is under development and is being built step by step
along with my FastAPI learning.

## Tech Stack

- Python
- FastAPI

## Setup

    python -m venv myenv
    myenv\Scripts\activate
    pip install "fastapi[standard]"
    fastapi dev main.py

Open http://127.0.0.1:8000/docs to see the API documentation.

## Current Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | / | Health check |
| GET | /complaints | List of complaints |
| GET | /departments | List of departments |
