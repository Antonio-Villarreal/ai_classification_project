# Use a Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy the application directory into the container
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    supervisor \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

RUN python3 download.py

# Expose port for Flask backend
EXPOSE 5001

# Expose port for Streamlit frontend
EXPOSE 8501

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Define the command to run your application
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
