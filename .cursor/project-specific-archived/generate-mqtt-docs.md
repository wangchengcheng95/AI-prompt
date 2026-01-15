# Generate MQTT Documentation

## Overview

Create comprehensive documentation for MQTT topics, message formats, and data upload protocols.

## Steps

1. **MQTT Configuration**
    - Document broker connection configuration
    - Document client ID format and naming conventions
    - Include authentication and security settings
    - Document connection timeout and keepalive settings
    - Include retry and reconnection policies
2. **MQTT Topics**
    - List all MQTT topics used for data upload
    - Document topic naming conventions
    - Include topic structure and hierarchy
    - Document QoS levels for each topic
    - Provide examples: `data/sensor/device`
3. **Message Formats**
    - Document Protobuf message format (primary format)
    - Document JSON message format (if used)
    - Document Custom Frame format (if used)
    - Include message structure and field descriptions
    - Provide message examples for each sensor type
4. **Sensor Data Messages**
    - Document message format for each sensor type:
      - Power sensors: Power data structure
      - Temperature/humidity sensors: Temperature and humidity data structure
      - Weight sensors: Weight data structure
      - Flow sensors: Flow data structure
      - TCP devices: TCP message format and protocol
      - Serial devices: Serial message format and protocol
5. **Usage Examples**
    - MQTT publish examples
    - Using mqtt_listener tool for debugging
    - Message parsing examples
    - Error handling examples

## MQTT Documentation Checklist

- [ ] MQTT broker configuration documented
- [ ] All topics listed with descriptions and QoS levels
- [ ] Message formats documented (Protobuf/JSON/Frame)
- [ ] All sensor data message structures documented
- [ ] Usage examples provided
- [ ] Testing tools documented (mqtt_listener)
- [ ] Documentation formatted per project standards (see `docs/` directory)
