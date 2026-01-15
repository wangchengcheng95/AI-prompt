# Run Regression Tests and Fix Failures

## Overview

Execute regression tests from both `test/integration/` (Shell scripts) and `test/regression/` (Go module), analyze failures, fix errors systematically, and verify all tests pass. This ensures the system maintains correctness across data collection, device communication, and message queue workflows.

## Test Structure

### Integration Tests (`test/integration/`)
- Shell script-based end-to-end tests
- Test multiple components: main application, mock services, message listeners
- Use virtual serial ports (socat) for device simulation
- Require message broker running on localhost

**Test scripts:**
- `test_basic.sh` - Basic integration test
- `test_full.sh` - Full integration test with message listener
- `test_device.sh` - Device communication integration test
- `test_device_mqtt.sh` - Device communication full data flow test

### Regression Tests (`test/regression/`)
- Independent Go module with its own `go.mod`
- Automated test framework with test cases, verifiers, and reporters
- Manages service orchestration (message broker, mock services, main application)
- Generates test reports

## Steps

### 1. **Prepare Test Environment**

**Check dependencies:**
- Verify `go` (1.24+), `socat`, `docker`, `docker-compose` are installed
- Check MQTT broker is running (or start via `docker compose`)

**Compile binaries:**
- Build main application: `go build -o bin/app ./cmd`
- Build mock services: `cd tools/mock && go build -o mock_service`
- Build message listener: `cd tools/listener && go build -o listener`
- Build regression test: `cd test/regression && go build -o regression_test ./cmd/runner`

**Setup virtual serial ports (for regression tests):**
```bash
cd test/regression
./scripts/create_virtual_serial.sh start
```

### 2. **Run Integration Tests**

Execute each integration test script from `test/integration/`:

```bash
cd test/integration
./test_basic.sh
./test_full.sh
./test_device.sh
./test_device_mqtt.sh
```

**Capture:**
- Exit codes (0 = success, non-zero = failure)
- Test output and error messages
- Log files from `logs/` and `/tmp/`
- Process IDs for cleanup

**Common failure patterns:**
- Binary not found (compilation required)
- Virtual serial port creation failed (socat not installed or ports in use)
- Message broker connection failed (broker not running)
- Timeout errors (service startup or data collection)
- Data validation failures (message parsing, data format)

### 3. **Run Regression Tests**

```bash
cd test/regression
./regression_test --config configs/test_config.yaml --verbose
```

**Capture:**
- Exit codes (0 = all passed, 1 = failures, 3 = service startup failed)
- Test report from `reports/`
- Service logs from `logs/`
- MQTT verification results

**Test case types:**
- Modbus device tests (power devices, temperature/humidity devices, weight devices)
- TCP device tests
- Serial device tests

### 4. **Analyze Failures**

**Categorize failures:**
- **Compilation errors**: Missing dependencies, syntax errors, import issues
- **Service startup failures**: Port conflicts, config errors, missing binaries
- **Communication errors**: Serial port connection, message broker connection, TCP connection
- **Data validation errors**: Message parsing, data format, missing fields
- **Timeout errors**: Service health checks, data collection timeouts
- **Resource cleanup errors**: Process cleanup, file cleanup, port cleanup

**Identify root causes:**
- Check error messages and stack traces
- Review relevant log files (`logs/app.log`, `logs/mock.log`, etc.)
- Verify configuration files match test requirements
- Check if failures are related to recent code changes
- Verify test environment setup (ports, broker, binaries)

**Prioritize fixes:**
1. Critical: Service startup failures, compilation errors
2. High: Communication errors, data validation errors
3. Medium: Timeout errors, resource cleanup issues
4. Low: Flaky tests, minor logging issues

### 5. **Fix Issues Systematically**

**For each failure category:**

**Compilation errors:**
- Fix syntax errors, missing imports, type mismatches
- Ensure Go version compatibility (1.24+)
- Check module dependencies and `go.mod` files

