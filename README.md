# FastAPI User Management API

A simple REST API built with **FastAPI** for managing users. This project demonstrates the implementation of CRUD operations, automated testing with **pytest**, and Continuous Integration using **GitHub Actions**.

## Features

- Create a user
- Retrieve all users
- Retrieve a specific user by ID
- Update an existing user
- Delete a user
- Prevent duplicate user creation
- Return appropriate HTTP status codes
- Automated unit tests with pytest
- GitHub Actions workflow for Continuous Integration
- Environment variable support using `.env`

## Technologies Used

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- pytest
- gRPC (basic demo)
- GitHub Actions
- python-dotenv

## Project Structure

```text
fastapi-user-management/
│
├── app/
│   ├── grpc/
│   ├── models.py
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── user.proto
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-user-management.git
```

Move into the project:

```bash
cd fastapi-user-management
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key_here
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/users` | Retrieve all users |
| GET | `/users/{id}` | Retrieve a single user |
| POST | `/users` | Create a new user |
| PUT | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |

## Example Request

### Create User

```http
POST /users
```

Request Body:

```json
{
  "id": 1,
  "username": "Ali"
}
```

Successful Response:

```json
{
  "id": 1,
  "username": "Ali"
}
```

## Testing

Run all unit tests:

```bash
python -m pytest
```

Current test coverage includes:

- Root endpoint
- User creation
- Duplicate user validation
- Retrieve all users
- Retrieve a single user
- User not found
- Update user
- Update missing user
- Delete user
- Delete missing user
- Empty user list

## Future Improvements

- Database integration (PostgreSQL or SQLite)
- JWT Authentication
- Password hashing
- Docker support
- API versioning
- User login and registration
- gRPC service expansion
- Deployment to a cloud platform

