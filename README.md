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
