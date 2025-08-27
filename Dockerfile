# Use Python base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy all project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask default port
EXPOSE 5000

# Run the Flask app with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
