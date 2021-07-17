# Generic Python Library for ML
This is a generic python library project for building ml tools.

 ## Documentation
 Contains `/docsrc/` for generating documentation with sphynx.

## Installation
.

## Usage 
.


## Contributing
.

## Running the Tests
The quickest way to run the tests is with a docker container. First, pull the image with `docker pull <repo>/container/path:<tag>`, then run and mount the container to your working directory and run the tests with:

```
docker run --mount type=bind,source=/path/to/your/project/,destination=/workspace --workdir /workspace/ -it <repo>/container/path:<tag> /bin/bash

python ./setup.py pytest
```

## Version
This project skeleton has a hard-coded version of `0.0.1`.
 