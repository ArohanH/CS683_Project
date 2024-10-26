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
    plt.title('L2 MPKI Values for Multiple Server Traces')
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
    [1.8861, 0.5871, 2.4732],  # MPKI values for Trace1
    [2.0408, 0.5730, 2.6138],  # MPKI values for Trace2
    [1.4784, 3.3386, 4.817],   # MPKI values for Trace3
    [1.8758, 3.9963, 5.8721],   # MPKI values for Trace4
    [1.7959, 4.1563, 5.952],   # MPKI values for Trace5
    [1.6948, 4.6063, 6.3011],   # MPKI values for Trace6
    [1.4265, 3.4126, 4.8391],   # MPKI values for Trace7
    [1.8196, 3.3405, 5.1601],   # MPKI values for Trace8
    [1.9784, 2.5822, 4.5606],   # MPKI values for Trace9
    [1.8138, 2.6686, 4.4824],   # MPKI values for Trace10
]
labels = ["MPKI_kernel", "MPKI_user", "MPKI_instruction_overall"]

plot_multiple_mpki_traces(trace_names, mpki_values_list, labels)
