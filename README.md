# AI API Documentation Generator 🚀

An AI-powered tool that analyzes **ASP.NET Core Controllers** and automatically generates API Documentation using local Large Language Models (LLMs).

The project uses **Python, Ollama, and Llama 3.2** to understand API structure, extract endpoint information, and generate professional documentation in Markdown format.

---

## 📌 Overview

API Documentation is an essential part of building professional APIs. It helps developers and integration teams understand available services, endpoints, request requirements, and responses.

However, keeping documentation updated during continuous development can be challenging.

This project explores how AI can assist developers by automatically generating API documentation from existing ASP.NET Core Controller code.

---

## ✨ Features

* Analyze ASP.NET Core Controllers using AI

* Extract API endpoint information

* Identify:

  * Controller name
  * Base route
  * HTTP methods
  * API routes
  * Request DTO references
  * Response types
  * Authorization information
  * Possible status codes

* Generate professional API Documentation in Markdown format

* Use local LLM execution with Ollama

* Stream generated documentation in real time

* No dependency on external AI APIs

---

## 🏗️ AI Workflow

The project follows a multi-step LLM workflow:

```
ASP.NET Core Controller
          |
          ▼
   LLM Analysis
          |
          ▼
 Structured API JSON
          |
          ▼
 Context Preparation
          |
          ▼
 Documentation Generation LLM
          |
          ▼
 API_Documentation.md
```

---

## 🔄 How It Works

### 1. API Analysis

The first LLM call analyzes the provided ASP.NET Core Controller and extracts API metadata.

Example:

```json
{
  "controller_name": "EmployeesController",
  "base_route": "/api/employees",
  "endpoints": [
    {
      "http_method": "POST",
      "route": "/",
      "request_dto": "CreateEmployeeDto",
      "response_type": "IActionResult",
      "possible_status_codes": [
        201
      ]
    }
  ]
}
```

---

### 2. Documentation Generation

The extracted API information is combined with the controller source code and sent to the documentation generation step.

The second LLM generates a structured API document:

Example:

```
API Documentation

API Name:
Employees API

Overview:
Creates a new employee.

Endpoint:
POST /api/employees

Request Body:
CreateEmployeeDto

Response:
201 Created
```

---

## 🛠️ Technologies

* Python
* Ollama
* Llama 3.2
* OpenAI Compatible API
* ASP.NET Core
* Markdown

---

## 📂 Project Structure

```
AI-API-Documentation/

│
├── main.py
├── analyzer.py
├── documentation.py
├── context_builder.py
├── prompts.py
│
├── output/
│   └── API_Documentation.md
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/LamaAlzahranii/AI-API-Documentation-Generator.git
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Ollama

Install Ollama:

https://ollama.com

Download Llama 3.2:

```bash
ollama pull llama3.2
```

Run Ollama:

```bash
ollama serve
```

---

## ▶️ Usage

Run:

```bash
python main.py
```

The generated documentation will be saved:

```
output/API_Documentation.md
```

---

## 🎯 Current Scope

The current version focuses on analyzing individual ASP.NET Core Controllers.

Future improvements may include:

* Automatically reading complete .NET projects
* Extracting DTO definitions
* Integrating Swagger/OpenAPI specifications
* Supporting multiple controllers
* Adding CI/CD integration
* Building a web interface

---

## 💡 Why Local AI?

This project uses local LLM execution to provide:

* Better control over data
* Customizable AI workflows
* No dependency on external AI services
* Future integration possibilities within enterprise environments

---

## 🤝 Contributions

Suggestions, feedback, and improvements are welcome.

Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License
