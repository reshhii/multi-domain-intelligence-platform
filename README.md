# Multi-Domain Intelligence Platform
## Secure Authentication & Database Analytics (Weeks 7–8)

**Student Name:** Reshika Sahadew  
**Course:** CST1510 – Multi-Domain Intelligence Platform  

---

## Project Overview

This project implements a secure, multi-domain intelligence platform developed
incrementally across laboratory weeks.

- **Week 7** focuses on secure user authentication using bcrypt and file-based storage.
- **Week 8** transitions the platform to a relational SQLite database and introduces
  data ingestion, CRUD operations, and analytical querying.

The platform is designed to support multiple technical domains, including
cybersecurity incidents and IT service management data.

---

## Week 7 – Secure Authentication System

### Features Implemented
- Secure password hashing using **bcrypt** with automatic salting
- User registration with duplicate username prevention
- Secure login with password verification
- Input validation for usernames and passwords
- File-based user data persistence (`users.txt`)

### Technical Details
- **Hashing Algorithm:** bcrypt (one-way hashing)
- **User Storage:** Plain text file (`users.txt`) with `username:hashed_password`
- **Security Measures:**
  - No plaintext password storage
  - Safe handling of malformed user records
  - Users file excluded from version control

---

## Week 8 – Database Layer & Data Analytics

### Features Implemented
- Migration from text-file storage to **SQLite database**
- Database schema creation using SQL
- CSV ingestion using **pandas**
- Secure data loading into relational tables
- CRUD-ready database structure
- Analytical SQL queries for extracting insights
- Integration of database analytics into the Streamlit dashboard

### Datasets Used
- `cyber_incidents.csv`
- `datasets_metadata.csv`
- `it_tickets.csv`

### Database Tables
- `incidents`
- `datasets_metadata`
- `it_tickets`

---

## Technologies Used

- Python 3.13
- SQLite
- pandas
- bcrypt
- Streamlit

---

## Project Structure
multi_domain_platform/
│
├── auth/ # Authentication logic (Week 7)
├── db/ # Database layer & analytics (Week 8)
├── data/ # CSV datasets
├── app.py # Streamlit application
├── security.py # Password hashing utilities
├── requirements.txt
├── README.md
└── .gitignore


---

## Conclusion

This project demonstrates a secure and scalable approach to building a multi-domain intelligence platform.  
It applies authentication best practices, structured data storage, and analytical querying techniques aligned with real-world software and data engineering principles.

Further enhancements can include advanced analytics, visualizations, and role-based access control.

---

