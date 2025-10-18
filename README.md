# Backend Wizards - Stage 0

Profile API with dynamic cat facts built with Python/Flask.

## Author
Prince Olamide Babalola

## Stack
Python/Flask

## Setup Instructions

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python flask_profile_api.py
```

5. Test the endpoint:
Visit http://localhost:5000/me in your browser

## API Endpoint

**GET /me**

Returns user profile with a dynamic cat fact.

Response format:
```json
{
  "status": "success",
  "user": {
    "email": "lionspride105@gmail.com",
    "name": "Prince Olamide Babalola",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-17T22:43:25.591727Z",
  "fact": "Random cat fact here"
}
```

## Deployment

Deployed on Railway: [Your URL will go here]

## Repository

GitHub: https://github.com/theGrimghost/backend-wizards-stage0







