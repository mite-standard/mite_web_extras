mite_web_extras
==========

[![DOI](https://zenodo.org/badge/1083685650.svg)](https://doi.org/10.5281/zenodo.17453501)


Contents
-----------------
- [Overview](#overview)
- [Attribution](#attribution)
- [For Developers](#for-developers)

## Overview

MITE (Minimum Information about a Tailoring Enzyme) is a community-driven database for the characterization of tailoring enzymes. These enzymes play crucial roles in the biosynthesis of secondary or specialized metabolites, naturally occurring molecules with strong biological activities, such as antibiotic properties.

This repository manages auxiliary files for the [MITE Webpage](https://mite.bioinformatics.nl/) and is intended for internal use. Briefly, the code in this repository:

- Downloads the newest version of `mite_data`
- Generates the BLAST databases needed by MITE Web
- Generates the Jinja2-compatibe mite JSON files
- Downloads `.pdb` files from AlphaFoldDB matching the UniProt Accessions in the MITE data files
- Generates visualizations of predicted protein structures

For more information, visit the [MITE Data Standard Organization page](https://github.com/mite-standard) or read our [publication](https://doi.org/10.1093/nar/gkaf969).

## Quickstart

Update the auxiliary files (automatically updates to the newest version of `mite_data`).

Previous temporary dirs (`data/data`, `data/fasta`, `data/pdb`) need to be manually removed if they are to be newly downloaded. 

```commandline
docker build -t mite-cli .
docker run --rm -v $(pwd)/data:/data -u $(id -u):$(id -g) -e HOME=/tmp mite-cli
```

Already existing images will not be overwritten.

## Attribution

### License

This repository is licensed under the [MIT License](LICENSE)

### Publications

You can find additional citation information in the [CITATION.cff](CITATION.cff) file. 

