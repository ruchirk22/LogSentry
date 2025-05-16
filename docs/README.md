# LogSentry

**A log analysis tool with ML-powered threat detection and Q&A capabilities.**

```In frontend/, run npm start (opens at <http://localhost:3000>)```

```In backend/ (with venv activated), run uvicorn main:app --reload (runs at <http://localhost:8000>)```

LogSentry provides a comprehensive log analysis platform with four core features designed to help security teams identify, analyze, and respond to threats efficiently.

## 1. Log Ingestion

The entry point for all data into LogSentry. It pulls logs from various sources to enable downstream analysis.

### Methods

- **Manual Upload**: Users upload log files (e.g., .log, .txt) via a web interface for ad-hoc analysis
- **Database Connection**: Connects to enterprise databases (e.g., Elasticsearch, PostgreSQL) or public feeds where logs are stored
- **Lightweight Agent**: A future option to pull logs from systems like Apache or Zeek IDS in real-time

### Supported Formats

- Apache logs
- Nginx logs
- Zeek IDS data
- Extensible to others

### Key Needs

- Flexibility (multiple formats)
- Scalability (large volumes)
- Security (safe uploads/connections)
- Ease of use

## 2. Threat Classification

Tags logs with threat categories (e.g., "Port scan," "SQL injection") for analysis.

### Approach

- Uses Hugging Face's Zero-Shot Text Classification (free pre-trained models)
- Classifies logs without extensive training

### Process Flow

- **Input**: Parsed logs from Log Ingestion
- **Output**: Labeled logs stored for further processing

## 3. Incident Clustering

Groups related alerts/incidents to reduce noise and highlight patterns.

### Approach

- Uses SentenceTransformer embeddings (free, pre-trained)
- Computes log similarity and clusters them

### Process Flow

- **Input**: Classified logs from Threat Classification
- **Output**: Clustered incidents for summarization or querying

## 4. Summarization

Generates concise incident reports for users.

### Approach

- Leverages a free Hugging Face summarization model (e.g., BART or T5)
- Summarizes clustered incidents

### Process Flow

- **Input**: Clustered incidents
- **Output**: Human-readable summaries

## 5. Q&A Interface

Allows users to query incidents conversationally (e.g., "How many SQL injection attempts in the last 24 hours?").

### Approach

- Natural language processing (NLP) with a lightweight, free model (e.g., DistilBERT)
- Parses queries and fetches results

### Process Flow

- **Input**: Stored logs and incidents
- **Output**: Answers in natural language via a dashboard
