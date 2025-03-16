import serial
import time
import statistics

# Configuration
PORT = '/dev/tty.usbserial-0001'  # Serial port for the sonar sensor
BAUD_RATE = 115200                # Baud rate for serial communication
MOVEMENT_THRESHOLD = 10           # Distance change (in cm) that indicates movement
SAMPLE_SIZE = 5                   # Number of readings to average
DELAY = 0.1                       # Delay between readings in seconds

def detect_movement():
    """
    Continuously reads from the sonar sensor and detects movement.
    """
    try:
        # Open serial connection
        print(f"Attempting to connect to sonar sensor on {PORT}...")
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        print("Connected to sonar sensor!")
        
        # Initialize variables
        previous_distance = None
        readings = []
        
        print("Starting movement detection...")
        print("Press Ctrl+C to stop")
        
        while True:
            try:
                # Read data from sensor
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    
                    # Try to parse the distance value
                    try:
                        distance = float(line)
                        print(f"Current distance: {distance:.2f} cm")
                        
                        # Add to readings list
                        readings.append(distance)
                        if len(readings) > SAMPLE_SIZE:
                            readings.pop(0)
                        
                        # Calculate average distance from readings
                        if len(readings) == SAMPLE_SIZE:
                            avg_distance = statistics.mean(readings)
                            
                            # Check for movement
                            if previous_distance is not None:
                                distance_change = abs(avg_distance - previous_distance)
                                if distance_change > MOVEMENT_THRESHOLD:
                                    print(f"MOVEMENT DETECTED! Distance changed by {distance_change:.2f} cm")
                                    if avg_distance < previous_distance:
                                        print("Someone is approaching the sensor")
                                    else:
                                        print("Someone is moving away from the sensor")
                            
                            previous_distance = avg_distance
                    except ValueError:
                        # If the line isn't a valid number, just ignore it
                        pass
            
            except Exception as e:
                print(f"Error reading from sensor: {e}")
            
            time.sleep(DELAY)
    
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nStopping movement detection")
    finally:
        # Close serial connection if it was opened
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed")

if __name__ == "__main__":
    detect_movement()