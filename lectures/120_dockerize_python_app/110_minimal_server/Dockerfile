# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Command to run the application
CMD ["fastapi", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]


# docker build -t minimal_server .
# docker run -d -p 8000:8000 minimal_server
# curl http://localhost:8000