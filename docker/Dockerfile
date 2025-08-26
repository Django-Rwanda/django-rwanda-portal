# Define the Version of python images

ARG VERSION=3.13.7-bookworm

# ----------- BUILD STAGE -----------
FROM python:${VERSION} AS build

# Set environment variables for Python and apt
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    PATH="/root/.local/bin:$PATH"

# Install system dependencies and uv package manager
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl build-essential ca-certificates \
    gcc libpq-dev libffi-dev libssl-dev && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory for the build stage
WORKDIR /app

# Copy dependency files to leverage Docker cache
COPY ./pyproject.toml ./uv.lock ./

# Install Python dependencies using uv
RUN uv sync 

# Copy the application source code and app runtime environment
COPY ./src ./env ./docker/nginx ./

# Collect static files for production
RUN uv run ./src/manage.py collectstatic --noinput && \
    chmod -R 755 /app && \
    find . -type d -name "__pycache__" -exec rm -rf {} +


# ----------- RUNTIME STAGE -----------
FROM python:${VERSION} AS runtime

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Install nginx and create necessary directories
# Also create a non-root user for running the application
RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y  nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    rm /etc/nginx/sites-enabled/default && \
    mkdir -p /run/nginx && \  
    # creating system user
    groupadd -r appgroup && \
    useradd -rg appgroup -m -d /home/appuser -s /usr/sbin/nologin appuser && \
    # Create a non-root user and group for running the application
    chown -R appuser:appgroup /run/nginx /app


# copy nginx configuration file from the build stage
COPY --from=build /app/nginx/nginx.conf /etc/nginx/

# Set the working directory for the runtime stage
WORKDIR /app

# Copy built application and dependencies from build stage, set ownership
COPY --chown=appuser:appgroup --from=build /app/ ./

# Delete it if it exists
RUN rm -f ./docker/nginx.conf \
    ./pyproject.toml \
    ./uv.lock 
    
# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 80

# Start the application using Gunicorn with Uvicorn worker
CMD ["/bin/sh", "-c", "nginx && /app/.venv/bin/gunicorn -k uvicorn.workers.UvicornWorker registry.asgi:application --bind 0.0.0.0:8000 --workers 4"]

# Healthcheck to ensure the service is running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s \
    CMD curl -f http://localhost:8000/ || exit 1    
