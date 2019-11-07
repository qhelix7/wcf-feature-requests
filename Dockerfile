FROM python:3.7

# Upgrade pip
RUN pip install --upgrade pip

# Copy code
COPY . .

# TODO: copy dist files
# ...

# Install dependencies
RUN pip install -r requirements.txt
CMD ["sh", "-c", "alembic upgrade head && /usr/local/bin/gunicorn --config gunicorn_config.py main:app"]
