# btamp

btamp is a simple tamper script designed to enhance SQL injection testing when used in conjunction with SQLMap. It encodes SQL payloads into base64, enabling evasion of systems that encrypt or encode input parameters.

## Installation

1. Clone the btamp repository:

    ```bash
    git clone https://github.com/nexzydev/btamp.git
    ```

2. Usage:

    - Download `btamp.py`.
    - Run SQLMap with the `--tamper` option pointing to `btamp.py`.

    Example:

    ```bash
    sqlmap -u "TARGET_URL_HERE" --tamper=path/to/btamp.py --other-options
    ```

## Features

- Encodes SQL payloads into base64.
- Designed to bypass systems encrypting or encoding input parameters.
- Works seamlessly with SQLMap for SQL injection testing.

## Usage

1. Download `btamp.py` from this repository.
2. Run SQLMap with `btamp.py` as the tamper script.

## Legal Disclaimer

This project is intended for educational and ethical security testing purposes only. Ensure proper authorization before using against any system or application. The developers hold no liability for any misuse of this tool.
