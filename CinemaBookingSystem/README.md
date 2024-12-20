# Cinema Booking System

## Group Members:
- Patriciah -152569 Mariam - 147398 Robert -150233 Keith - 147478 Miles 
  - 151090

## Project Description:
This is a simple API for a Cinema Booking System built using Django. It allows users to manage cinema bookings, movies, and related entities.

## Models:
- **Movie**: Represents a movie with a title, description, and release date.
- **Booking**: Stores information about a booking, such as the movie and user.
- **User**: Extends Django's User model for custom user fields.

## Views/Viewsets:
- The project uses **Django REST Framework** viewsets to handle CRUD operations for each model.

## Serializers:
- The serializers are responsible for transforming model data into JSON format and vice versa.

## URLs:
- The URLs route to appropriate views for each CRUD operation, following RESTful conventions.

## Testing:
- All API endpoints are tested using **Postman** to ensure correct functionality (GET, POST, PUT, DELETE operations).
- You can test the API by running the server locally (`python manage.py runserver`).

## Setup Instructions:
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd CinemaBookingSystem
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Contributions:
- Each group member worked on a specific aspect of the project (e.g., models, views, testing).

