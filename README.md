# CommunityData.io

A federated data catalog for community-managed open data portals.

## Current status

A basic CKAN instance to support this effort has been [set up](http://communitydata.io/api/util/status), and several community-managed data portals have [been identified](communityopendatacatalogs.csv).

## How you can help

See the [issues list](https://github.com/mheadd/communitydata.io/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22) for opportunities to assist this project. Got ideas? Add a [new issue](https://github.com/mheadd/communitydata.io/issues/new).

## Setup

This project runs on [CKAN](http://github.com/ckan/ckan). This repo is
self-contained, all the source code you need to run the project is within the
repo. CKAN and re-usable extensions are included as submodules. To check them
out, run:

```git submodule update```

If you are used to setting up CKAN development environments, you can follow
your usual workflow.

Alternatively, you can also initialize this repo as a
[datacats](http://github.com/boxkite/datacats) environment:

```
pip install datacats
datacats pull
cd communitydata.io/
datacats init
```

## Deployment
If you are a committer and want deploy privileges, talk to
[@mheadd](http://github.com/mheadd).
