

# Mini RAG Application

A production-ready Retrieval-Augmented Generation (RAG) system built with FastAPI, featuring multi-provider LLM support, vector database integration, and enterprise-grade architecture.

## 🎯 Overview

This RAG application enables intelligent document processing and question-answering by combining vector search with large language models. The system supports multiple LLM providers (OpenAI, Cohere, Groq, HuggingFace) and implements a scalable, modular architecture suitable for production deployment.

### Key Features

- **Multi-Provider LLM Support**: Seamlessly switch between OpenAI, Cohere, Groq, and HuggingFace
- **Vector Database Integration**: Efficient similarity search using Qdrant with configurable embedding models
- **Document Processing Pipeline**: Automated chunking, embedding, and indexing of documents
- **RESTful API**: Clean FastAPI endpoints with comprehensive request/response validation
- **Multi-Language Support**: Built-in template system supporting Arabic and English
- **Production-Ready Infrastructure**: Docker Compose setup with MongoDB 

- **Factory Pattern Architecture**: Extensible provider system for easy integration of new services

## 🏗️ Architecture & Design Patterns

### Project Structure
```
src/
├── controllers/          # Business logic layer
│  
├── models/              # Data models & schemas
│   
├── routes/              # API endpoints
│   
├── stores/              # External service integrations
│   ├── llm/                # LLM provider abstraction
│   └── vectordb/           # Vector database abstraction
|
└── helpers/             # Configuration & utilities
```

### Design Patterns Implemented

1. **Factory Pattern**: `LLMProviderFactory` and `VectorDBProviderFactory` for runtime provider selection
2. **Repository Pattern**: Data access layer abstraction through controllers
3. **Dependency Injection**: FastAPI's dependency system for service management
4. **Template Method**: Base controllers defining common operations
5. **Strategy Pattern**: Pluggable LLM and vector database providers

## 🚀 Technology Stack

### Backend Framework
- **FastAPI**: Modern, high-performance web framework
- **Python 3.12**: Type hints and async/await support
- **Pydantic**: Data validation and settings management

### AI/ML Stack
- **LangChain**: LLM orchestration and document processing
- **Sentence Transformers**: Local embedding model support
- **OpenAI/Cohere/Groq APIs**: Multiple LLM provider options

### Databases
- **MongoDB**: Document storage for projects and metadata
- **Qdrant**: Vector database for semantic search

### Infrastructure
- **Docker & Docker Compose**: Containerized deployment
- **Motor**: Async MongoDB driver
- **Uvicorn**: ASGI server with production capabilities

## 💡 Production-Ready Skills Demonstrated

### 1. **Scalable Architecture**
   - Modular design with clear separation of concerns
   - Factory pattern for easy provider switching
   - Async/await for high-concurrency operations
   - Configuration management with environment variables

### 2. **API Design Best Practices**
   - RESTful endpoint structure
   - Request validation using Pydantic schemas
   - Proper HTTP status codes and error handling
   - API versioning capability

### 3. **Database Management**
   - NoSQL (MongoDB) for flexible document storage
   - Vector database (Qdrant) for similarity search
   - Efficient indexing and query optimization
   - Connection pooling and lifecycle management

### 4. **External Service Integration**
   - Abstract interfaces for third-party APIs
   - Graceful error handling and fallback mechanisms
   - Rate limiting considerations
   - API key management and security

### 5. **DevOps & Deployment**
   - Docker containerization
   - Docker Compose for multi-service orchestration
   - Environment-based configuration
   - Production server setup (Uvicorn)

### 6. **Code Quality**
   - Type hints throughout the codebase
   - Enum-based constants for type safety
   - Consistent naming conventions
   - Modular, testable code structure

### 7. **Internationalization**
   - Multi-language template system
   - Language-specific prompt engineering
   - Configurable locale support

## 📋 Requirements

- **Python 3.12**
- **Docker & Docker Compose**

### System Dependencies (Linux)

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

## ⚙️ Installation

### 1. Set Up Python Environment

Using MiniConda (Recommended):

```bash
# Download and install MiniConda
# https://docs.anaconda.com/free/miniconda/#quick-command-line-install

# Create environment
conda create -n mini-rag python=3.12
conda activate mini-rag
```

### 2. Install Python Dependencies

```bash
cd src
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Application config
cd src
cp .env.example .env

# Docker services config
cd ../docker
cp .env.example .env
```

Edit `.env` files with your credentials:
- `OPENAI_API_KEY`: Your OpenAI API key
- `COHERE_API_KEY`: Your Cohere API key (optional)
- `GROQ_API_KEY`: Your Groq API key (optional)
- `HUGGINGFACE_API_KEY`: Your HuggingFace API key (optional)
- Database credentials for MongoDB

### 4. Start Docker Services

```bash
cd docker
docker compose up -d
```

This starts:
- **MongoDB** (port 27007): Document database

### 5. Run the Application

```bash
cd src
uvicorn main:app --reload 
```

## 🔗 API Endpoints

### Access Points

- **API Documentation (Swagger)**: http://127.0.0.1:8000/docs
- **API Base URL**: http://127.0.0.1:8000

### Main Endpoints

- `POST /api/data/projects/{project_id}/assets/`: Upload documents
- `POST /api/nlp/projects/{project_id}/index`: Index documents to vector DB
- `POST /api/nlp/projects/{project_id}/query`: Query the RAG system
- `GET /api/data/projects/`: List all projects

## 🔧 Configuration

### Switching LLM Providers

Edit `src/.env`:

```env
# Options: openai, cohere, groq, huggingface
GENERATION_BACKEND=openai
GENERATION_MODEL_ID=gpt-4-turbo-preview

EMBEDDING_BACKEND=openai
EMBEDDING_MODEL_ID=text-embedding-3-small
EMBEDDING_MODEL_SIZE=1536
```

### Language Configuration

```env
PRAIMARY_LANGUAGE=en  # en or ar
DEFALUT_LANGUAGE=en
```

## 🐳 Docker Services

The application uses Docker Compose for service orchestration:

```yaml
services:
  mongodb:    # Document storage
```

To stop services:
```bash
cd docker
docker compose down
```

### Optional: Enhanced Terminal Display

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## 🎓 Skills & Technologies Learned

This project demonstrates proficiency in:

✅ **Backend Development**: FastAPI, async Python, RESTful API design  
✅ **AI/ML Integration**: RAG architecture, vector databases, embedding models  
✅ **System Design**: Factory patterns, dependency injection, modular architecture  
✅ **Database Engineering**: MongoDB, vector databases, data modeling  
✅ **DevOps**: Docker, containerization, environment management  
✅ **Production Engineering**: Error handling, configuration management, scalability  
✅ **API Integration**: Multiple LLM providers, external service abstraction  
✅ **Code Quality**: Type hints, clean architecture, maintainable code

## 📝 License

This project is created for educational purposes and portfolio demonstration.


## 📧 Contact

For questions or collaboration opportunities, feel free to reach out .
