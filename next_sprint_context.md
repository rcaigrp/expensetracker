# Next Sprint Context: ExpenseTracker

## Status
Parked due to budget exhaustion and persistent test failures.

## Known Bugs / Failures
- `pytest /workspace/projects/ExpenseTracker/acceptance_tests` consistently returns exit code 1.
- Truncated stderr/stdout logs indicate pip warnings but no clear test failure reason in the provided logs.
- Possible issues:
  - `pytest` environment setup in Docker containers.
  - Test mocking (`responses`/`unittest.mock`) not correctly configured.
  - File I/O paths (`os.getcwd()` vs absolute) causing mismatches between module and tests.
  - `sys.path` adjustments for module imports.

## Checklist for Resumption
1. Verify `pytest` runs correctly in the Docker environment.
2. Check `responses` library mocking for file I/O or API calls (if any).
3. Ensure absolute paths are used consistently for data files.
4. Run tests locally in a virtual environment to isolate system-wide pip issues.
5. Review exact pytest output for assertion errors or import failures.
