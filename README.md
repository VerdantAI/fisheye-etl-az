# fisheye-etl-az
Setup and load Fisheye data into Azure

## Overview

In this case we are using Azure services.  We'll use the Serverless functions to manage the load into ADLS gen 2 (as a blob) then load that blob into Postgres.  Some links for reference:
* [Azure Setup Instructions](https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-serverless-cloud-etl-01) here to help get us started.
* [ADLS into Postgres](https://docs.microsoft.com/en-us/azure/data-factory/connector-azure-database-for-postgresql?tabs=data-factory)


## EPA ECHO Data
Our initial use case is data from the [EPA ECHO](https://echo.epa.gov/tools/data-downloads#exporter) dataset.  We'll start with these.
* [FRS Facility Data](https://echo.epa.gov/tools/data-downloads/frs-download-summary)
* [ECHO Demographic Data](https://echo.epa.gov/tools/data-downloads/demographic-download-summary)
* [ECHO Air Quality Data](https://echo.epa.gov/tools/data-downloads/icis-air-download-summary)
* [ECHO Air Emissions Summary](https://echo.epa.gov/tools/data-downloads/air-emissions-download-summary)

Most of these are `.zip` files containing multile child files.  We'll have to identify how to use Azure resources to unpack and load them, since the examples basically loady from local `.csv` files.

## Local Dev
We are using [Python virtual environments](https://docs.python.org/3/library/venv.html). If you are unfamiliar with `venv` please reach out to the other contributors.  Please use the [requirements.txt](requirements.txt) in the current environment.

Make sure you have a file called `.env` that resembles the file [.env.sample](.env.sample).  Cop the sample file and replace with your values.

### Database
For local dev, please install postgres and set up a database called "fisheye-dev".  We'll create a schema called "epa" until we have a full architecture review.  If you are using [Windows Subsystem for Linux (WSL2)](https://docs.microsoft.com/en-us/windows/wsl/install) you can follow [these instructions for Postgresql](https://harshityadav95.medium.com/postgresql-in-windows-subsystem-for-linux-wsl-6dc751ac1ff3).  You will need to install the database locally until we have establihed a public SQL server.

Remember to login to postgres as `postgres` and create a user for the application.  These credentials should be unique and will only apply to your local database.  Here is an example

```
>  sudo -u postgres createuser buddha
> sudo -u postgres createdb fisheye_dev
```
Login to the db
```
> sudo -u postgres psql
> psql (12.11 (Ubuntu 12.11-0ubuntu0.20.04.1))
Type "help" for help.

> alter user buddha with encrypted password 'epa4you';
> grant all privileges on database fisheye_dev to buddha ;
```

At this point, you're still the `postgres` user, so logout and re-enter the db

```
psql buddha -d fisheye_dev
```

There are no tables.  But let's create the epa schema.

```
> create schema epa
```

All right! Now you should have some structure and you can either a) join the ETL team or b) go back to Python.

You may have to run the script several times to load the database.  It runs out of memory, but if you run it again it will just work on the new tables.