# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy requirements and install Python dependencies
COPY pyproject.toml uv.lock ./

# Create virtual environment and install dependencies
RUN uv venv .venv && \
    . .venv/bin/activate && \
    uv sync --frozen --no-dev

# Copy application code
COPY . .

# Make the server executable
RUN chmod +x mcp_server_http.py

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"
ENV PYTHONUNBUFFERED=1

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Expose the default port (will be overridden by PORT env var at runtime)
EXPOSE 8000

# Health check - Test if the server is responding
# Since MCP servers don't typically have a /health endpoint, we'll check if the server is listening
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${PORT:-8000}/ || exit 1

# Run the server using the virtual environment
CMD ["/app/.venv/bin/python", "mcp_server_http.py"] 