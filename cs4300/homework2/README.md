# Movie Theater Booking App

A Django + Django REST Framework app for viewing movies, booking seats, and checking booking history — with both a REST API and a Bootstrap-based web UI.

## Live Demo
Render URL: https://cs4300-otnk.onrender.com

**Note on data:** This app uses SQLite, which resets on redeploy on Render's free tier. The current live data (movies, seats) was added directly through /admin/ and will remain visible unless the app is redeployed again.

## Features
- View movie listings (via API and web page)
- Book seats for a movie, with per-movie seat availability (via API and web page)
- View and cancel booking history (via API and web page)


## API Endpoints
- `GET/POST /api/movies/` — list and create movies
- `GET/POST /api/seats/` — list and create seats
- `GET/POST /api/bookings/` — view booking history, create new bookings

## Setup Instructions (Local)
1. Clone the repo: `git clone https://github.com/nicoleleva1/cs4300`
2. Navigate into the project: `cd homework2`
3. Create a virtual environment: `python3 -m venv myenv`
4. Activate it: `source myenv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver 0.0.0.0:3000`

## Running Tests
- Unit/integration tests: `python manage.py test`
- Test coverage: `coverage run --source='.' manage.py test && coverage report`
- BDD tests: `python manage.py behave`

## AI Usage Disclosure
Claude (Anthropic) was used throughout this assignment to help generate boilerplate code for models, views, serializers, templates, and test cases; to explain Django and Django REST Framework concepts; and to troubleshoot environment, git, and deployment errors (virtual environment issues, CSRF/ALLOWED_HOSTS configuration, Render deployment setup, and a per-movie seat availability bug). All generated code was reviewed, tested, and adjusted by me before being included in this project.

