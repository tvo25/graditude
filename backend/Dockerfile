FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./config/requirements /config/requirements
RUN pip install --no-cache-dir -r /config/requirements/local.txt \
    && rm -rf /config/requirements

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - config.wsgi:application
