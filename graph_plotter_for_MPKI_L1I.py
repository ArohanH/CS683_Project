import matplotlib.pyplot as plt
import numpy as np

def plot_multiple_mpki_traces(trace_names, mpki_values_list, labels):
    """
    Plots a bar graph of MPKI values for multiple server traces.

    Parameters:
    - trace_names (list): List of server trace names (e.g., ["Trace1", "Trace2"]).
    - mpki_values_list (list of lists): A list where each sublist contains 3 MPKI values for a trace.
    - labels (list): List of labels for each MPKI value type (e.g., ["MPKI1", "MPKI2", "MPKI3"]).
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
        mpki_values = [trace[i] for trace in mpki_values_list]
        plt.bar(x + offsets[i], mpki_values, width=bar_width, label=labels[i])
    
    # Set x-axis labels
    plt.xlabel('Server Traces')
    plt.ylabel('MPKI Values')
    plt.title('L1I MPKI Values for Multiple Server Traces')
    plt.xticks(x + bar_width, trace_names)
    plt.legend(title="MPKI Types")

    # Display values on top of each bar
    for i in range(num_mpki):
        for j, val in enumerate(mpki_values_list):
            plt.text(x[j] + offsets[i], val[i] + 0.1, round(val[i], 2), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

# Example usage
trace_names = ["server_021", "server_022", "server_023", "server_024", "server_025", "server_026", "server_027", "server_028", "server_029", "server_030"]
mpki_values_list = [
    [42.3847, 6.4206, 48.8053],  # MPKI values for Trace1
    [42.4429, 6.3950, 48.8379],  # MPKI values for Trace2
    [12.4898, 37.5286, 50.0184],   # MPKI values for Trace3
    [12.4905, 37.6558, 50.1463],   # MPKI values for Trace4
    [17.5060, 37.8045, 55.3105],   # MPKI values for Trace5
    [17.2518, 37.4343, 54.6861],   # MPKI values for Trace6
    [17.3866, 37.7609, 55.14],   # MPKI values for Trace7
    [23.3984, 34.5108, 57.9092],   # MPKI values for Trace8
    [23.1126, 34.1707, 57.2833],   # MPKI values for Trace9
    [23.1203, 35.8327, 58.953],   # MPKI values for Trace10
]
labels = ["MPKI_kernel", "MPKI_user", "MPKI_overall"]

plot_multiple_mpki_traces(trace_names, mpki_values_list, labels)
