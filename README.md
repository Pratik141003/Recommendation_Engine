# 📘 AI-Assisted PBAS Recommendation System

### (Target-Based Faculty Professional Growth Engine)

------------------------------------------------------------------------

## 🚀 Project Overview

This project is an AI-assisted Performance Based Appraisal System (PBAS)
backend designed for faculty members under NAAC/SPPU guidelines.

The system:

-   Tracks teacher performance category-wise
-   Compares achievements against defined academic targets
-   Identifies improvement areas
-   Recommends high-quality professional development resources
-   Generates positive, growth-oriented suggestions
-   Displays structured output in the terminal (VS Code)

This version is backend-only and terminal-based. It is designed to
integrate with a web application in the future.

------------------------------------------------------------------------

# 🧠 Core Objective

To build a smart, target-driven faculty recommendation engine that:

-   Encourages professional growth
-   Aligns with PBAS evaluation structure
-   Suggests real-world courses from trusted platforms
-   Provides positive and constructive feedback

------------------------------------------------------------------------

# 🏗 System Architecture

Built Using: - Python 3 - PostgreSQL - psycopg2 - Structured relational
database design

------------------------------------------------------------------------

# 🗄 Database Structure

## 1️⃣ teachers

Stores faculty details such as name, email, department, designation,
experience, and qualification.

## 2️⃣ pbas_categories

Stores PBAS evaluation categories: - Teaching Learning\
- Research & Publications\
- FDP / Certifications\
- Student Feedback

## 3️⃣ teacher_targets

Defines expected performance for each teacher per category and academic
year.

## 4️⃣ teacher_achievements

Stores actual performance data for comparison.

## 5️⃣ resource_library

Stores curated professional development resources including: - Title -
Platform (Coursera, NPTEL, SWAYAM, Udemy, edX, etc.) - Duration -
Resource Type - Description - Direct URL

------------------------------------------------------------------------

# ⚙️ How the System Works

1.  Fetch teacher targets and achievements\
2.  Compare achieved values with minimum required targets\
3.  Detect improvement areas\
4.  Select matching professional resource\
5.  Generate positive AI-style recommendation\
6.  Display structured output in terminal

------------------------------------------------------------------------

# 📊 Sample Output Structure

Teacher Details\
Category\
Resource Title\
Platform\
Duration\
URL\
Positive Suggestion Message

------------------------------------------------------------------------

# 🎯 Key Features

✔ Target-based recommendation logic\
✔ Real-world course platforms integrated\
✔ Clean terminal report formatting\
✔ Modular database connection\
✔ Scalable architecture\
✔ Ready for frontend integration

------------------------------------------------------------------------

# 🔐 Project Structure

recommendation_engine/\
│\
├── recommend_courses.py\
├── db_config.py\
├── README.md

------------------------------------------------------------------------

# 🧪 Technologies Used

-   Python\
-   PostgreSQL\
-   SQL\
-   psycopg2

------------------------------------------------------------------------

# 🔄 Future Enhancements

-   Web UI integration\
-   Authentication system\
-   PDF report generation\
-   Analytics dashboard\
-   Priority-based ranking\
-   API-based live course integration

------------------------------------------------------------------------

# 🏁 Project Status

✔ Faculty data inserted\
✔ Targets assigned\
✔ Achievements simulated\
✔ Resource library created\
✔ Intelligent recommendation engine implemented\
✔ Terminal output working

