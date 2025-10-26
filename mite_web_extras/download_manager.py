"""Download data from Zenodo and organize

Copyright (c) 2024-present Mitja Maximilian Zdouc, PhD

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
import os
import shutil
from pathlib import Path

import requests
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class DownloadManager(BaseModel):
    """Download data and prepare for use by mite_web

    Attributes:
        record_url: Zenodo URL for mite_data: always resolves to latest version
        data: the location to download data to
    """

    record_url: str = "https://zenodo.org/api/records/13294303"
    data: Path = Path("/data")

    def download_data(self) -> None:
        """Download data from Zenodo

        Raises:
            RuntimeError: Could not download files
        """
        response_metadata = requests.get(self.record_url)
        if response_metadata.status_code != 200:
            raise RuntimeError(
                f"Error fetching 'mite_data' record metadata: {response_metadata.status_code}"
            )

        record_metadata = response_metadata.json()
        version = record_metadata["metadata"]["version"]
        files_url = record_metadata["files"][0]["links"]["self"]

        response_data = requests.get(files_url)
        if response_data.status_code != 200:
            raise RuntimeError(
                f"Error downloading 'mite_data' record: {response_data.status_code}"
            )

        with open(self.data.joinpath("record.zip"), "wb") as f:
            f.write(response_data.content)

        with open(self.data.joinpath("version.json"), "w") as f:
            f.write(json.dumps({"version_mite_data": f"{version}"}))

    def organize_data(self) -> None:
        """Unpacks data, moves to convenient location, cleans up

        Raises:
            NotADirectoryError: directory not unzipped in expected location
            RuntimeError: Could not determine data location in downloaded folder
        """
        filename = self.data.joinpath("record.zip")
        extract_dir = self.data.joinpath("record")

        shutil.unpack_archive(filename=filename, extract_dir=extract_dir, format="zip")
        if not extract_dir:
            raise NotADirectoryError(extract_dir)

        matching_dirs = list(extract_dir.glob("mite-standard-mite_data-*"))
        if not matching_dirs:
            raise RuntimeError(
                f"Could not determine data storage location in downloaded directory."
            )
        subdir = matching_dirs[0]

        dst_old = self.data.joinpath("data")
        if dst_old.exists():
            shutil.rmtree(dst_old)
        shutil.move(
            src=extract_dir.joinpath(subdir).joinpath("mite_data/data").resolve(),
            dst=self.data.resolve(),
        )

        dst_old = self.data.joinpath("fasta")
        if dst_old.exists():
            shutil.rmtree(dst_old)
        shutil.move(
            src=extract_dir.joinpath(subdir).joinpath("mite_data/fasta").resolve(),
            dst=self.data.resolve(),
        )

        os.remove(filename)
        shutil.rmtree(extract_dir)
