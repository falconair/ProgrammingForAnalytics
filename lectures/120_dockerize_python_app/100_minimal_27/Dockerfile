# Use a small base image .... dangerously old!
FROM python:2.7-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py .

# Run the application
CMD ["python", "app.py"]

# docker build -t hello_app .
# docker run hello_app