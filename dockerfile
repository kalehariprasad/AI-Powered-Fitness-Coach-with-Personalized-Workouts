FROM python:3.13-slim

# Install system packages required for NumPy and other Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git libgl1-mesa-glx gcc make && \
    apt-get -f install && \
    rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install Python packages
RUN pip install -r requirements.txt

# (Optional but helpful) Pre-pull model to avoid wait on first run
RUN ollama pull llama3:latest

# Expose Streamlit and Ollama ports
EXPOSE 8501 11434

# Run Ollama in the background and launch the Streamlit app
CMD bash -c "\
    ollama serve & \
    sleep 5 && \
    streamlit run app.py"
