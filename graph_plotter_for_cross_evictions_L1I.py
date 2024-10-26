import matplotlib.pyplot as plt
import numpy as np

def plot_multiple_mpki_traces(trace_names, mpki_values_list, labels):
    """
    Plots a bar graph of MPKI values for multiple server traces in thousands (K).

    Parameters:
    - trace_names (list): List of server trace names (e.g., ["Trace1", "Trace2"]).
    - mpki_values_list (list of lists): A list where each sublist contains MPKI values for a trace.
    - labels (list): List of labels for each MPKI value type.
    """
    # Number of traces and types of MPKI per trace
    num_traces = len(trace_names)
    num_mpki = len(labels)
    
    # Generate bar positions
    bar_width = 0.2
    x = np.arange(num_traces)
    offsets = [bar_width * i for i in range(num_mpki)]

    # Create the plot
    plt.figure(figsize=(12, 6))
    
    for i in range(num_mpki):
        # Convert values to thousands
        mpki_values = [trace[i] / 1000 for trace in mpki_values_list]
        plt.bar(x + offsets[i], mpki_values, width=bar_width, label=labels[i])
    
    # Set x-axis labels
    plt.xlabel('Server Traces')
    plt.ylabel('Eviction Numbers (in thousands)')
    plt.title('L1I Cross Evictions for Multiple Server Traces')
    plt.xticks(x + bar_width, trace_names)
    plt.legend(title="Eviction Types")

    # Display values on top of each bar vertically
    for i in range(num_mpki):
        for j, val in enumerate(mpki_values_list):
            # Display values in thousands with 'K' suffix and vertical orientation
            plt.text(x[j] + offsets[i], val[i] / 1000 + 0.1, f"{round(val[i] / 1000, 2)}K", 
                     ha='center', va='bottom', rotation=90)
    
    plt.tight_layout()
    plt.show()

# Example usage
trace_names = ["server_021", "server_022", "server_023", "server_024", "server_025", 
               "server_026", "server_027", "server_028", "server_029", "server_030"]
mpki_values_list = [
    [387144, 36703, 36915, 27291],
    [387525, 36904, 36656, 27294],
    [59690, 65208, 65208, 310078],
    [62880, 62025, 62025, 314533],
    [90737, 84323, 84281, 293764],
    [89827, 82691, 82691, 291652],
    [90022, 83844, 83844, 293765],
    [138604, 95380, 95813, 249295],
    [138652, 92474, 92474, 249233],
    [133965, 97238, 97194, 261133]
]
labels = ["Kernel-Kernel", "Kernel-User", "User-Kernel", "User-User"]

plot_multiple_mpki_traces(trace_names, mpki_values_list, labels)
