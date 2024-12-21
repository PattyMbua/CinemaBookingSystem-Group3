# Cinema Booking System

## Group Members:

- Patriciah -152569 Mariam - 147398 Robert -150233 Keith - 147478 Miles - 151090 - Ian Gatumu - 103435

## Project Description:

This is a simple API for a Cinema Booking System built using Django. It allows users to manage cinema bookings, movies, and related entities.

# Save the README content to a markdown file again for download

readme_with_images_path = "/mnt/data/README_with_images.md"

# Create updated README content with image references for Postman screenshots

readme_with_images_content = """

# Cinema Booking API

This project is a Cinema Booking System API built with Django Rest Framework. It supports CRUD operations for Movies, Cinema Halls, Shows, Customers, and Bookings.

---

## 1. Project Implementation

### 1.1 Models and Relationships

- **Movie**:

  - Fields: `title`, `description`, `duration`, `release_date`.
  - Relationships: A `Show` is associated with a `Movie`.

- **CinemaHall**:

  - Fields: `name`, `capacity`.
  - Relationships: A `Show` is associated with a `CinemaHall`.

- **Show**:

  - Fields: `movie`, `cinema_hall`, `start_time`, `end_time`.
  - Relationships: References a `Movie` and a `CinemaHall`.

- **Customer**:

  - Fields: `name`, `email`.
  - Relationships: A `Booking` is associated with a `Customer`.

- **Booking**:
  - Fields: `show`, `customer`, `seats`.
  - Relationships: References a `Show` and a `Customer`.

---

### 1.2 Views/ViewSets and Their Roles

- **MovieViewSet**:

  - Handles CRUD operations for Movies.
  - Example: List all movies or create a new movie.

- **CinemaHallViewSet**:

  - Manages Cinema Hall operations.
  - Example: Update or delete a specific cinema hall.

- **ShowViewSet**:

  - Supports operations for Shows.
  - Example: Create a new show or list all available shows.

- **CustomerViewSet**:

  - Manages Customer operations.
  - Example: Retrieve details for a customer.

- **BookingViewSet**:
  - Handles bookings.
  - Example: Book seats for a show.

---

### 1.3 Serializers and Validation Rules

- **MovieSerializer**:

  - Ensures all fields (`title`, `description`, `duration`, `release_date`) are required.

- **CinemaHallSerializer**:

  - Validates that `capacity` is a positive integer.

- **ShowSerializer**:

  - Validates that `start_time` is earlier than `end_time`.

- **CustomerSerializer**:

  - Ensures `email` follows a valid email format.

- **BookingSerializer**:
  - Validates that the number of `seats` booked does not exceed the available seats for a show.

---

### 1.4 URL Patterns and Their Purpose

- `/api/movies/`:

  - **Purpose**: Manage Movies (GET, POST, PUT, DELETE).

- `/api/cinema-halls/`:

  - **Purpose**: Manage Cinema Halls (GET, POST, PUT, DELETE).

- `/api/shows/`:

  - **Purpose**: Manage Shows (GET, POST, PUT, DELETE).

- `/api/customers/`:

  - **Purpose**: Manage Customers (GET, POST, PUT, DELETE).

- `/api/bookings/`:
  - **Purpose**: Manage Bookings (GET, POST, PUT, DELETE).

---

## 2. Tests Conducted

### 2.1 Postman Testing

- Endpoints tested for Movies, Cinema Halls, Shows, Customers, and Bookings.
- Each endpoint supports:
  - **GET**: Retrieve data.
  - **POST**: Add new data.
  - **PUT**: Update existing data.
  - **DELETE**: Remove data.

#### Evidence of Tests

- **Movies Endpoint**:

  - GET:  
    ![Movies GET](postman_screenshots/screenshot_1.png)
  - POST:  
    ![Movies POST](postman_screenshots/screenshot_2.png)
  - PUT:  
    ![Movies PUT](postman_screenshots/screenshot_3.png)
  - DELETE:  
    ![Movies DELETE](postman_screenshots/screenshot_4.png)

- **Cinema Halls Endpoint**:

  - GET:  
    ![Cinema Halls GET](postman_screenshots/screenshot_5.png)
  - POST:  
    ![Cinema Halls POST](postman_screenshots/screenshot_6.png)

- **Shows Endpoint**:

  - GET:  
    ![Shows GET](postman_screenshots/screenshot_7.png)
  - POST:  
    ![Shows POST](postman_screenshots/screenshot_8.png)

- **Customers Endpoint**:

  - GET:  
    ![Customers GET](postman_screenshots/screenshot_9.png)
  - POST:  
    ![Customers POST](postman_screenshots/screenshot_10.png)

- **Bookings Endpoint**:
  - GET:  
    ![Bookings GET](postman_screenshots/screenshot_11.png)
  - POST:  
    ![Bookings POST](postman_screenshots/screenshot_12.png)

---

### 2.2 Summary of Results

- All endpoints passed the CRUD operations with correct status codes:
  - **200**: Success for GET requests.
  - **201**: Success for POST requests.
  - **204**: Success for DELETE requests.
  - **400/404**: Handled invalid requests appropriately.
