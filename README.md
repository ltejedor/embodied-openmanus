# 🤖 OpenManus (Fork): Embodied OpenManus: Bridging AI and the Physical World

This fork of OpenManus extends the original project by adding capabilities for physical world interaction through various sensors and microcontrollers. By integrating with ESP-32 devices and sensors like sonar distance sensors, our agent can now perceive and respond to the physical environment, enabling a new class of embodied AI applications.

Key features of this embodied extension include:
- Integration with ESP-32 microcontrollers for sensor data collection
- Support for multiple sensor types (sonar, raindrop, GPS)
- Real-time movement detection and distance sensing
- Visualization tools for sensor data
- Agent tools that can directly interact with physical hardware

We're also excited to introduce [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL), an open-source project dedicated to reinforcement learning (RL)- based (such as GRPO) tuning methods for LLM agents, developed collaboratively by researchers from UIUC and OpenManus.

## Project Demo

<video src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" data-canonical-src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## Installation

We provide two installation methods. Method 2 (using uv) is recommended for faster installation and better dependency management.

### Method 1: Using conda

1. Create a new conda environment:

```bash
conda create -n open_manus python=3.12
conda activate open_manus
```

2. Clone the repository:

```bash
git clone https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# For hardware support, install additional dependencies
pip install pyserial pyserial-asyncio matplotlib
```

### Method 2: Using uv (Recommended)

1. Install uv (A fast Python package installer and resolver):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:

```bash
git clone https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
```

3. Create a new virtual environment and activate it:

```bash
uv venv --python 3.12
source .venv/bin/activate  # On Unix/macOS
# Or on Windows:
# .venv\Scripts\activate
```

4. Install dependencies:

```bash
uv pip install -r requirements.txt
# For hardware support, install additional dependencies
uv pip install pyserial pyserial-asyncio matplotlib
```

## Configuration

OpenManus requires configuration for the LLM APIs it uses. Follow these steps to set up your configuration:

1. Create a `config.toml` file in the `config` directory (you can copy from the example):

```bash
cp config/config.example.toml config/config.toml
```

2. Edit `config/config.toml` to add your API keys and customize settings:

```toml
# Global LLM configuration
[llm]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
max_tokens = 4096
temperature = 0.0

# Optional configuration for specific LLM models
[llm.vision]
model = "gpt-4o"
base_url = "https://api.openai.com/v1"
api_key = "sk-..."  # Replace with your actual API key
```

### Hardware Configuration

For sensor integration, you may need to update the following:

1. Serial port settings in scripts:
   - Update the `PORT` variable in `sonar_movement_detector.py` to match your device
   - When using the SonarDistanceSensor tool, provide the correct port parameter

2. ESP-32 pin configurations:
   - If needed, modify pin assignments in the Arduino sketches to match your wiring

## Hardware Requirements

To use the embodied features of OpenManus, you'll need the following hardware components:

- ESP-32 microcontroller (ESP32-WROOM or similar)
- HC-SR04 ultrasonic distance sensor
- Optional: Raindrop sensor module
- Optional: GPS module
- Breadboard and jumper wires
- USB cable for connecting ESP-32 to your computer
- Serial adapter if your computer doesn't have a direct serial connection

### Supported Sensors

| Sensor Type | Description | Status |
|-------------|-------------|--------|
| HC-SR04 Sonar | Ultrasonic distance sensor (2cm-400cm range) | Fully supported |
| Raindrop Sensor | Detects water/moisture | Basic support |
| GPS Module | Location tracking | Experimental |

## Hardware Setup

### Sonar Distance Sensor Setup

1. Connect the HC-SR04 sensor to your ESP-32:
   - VCC to 5V
   - GND to GND
   - TRIG to GPIO 47 (configurable in code)
   - ECHO to GPIO 48 (configurable in code)

2. Flash the ESP-32 with the provided code:
   ```bash
   # Using Arduino IDE
   # Open esp-32/lora_depth_sensor/lora_depth_sensor.ino and upload to your device

   # Or using esptool
   esptool.py --port /dev/ttyUSB0 write_flash 0x10000 esp-32/lora_depth_sensor/lora_depth_sensor.ino.bin
   ```

