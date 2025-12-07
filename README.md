# Simple FastAPI Hospital Management System

A **simple hospital management API** built with **FastAPI** and **Pydantic**.  
This project allows you to perform basic **CRUD operations** on patients using an **in-memory storage** (no database required).

---

## Features

- Create, Read, Update, and Delete (CRUD) patients
- FastAPI framework with automatic **Swagger docs**
- Beginner-friendly, lightweight, and easy to extend
- In-memory storage for simplicity (perfect for learning)
- Ready to integrate with a database in the future

---

## Technologies Used

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

---
---| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| POST   | `/patients/`     | Create a new patient |
| GET    | `/patients/`     | Get all patients     |
| GET    | `/patients/{id}` | Get patient by ID    |
| PUT    | `/patients/{id}` | Update patient by ID |
| DELETE | `/patients/{id}` | Delete patient by ID |
