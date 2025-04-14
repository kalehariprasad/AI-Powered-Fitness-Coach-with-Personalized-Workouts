# Use a slim Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies for Streamlit, FPDF, and Hugging Face's transformers
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 libsm6 libxrender1 libxext6 curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copy application files to the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose the default port for Streamlit
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit.py"]
