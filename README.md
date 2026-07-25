# AI API Documentation Generator 🚀

An AI-powered tool that automatically analyzes **ASP.NET Core APIs** and generates professional API documentation using **Local LLMs**.

The project uses **Python + Ollama + Llama 3.2** to analyze controllers, extract API information, and generate structured API documentation in Markdown format.

---

## 📌 Overview

Writing and maintaining API documentation is an important part of building professional APIs. However, keeping documentation updated during continuous development can be challenging.

This project explores how AI can help automate this process by analyzing backend code and generating documentation automatically.

The goal is not only to generate text using an LLM, but to build an AI workflow that understands the API structure and produces reusable documentation.

---

## ✨ Features

✅ Analyze ASP.NET Core Controllers using AI
✅ Extract API metadata and endpoint information
✅ Generate structured API documentation automatically
✅ Use local LLM execution with Ollama
✅ No dependency on external AI services
✅ Generate Markdown documentation ready for publishing
✅ Streaming output during documentation generation

---

## 🏗️ Architecture

The solution follows a multi-step AI workflow:

```
ASP.NET Core Controller
          |
          ▼
   LLM Analysis Layer
          |
          ▼
 Structured API JSON
          |
          ▼
 Context Builder
          |
          ▼
 Documentation Generation LLM
          |
          ▼
 API_Documentation.md
```

---

## 🔄 Workflow

### 1. API Analysis

The first LLM call analyzes the ASP.NET Core Controller and extracts:

* Controller name
* Base route
* HTTP methods
* Endpoints
* Request DTOs
* Response types
* Authorization information
* Status codes

Example output:

```json
{
  "controller_name": "EmployeesController",
  "base_route": "/api/employees",
  "endpoints": [
    {
      "http_method": "POST",
      "route": "/",
      "request_dto": "CreateEmployeeDto",
      "possible_status_codes": [
        201
      ]
    }
  ]
}
```

---

### 2. Documentation Generation

The extracted API information is combined with the controller source code and sent to the documentation generation layer.

The second LLM generates a professional API document:

```
API Documentation

API Name:
Employees API

Endpoint:
POST /api/employees

Request Body:
- Employee fields

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

Activate it:

**Mac/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install and run Ollama

Install Ollama:

https://ollama.com

Download the required model:

```bash
ollama pull llama3.2
```

Run Ollama:

```bash
ollama serve
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

The generated documentation will be saved automatically:

```
output/
 └── API_Documentation.md
```

---

## 📂 Project Structure

```
AI-API-Documentation-Generator/

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

## 🎯 Future Improvements

Possible future enhancements:

* Automatically scan complete .NET solutions
* Extract DTO and model definitions
* Integrate with Swagger/OpenAPI specifications
* Generate documentation for multiple APIs
* Add API documentation versioning
* Build a web interface for enterprise usage
* Integrate with CI/CD pipelines

---

## 💡 Why Local AI?

Using local LLMs provides:

* Better control over data
* No dependency on external APIs
* Ability to customize the workflow
* Potential integration with enterprise environments

---

## 🤝 Contribution

Feedback, ideas, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.
