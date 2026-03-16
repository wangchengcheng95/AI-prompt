# Generate MQTT/Device Protocol Documentation

## Overview

Create comprehensive documentation for MQTT topics, message formats, and device communication protocols (Modbus, TCP, Serial) following the project's documentation standards.

## Steps

1. **MQTT Protocol Documentation**
    - Document MQTT broker configuration and connection details
    - List all MQTT topics used for data upload
    - Document message formats (Protobuf, JSON, Custom Frame)
    - Include QoS levels and retention policies
    - Provide message examples for each sensor type
2. **Device Communication Protocols**
    - Document Modbus RTU protocol specifications
    - Document TCP server protocol (for scanners)
    - Document Serial port protocol (for scanners)
    - Include register addresses, function codes, and data formats
    - Provide communication flow diagrams
3. **Data Models**
    - Define all Protobuf message types
    - Document sensor data structures
    - Include field descriptions, types, and units
    - Show relationships between models
    - Provide example payloads for each sensor type
4. **Usage Examples**
    - Common use case scenarios
    - MQTT publish/subscribe examples
    - Device communication examples
    - Error handling examples
    - Testing with mqtt_listener tool

## Protocol Documentation Checklist

- [ ] MQTT broker configuration documented
- [ ] All MQTT topics listed with descriptions
- [ ] Message formats documented (Protobuf/JSON/Frame)
- [ ] Modbus RTU protocol documented
- [ ] TCP/Serial protocols documented
- [ ] Data models defined with field descriptions
- [ ] Usage examples provided
- [ ] Documentation formatted per project standards (see `docs/` directory)
