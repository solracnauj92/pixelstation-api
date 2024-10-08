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
-----

# Key Features Implemented / User Stories

### 1. User Profile Management
Manage your profile to update personal information and preferences.

- **User Story**: As a user, I want to create and edit my profile so that others can know more about me.
  - **Description**: Users should be able to enter and update personal information such as bio, location, and interests.
  - **Acceptance Criteria**: Users can fill out and update profile information, with changes reflected on their profile page.

- **User Story**: As a user, I want to upload a profile picture so that my profile is visually recognizable.
  - **Description**: Users should have the option to upload, change, or remove a profile picture.
  - **Acceptance Criteria**: Users can upload a profile picture, see it displayed on their profile, and change or delete it as needed.

---

### 2. Creating and Managing Posts
Create and manage posts to share content with others.

- **User Story**: As a user, I want to create a new post so that I can share content with my followers.
  - **Description**: Users should be able to create posts with text, images, or other media.
  - **Acceptance Criteria**: Users can create a post, which is then displayed in their feed and visible to their followers.

- **User Story**: As a user, I want to edit or delete my posts so that I can manage the content I share.
  - **Description**: Users should have the ability to modify or remove their own posts.
  - **Acceptance Criteria**: Users can edit the content of a post or delete it entirely, with changes reflected in real-time.

---

### 3. Like and Unlike Functionality
Like or unlike posts to express appreciation for content.

- **User Story**: As a user, I want to like a post to express my appreciation for the content.
  - **Description**: Users should be able to click a like button on posts.
  - **Acceptance Criteria**: Users can click a like button, increasing the like count on the post.

- **User Story**: As a user, I want to unlike a post I previously liked to change my reaction.
  - **Description**: Users should be able to remove their like from a post.
  - **Acceptance Criteria**: Users can click an unlike button, decreasing the like count on the post.

---

### 4. Commenting on Posts
Comment on posts to engage in discussions with others.

- **User Story**: As a user, I want to comment on a post to engage in discussions.
  - **Description**: Users should be able to leave comments on posts to start or join conversations.
  - **Acceptance Criteria**: Users can enter and submit a comment, which appears under the post.

- **User Story**: As a user, I want to edit or delete my comments to manage my interactions.
  - **Description**: Users should be able to modify or remove their comments.
  - **Acceptance Criteria**: Users can edit the content of a comment or delete it, with changes reflected in real-time.

---

### 5. User Registration and Sign In
Register and sign in to access the platform and its features.

- **User Story**: As a user, I want to create an account so that I can use the platform.
  - **Description**: Users should be able to sign up by providing necessary details like username, email, and password.
  - **Acceptance Criteria**: Users can fill out a registration form, submit it, and receive a confirmation email to activate the account.

- **User Story**: As a user, I want to sign in to my account to access my profile and posts.
  - **Description**: Users should be able to log in using their registered email and password.
  - **Acceptance Criteria**: Users can enter credentials on a login form, submit them, and access their account if the credentials are correct.

---

### 6. Site Navigation
Enjoy intuitive navigation to easily find content and features.

- **User Story**: As a user, I can view a navbar from every page to navigate easily between pages.
  - **Description**: A consistent navigation bar is available on all pages, providing links to essential parts of the site (e.g., Home, Profile, Notifications, Messages).
  - **Acceptance Criteria**: Navbar appears on every page and contains links that function correctly.

---

### 7. Following and Unfollowing Users
Manage your social connections effectively.

- **User Story**: As a user, I want to follow other users to see their posts in my feed.
  - **Description**: Users should be able to follow other users to receive their updates.
  - **Acceptance Criteria**: Users can click a follow button, and the followed user’s posts appear in their feed.

- **User Story**: As a user, I want to unfollow users I am no longer interested in so that my feed stays relevant.
  - **Description**: Users should be able to unfollow users they are no longer interested in.
  - **Acceptance Criteria**: Users can click an unfollow button, and the unfollowed user’s posts no longer appear in their feed.

---

### 8. Followers and Following Lists
Display the users' social connections.

- **User Story**: As a user, I want to see a list of my followers to know who is following me.
  - **Description**: Users should be able to view a list of people who follow them.
  - **Acceptance Criteria**: Users can access a followers list from their profile.

- **User Story**: As a user, I want to see a list of users I am following to manage my connections.
  - **Description**: Users should be able to view a list of people they are following.
  - **Acceptance Criteria**: Users can access a following list from their profile.

---

### 9. Messaging Functionality
Communicate privately with other users.

- **User Story**: As a user, I want to send messages to other users to communicate privately.
  - **Description**: Users should be able to send direct messages to other users.
  - **Acceptance Criteria**: Users can compose and send a message, which is received by the recipient.

