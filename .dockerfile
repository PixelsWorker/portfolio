# Use a slim Python image to reduce overhead
FROM python:3.9-slim

# Ensure Python output is logged directly (no buffering)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (build tools and PostgreSQL client libraries)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your Django project code into the container
COPY . .

# Declare a volume for your portfolio data
VOLUME ["/app/portfolio"]

# Collect static files (ensure STATIC_ROOT is defined in settings.py)
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Use a single worker to conserve memory in a constrained environment
CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "1"]
