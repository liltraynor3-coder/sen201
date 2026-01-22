
# SEN ASSIGNMENT – Library Management System (Python)

## Project Overview
This project is a **Library Management System (LMS)** developed using Python.  
It allows a librarian to manage books and users, issue and return books, and track library records.

This repository demonstrates the **complete Software Engineering (SEN) SDLC process**, from requirement analysis to implementation and testing.

---

## Software Development Life Cycle (SDLC)

### 1. Requirement Analysis
**Functional Requirements**
- Add new books to the library
- Register users
- Issue books to users
- Return books
- View all books and their status

**Non‑Functional Requirements**
- Simple command-line interface
- Written in Python
- Easy to maintain and extend

---

### 2. System Design
**System Architecture**
- Single Python application
- Uses classes to represent core entities

**Main Components**
- `Book`
- `User`
- `LibrarySystem`

**Data Storage**
- In‑memory storage using Python lists and dictionaries

---

### 3. Implementation
The system is implemented using object‑oriented programming in Python.

Files:
- `main.py` → Entry point of the application
- `library.py` → Core library logic
- `models.py` → Book and User classes

---

### 4. Testing
Testing is done manually by:
- Adding books and users
- Issuing and returning books
- Checking for invalid operations

---

### 5. Deployment
The application runs locally using:
```bash
python main.py
```

---

### 6. Maintenance
The system can be extended to:
- Use a database
- Add authentication
- Build a GUI or web version

---

## How to Run the Project
1. Clone the repository
2. Navigate to the project folder
3. Run:
```bash
python main.py
```

---

## GitHub Repository
Upload this folder directly to GitHub as required by the assignment.
