# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Set the environment variable for Django settings
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=yaya_webhook.settings

# Expose the port the app runs on
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "http://127.0.0.1:8000"]
