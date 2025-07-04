#DockerFile using gunicorm for production

FROM public.ecr.aws/docker/library/python:3.12-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies \
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code
COPY . /app/
# Expose the port the app runs on
EXPOSE 8000
# Start the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "testApplication.wsgi:application"]