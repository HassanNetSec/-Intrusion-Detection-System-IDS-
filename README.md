
# Intrusion-Detection-System-IDS-
A lightweight Intrusion Detection System (IDS) that monitors network traffic in real-time to detect and alert against attacks like ARP spoofing, port scanning, and SYN Flood DDoS, providing security insights through packet capture and analysis

🧠 Features-

•	📡 Real-time Packet Monitoring with Scapy

•	⚙️ Backend API using FastAPI + SQLAlchemy

•	💽 PostgreSQL for efficient data storage

•	🔐 JWT Authentication for secure API access

•	🔄 Server-Sent Events (SSE) for real-time alerts

•	🧵 Threading to manage simultaneous capture and analysis tasks

•	🖥️ Modern Frontend built with Next.js + Axios

•	🧾 Data Validation with Pydantic


📦 Tech Stack

Backend: FastAPI, SQLAlchemy, PostgreSQL, Scapy, JWT, SSE, Pydantic

Frontend: Next.js, Axios

Concurrency: Python `threading`

Realtime: Server-Sent Events (SSE)

🚀 Getting Started

📁 Clone the Repository

git clone https://github.com/yourusername/Intrusion-Detection-System-IDS.git
cd Intrusion-Detection-System-IDS

🖥️ Frontend Setup

The Frontend/ directory only contains the core UI components and pages inside the app/ folder. If you're setting up the frontend from scratch, here’s how to proceed

1 Create the Next.js Project

      npx create-next-app@latest frontend    
2 Move the Uploaded Code into the Correct Folder

•If you've opted to use the src/ directory during setup, place the contents of the uploaded app/ folder into frontend/src/app/.

•If you didn't choose the src/ structure, place the contents directly inside frontend/app/.
     
Run development server

    npm run dev



⚙️ Backend Setup (Python 3.10+)

1. Create virtual environment

python -m venv venv
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt
4. Set Environment Variables
Create a `.env` file and add:
DATABASE_URL=postgresql://user:password@localhost:5432/ids_db
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256

5. Run the API
uvicorn app.main:app --reload
🖥️ Frontend Setup
1. Navigate to Frontend Directory
cd frontend
2. Install Node Modules
npm install
3. Run Development Server
npm run dev
🔍 Use Case
This system is suitable for:

•	Home and office network monitoring

•	Educational and learning environments

•	Lightweight security monitoring on edge devices

🛠 Libraries & Tools Used

Backend

•	Scapy - Packet Sniffing and Analysis

•	FastAPI - Web API Framework

•	SQLAlchemy - ORM

•	PostgreSQL - Relational Database

•	Pydantic - Data Validation

•	JWT - Authentication

•	SSE - Realtime Alerts

•	threading - Concurrent Packet Processing

Frontend

•	Next.js

•	Axios

🔐 Authentication

JWT tokens are used for authenticating API requests.
Tokens must be included in the Authorization header as:
Authorization: Bearer <your_token>

📄 License

    MIT License
    
🤝 Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a PR.

✉️ Contact

 Have questions or suggestions?
 Reach out via issues on GitHub.

