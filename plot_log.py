import pyulog
import matplotlib.pyplot as plt
import argparse

def read_and_plot_ulog(file_name: str, message_name: str):
    """
    Read a ULog file and plot all fields of the specified message.

    Args:
        file_name (str): Path to the ULog file.
        message_name (str): Name of the message to plot.

    Returns:
        None
    """
    # Read the ULog file
    ulog = pyulog.ULog(file_name)

    message_data = ulog.get_dataset(message_name)

    timestamp = message_data.data['timestamp'] / 1e6  # Convert to seconds

    for field_name in message_data.data:
        if field_name != 'timestamp' and field_name != 'timestamp_sample':  # Skip the timestamp fields for plotting
            print(field_name)
            field_data = message_data.data[field_name]
            
            plt.plot(timestamp, field_data, label=field_name)
        
    plt.xlabel('Time [s]')
    plt.ylabel('Unknown Units []')
    plt.title(message_name)
    plt.legend(loc='best')
    plt.grid(True)
    plt.savefig(f"{message_name}.png", dpi=400)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read and plot ULog file.')
    parser.add_argument('--file_name', default='logs/test.ulg', help='Path to the ULog file.')
    parser.add_argument('--message_name', default='actuator_controls_0', help='Name of the message to plot.')
    args = parser.parse_args()

    read_and_plot_ulog(args.file_name, args.message_name)
