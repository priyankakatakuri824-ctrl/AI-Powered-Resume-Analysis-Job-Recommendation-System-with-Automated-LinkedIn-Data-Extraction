AI-Powered Resume Analysis & Job Recommendation System
with Automated LinkedIn Data Extraction

An intelligent platform built with Python, capable of analyzing resumes using AI, extracting skills, evaluating strengths/weaknesses, and recommending relevant jobs by scraping data from LinkedIn.
Includes user authentication, resume upload, text extraction, and dashboard features.

⭐ Key Features

🔐 Secure user registration & login (bcrypt password hashing)

📤 Resume upload (PDF/DOCX with validation)

📄 Resume text extraction using PyPDF2 & python-docx

🤖 AI-Powered resume analysis (LLM/LangChain) (Milestones 2 & 3)

🔍 Automated LinkedIn job scraping using Selenium

🎯 Job matching & recommendation engine

📊 User dashboard with recent activity & stats

🗄️ MongoDB/SQLite-based data storage

🧩 Modular code structure (backend, frontend, utils)

🏗️ Project Architecture
project/
│── backend/
│   ├── auth.py               # User authentication logic
│   ├── resume_parser.py      # PDF/DOCX text extraction
│
│── frontend/
│   ├── registration.py       # Registration UI
│   ├── login.py              # Login UI
│   ├── dashboard.py          # User dashboard
│
│── utils/
│   ├── database.py           # DB connection + CRUD functions
│
│── data/
│   ├── resumes/              # Uploaded resumes
│   ├── database.db           # If using SQLite
│
│── .env                      # API keys, DB URI
│── .gitignore
│── README.md
│── main.py                   # Main Streamlit routing script
│── requirements.txt

✅ Task 1: Project Environment Setup
Objective:

Prepare the complete development environment and define a maintainable project folder structure.

Detailed Explanation:

This task ensures your project starts with a clean, organized, and scalable foundation. It includes:

Installing Python 3.9+

Ensures compatibility with modern libraries like Streamlit, LangChain, and Selenium.

Creating a Virtual Environment

Prevents conflicts between global Python packages and project-specific dependencies.

Installing Required Libraries:

Streamlit → UI development

LangChain → LLM/AI integration

Selenium → LinkedIn job scraping

PyPDF2 & python-docx → Resume file processing

bcrypt → Secure password hashing

MongoDB/SQLite libraries → Data storage
These libraries support key functionalities like authentication, PDF parsing, AI analysis, etc.

Creating a Well-Organized Folder Structure:

backend/
frontend/
utils/
data/


Separating concerns improves readability and scalability.

Initializing Git Repository

Enables version control for tracking changes and collaborating with team members.

Creating .gitignore

Prevents committing sensitive files like __pycache__, .env, and virtual environment folders.

Creating .env File

Stores secret keys (API keys, DB URIs) securely.

Documenting Setup Steps

The README should clearly explain installation, environment setup, and how to run the project.

Why This Matters:

A strong foundation avoids bugs, reduces confusion, and keeps the team aligned. Proper structuring makes future development smoother and more secure.

✅ Task 2: Design Database Schema
Objective:

Define a robust and scalable data model for user accounts, resume analysis, and job recommendations.

Detailed Explanation:

Database design ensures efficient data flow and management. This task includes:

Choosing Database:

MongoDB → Flexible document-based storage

SQLite → Lightweight SQL database

User Schema:
Stores essential user details:

user_id, name, email, hashed_password, registration_date, resume_path

Resume Analysis Schema:
Stores AI analysis output:

Extracted resume text

Skills identified

Strengths & weaknesses

Recommended skills

Analysis score

Timestamps

Job Recommendation Schema:
For storing LinkedIn job data:

Job title

Company

Location

Job description

Match percentage

Job URL

Scraping timestamp

CRUD Operations:
Implemented in utils/database.py for accessing and modifying database entries.

Indexing & Validation:

Index fields like email, user_id

Validate email format

Ensure uniqueness of user emails

