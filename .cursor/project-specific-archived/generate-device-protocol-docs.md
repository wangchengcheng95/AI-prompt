# Generate Device Protocol Documentation

## Overview

Create comprehensive documentation for device communication protocols used in the Edge Agent project, including Modbus RTU, TCP, and Serial protocols.

## Steps

1. **Protocol Overview**
    - List all supported communication protocols
    - Document protocol selection and configuration
    - Explain when to use each protocol type
    - Include architecture diagrams showing protocol layers
2. **Modbus RTU Protocol**
    - Document Modbus RTU specifications
    - List supported function codes (e.g., Function Code 4 for reading input registers)
    - Document register addressing scheme
    - Include device address configuration
    - Provide communication flow examples
    - Document timeout and retry mechanisms
3. **TCP Protocol**
    - Document TCP server configuration (port, timeout, buffer size)
    - Document message formats (length-based, delimiter-based)
    - Include connection management (max connections, exclusive mode)
    - Provide data flow diagrams
    - Document response handling
4. **Serial Protocol**
    - Document serial port configuration (baudrate, databits, stopbits, parity)
    - Document message formats and framing
    - Include timeout and retry mechanisms
    - Provide communication examples
5. **Sensor-Specific Protocols**
    - Document protocol for each sensor type:
      - `power_htac8uis`: Modbus register addresses and data format
      - `power_hc33c3`: Modbus register addresses and data format
      - `th_sht30`: Modbus register addresses and data format
      - `weight_sj101cx`: Modbus register addresses and data format
      - `water_modx420`: Modbus register addresses and data format
      - `tcp_scanner`: TCP message format and protocol
      - `serial_scanner`: Serial message format and protocol

## Device Protocol Documentation Checklist

- [ ] Protocol overview complete
- [ ] Modbus RTU protocol documented with function codes and registers
- [ ] TCP protocol documented with message formats
- [ ] Serial protocol documented with configuration parameters
- [ ] All sensor-specific protocols documented
- [ ] Communication flow diagrams included
- [ ] Configuration examples provided
- [ ] Documentation formatted per project standards (see `docs/` directory)