**Service startup failures:**
- Fix configuration file errors (YAML syntax, missing fields, invalid values)
- Resolve port conflicts (check if ports are in use, update configs)
- Ensure binaries are compiled and executable
- Fix Docker/message broker startup issues

**Communication errors:**
- Fix serial port connection issues (virtual port paths, permissions)
- Fix message broker connection issues (broker URL, credentials, topic names)
- Fix TCP connection issues (addresses, timeouts, connection handling)
- Verify device communication protocols match specifications

**Data validation errors:**
- Fix message structure mismatches
- Ensure data fields match expected format
- Fix data type conversions and parsing logic
- Verify message headers and payloads

**Timeout errors:**
- Increase timeout values if legitimate delays exist
- Fix service health check logic
- Fix data collection polling intervals
- Ensure proper context cancellation handling

**Resource cleanup:**
- Fix process cleanup in test scripts (trap handlers, PID tracking)
- Fix file cleanup (log files, temporary files)
- Fix virtual serial port cleanup (socat process management)

**Code changes must:**
- Follow project architecture (handler/service/repository layers)
- Respect engineering doctrine (context propagation, error handling, no implicit behavior)
- Maintain Go backend rules (no panic, no global variables, proper error wrapping)
- Not break existing functionality

### 6. **Re-run Tests After Fixes**

**After each fix:**
1. Re-compile affected binaries
2. Re-run the specific failing test
3. Verify the fix resolves the issue
4. Check for regressions in other tests

**After all fixes:**
1. Run full integration test suite
2. Run full regression test suite
3. Verify all tests pass
4. Check test reports for any warnings

### 7. **Cleanup Test Environment**

**Integration tests:**
- Test scripts use `trap` handlers for automatic cleanup
- Manually verify: `pkill -f socat`, `pkill -f mock`, `pkill -f app`, `pkill -f listener`
- Remove test log files from `logs/` and `/tmp/`
- Remove virtual serial port symlinks from `/tmp/vserial/`

**Regression tests:**
```bash
cd test/regression
./scripts/create_virtual_serial.sh stop
./regression_test --cleanup
```

## Test Recovery Checklist

- [ ] Dependencies verified (go, socat, docker, docker-compose)
- [ ] All binaries compiled successfully
- [ ] Virtual serial ports created (for regression tests)
- [ ] MQTT broker running
- [ ] Integration tests executed and results captured
- [ ] Regression tests executed and results captured
- [ ] Failures categorized and root causes identified
- [ ] Fixes applied following project rules
- [ ] Tests re-run after each fix
- [ ] All tests passing
- [ ] Test environment cleaned up
- [ ] Test reports reviewed

## Common Issues and Solutions

### Issue: Binary not found
**Solution:** Compile the binary: `go build -o <binary> <path>`

### Issue: Virtual serial port creation failed
**Solution:**
- Install socat: `apt-get install socat`
- Check if ports are in use: `lsof | grep pts`
- Restart virtual ports: `./scripts/create_virtual_serial.sh restart`

### Issue: Message broker connection failed
**Solution:**
- Start message broker: `cd docker/infrastructure && docker compose up -d`
- Verify broker is running: `docker ps | grep broker`
- Check broker URL in configs matches running broker

### Issue: Test timeout
**Solution:**
- Check service health: review logs for startup errors
- Increase timeout values in test configs if legitimate delays exist
- Verify services are actually running: `ps aux | grep <service>`

### Issue: Data validation failure
**Solution:**
- Check message structure matches expected format
- Verify data fields in test fixtures match actual device output
- Review message parsing logic in verifiers

## Notes

- Integration tests modify config files (with backup/restore)
- Tests run multiple background processes; ensure ports are not in use
- All shell commands must have explicit timeouts (per engineering doctrine)
- Test scripts use `set -e` for error handling; failures stop execution
- Regression tests are independent Go module; changes to main module may require updates
