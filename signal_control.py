def traffic_signal_control(vehicle_count):
    if vehicle_count > 200:
        return 'Green'
    else:
        return 'Red'

if __name__ == "__main__":
    test_count = 220  # Example vehicle count
    signal_status = traffic_signal_control(test_count)
    print(f'Traffic Signal Status: {signal_status}')
