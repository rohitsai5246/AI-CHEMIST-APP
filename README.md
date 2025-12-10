🧪 AI Chemist App

A tiny experiment where chemistry meets artificial intelligence.

🌍 What is this project about?

Chemistry is fun… until you have to memorize reaction mechanisms, molecular structures, toxicity levels, or medicine compositions that look like alien language. I wanted something that could see a chemical image and explain it back to me like a friendly teacher — not like a scary textbook.

So I built AI Chemist.

This app lets you:

Upload a chemical structure (drawn by hand, printed pages, textbook snapshots, etc.)

Ask anything you want about it.

Get clear explanations from Google’s Gemini Vision AI.

Think of it as a chemist friend who lives inside your browser.

🔍 Why did I build this?

As students, we often scan Google or YouTube for hours just to understand a single molecule or drug composition. Some explanations are too complicated, some too simplified, and some just don’t exist.

This app solves that problem — you click a button, show an image, ask a question, and get the exact explanation you want. Simple.

🚀 What can the AI Chemist do?

Here are some real-world examples that it can answer after seeing an image:

If you upload…	It can tell you…
A hand-drawn benzene ring	Aromaticity, stability, uses & reactions
Medicine blister pack	Active chemicals, side effects, dosage info
Chemical formula from notebook	Name, properties, hazards, polarity, bond angles
Lab screenshot	Required safety gear, risks, ideal storage conditions

It’s not perfect (yet), but it’s genuinely helpful.

🛠️ How it works (in simple words)

You upload a photo.

The app safely sends it to Google Gemini Vision.

Gemini looks at what’s inside the image.

You ask a question about that image.

The model replies with chemistry knowledge related to the content.

Behind the scenes, it’s a mix of:

Python

Streamlit

PIL for image handling

Google Generative AI SDK

dotenv to hide the API key

📦 Installation (if you want to try it yourself)

👉 First, clone the repo:

git clone https://github.com/YourUsername/AI-Chemist-App.git
cd AI-Chemist-App


👉 Install dependencies:

pip install -r requirements.txt


👉 Create a .env file (don’t upload it to GitHub) and add this line:

GOOGLE_API_KEY=your_api_key_here


👉 Run the app:

streamlit run app.py


That’s it. The app will open in your browser.

⚠️ A little disclaimer

This project is made for learning, academic support, and curiosity.
Please don’t use it for:

serious medical decisions

industrial chemical safety

replacing professional lab analysis

AI can explain a molecule; it can’t replace a proper lab. At least not yet. 🙂

💡 Ideas for future improvements

If I continue building this (or if someone wants to contribute), I’d love to add:

Reaction prediction based on structures

Equation balancing

Organic synthesis suggestions

3D molecular visualization

Toxicity lookup from official chemical databases (PubChem integration)