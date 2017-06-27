[![Build Status](https://img.shields.io/travis/pennsignals/fuzzy-engine.svg?style=flat-square)](https://travis-ci.org/pennsignals/fuzzy-engine) [![Docker Repository on Quay](https://quay.io/repository/pennsignals/fuzzy-engine/status "Docker Repository on Quay")](https://quay.io/repository/pennsignals/fuzzy-engine)

`fuzzy-engine` is a mock web service that returns JSON formatted HTTP responses containing randomized patient data. This web service is for the ["Real-time Meatspace Data Science"](https://github.com/pennsignals/data-intelligence) presentation given by [Jason Walsh](https://github.com/rightlag) and [Michael Becker](https://github.com/mdbecker) for the [Data Intelligence Conference](http://data-intelligence.ai/) hosted by Capital One.

# Usage

## Local Deployment

    $ git clone https://github.com/pennsignals/fuzzy-engine.git
    $ cd fuzzy-engine
    $ docker-compose up -d

Visit: http://localhost/

<p align="center">
  <img src="https://user-images.githubusercontent.com/2184329/27520384-ad1f3736-59d8-11e7-9c60-c1e41a3ddbd3.png">
</p>

## Cloud Deployment

> **Note:** You must be *logged* in to Docker Cloud for the button to work correctly. If you are not logged in, you’ll see a 404 error instead.

To deploy Docker Cloud nodes, you first need to grant Docker Cloud access to your infrastructure; this could mean granting access to a cloud services provider such as AWS or Azure, or installing the Docker Cloud Agent on your hosts. Once complete, you can provision nodes directly from within Docker Cloud using the Web UI, CLI or API.

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/)
