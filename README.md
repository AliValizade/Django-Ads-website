# Django Ads Website

A Django-based classified advertisements web application for managing categories, advertisements, advertiser information, images, and user accounts.

## Overview

**Django Ads Website** is a web application built with Django for creating and managing classified advertisements.

The project provides a structured backend for:

* User registration and authentication
* Advertisement management
* Hierarchical categories
* Advertisement images
* Advertiser contact information
* Location information
* Advertisement activation/deactivation
* MySQL database integration

The project is designed as an educational and practical Django web application demonstrating how a classified ads platform can be structured using Django's models, forms, views, templates, authentication system, and ORM.

## Features

### User Management

* Custom Django user model
* User registration
* Login and logout
* Authentication-based navigation
* Additional user information such as age

### Advertisement Management

Each advertisement can contain:

* Title
* Description
* Keywords
* Category
* URL
* Advertiser name or company
* Phone number
* Mobile number
* Instagram ID
* WhatsApp number
* State
* City
* Address
* Active/inactive status
* Creation and modification timestamps

### Categories

The application supports hierarchical categories using a self-referencing category model.

Each category can have:

* Title
* Description
* Parent category
* Child categories
* Related advertisements

### Advertisement Images

Advertisements can have multiple uploaded images.

The application also supports assigning a main image to an advertisement.

### Location Information

Advertisements contain structured location information including:

* State
* City
* Address

This provides a foundation for building location-based advertisement browsing in future versions.

## Project Structure

```text
Django-Ads-website/
├── ads/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── migrations/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── registration/
│   ├── _base.html
│   └── home.html
│
├── manage.py
└── requirements.txt
```

## Technology Stack

* **Python**
* **Django 5.0.3**
* **MySQL**
* **Django ORM**
* **Django Authentication**
* **Django Templates**
* **HTML**
* **CSS**

Project dependencies are defined in `requirements.txt`.

## Data Model

The main domain models are:

### Category

Represents advertisement categories and supports parent/child relationships.

### Ad

Represents an individual classified advertisement and contains the main advertisement information, advertiser details, contact information, and location.

### AdImage

Stores images associated with advertisements.

### CustomUser

Extends Django's default user model with additional user information.

## Configuration

The project uses environment variables for sensitive configuration values such as:

* Django secret key
* Database name
* Database username
* Database password

This keeps sensitive configuration outside the source code.

## Installation

Clone the repository:

```bash
git clone https://github.com/AliValizade/Django-Ads-website.git
cd Django-Ads-website
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and configure the required environment variables:

```env
DJANGO_SECRET_KEY=your-secret-key

DATABASE_NAME=your-database-name
DATABASE_USER=your-database-user
DATABASE_PASSWORD=your-database-password
```

Configure your MySQL server according to your local environment.

## Database Setup

Run migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

## Run the Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Django Admin

The Django admin interface can be used to manage:

* Users
* Categories
* Advertisements
* Advertisement images

Create a superuser first and then access:

```text
http://127.0.0.1:8000/admin/
```

## Learning Objectives

This project demonstrates practical Django concepts including:

* Django project structure
* Django applications
* Models and relationships
* Self-referencing foreign keys
* Custom user models
* Model forms
* Class-based views
* Authentication
* Django admin
* File and image uploads
* URL routing
* Templates
* MySQL integration
* Environment-based configuration
* Django ORM

## Future Improvements

Possible improvements for future versions include:

* Advanced advertisement search
* Filtering by category and location
* Pagination
* User dashboard
* Advertisement creation/editing from the frontend
* Favorites and saved advertisements
* Advertisement expiration
* Advanced image management
* Search by keywords
* REST API
* Better frontend/UI
* Responsive design
* Advertisement statistics
* Moderation workflow
* SEO improvements

## Project Status

This repository represents an educational and practical Django web application and can serve as a foundation for developing a more complete classified advertisements platform.

## Author

**Ali Valizade**

Python Developer | Django | AI, NLP & Automation | University Instructor

GitHub: [AliValizade](https://github.com/AliValizade)
