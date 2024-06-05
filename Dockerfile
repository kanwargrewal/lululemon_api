FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERed 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    gcc \
    libffi-dev \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

# Collect static files
#RUN python manage.py collectstatic --noinput
RUN pip install gunicorn

EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lululemon_api.wsgi:application"]
