42 School Final Project: Full-Stack Web Application

📚 Project Overview
ft_transcendence is the ultimate project of the 42 curriculum, where students design and build a complete web application from scratch. It brings together all the knowledge acquired throughout the program: web development, networking, databases, security, and deployment.

The goal is to create a fully functional online ping-pong game platform with user authentication, matchmaking, chat features, and real-time gameplay — following modern web application standards.

🛠️ Features
Authentication System

OAuth 2.0 (using 42 Intra login)

Two-Factor Authentication (2FA)

User Profiles

Avatars

Match history and stats

Real-Time Pong Game

Play against other users

Game invites and matchmaking system

Chat System

Public channels, private messages, and group chats

Real-time messaging with WebSockets

Friends and Blocking System

Add or block users

Responsive UI/UX

Optimized for both desktop and mobile devices

Deployment

Dockerized services

Ready for production

🧱 Tech Stack
Frontend: React.js / Next.js

Backend: NestJS (Node.js Framework)

Database: PostgreSQL

Authentication: Passport.js (with OAuth2 and 2FA)

Real-Time Communication: WebSockets (Socket.io)

Containerization: Docker / Docker-Compose

Deployment: Nginx, SSL certificates (HTTPS)

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your_username/ft_transcendence.git
cd ft_transcendence
Create an .env file and configure environment variables based on .env.example.

Build and run with Docker:

bash
Copy
Edit
docker-compose up --build
Access the application at:

bash
Copy
Edit
http://localhost:3000
🧪 Development Setup (without Docker)
Install backend dependencies:

bash
Copy
Edit
cd backend
npm install
npm run start:dev
Install frontend dependencies:

bash
Copy
Edit
cd frontend
npm install
npm run dev
Make sure PostgreSQL is running and your database is properly configured.

📄 Project Structure
vbnet
Copy
Edit
ft_transcendence/
├── backend/
│   └── (NestJS server files)
├── frontend/
│   └── (React/Next.js client files)
├── docker-compose.yml
└── README.md
✍️ Authors
Zhenya - zkarape

🏆 Acknowledgements
42 School and its amazing curriculum

NestJS and React documentation

Socket.io team for real-time communication support

Special thanks to everyone who supported us throughout the project!

📜 License
This project is for educational purposes under the 42 Network guidelines.
Feel free to fork and build upon it for personal learning!

