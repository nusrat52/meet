# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1 

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Start Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "first_django.wsgi:application"]