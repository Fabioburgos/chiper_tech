# Start from a base image
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
FROM python:3.10-slim

WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT 8080

# Copy the application code into the container
# COPY ["main.py", "constants.py", "data.py", "db", "./"] .
COPY . .

# Expose the app port
EXPOSE 8000

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]