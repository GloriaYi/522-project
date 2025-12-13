## Test suite developer notes

### Running the tests
Tests are run using the `pytest` command in the root of the project. This command will automatically discover all tests inside the `tests/` directory.

### Preparing test data
No special preparation is needed for the test data. Small inline DataFrames are used for unit tests.

### Test teardown
Tests clean up after themselves, no manual cleanup is needed. Tests that write output files use `tmp_path` and Pytest’s `tmp_path` fixture automatically creates a temporary directory that is deleted after the test session. Tests do not write anything into `results/` or `data/`
