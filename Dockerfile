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

# Switch to non-root user
USER app

# Expose the default port (will be overridden by PORT env var at runtime)
EXPOSE 8000

# Health check - test the MCP endpoint with a simple ping
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/mcp || exit 1

# Set the default command
CMD ["python", "mcp_server_http.py"] 