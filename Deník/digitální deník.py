import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Digitální Deník', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Strana {self.page_no()}', 0, 0, 'C')

def add_entry():
    content = entry_text.get("1.0", tk.END).strip()
    if content:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} - {content}"
        entries.append(entry)
        entry_listbox.insert(tk.END, entry)
        entry_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Entry cannot be empty")

def save_pdf():
    if entries:
        pdf_file_name = "Deník/denik.pdf"
        if not os.path.exists("Deník"):
            os.makedirs("Deník")
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        for entry in entries:
            pdf.multi_cell(0, 10, entry)
        pdf.output(pdf_file_name)
        messagebox.showinfo("Info", f"Entries saved to {pdf_file_name}")
    else:
        messagebox.showwarning("Warning", "No entries to save")

# Setup the main application window
root = tk.Tk()
root.title("Digitální Deník")
root.geometry("500x400")

# Setup text widget for journal entry input
entry_text = tk.Text(root, height=10, width=50)
entry_text.pack(pady=10)

# Setup frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add Entry button
add_button = tk.Button(button_frame, text="Přidat záznam", command=add_entry)
add_button.pack(side=tk.LEFT, padx=10)

# Save to PDF button
save_button = tk.Button(button_frame, text="Uložit do PDF", command=save_pdf)
save_button.pack(side=tk.LEFT, padx=10)

# Setup listbox to display entries
entry_listbox = tk.Listbox(root, width=80, height=10)
entry_listbox.pack(pady=10)

# List to store entries
entries = []

# Start the main event loop
root.mainloop()