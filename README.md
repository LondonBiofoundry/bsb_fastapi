# BasicSynBio API

This API is build with [Fast API](https://fastapi.tiangolo.com) and can be accessed at https://app-basicsynbio.co.uk CORS dependent. The documentation can be viewed at https://app-basicsynbio.co.uk/docs/

At the documentation a list of the endpoints can be seen and tested!

## Testing

This repo uses snapshot testing with pytest, to run simply run:
```bash
$ pytest
```
[![Pytest](https://github.com/LondonBiofoundry/bsb_fastapi/actions/workflows/pytest.yml/badge.svg)](https://github.com/LondonBiofoundry/bsb_fastapi/actions/workflows/pytest.yml)

## Linting

This repo is linted with black python linter, to lint simply run
```bash
$ black .
```
[![Lint](https://github.com/LondonBiofoundry/bsb_fastapi/actions/workflows/black.yml/badge.svg)](https://github.com/LondonBiofoundry/bsb_fastapi/actions/workflows/black.yml)
