import shutil
from pathlib import Path


def cleanup() -> None:
    """Removes irrelevant dirs"""
    dirs = [Path("/data/data"), Path("/data/fasta"), Path("/data/pdb")]
    for d in dirs:
        shutil.rmtree(d, ignore_errors=False)


if __name__ == "__main__":
    cleanup()
