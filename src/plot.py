import re
import matplotlib.pyplot as plt

# Function to extract the PC values from the text lines
def extract_pc_values(filename):
    pc_values = []
    with open(filename, 'r') as file:
        for line in file:
            # Using regular expression to find the last value in the line (PC value)
            match = re.search(r'is (\d+)$', line.strip())
            if match:
                pc_values.append(int(match.group(1)))
    return pc_values

# Generate a plot of PC values
def plot_pc_values(pc_values):
    plt.plot(pc_values, marker='o')
    plt.title('Plot of Instruction Pointer (PC) values')
    plt.xlabel('Instruction Number')
    plt.ylabel('Instruction Pointer (PC)')
    plt.grid(True)
    plt.show()

# Main function to read the file and plot the values
if __name__ == "__main__":
    filename = 'output.txt'  # Replace with your text file path
    pc_values = extract_pc_values(filename)
    plot_pc_values(pc_values)
