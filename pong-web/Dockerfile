# Build stage. Compiles the dependencies into a virtualenv that gets copied
FROM python:3.14-slim AS build

WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# runtime stage
FROM python:3.14-slim

# run as a normal user
RUN useradd --uid 1000 --create-home --shell /usr/sbin/nologin appuser

COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --chown=appuser:appuser pong.py app.py ./

USER appuser
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"

# gunicorn rather than a Flask development server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]