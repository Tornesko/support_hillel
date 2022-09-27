FROM --platform=linux/x86_64 python:3.10-slim


# Change working directory
WORKDIR /app/


# Copy project files
COPY . .


# Install deps
RUN pip install -r requirements.txt


CMD sleep 3 \
    && .\ manage.py migrate \
    && .\ manage.py runserver 0.0.0.0:80