- **User Story**: As a user, I want to receive messages from other users to have conversations.
  - **Description**: Users should be able to receive and read direct messages from other users.
  - **Acceptance Criteria**: Users can receive notifications for new messages and read them in a dedicated inbox.

---

### 10. User Notifications
Keep users informed about interactions.

- **User Story**: As a user, I want to receive notifications for likes, comments, follows, and messages to stay informed about interactions with my content.
  - **Description**: Users should receive real-time notifications for various activities related to their account.
  - **Acceptance Criteria**: Users receive notifications for likes, comments, follows, and messages, either through the app or via email.

---

### 11. Search Functionality
Find users and content easily.

- **User Story**: As a user, I want to search for other users to connect with them.
  - **Description**: Users should be able to search for other users by name or username.
  - **Acceptance Criteria**: Users can enter a query in a search bar and see a list of matching users.

- **User Story**: As a user, I want to search for posts by keywords to find relevant content.
  - **Description**: Users should be able to search for posts using keywords.
  - **Acceptance Criteria**: Users can enter keywords in a search bar and see a list of matching posts.

---

### 12. Feed and Timeline
Interact with your and others’ content.

- **User Story**: As a user, I want to see a feed of posts from users I follow to stay updated with their latest content.
  - **Description**: Users should have a feed that displays posts from the users they follow.
  - **Acceptance Criteria**: Users can view a feed with the latest posts from followed users.

- **User Story**: As a user, I want to see my own posts in my timeline to review my shared content.
  - **Description**: Users should be able to view a chronological list of their own posts.
  - **Acceptance Criteria**: Users can access a personal timeline that shows all their posts.

---

### 13. Privacy Settings
Control your privacy on the platform.

- **User Story**: As a user, I want to set my profile to private so that only approved followers can see my posts.
  - **Description**: Users should have the option to make their profile private.
  - **Acceptance Criteria**: Users can toggle a privacy setting that restricts profile visibility to approved followers.

- **User Story**: As a user, I want to manage my notification preferences to receive alerts that are important to me.
  - **Description**: Users should be able to customize which notifications they receive and how.
  - **Acceptance Criteria**: Users can access and adjust notification settings to their preference.

-----------------------

# Dependencies Documentation

Documentation for project dependencies is crucial for developers:

- **Understanding Functionality**: Provides insights into how each dependency works and its purpose.
- **Usage Guidelines**: Offers examples and best practices for integration and configuration.
- **API Reference**: Acts as a comprehensive guide to all classes, methods, and parameters.
- **Updates and Changes**: Keeps developers informed about new features, bug fixes, and compatibility issues.
- **Community Support**: Provides forums and resources for troubleshooting and community interaction.
- **Security and Stability**: Ensures secure configurations and stable integrations within projects.

Accurate and accessible documentation enhances development efficiency and promotessoftware solutions.


This project uses the following Python packages. **Note**: I had to downgrade all packages to ensure compatibility with the frontend dependencies, particularly due to the need for matching versions across both back-end and front-end setups.

| Package                               | Version      | Description                                    |
|---------------------------------------|--------------|------------------------------------------------|
| asgiref                               | 3.8.1        | ASGI utilities for Django                      |
| cloudinary                            | 1.41.0       | Cloud-based image and video management         |
| dj-database-url                       | 0.5.0        | Utility to parse database URLs for Django      |
| dj-rest-auth                          | 2.1.9        | REST API endpoints for authentication          |
| Django                                | 3.2.23       | High-level web framework                       |
| django-allauth                        | 0.52.0       | Authentication and account management          |
| django-cloudinary-storage             | 0.3.0        | Storage backend for Cloudinary                 |
| django-cors-headers                   | 4.3.1        | CORS headers for responses                     |
| django-filter                         | 23.4         | Queryset filtering                             |
| djangorestframework                   | 3.14.0       | Toolkit for building APIs                      |
| djangorestframework-simplejwt         | 5.3.1        | JWT authentication                             |
| gunicorn                              | 23.0.0       | WSGI HTTP server for UNIX                      |
| oauthlib                              | 3.2.2        | OAuth request-signing logic                    |
| pillow                                | 10.4.0       | Image processing                               |
| psycopg2                              | 2.9.9        | PostgreSQL adapter                             |
| PyJWT                                 | 2.9.0        | JSON Web Token handling                        |
| python3-openid                        | 3.2.0        | OpenID authentication                          |
| pytz                                  | 2024.2       | Timezone calculations                          |
| requests-oauthlib                     | 2.0.0        | OAuth for requests                             |
| sqlparse                              | 0.5.1        | SQL parsing                                    |

### Installation

You can install the required packages using pip:

pip install -r requirements.txt

### Documentations 

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
