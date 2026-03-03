mite_web_extras
==========

[![DOI](https://zenodo.org/badge/1083685650.svg)](https://doi.org/10.5281/zenodo.17453501)


Contents
-----------------
- [Overview](#overview)
- [Documentation](#documentation)
- [Attribution](#attribution)
- [For Developers](#for-developers)

## Overview

MITE (Minimum Information about a Tailoring Enzyme) is a community-driven database for the characterization of tailoring enzymes. 
These enzymes play crucial roles in the biosynthesis of secondary or specialized metabolites, naturally occurring molecules with strong biological activities, such as antibiotic properties.

This repository manages artifacts for the [MITE Webpage](https://mite.bioinformatics.nl/) and is intended for internal use.

For more information, visit the [MITE Data Standard Organization page](https://github.com/mite-standard) or read our [publication](https://doi.org/10.1093/nar/gkaf969).

## Documentation

This repository contains artifacts derived from the `mite_data` dataset, utilized by the [MITE Webpage](https://mite.bioinformatics.nl/).

This includes:
- The BLAST databases
- Jinja2-compatible mite JSON files 
- Images of predicted protein structures

The code is designed to run as CI/CD by GitHub Actions.

## Attribution

### License

This repository is licensed under the [MIT License](LICENSE)

### Publications

You can find additional citation information in the [CITATION.cff](CITATION.cff) file. 

## For Developers

### Release checklist

Workflow for release creation (for details, see below):

- In GitHub GUI, under Actions, manually trigger the `Prepare release` workflow and wait for successful passing. This will create artifacts and open a new pull request
- Check the newly generated pull request, approve and merge it
- Update minor `version` in [pyproject.toml](pyproject.toml) file and update the [CHANGELOG](CHANGELOG.md), merge to main.
- On [new release](https://github.com/mite-standard/mite_web_extras/releases/new), fill in tag (as `version` in `pyproject.toml`), add v`version` as release title, and add release notes (identical to `changelog`).
- Zenodo will automatically grab the new release.

### Manual updating

Locally, the artifacts can be updated using the following commands.

```commandline
docker build -t mite-cli .
docker run --rm -v $(pwd)/data:/data -u $(id -u):$(id -g) -e HOME=/tmp mite-cli
```
