📊 Financial Document Management System with Semantic RAG


🚀 Overview
A high-performance FastAPI-based system designed to manage, analyze, and extract insights from financial documents such as Invoices, Reports, and Contracts.

This system leverages Retrieval-Augmented Generation (RAG) and semantic search to allow users to ask complex financial queries and receive accurate, context-aware answers.

✨ Key Features

📄 Multi-Format Support
Handles PDF, Excel (.xlsx), Word (.docx), and Text (.txt)

🔍 Advanced Semantic Search
Uses BAAI/bge-small-en-v1.5 embeddings + Qdrant Vector DB

🔐 Role-Based Access Control (RBAC)
Admin
Financial Analyst
Auditor
Client

🛡️ Secure Authentication
JWT-based authentication with Bcrypt password hashing

⚡ Two-Stage Retrieval Pipeline
Top 20 candidates → Top 5 reranked results
Improves financial query precision

🧠 Architecture (RAG Pipeline)
Document → Text Extraction → Chunking → Embeddings → Qdrant DB → Retrieval → Reranking → Answer Generation

⚙️ Technical Challenges & Solutions
1. 📑 Parsing Complex Financial Data

Problem:
Unstructured PDFs and structured Excel sheets lose contextual relationships during extraction.

Solution:

Used PyMuPDF (Fitz) for accurate PDF parsing
Used Pandas to convert Excel into structured text
Applied chunking strategies to preserve semantic meaning
2. 🔐 Secure Role-Based Access (RBAC)

Problem:
Prevent unauthorized access across shared APIs.

Solution:

Implemented FastAPI Dependency Injection
Verified:
JWT Token
User Role (stored in SQLite)
Enforced access control at endpoint level
3. 📊 Financial Semantic Accuracy

Problem:
Generic embeddings fail for financial terminology.

Solution:

Switched to BGE-small (optimized for retrieval)
Used Recursive Character Chunking
Preserved financial context (liquidity, leverage, solvency)
🛠️ Tech Stack
Backend: FastAPI
Database: SQLite
Vector DB: Qdrant
Embeddings: BAAI/bge-small-en-v1.5
Authentication: JWT + Bcrypt
Parsing: PyMuPDF, Pandas
🧑‍💻 Installation & Setup
Prerequisites
Python 3.10+
pip
1. Clone Repository
git clone https://github.com/siddheshasati/Financial_Doc_Manager.git
cd Financial_Doc_Manager
2. Create Virtual Environment
python -m venv venv

Activate:

Windows:
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
uvicorn main:app --reload
📘 API Usage Guide
Open Swagger UI:
👉 http://127.0.0.1:8000/docs
Steps:
Register User → /auth/register
Login & Authorize → Use JWT
Upload Documents
Search using RAG → /rag/search
✅ Project Checklist
✔ FastAPI Backend
✔ JWT Authentication
✔ Role-Based Access Control
✔ RAG Pipeline Implementation
✔ Financial Semantic Search
✔ Reranking Mechanism
📈 Future Improvements
📊 Dashboard for financial insights visualization
☁️ Cloud deployment (AWS / Azure)
🧠 Fine-tuned financial LLM
📁 Multi-user document collaboration


📬 Contact
Siddhesh Asati
GitHub: https://github.com/siddheshasati

⭐ If you found this useful, give it a star!
