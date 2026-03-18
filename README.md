🌸 Women Safety App — Simple Guardian Prototype 🌸
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=ff69b4,8a2be2&height=180&section=header&text=Women%20Safety%20App&fontSize=35&fontColor=ffffff"/> </p> <p align="center"> <img src="https://readme-typing-svg.herokuapp.com?color=FF69B4&size=20&center=true&vCenter=true&width=600&lines=Python+Based+Safety+Prototype;Client-Server+Architecture;Runs+Locally+with+SQLite"/> </p>
<p align="center"> <img src="https://img.shields.io/badge/Status-Prototype-ff69b4?style=for-the-badge"/> <img src="https://img.shields.io/badge/Architecture-Client--Server-blueviolet?style=for-the-badge"/> <img src="https://img.shields.io/badge/Database-SQLite-success?style=for-the-badge"/> <img src="https://img.shields.io/badge/User-metadore-ff1493?style=for-the-badge"/> </p>
💖 About The Project

This is a Python-based Women Safety App Prototype that demonstrates how emergency systems can be built using a client-server architecture running locally.

⚡ Key focus:

Simple implementation

Fast execution

No external dependencies

Fully local system

“In emergencies, simplicity is power.”

🚀 Features
🆘 SOS Trigger

Sends emergency request from client to server

Can be extended for alerts & notifications

📡 Client-Server Communication

Real-time interaction between client and server

Simulates emergency request handling

🗄️ Local Database Support

Uses SQLite (safezone.db)

Stores safety-related data locally

🧪 Demo Mode

demo_client.py allows easy testing of features

🧠 Working Architecture

This project follows a simple client-server model:

🖥️ server.py handles backend logic

📱 client.py / demo_client.py act as client-side apps

🗄️ safezone.db stores data locally

🔄 Flow:

Client sends request (SOS / data)

Server processes request

Data stored/retrieved from database

Response sent back to client

Designed to run completely on a local machine without external services

📂 Project Structure
📦 Women-Safety-App
 ┣ 📄 app.py            # Main application entry point
 ┣ 📄 app1.py           # Alternate / experimental logic
 ┣ 📄 client.py         # Client-side communication
 ┣ 📄 demo_client.py    # Demo/testing client
 ┣ 📄 server.py         # Backend server
 ┣ 📄 codathon.py       # Hackathon prototype version
 ┣ 📄 safezone.db       # SQLite database
⚙️ How to Run (Local Setup)
# Clone the repository
git clone https://github.com/metadore/women-safety-app.git

cd women-safety-app
▶️ Run the project:
# Step 1: Start the server
python server.py
# Step 2: Run client (in a new terminal)
python client.py
🧪 Demo Mode:
python demo_client.py
🛠️ Tech Stack

🐍 Python

🔌 Socket Programming (assumed for client-server)

🗄️ SQLite Database

⚙️ Local Execution Environment

🎯 Purpose of This Project

This project is built to:

Demonstrate basic safety system design

Showcase client-server architecture in Python

Serve as a foundation for advanced safety apps

🌟 Future Improvements

📍 Real-time GPS tracking

📲 SMS / alert integration

🌐 Web or mobile interface

🤖 Smart triggers (voice / shake detection)

☁️ Cloud deployment

🤝 Contribution

Feel free to improve this project:

Fork → Clone → Modify → Pull Request 🚀
📜 License

MIT License — free to use and modify

💬 Final Note

“Technology becomes meaningful when it solves real-world problems simply.”

⭐ Support

If you found this useful:

⭐ Star the repo

🍴 Fork it

📢 Share it

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=8a2be2,ff69b4&height=100&section=footer"/> </p>
