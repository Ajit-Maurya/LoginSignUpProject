# Use the official Python image based on Alpine
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Update Alpine and install required packages
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libc-dev \
    linux-headers \
    jpeg-dev \
    zlib-dev \
    libjpeg

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "AuthProj.wsgi:application"]
