![lgogwall](Documentation/images/logowallpaper.jpg) 
# [PIXELSTATION API](https://pixelstationproject5-api-1a9dadf46f0b.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/solracnauj92/pixelstation-api)](https://github.com/solracnauj92/pixelstation-api/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/solracnauj92/pixelstation-api)](https://github.com/solracnauj92/pixelstation-api/commits/main)




Welcome to Pixelstation API, a backend service for [Pixelstation](https://pixelstationproject5-api-1a9dadf46f0b.herokuapp.com), providing essential functionality for managing users, profiles, and more.


## Aim of the Website

Pixel Station aims to create a dynamic and inclusive community that celebrates the timeless charm of retro gaming. Join us on this nostalgic journey!

## Key Findings from User Research

At the beginning of the Pixel Station project, conducting thorough research was essential, even though this project mainly focuses on backend development. Understanding the target audience and the types of users I aim to attract helped shape the overall feel of the website, ensuring that the correct Django apps are implemented to meet user needs.

### Target Audience

![Users](Documentation/images/users.jpg) 

Pixel Station caters to a diverse group of gaming enthusiasts:

1. **Retro Gamers (30-50):**
   - Nostalgic for classics like Super Mario Bros.
   - Enthusiastic about discussing gaming evolution.

2. **Content Creators (20-35):**
   - Streamers and YouTubers focusing on retro gaming.
   - Seeking a collaborative community.

3. **Casual Gamers (18-30):**
   - Curious about the origins of gaming.
   - Open to discovering vintage titles.

4. **Parent-Educators (30-50):**
   - Parents introducing kids to childhood games.
   - Educators incorporating retro games into teaching.

5. **Generation Alpha (5-15):**
   - Kids and teens curious about gaming history.
   - Introduced to classic games by family.

6. **Collectors and Historians (All Ages):**
   - Collectors of retro gaming items.
   - Engaging in discussions about gaming eras.

### User Personas

1. **As a Classic Gamer:**
   - I want to browse and join discussions about my favorite classic games to connect with like-minded enthusiasts.

2. **As a Retro Streamer:**
   - I want to share my retro gaming experiences, collaborate with fellow creators, and grow my audience within the Pixel Station community.

3. **As a Casual Explorer:**
   - I want to discover and learn about vintage games, understanding their impact on the gaming industry.

4. **As a Gaming Parent:**
   - I want to find recommendations for classic games suitable for my child's age and interests, fostering a shared gaming experience.

5. **As a Teacher:**
   - I want to access resources that help integrate retro gaming into my teaching methods, making learning more engaging for my students.

6. **As a Generation Alpha Gamer:**
   - I want to explore the history of gaming, play classic games, and connect with other young gamers who share similar interests.

7. **As a Retro Collector:**
   - I want to showcase my collection, discuss rare finds, and connect with other collectors to exchange tips and experiences.

8. **As a Historian:**
   - I want to contribute to discussions about the historical significance of different gaming eras and share my knowledge with the community.

### Testimonials generated 

1. **Johnny - Retro Gamer (Age: 38):**
   > "Pixel Station has reignited my love for classic games! Connecting with fellow enthusiasts in the community has been a blast. The discussions about gaming evolution take me on a trip down memory lane. This platform truly captures the essence of retro gaming."

2. **Sam- Casual Explorer (Age: 25):**
   > "Being a casual gamer, I was curious about vintage titles, and Pixel Station has been the perfect guide! I've discovered hidden gems and learned so much about the origins of gaming. The community is welcoming, making my exploration of retro games even more enjoyable."

3. **Amy - Retro Streamer (Age: 32):**
   > "Pixel Station is a haven for content creators like me! Sharing my retro gaming experiences with a collaborative community has been fantastic. The support and engagement from viewers within the Pixel Station community have significantly boosted my channel. It's more than just a platform; it's a retro gaming family!"

---
# Overview of Django Apps

This project consists of several interconnected Django apps, each responsible for specific functionalities:

![DjangoApps](Documentation/images/django-flowchart.png) 

### Comment App

The **Comment** app allows users to comment on posts.

#### Functionality Breakdown:
- **Models (models.py)**: Defines comment structure.
- **Serializers (serializers.py)**: Transforms comment data between Python objects and JSON.
- **Views (views.py)**: Handles requests for comments, interacting with models and serializers.
- **URLs (urls.py)**: Routes requests to views.
- **Admin (admin.py)**: Manages comments in the Django admin interface.
- **Migrations (migrations/)**: Tracks database schema changes.
- **Tests (tests.py)**: Ensures functionality works as expected.

#### Comment Model:
- **Fields**: `owner`, `post`, `content`, `created_at`, `updated_at`.
- **Ordering**: Comments are ordered by creation date (newest first).

#### Serializers:
- **CommentSerializer**: Handles serialization and deserialization of comments.
- **CommentDetailSerializer**: Extends CommentSerializer for detailed views.

---

### Follower App

The **Follower** app allows users to follow/unfollow each other.

#### Functionality Breakdown:
- **Models (models.py)**: Defines follower structure.
- **Serializers (serializers.py)**: Transforms follower data for API responses.
- **Views (views.py)**: Handles follower-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages followers in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Follower Model:
- **Fields**: `owner`, `followed`, `created_at`.
- **Ordering**: Newest followers first.
- **Unique Constraint**: Prevents duplicate follow relationships.

#### Serializers:
- **FollowerSerializer**: Handles serialization of follower data.

---

### Forum App

The **Forum** app enables users to create forums, threads, and posts.

#### Functionality Breakdown:
- **Models (models.py)**: Defines structures for forums, threads, and posts.
- **Serializers (serializers.py)**: Transforms forum data.
- **Views (views.py)**: Handles forum-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages forums in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Models:
- **Forum**: Fields include `name`, `description`, `created_at`.
- **Thread**: Fields include `forum`, `title`, `creator`, `created_at`.
- **Post**: Fields include `thread`, `author`, `content`, `created_at`.

#### Serializers:
- **ForumSerializer**: Serializes forum data.
- **ThreadSerializer**: Serializes thread data.
- **PostSerializer**: Serializes post data.

---

### Game Library App

The **Game Library** app allows users to manage their game collections.

#### Functionality Breakdown:
- **Models (models.py)**: Defines game and collection structures.
- **Serializers (serializers.py)**: Transforms game data.
- **Views (views.py)**: Handles game-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages games in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Models:
- **Game**: Fields include `title`, `developer`, `release_date`, `platform`.
- **GameCollection**: Fields include `user`, `game`, `added_at`.

#### Serializers:
- **GameSerializer**: Serializes game data.
- **GameCollectionSerializer**: Serializes game collection data.

---

### Likes App

The **Likes** app allows users to express appreciation for posts.

#### Functionality Breakdown:
- **Models (models.py)**: Defines like structure.
- **Serializers (serializers.py)**: Transforms like data.
- **Views (views.py)**: Handles like-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages likes in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Like Model:
- **Fields**: `owner`, `post`, `created_at`.

#### Serializers:
- **LikeSerializer**: Handles like data serialization.

---

### Messaging App

The **Messaging** app enables users to send and receive messages.

#### Functionality Breakdown:
- **Models (models.py)**: Defines message structure.
- **Serializers (serializers.py)**: Transforms message data.
- **Views (views.py)**: Handles message-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages messages in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Message Model:
- **Fields**: `sender`, `receiver`, `content`, `timestamp`.

#### Serializers:
- **MessageSerializer**: Handles message data serialization.

---

### Post App

The **Post** app allows users to create and manage posts.

#### Functionality Breakdown:
- **Models (models.py)**: Defines post structure.
- **Serializers (serializers.py)**: Transforms post data.
- **Views (views.py)**: Handles post-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages posts in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Post Model:
- **Fields**: `owner`, `created_at`, `updated_at`, `title`, `content`, `comments`, `likes`, `image`, `image_filter`.

#### Serializers:
- **PostSerializer**: Handles post data serialization.

---

### User Profile App

The **User Profile** app allows users to create and manage profiles.

#### Functionality Breakdown:
- **Models (models.py)**: Defines profile structure.
- **Serializers (serializers.py)**: Transforms profile data.
- **Views (views.py)**: Handles profile-related requests.
- **URLs (urls.py)**: Routes requests.
- **Admin (admin.py)**: Manages profiles in the admin interface.
- **Migrations (migrations/)**: Tracks schema changes.
- **Tests (tests.py)**: Ensures expected functionality.

#### Profile Model:
- **Fields**: `owner`, `created_at`, `updated_at`, `name`, `content`, `image`.

#### Serializers:
- **ProfileSerializer**: Handles profile data serialization.

#### Views:
- **ProfileList View**: Lists user profiles.
- **ProfileDetail View**: Retrieves and updates specific profiles.

---

## Conclusion

This project integrates multiple apps to facilitate user interaction and content management, providing a comprehensive platform for users.


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