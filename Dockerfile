# Use lightweight Python base image
FROM python:3.9-slim


# Set work directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the application code (src folder)
COPY src/ ./src

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "-m", "src.todo_app.app"]
