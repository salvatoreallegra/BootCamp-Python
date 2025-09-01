# ---------- Base ----------
FROM python:3.12-slim

# Fast, clean Python logs & predictable I/O
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_DATA_DIR=/app/data

# Create non-root user and working dir
RUN useradd -m appuser
WORKDIR /app

# ---------- Dependencies (cached) ----------
# Copy only requirements first to leverage layer caching
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# ---------- App code ----------
# Copy your package code into the image
COPY bootcamp_python /app/bootcamp_python

# Make sure data dir exists and has an empty JSON list so first run works
# Also fix ownership so the non-root user can write
RUN mkdir -p "$APP_DATA_DIR" \
    && printf "[]\n" > "$APP_DATA_DIR/tasks.json" \
    && chown -R appuser:appuser /app

# Drop privileges
USER appuser

# ---------- Runtime ----------
# Your CLI module; default subcommand is "list"
ENTRYPOINT ["python", "-m", "bootcamp_python.cli.tasks_cli"]
CMD ["list"]
