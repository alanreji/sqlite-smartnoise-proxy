# sqlite-smartnoise-proxy
The SmartNoise MITM Proxy prototype is a proof of concept implementation of a privacy-preserving technology using differential privacy (DP). The goal of this prototype is to demonstrate the functionality of the SmartNoise SDK by creating a MITM proxy that sits between a querier and a database, and enables basic aggregate queries while rejecting other queries.

**Table of Contents**

<!--ts-->
   * [Installation](#installation)
   * [Usage](#usage)
   * [Unit tests](#unit-tests)
   * [Configuration and metadata](#configuration-and-metadata)
   * [DB reinitialization](#db-reinitialization)
<!--te-->

#### Installation
- Clone the project repository to your local machine using `git clone <repository URL>`
- Navigate to the project directory using `cd <project directory>`
- Create a virtual environment using `python3 -m venv venv`
- Activate the virtual environment using `source venv/bin/activate` on Linux/Mac or `venv\Scripts\activate` on Windows
- Upgrade pip using `pip install --upgrade pip`
- Install project dependencies using `pip install -r requirements.txt`
- Run the application using `python run.py`
- Access the API at http://127.0.0.1:5050/runQuery/ (There is no web page)
- Remember to deactivate the virtual environment using deactivate when you're done using the application

#### Usage

```bash
curl --location 'http://127.0.0.1:5050/runQuery' \
--header 'X-API-Key: d21976fe-b5a0-4132-9d0d-f88f6b1d398c' \
--header 'Content-Type: application/json' \
--data '{
    "query": "SELECT COUNT(*) FROM employees;"
}'
```
The API key can be found in the `config/config.json` file (API keys shouldn't be saved in config files).

#### Unit tests

Run unit tests using `python unit_tests.py`

#### API testing

API testing can be done using the postman collection test suite available at https://github.com/alanreji/smartnoise-proxy-api-test-suite

#### Configuration and metadata

> **Warning**
> It is important to not store sensitive information such as privacy parameters and API keys in the config file, as this can lead to potential security breaches. While this project may demonstrate the basic functionality of an interface/proxy for a DBMS, it is recommended to take additional security measures and best practices when deploying it in a real-world setting.

The application works with a set of configuration, which can be found in the `config` directory. The config file contains `allowed_sql_functions`, `api_key` and privacy attributes - `epsilon`, `delta`, and `privacy budget`.
The `metadata.yaml` contains metadata about the datastore/tables which we are applying DP on.

#### DB reinitialization

If you want to work with a different set of data, you have to delete the existing `.db` file from the `data` folder, update the CSV with modified data, and run `python db_init_script.py`. This will populate the new db. When the data is changed, the 'metadata.yaml' also needs to be updated.
