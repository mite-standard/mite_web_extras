"""Manages building of a BLAST database.

Copyright (c) 2024 to present Mitja Maximilian Zdouc, PhD and individual contributors.

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
import shutil
import subprocess
from pathlib import Path
from typing import Self

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class BlastManager(BaseModel):
    """Manages the building of a BLAST database.

    Attributes:
        data: data volume
    """

    data: Path = Path("/data")

    def concat_fasta_files(self: Self) -> None:
        """Concatenates individual FASTA files into a single one for BLAST processing."""
        src = self.data.joinpath("fasta")
        trgt = self.data.joinpath("mite_concat.fasta")

        with open(trgt, "w") as outfile:
            for filename in src.iterdir():
                if filename.suffix == ".fasta":
                    with open(filename) as infile:
                        shutil.copyfileobj(infile, outfile)
                        outfile.write("\n")

    def generate_blast_db(self: Self) -> None:
        """Starts subprocess to generate a BLAST DB from the (downloaded) protein FASTA files"""
        blast = self.data.joinpath("blast")
        if blast.exists():
            shutil.rmtree(blast)

        with open(self.data.joinpath("version.json")) as infile:
            version_data = json.load(infile)
            version = version_data.get("version_mite_data")

        command = [
            "makeblastdb",
            "-in",
            f"{self.data.joinpath("mite_concat.fasta")}",
            "-dbtype",
            "prot",
            "-out",
            f"{blast.joinpath("mite_blastfiles")}",
            "-title",
            f"MITE v{version} BLAST DB",
        ]
        subprocess.run(command, check=True)
