# Job Application Portal

A full-stack web application for managing job listings and applications. The portal allows users to browse available jobs, submit applications, and store the data securely in a database.

## Features
- Display a list of available jobs.
- Allow users to submit job applications through a HTML form.
- Store applications securely in a database.
- Responsive design for a seamless experience across devices.
- Deployed to a cloud hosting platform for easy access.

## Tools, Libraries & Frameworks Used

### **Flask**
- Used as the **backend framework** to create the web application.
- Managed routes for:
  - Displaying job listings.
  - Handling job application forms.
  - Serving HTML templates dynamically.

### **Python, HTML, CSS, SQL**
- **Python**: The primary programming language for the backend logic, database interactions, and data processing.
- **HTML**: Designed the structure of web pages like job listings, application forms, and confirmation pages.
- **CSS**: Styled the frontend to make it visually appealing and user-friendly.
- **SQL**: Managed database operations, such as storing job and application data.

### **Bootstrap**
- Used for **responsive frontend design**:
  - Ensured the application worked well across various devices and screen sizes.
  - Leveraged Bootstrap components (forms, grids, modals) for faster UI development.

### **SQLAlchemy**
- Served as the **ORM (Object Relational Mapper)**:
  - Simplified database queries and operations.
  - Managed the connection to the database.
  - Provided methods to interact with tables (e.g., `Jobs`, `Applications`).

### **Aiven (DB)**
- Used as a **cloud-hosted database solution**:
  - Stored job postings and application data.
  - Ensured data persistence and scalability for your project.

### **Gunicorn**
- Deployed as the **WSGI HTTP Server**:
  - Facilitated running your Flask application in a production environment.
  - Managed concurrent requests efficiently for better performance.

### **Render**
- Used for **hosting the web application**:
  - Deployed the Flask app and connected it to the Aiven database.
  - Ensured continuous availability and access via a public URL.

## Database Schema

### **Jobs Table**
- `id`
- `title`
- `location`
- `salary (optional)`
- `currency (optional)`
- `responsibilities`
- `requirements`

### **Applications Table**
- `id`
- `job_id`
- `first_name`
- `last_name`
- `email`
- `phone`
- `address`
- `city`
- `state`
- `zip`
- `link` (for resume)
