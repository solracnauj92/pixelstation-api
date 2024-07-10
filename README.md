# [PIXELSTATION API](https://pixelstationproject5-api-1a9dadf46f0b.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/solracnauj92/pixelstation-api)](https://github.com/solracnauj92/pixelstation-api/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/solracnauj92/pixelstation-api)](https://github.com/solracnauj92/pixelstation-api/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/solracnauj92/pixelstation-api)](https://github.com/solracnauj92/pixelstation-api)

---

# Introduction

Welcome to Pixelstation API, a backend service for [Pixelstation](https://pixelstationproject5-api-1a9dadf46f0b.herokuapp.com), providing essential functionality for managing users, profiles, and more.

---
## Installed Apps

The following is a list of Django apps included in the `INSTALLED_APPS` setting in `settings.py`:

- **django.contrib.admin**: Django's built-in administrative interface.
  
- **django.contrib.auth**: Handles user authentication and permissions.
  
- **django.contrib.contenttypes**: Framework for content types and generic relations.
  
- **django.contrib.sessions**: Manages user sessions across requests.
  
- **django.contrib.messages**: Messaging framework for user feedback.
  
- **cloudinary_storage**: Integrates Cloudinary for static and media file storage.
  
- **django.contrib.staticfiles**: Manages static files for serving in production.
  
- **cloudinary**: Cloud-based image and video management service.
  
- **rest_framework**: Django REST framework for building Web APIs.
  
- **django_filters**: Adds dynamic filtering to Django querysets.
  
- **rest_framework.authtoken**: Token-based authentication for Django REST framework.
  
- **dj_rest_auth**: Extends REST framework with additional authentication features.
  
- **django.contrib.sites**: Enables handling multiple websites in a single Django instance.
  
- **allauth**: Complete authentication system for Django including social authentication.
  
- **allauth.account**: Manages user accounts and related functionalities.
  
- **allauth.socialaccount**: Provides social network authentication using Django Allauth.
  
- **dj_rest_auth.registration**: User registration endpoints for Django REST framework.
  
- **corsheaders**: Adds Cross-Origin Resource Sharing (CORS) support.
  
- **profiles**: Manages user profiles or user-specific data.
  
- **posts**: Handles creation and management of posts.
  
- **comments**: Manages comments related to posts or other content.
  
- **likes**: Provides functionalities for liking or favoriting content.
  
- **followers**: Manages user follow relationships.
  
- **forums**: Provides features for creating and managing discussion forums.
  
- **messaging**: Handles messaging functionalities.
  
- **game_library**: Manages game libraries.

# Dependencies

Here are the dependencies used in this project:

- **asgiref** (version 3.8.1)
- **cloudinary** (version 1.40.0)
- **dj-database-url** (version 0.5.0)
- **dj-rest-auth** (version 6.0.0)
- **Django** (version 5.0.7)
- **django-allauth** (version 0.63.3)
- **django-allauth-cas** (version 1.0.0)
- **django-cloudinary-storage** (version 0.3.0)
- **django-cors-headers** (version 4.4.0)
- **django-filter** (version 24.2)
- **djangorestframework** (version 3.15.2)
- **djangorestframework-simplejwt** (version 5.3.1)
- **gunicorn** (version 22.0.0)
- **lxml** (version 5.2.2)
- **pillow** (version 10.3.0)
- **psycopg2** (version 2.9.9)
- **PyJWT** (version 2.8.0)
- **python-cas** (version 1.6.0)
- **pytz** (version 2024.1)
- **setuptools** (version 70.3.0)
- **sqlparse** (version 0.5.0)

### Dependencies Documentation

Documentation for project dependencies is crucial for developers:

- **Understanding Functionality**: Provides insights into how each dependency works and its purpose.
- **Usage Guidelines**: Offers examples and best practices for integration and configuration.
- **API Reference**: Acts as a comprehensive guide to all classes, methods, and parameters.
- **Updates and Changes**: Keeps developers informed about new features, bug fixes, and compatibility issues.
- **Community Support**: Provides forums and resources for troubleshooting and community interaction.
- **Security and Stability**: Ensures secure configurations and stable integrations within projects.

Accurate and accessible documentation enhances development efficiency and promotessoftware solutions.

- **Django**: The web framework
  - [Django Documentation](https://docs.djangoproject.com/en/stable/)

- **django-allauth**: Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
  - [django-allauth Documentation](https://docs.allauth.org/en/latest/)

- **django-rest-auth**: A set of REST API endpoints for handling User Registration, User Authentication, Password Reset, and more.
  - [django-rest-auth Documentation](https://dj-rest-auth.readthedocs.io/en/latest/)

- **djangorestframework**: Powerful and flexible toolkit for building Web APIs.
  - [Django REST framework Documentation](https://www.django-rest-framework.org/)

- **djangorestframework-simplejwt**: A JSON Web Token authentication plugin for Django REST Framework.
  - [djangorestframework-simplejwt Documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

- **django-cors-headers**: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).
  - [django-cors-headers Documentation](https://pypi.org/project/django-cors-headers/)

- **cloudinary**: Cloudinary provides easy-to-use, cloud-based media management solutions for web and mobile developers.
  - [Cloudinary Documentation](https://cloudinary.com/documentation)

- **dj-database-url**: Allows you to utilise the DATABASE_URL environment variable to configure Django applications with a database connection.
  - [dj-database-url Documentation](https://pypi.org/project/dj-database-url/)

- **psycopg2**: PostgreSQL adapter for Python.
  - [psycopg2 Documentation](https://www.psycopg.org/docs/)

- **PyJWT**: JSON Web Token implementation in Python.
  - [PyJWT Documentation](https://pyjwt.readthedocs.io/en/stable/)

These dependencies are listed in `requirements.txt` to ensure consistent development and deployment environments.

# Installation

To install Pixelstation API locally, follow these steps:

```bash
# Clone the repository
git clone <repository_url>
cd pixelstation-api

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a `.env` file and add necessary variables.

# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver