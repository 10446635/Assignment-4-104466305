FROM python:3.14-slim

RUN useradd --uid 1000 --create-home --shell /usr/sbin/nologin appuser

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY --chown=appuser:appuser pong.py pong_cli.py ./

RUN mkdir -p /data && chown appuser:appuser /data
VOLUME ["/data"]

USER appuser

ENTRYPOINT ["python", "pong_cli.py"]
CMD ["--frames", "20"]