3. Note the serial port your device is connected to (e.g., `/dev/ttyUSB0` on Linux or `COM3` on Windows)

### Raindrop Sensor Setup (Optional)

If you're using the raindrop sensor:

1. Connect the sensor to your ESP-32:
   - VCC to 3.3V
   - GND to GND
   - DO to any digital pin (configured as GPIO 36 in the example code)

2. The same firmware (`lora_depth_sensor.ino`) supports both sensors.

## Sensor Visualization and Interaction

OpenManus includes tools for visualizing and interacting with sensor data:

### Sonar Distance Visualization

The sonar sensor data can be visualized in multiple formats:
- Polar coordinates (sonar_map_polar.png)
- Cartesian coordinates (sonar_map_cartesian.png)
- 3D representation (sonar_map_3d.png)

### Movement Detection

The `sonar_movement_detector.py` script provides real-time movement detection using the sonar sensor:

```bash
# Adjust the PORT variable in the script to match your setup
python sonar_movement_detector.py
```

This will continuously monitor for movement and report when objects approach or move away from the sensor.

## Agent Interaction with Sensors

The OpenManus agent can directly interact with physical sensors through the `SonarDistanceSensor` tool. This allows the agent to:

1. Read distance measurements from the environment
2. Detect obstacles or movement
3. Make decisions based on physical world data

Example agent prompt:
```
Measure the distance to the nearest object and alert me if anything comes closer than 30cm.
```

The agent will use the SonarDistanceSensor tool to continuously monitor distances and provide alerts based on the specified threshold.

## Quick Start

One line for run OpenManus:

```bash
python main.py
```

Then input your idea via terminal!

For unstable version, you also can run:

```bash
python run_flow.py
```

## Example Use Cases

The embodied OpenManus agent can be used for various physical world interaction scenarios:

### 1. Smart Home Monitoring

```
Monitor the room entrance and alert me when someone enters.
```

The agent will use the sonar sensor to detect movement at the entrance and send notifications when someone enters the room.

### 2. Distance-Based Automation

```
Turn on the light when an object is detected within 50cm of the sensor.
```

The agent can trigger actions based on proximity detection, enabling simple automation scenarios.

### 3. Environmental Monitoring

```
Check if it's raining and send me an alert if water is detected.
```

Using the raindrop sensor, the agent can monitor for precipitation and provide weather alerts.

### 4. Data Collection and Analysis

```
Collect distance measurements every 5 minutes for the next hour and create a visualization of the data.
```

The agent can perform systematic data collection and generate visualizations to help analyze patterns over time.

## How to contribute

We welcome any friendly suggestions and helpful contributions! Just create issues or submit pull requests.

Or contact @mannaandpoem via 📧email: mannaandpoem@gmail.com

**Note**: Before submitting a pull request, please use the pre-commit tool to check your changes. Run `pre-commit run --all-files` to execute the checks.

## Community Group
Join our networking group on Feishu and share your experience with other developers!

<div align="center" style="display: flex; gap: 20px;">
    <img src="assets/community_group.jpg" alt="OpenManus 交流群" width="300" />
</div>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mannaandpoem/OpenManus&type=Date)](https://star-history.com/#mannaandpoem/OpenManus&Date)

## Acknowledgement

Thanks to [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
and [browser-use](https://github.com/browser-use/browser-use) for providing basic support for this project!

Additionally, we are grateful to [AAAJ](https://github.com/metauto-ai/agent-as-a-judge), [MetaGPT](https://github.com/geekan/MetaGPT), [OpenHands](https://github.com/All-Hands-AI/OpenHands) and [SWE-agent](https://github.com/SWE-agent/SWE-agent).

OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

## Cite
```bibtex
@misc{openmanus2025,
  author = {Xinbin Liang and Jinyu Xiang and Zhaoyang Yu and Jiayi Zhang and Sirui Hong},
  title = {OpenManus: An open-source framework for building general AI agents},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/mannaandpoem/OpenManus}},
}
```
