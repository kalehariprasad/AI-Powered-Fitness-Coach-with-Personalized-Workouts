# Use official Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install system dependencies (curl for Ollama install)
RUN apt-get update && apt-get install -y curl && \
    apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Expose ports for Streamlit and Ollama
EXPOSE 8501 11434

# Run both Ollama and Streamlit
CMD ["/bin/sh", "-c", "ollama serve & streamlit run streamlit.py"]
