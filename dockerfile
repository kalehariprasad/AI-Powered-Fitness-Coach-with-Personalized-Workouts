# --------------------------
# Stage 1: Builder
# --------------------------
    FROM python:3.9-slim AS builder

    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    WORKDIR /app
    
    # Install pip and project dependencies
    COPY requirements.txt .
    RUN pip install --upgrade pip && pip install -r requirements.txt
    
    # --------------------------
    # Stage 2: Final image with Ollama and Streamlit
    # --------------------------
    FROM python:3.9-slim
    
    WORKDIR /app
    
    # Install system dependencies (curl needed for Ollama)
    RUN apt-get update && apt-get install -y curl && apt-get clean
    
    # Copy files
    COPY . /app
    
    # Copy installed Python packages from builder
    COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
    COPY --from=builder /usr/local/bin /usr/local/bin
    
    # Install Ollama
    RUN curl -fsSL https://ollama.com/install.sh | sh
    
    # Expose ports for Streamlit and Ollama
    EXPOSE 8501 11434
    
    # Start both Ollama and Streamlit
    CMD ["/bin/sh", "-c", "ollama serve & streamlit run streamlit.py"]
    