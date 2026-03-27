 Multimodal Manufacturing Creator
Project: GAI-12 | Group 12D9 | Division D9

🧠 Tech Stack
FeatureToolCostProduct DescriptionGroq API + LLaMA 3.1Free (14,400 req/day)Product ImagePollinations.ai (Flux)Free, no key neededFrontendStreamlitFree

🚀 Setup & Run
Step 1 — Get Groq API Key (2 minutes)

Go to https://console.groq.com
Sign up (Google login works)
Click API Keys → Create API Key
Copy the key (starts with gsk_...)

Step 2 — Install dependencies
bashpip install -r requirements.txt
Step 3 — Run the app
bashstreamlit run app.py
Step 4 — Use the app

Open http://localhost:8501
Paste your Groq API key in the sidebar
Type your manufacturing concept
Click ⚡ Generate


📁 Project Structure
├── app.py            ← Main Streamlit app
├── requirements.txt  ← Python dependencies (streamlit, requests)
└── README.md         ← This file

💡 Example Prompts

"Smart robotic arm for automotive welding with AI defect detection"
"Self-cleaning conveyor belt for food processing plants"
"Autonomous quality inspection drone for warehouses"
"Wearable exoskeleton for factory workers to reduce spinal load"


⚡ Why Groq?

LLaMA 3.1 runs in 2-3 seconds on Groq cloud (vs 2-3 mins locally)
Completely free — 14,400 requests/day
No GPU or local setup needed