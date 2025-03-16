import asyncio
import serial_asyncio
from app.exceptions import ToolError
from app.tool.base import BaseTool, CLIResult, ToolResult

class SonarDistanceSensor(BaseTool):
    """
    A tool for reading a distance measurement from the HC-SR04 Sonar Distance Sensor.
    Assumes the sensor is connected via a microcontroller to a serial port.
    """
    name: str = "SonarDistanceSensor"
    description: str = (
        "Reads a distance measurement from the HC-SR04 sonar sensor. "
        "Parameters include the serial port (e.g., '/dev/ttyUSB0' or 'COM3') "
        "and optionally the baud rate (default is 115200)."
    )
    parameters: dict = {
        "type": "object",
        "properties": {
            "port": {
                "type": "string",
                "description": "The serial port for the sensor (e.g., '/dev/ttyUSB0' on Linux or 'COM3' on Windows)"
            },
            "baud": {
                "type": "integer",
                "description": "The baud rate for the serial connection",
                "default": 115200
            }
        },
        "required": ["port"]
    }

    async def execute(self, port: str, baud: int = 115200, **kwargs) -> CLIResult:
        """
        Connects to the sensor over the provided serial port and reads one line of data.
        """
        try:
            # Open an asynchronous serial connection using pyserial-asyncio.
            reader, writer = await serial_asyncio.open_serial_connection(url=port, baudrate=baud)
        except Exception as e:
            raise ToolError(f"Error opening serial port: {e}")

        try:
            # Wait up to 5 seconds for a line of sensor data.
            try:
                line = await asyncio.wait_for(reader.readline(), timeout=5.0)
            except asyncio.TimeoutError:
                raise ToolError("Timeout while reading from sensor.")

            # Decode the line (assuming UTF-8 encoding).
            reading = line.decode("utf-8", errors="replace").strip()
            # Return the sensor reading in the tool result.
            return ToolResult(output=reading)
        finally:
            writer.close()
            await writer.wait_closed()

if __name__ == "__main__":
    # For local testing
    async def test():
        sensor = SonarDistanceSensor()
        result = await sensor.execute(port="/dev/ttyUSB0")  # adjust the port as needed
        print("Sensor Reading:", result.output)
    asyncio.run(test())
