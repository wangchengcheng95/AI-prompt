# Generate MQTT Documentation

## Overview

Create comprehensive documentation for MQTT topics, message formats, and data upload protocols used in the Edge Agent project.

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
    - Provide examples: `rdata/sensor/server`
3. **Message Formats**
    - Document Protobuf message format (primary format)
    - Document JSON message format (if used)
    - Document Custom Frame format (if used)
    - Include message structure and field descriptions
    - Provide message examples for each sensor type
4. **Sensor Data Messages**
    - Document message format for each sensor type:
      - `power_htac8uis`: Power data structure
      - `power_hc33c3`: Power data structure
      - `th_sht30`: Temperature and humidity data structure
      - `weight_sj101cx`: Weight data structure
      - `water_modx420`: Water flow data structure
      - `tcp_scanner`: Scanner data structure
      - `serial_scanner`: Scanner data structure
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
