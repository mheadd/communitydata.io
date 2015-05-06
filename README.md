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

### Setting up the Harvester
Point the `ckan.harvest.mq.hostname` variable in the .ini to a redis instance,
which will act as a job queue. Then to run jobs, run the commands in the
harvester [docs](https://github.com/ckan/ckanext-harvest#running-the-harvest-jobs)

Note - if you are using datacats, you can run these commands easily like so:
```
cd community/ckanext-harvest/
datacats paster harvester gather_consumer
datacats paster harvester fetch_consumer
datacats paster harvester run
```

You will of course still need to set up
[harvest sources](communityopendatacatalogs.csv) on the ckan harvest admin
interface at `/harvest`.

## Deployment
If you are a committer and want deploy privileges, talk to
[@mheadd](http://github.com/mheadd).
