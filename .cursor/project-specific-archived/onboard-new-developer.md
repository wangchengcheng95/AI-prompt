# Onboard New Developer

## Overview

Comprehensive onboarding process to get a new developer up and running quickly with the project.

## Steps

1. **Environment setup**
    - Install Go 1.24+
    - Set up development environment
    - Configure IDE and extensions (VS Code/Cursor recommended)
    - Set up git and SSH keys
    - Install Docker (for MQTT broker and testing)
    - Install socat (for virtual serial port testing): `sudo apt-get install socat`
2. **Project familiarization**
    - Review project structure (see `docs/REPOSITORY_STRUCTURE.md`)
    - Understand architecture (see `docs/设计文档.md`)
    - Read key documentation in `docs/` directory
    - Set up local MQTT broker (using Docker: `docker/infrastructure`)
    - Set up virtual serial ports for testing (use `test/integration/create_virtual_serial.sh`)
3. **Testing setup**
    - Run integration tests: `test/integration/`
    - Use sensor_mock for device simulation: `tools/sensor_mock/`
    - Use mqtt_listener for debugging: `tools/mqtt_listener/`
    - Review test scripts and understand test patterns

## Onboarding Checklist

- [ ] Development environment ready (Go 1.24+, Docker, socat)
- [ ] All tests passing (`go test ./...`)
- [ ] Can run application locally with test config
- [ ] MQTT broker set up and working
- [ ] Virtual serial ports configured for testing
- [ ] Can run integration tests successfully
- [ ] First PR submitted
