<mite_web_extras>
==========


Contents
-----------------
- [Overview](#overview)
- [Attribution](#attribution)
- [For Developers](#for-developers)

## Overview

MITE (Minimum Information about a Tailoring Enzyme) is a community-driven database for the characterization of tailoring enzymes. These enzymes play crucial roles in the biosynthesis of secondary or specialized metabolites, naturally occurring molecules with strong biological activities, such as antibiotic properties.

This repository manages auxiliary files for the [MITE Webpage](https://mite.bioinformatics.nl/) and is intended for internal use.

For more information, visit the [MITE Data Standard Organization page](https://github.com/mite-standard) or read our [publication](https://doi.org/10.1093/nar/gkaf969).

## Attribution

### License

This repository is licensed under the [MIT License](LICENSE)

### Publications

You can find additional citation information in the [CITATION.cff](CITATION.cff) file. 

## For Developers

Install package and run tests

```commandline
uv sync
uv run pre-commit install
uv run pytest
```