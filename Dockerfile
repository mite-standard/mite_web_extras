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


# Install python and uv
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && apt-get install -y python3.12 python3.12-dev python3-pip
RUN pip install --upgrade pip
RUN pip install uv
ENV PYTHONUNBUFFERED=1

# Set up workspace
ENV INSTALL_PATH=/mite_web_extras
WORKDIR $INSTALL_PATH

# Copy the whole repository
COPY . .

# Install package and dependencies
RUN uv sync

RUN chmod +x ./entrypoint_docker.sh
RUN chmod +x ./mite_web_extras/run_pymol.sh

# Set default entrypoint to your CLI
ENTRYPOINT ["./entrypoint_docker.sh"]