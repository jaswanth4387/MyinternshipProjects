import tkinter as tk
from tkinter import ttk

# Conversion factors
conversion_factors = {
    'Meter': 1.0,
    'Kilometer': 0.001,
    'Centimeter': 100,
    'Millimeter': 1000,
    'Mile': 0.000621371,
    'Yard': 1.09361,
    'Foot': 3.28084,
    'Inch': 39.3701,
}

class LengthConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Length Converter")

        # Variables
        self.value_var = tk.StringVar()
        self.source_unit_var = tk.StringVar()
        self.target_unit_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Entry for user input
        value_label = ttk.Label(root, text="Enter Value:")
        value_label.grid(row=0, column=0, padx=10, pady=10)
        value_entry = ttk.Entry(root, textvariable=self.value_var)
        value_entry.grid(row=0, column=1, padx=10, pady=10)

        # Combobox for source unit
        source_unit_label = ttk.Label(root, text="Source Unit:")
        source_unit_label.grid(row=1, column=0, padx=10, pady=10)
        source_unit_combobox = ttk.Combobox(root, textvariable=self.source_unit_var, values=list(conversion_factors.keys()))
        source_unit_combobox.grid(row=1, column=1, padx=10, pady=10)
        source_unit_combobox.set("Meter")

        # Combobox for target unit
        target_unit_label = ttk.Label(root, text="Target Unit:")
        target_unit_label.grid(row=2, column=0, padx=10, pady=10)
        target_unit_combobox = ttk.Combobox(root, textvariable=self.target_unit_var, values=list(conversion_factors.keys()))
        target_unit_combobox.grid(row=2, column=1, padx=10, pady=10)
        target_unit_combobox.set("Meter")

        # Button to perform conversion
        convert_button = ttk.Button(root, text="Convert", command=self.convert)
        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result label
        result_label = ttk.Label(root, text="Result:")
        result_label.grid(row=4, column=0, padx=10, pady=10)
        result_entry = ttk.Entry(root, textvariable=self.result_var, state='readonly')
        result_entry.grid(row=4, column=1, padx=10, pady=10)

    def convert(self):
        try:
            value = float(self.value_var.get())
            source_unit = self.source_unit_var.get()
            target_unit = self.target_unit_var.get()

            source_factor = conversion_factors[source_unit]
            target_factor = conversion_factors[target_unit]

            result = value * (source_factor / target_factor)
            self.result_var.set(f"{result:.4f}")

        except ValueError:
            self.result_var.set("Error: Please enter a valid numeric value.")
        except KeyError:
            self.result_var.set("Error: Unsupported units selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LengthConverterApp(root)
    root.mainloop()
