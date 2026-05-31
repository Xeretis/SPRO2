import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


def open_and_plot():
    # Open file picker
    file_path = filedialog.askopenfilename(
        title="Select BIN file",
        filetypes=[("BIN files", "*.bin"), ("All files", "*.*")]
    )

    if not file_path:
        return

    try:
        # Read 16-bit little-endian signed integers
        data = np.fromfile(file_path, dtype='<i2')

        print(f"Loaded {len(data)} samples")

        # Plot
        plt.figure(figsize=(12, 5))
        plt.plot(data)
        plt.title(f"Plot of {file_path}")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.show()

    except Exception as e:
        print("Error:", e)


# Create GUI window
root = tk.Tk()
root.title("BIN Plotter")
root.geometry("300x120")

button = tk.Button(
    root,
    text="Open .bin File",
    command=open_and_plot,
    height=2,
    width=20
)

button.pack(pady=30)

root.mainloop()