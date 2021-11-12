# Note: work in progress
This repository contains the BioHackathon-Europe 2021 attempt to align Beacon with OMOP data model (stored in Postgres database)

The UI designed for this project can be found within the [BH2021-omop-frontend
](https://github.com/elixir-luxembourg/BH2021-omop-frontend) repo

# Beacon v2.x

[![Testsuite](https://github.com/EGA-archive/beacon-2.x/workflows/Testsuite/badge.svg)](https://github.com/EGA-archive/beacon-2.x/actions)

This repository is an implementation of the [Beacon v2.0 specification](https://github.com/ga4gh-beacon/specification-v2) and contains:

* the (Python 3.7+) [source code for beacon](beacon),
* instructions for a [local deployment](deploy) (using docker and docker-compose),



### Version notes

* Fusions (`mateName`) are not supported.


### Acknowlegments

We thank the [CSC Finland](https://www.csc.fi/) team for their
contribution with a [python implementing of version
1](https://github.com/CSCfi/beacon-python). They, in turn, got help
from members of [NBIS](https://nbis.se/) and
[DDBJ](https://www.ddbj.nig.ac.jp).

### Future works

- Increase functionality of the implementation
  - allow for querying using any default model(s) + easy extension to include custom models
  - better integration with the OMOP CDM
- Look at alternate routes to integration such as leveraging the [OHDSI webapi](https://github.com/OHDSI/WebAPI) which is installed on top of all EHDEN OMOP CDM DB's
- Increase functionality of the UI


