def detect_incident(vehicle_count):
    if vehicle_count > 200:
        return True
    return False

if __name__ == "__main__":
    test_count = 220  # Example vehicle count
    incident_detected = detect_incident(test_count)
    if incident_detected:
        print('Traffic incident detected!')
    else:
        print('No incident detected.')
