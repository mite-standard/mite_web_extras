# Inspired by https://github.com/astral-sh/uv-docker-example/blob/main/standalone.Dockerfile

# First, build the application in the `/mite_web_extras` directory
FROM ghcr.io/astral-sh/uv:bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_NO_DEV=1

# Configure the Python directory so it is consistent, only use managed version
ENV UV_PYTHON_INSTALL_DIR=/python UV_PYTHON_PREFERENCE=only-managed

# Install Python before the project for caching
RUN uv python install 3.12

# Download and install dependencies
WORKDIR /mite_web_extras
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project

# Install project
COPY . /mite_web_extras
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync


FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install generic dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --fix-missing \
    software-properties-common \
    build-essential \
    libxrender1 \
    libxtst6 \
    netcat \
    ncbi-blast+ \
    pymol \
    wget && \
    rm -rf /var/lib/apt/lists/*


# Setup a non-root user
RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

# Copy the Python version
COPY --from=builder --chown=nonroot:nonroot /python /python

# Copy the application from the builder
COPY --from=builder --chown=nonroot:nonroot /mite_web_extras /mite_web_extras

# Place executables in the environment at the front of the path
ENV PATH="/mite_web_extras/.venv/bin:$PATH"

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Use `/mite_web_extras` as the working directory
WORKDIR /mite_web_extras

# Use the non-root user to run our application
USER nonroot

# Set default entrypoint to your CLI
CMD ["./entrypoint_docker.sh"]