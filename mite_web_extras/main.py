"""Entrypoint of data generation script

Copyright (c) 2025 to present Mitja M. Zdouc, PhD and individual contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import logging
import sys
from pathlib import Path

import coloredlogs

from .download_manager import DownloadManager
from .pdb_manager import PdbManager


def config_logger() -> logging.Logger:
    """Set up a module-specific logger with nice formatting

    :return
        A Logger object
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        coloredlogs.ColoredFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    )
    logger.addHandler(console_handler)
    return logger


def main() -> None:
    """Function to execute main body of code"""
    logger = config_logger()
    logger.info("Started mite_web_extras")

    dnld_mngr = DownloadManager()
    dnld_mngr.download_data()
    dnld_mngr.organize_data()

    pdb_mngr = PdbManager()
    pdb_mngr.collect_uniprot_acc()
    pdb_mngr.download_pdbs()

    logger.info("Completed mite_web_extras")


if __name__ == "__main__":
    main()
