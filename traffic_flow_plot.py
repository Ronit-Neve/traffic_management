import pandas as pd
import matplotlib.pyplot as plt

def plot_traffic_flow(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['timestamp'], data['vehicle_count'], marker='o', linestyle='-')
    plt.xlabel('Timestamp')
    plt.ylabel('Vehicle Count')
    plt.title('Traffic Flow Over Time')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/traffic_flow_plot.png')
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/traffic_data.csv')
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    plot_traffic_flow(data)

