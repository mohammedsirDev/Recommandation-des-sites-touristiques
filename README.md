🇲🇦 Recommandatios des Sites Touristiques
https://drive.google.com/file/d/164UriypyE19tyL98YVoDnfc28J4auOVw/view?usp=drive_link
Discover the Best Places to Visit in Morocco

Recommandatios des Sites Touristiques is a full-stack web platform built to help travelers discover, explore, and review the best tourist destinations in Morocco.

If visitors don’t know which places are worth visiting, they simply use this platform to find curated locations, activities, pricing details, opening hours, and map locations — all in one place.

The system is powered by Django with a customized admin interface using Jazzmin.

🌍 Platform Vision

To provide a centralized digital travel guide for Morocco that combines:

Destination discovery

Practical travel information

Community reviews

Personalized user experience

🏗 System Architecture

The platform follows a role-based structure:

👤 User

Handles authentication (register, login, password management).

🧳 Voyageur (Traveler Profile)

Extended profile linked to User. Can:

Leave reviews

Rate destinations

Add sites to favorites

Manage personal account

Change password securely

🛡 Admin

Full system control via enhanced Django Admin (Jazzmin):

Manage tourist sites

Moderate reviews

Control users

Maintain content quality

✨ Core Features
🔎 Destination Discovery

Each tourist site includes:

📍 Map location

💰 Price information

🕒 Opening hours

🎯 Activities available

📝 Description

⭐ Ratings and reviews

🔍 Advanced Filtering System

Users can filter destinations by:

Name

Category

Activity type

Location

Filtering is implemented at the database query level for efficiency.

👤 Authentication & Account Management

Secure user registration

Login & logout system

Password change functionality

Personalized traveler profile

⭐ Reviews & Ratings

Registered travelers can:

Leave reviews

Rate tourist sites

Share experiences

This creates a community-driven recommendation ecosystem.

❤️ Favorites System

Users can:

Save destinations to favorites

View saved places in their profile

Build a personalized travel list

🛠 Admin Dashboard (Jazzmin Design)

The backend uses:

Django

Jazzmin for modern admin UI

Admin capabilities:

Add / Edit / Delete destinations

Manage activities & pricing

Moderate user reviews

Manage user accounts

⚙️ Technology Stack

Backend:

Python

Django

Admin UI:

Jazzmin

Frontend:

HTML

CSS

JavaScript

Bootstrap

Database:

SQLite (Development)

Designed for future PostgreSQL migration

🧠 Engineering Highlights

Extended User model (User → Voyageur)

Role-based behavior control

Database-level filtering queries

Secure password management

Structured relational database design

Clean separation between public interface and admin control

🎯 Target Users

Tourists visiting Morocco

Travelers planning trips

Local explorers

Travel enthusiasts

👨‍💻 Author

Mohammed Sir
Software Engineering Student
GitHub: github.com/mohammedsirDev
