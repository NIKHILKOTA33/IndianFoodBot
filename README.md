# IndianFoodBot - Local Recipe Chatbot (Excel Dataset + FastAPI + Ollama + Streamlit)

## Project Overview
IndianFoodBot is a locally running AI-powered recipe chatbot that suggests the best matching recipe based on user-provided ingredients.

The system loads an Indian food dataset from an Excel file (`IndianFoodDatasetXLS.xlsx`), finds the most relevant recipe using fuzzy ingredient matching, and generates a conversational recipe response using a local LLM model running through Ollama.

This project works completely offline once the dataset and model are available.

---

## Features
- Loads Indian recipe dataset directly from Excel (`.xlsx`)
- Accepts ingredients from user input (comma-separated)
- Finds the best matching recipe from the dataset
- Uses fuzzy matching to handle spelling variations and partial ingredient matches
- Generates a chatbot-style recipe response using a locally running LLM
- Clean web interface using Streamlit
- API-based backend using FastAPI

---

## Tech Stack
- Python 3.10+
- FastAPI (Backend API Server)
- Streamlit (Frontend UI)
- Ollama (Local LLM runtime)
- RapidFuzz (Fuzzy matching engine)
- Pandas + OpenPyXL (Excel file processing)

---

## Project Structure
```
IndianFoodBot/
│
├── backend/
│   ├── main.py
│   ├── dataset_loader.py
│   ├── recipe_retriever.py
│   ├── llm_client.py
│   ├── utils.py
│   ├── data/
│   │   └── IndianFoodDatasetXLS.xlsx
│   ├── requirements.txt
│
├── frontend/
│   ├── web_ui.py
│   ├── requirements.txt
│
└── README.md
```

---

## Dataset Requirement
This project requires the Indian Food Excel dataset file.

Place the dataset here:

```
backend/data/IndianFoodDatasetXLS.xlsx
```

Dataset Columns Used:
- Srno
- RecipeName
- Ingredients
- Instructions
- Cuisine
- Course
- Diet
- PrepTimeInMins
- CookTimeInMins
- TotalTimeInMins
- Servings
- URL

---

# Setup Instructions (Windows/Linux)

## Step 1: Install Python
Make sure Python 3.10+ is installed.

Check version:
```bash
python --version
```

---

## Step 2: Install Ollama (Local LLM)
Download and install Ollama from:

https://ollama.com/

Verify installation:
```bash
ollama --version
```

---

## Step 3: Download a Small Model (Recommended)
To avoid laptop lag/hanging, use a small model:

```bash
ollama pull tinyllama
```

Run model:
```bash
ollama run tinyllama
```

⚠️ Keep this terminal open while running the project.

---

# Installation Commands

## Backend Installation
Go to backend folder:

```bash
cd backend
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

---

## Frontend Installation
Go to frontend folder:

```bash
cd frontend
```

Install frontend dependencies:

```bash
pip install -r requirements.txt
```

---

# How to Run the Project

## Step 1: Start Ollama Model
Open Terminal 1:

```bash
ollama run tinyllama
```

---

## Step 2: Start Backend API (FastAPI)
Open Terminal 2:

```bash
cd backend
python -m uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

## Step 3: Start Frontend UI (Streamlit)
Open Terminal 3:

```bash
cd frontend
streamlit run web_ui.py
```

Streamlit UI will run at:

```
http://localhost:8501
```

---

# Sample Input and Expected Output

## Sample Input
User enters in Streamlit textbox:

```
egg
```

OR

```
onion, tomato
```

---

## Expected Output
The UI will display:

### 1. Chatbot Response
A conversational response describing the recipe steps.

Example:

```
You can prepare Boiled Eggs Recipe.
Boil the eggs for 8-12 minutes.
Cool them in cold water and peel.
Serve with salt and pepper.
```

### 2. Best Recipe Match Details
- Recipe Name
- Cuisine
- Course
- Diet
- Total Time
- Similarity Score
- URL

Example:

```
Recipe Name: How To Boil Eggs At Home - Boiled Eggs Recipe
Cuisine: Continental
Course: Eggetarian
Diet: Vegetarian
Total Time: 10 mins
Similarity Score: 33.33%
URL: http://www.archanaskitchen.com/boiled-eggs-recipe
```

### 3. Dataset Ingredients and Instructions
Ingredients and full instructions will be displayed below the recipe details.

---

# API Usage (Verification)

## Endpoint
```
POST /chat
```

## Sample Request Body
```json
{
  "ingredients": ["egg"]
}
```

## Sample Response Output (JSON)
```json
{
  "status": "success",
  "best_match": {
    "recipe_name": "How To Boil Eggs At Home - Boiled Eggs Recipe",
    "cuisine": "Continental",
    "total_time_mins": 10,
    "similarity_score": 33.33
  },
  "chatbot_response": "..."
}
```

---

# Common Issues and Fixes

## Issue: "No recipe found"
Reason: Ingredient name does not match dataset text.
Fix: Use more common dataset ingredients like:
- onion
- tomato
- egg
- potato
- rice
- paneer

---



# AI Assistance Disclosure (Efficiency Improvement)
This project was developed with assistance from AI tools (ChatGPT) to improve development efficiency, code structuring, and modular design.

AI support was used for:
- Generating initial project structure
- Writing modular backend and frontend code
- Improving fuzzy matching logic using RapidFuzz
- Writing professional documentation

All generated code was reviewed, tested, and manually modified to ensure correctness and successful execution.

---

# Author
Nikhil Kota
