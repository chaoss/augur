To test augur, set up your environment for testing:

`
export DB_TEST_URL=mysql+pymysql://<username>:<pass>@<host>:<post>/<database>
`

After that, run `make test` to run the pytest unit tests.

If you don't have both Python 2 and 3, you can run the tests individually

 - Python 2: `python2 -m pytest`
 - Python 3: `python3 -m pytest`

To test the Augur API, run `make test-api`.
- You will need to add a Postman API key to your `augur.config.json`.