Why This Matters:

A well-structured database ensures smooth resume analysis, fast job retrieval, and reliable user authentication.

✅ Task 3: Build User Registration Page (Frontend)
Objective:

Create a clean, professional, user-friendly registration interface using Streamlit.

Detailed Explanation:

New Frontend Page:
frontend/registration.py handles all UI elements for registration.

Form Fields:

Full Name

Email Address

Password

Confirm Password

Real-Time Validation:

Name must contain only letters

Email must follow standard format (regex)

Password must include uppercase, lowercase, number, special character

Passwords must match

Error Messages:
Clear validation messages displayed under each input.

Submit Button:
On clicking "Register", data is sent to backend for processing.

Navigation Link:
Takes existing users to the login page.

UI Styling:
Uses Streamlit layout and themes for a professional look.

Why This Matters:

This is the first user interaction with your platform—clean design and strong validation ensure trust and prevent faulty data entry.

✅ Task 4: Implement User Authentication Backend
Objective:

Securely register and authenticate users using hashed passwords and persistent sessions.

Detailed Explanation:

Authentication Module:
All logic inside backend/auth.py.

Registration Backend:

Check if email already exists

Hash password using bcrypt

Save user to database

Login Backend:

Verify email

Check hashed password using bcrypt

If valid, create a user session

Session Management:
Uses st.session_state to store:

logged-in user ID

user name

navigation state

Logout Function:
Clears session data.

Comprehensive Error Handling:
For invalid credentials, DB connection issues, and validation failures.

Why This Matters:

This ensures that only authorized users can access the system. Security is critical for protecting user data and uploaded documents.

✅ Task 5: Build Resume Upload Interface (Frontend)
Objective:

Let users upload their resume in PDF/DOCX format with validation and feedback.

Detailed Explanation:

File Uploader Component:
Created using st.file_uploader().

Validation Checks:

Only PDF/DOCX files allowed

Maximum size: 5 MB

Attempt to read file to ensure it's not corrupted

File Preview:

Show file name, size, upload date

Option for PDF first-page preview (if dependencies installed)

Upload Button:
Sends file to backend for saving.

Success Messages:
Shows confirmation after saving.

Re-upload Option:
Users can replace the old resume anytime.

Storage Directory:
Files stored under:

data/resumes/

Why This Matters:

A smooth upload experience is essential since resume analysis is the core functionality of this app.

✅ Task 6: Implement Resume Text Extraction (Backend)
Objective:

Extract meaningful text from PDF and DOCX files for AI-based analysis.

Detailed Explanation:

Extraction Module:
Implemented in backend/resume_parser.py.

PDF Extraction:

Use PyPDF2 or pdfplumber

Loop through pages and extract text

Handle image-based PDFs (mention OCR limitations)

DOCX Extraction:
Use python-docx to read paragraphs and maintain basic formatting.

Unified Function:
Detects file type and processes accordingly.

Cleaning the Text:

Remove extra whitespace

Normalize special characters

Fix encoding issues

Store in DB:
Save the extracted text under the user's analysis record.

Error Handling:
Detect corrupted files or password-protected files.

Why This Matters:

AI analysis depends on accurate text extraction. Clean and complete extraction ensures better results from LLMs.

✅ Task 7: Create User Dashboard (Frontend)
Objective:

Provide a centralized interface for users to navigate the app and view key features.

Detailed Explanation:

Dashboard File:
frontend/dashboard.py

Dashboard Sections:

Header: Welcome message + Logout

Navigation Menu: Profile, Upload Resume, Resume Analysis, Job Recommendations

Quick Stats: Resume uploaded, last analysis date, job recommendation count

Recent Activity: Latest actions

Call-to-Action Cards: Helpful next steps

Session Management:
Ensures only logged-in users can access the dashboard.

Navigation Handling:
Uses session state to keep track of current page.

Responsive Layout:
Designed to be clear, intuitive, and visually appealing.

Why This Matters:

This page serves as the main user interaction hub, making navigation simple and efficient.
