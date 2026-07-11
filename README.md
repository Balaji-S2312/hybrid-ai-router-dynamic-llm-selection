# Hybrid AI Router with Dynamic LLM Selection

## Overview

Hybrid AI Router is an intelligent AI orchestration system that dynamically routes user queries between a local Large Language Model (LLM) and a cloud-based LLM based on query complexity. The objective is to optimize latency, cost, privacy, and response quality while providing a seamless user experience.

---

## Features

- Dynamic LLM selection
- Local AI inference using Qwen 2.5 1.5B Instruct
- Cloud AI inference using Meta Llama 3.1 8B (via Grok API)
- FastAPI backend
- Interactive web dashboard
- Complexity and confidence estimation
- Latency monitoring
- Response evaluation

---

## Tech Stack

### Backend
- Python
- FastAPI
- Transformers
- PyTorch

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### AI Models
- Local: Qwen/Qwen2.5-1.5B-Instruct
- Cloud: Meta Llama 3.1 8B (via Grok API)

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd Hybrid-Router
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

---

## 3. Activate the Virtual Environment

Windows

```bash
.\.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Create a `.env` file in the project root and add your API credentials.

Example:

```env
GROK_API_KEY=your_api_key_here
```

---

## 6. Run the Backend

```bash
uvicorn api:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 7. Run the Frontend

Open a new terminal.

Navigate to the frontend directory:

```bash
cd frontend
```

Run a local web server:

```bash
python -m http.server 5500
```

Open your browser and visit:

```
http://localhost:5500
```

---

# Project Workflow

```
User Query
      │
      ▼
FastAPI Backend
      │
      ▼
Complexity Classifier
      │
      ▼
Hybrid AI Router
   ┌─────────────┐
   │             │
   ▼             ▼
Local LLM    Cloud LLM
(Qwen 2.5)   (Meta Llama 3.1)
   │             │
   └──────┬──────┘
          ▼
Response Evaluation
          ▼
Frontend Dashboard
```

---

# Usage

1. Open the frontend in your browser.
2. Enter your query.
3. Click **Generate**.
4. The system will:
   - Analyze the query
   - Select the appropriate LLM
   - Generate a response
   - Display routing metrics including:
     - Selected Model
     - Complexity
     - Confidence
     - Latency
     - Evaluation Status

---

# Folder Structure

```
Hybrid-Router/
│
├── api.py
├── classifier.py
├── router.py
├── model_manager.py
├── evaluator.py
├── logger.py
├── requirements.txt
├── .env
├── frontend/
│   ├── index.html
│   ├── css/
│   └── js/
└── README.md
```

---

# Future Improvements

- Context-aware semantic routing
- Retrieval-Augmented Generation (RAG)
- Multi-agent orchestration
- Real-time token usage tracking
- Learning-based routing optimization
- GPU acceleration
- Multi-cloud LLM support

---

# Author

**Balaji Sivaprakasam**

AMD Hackathon 2026