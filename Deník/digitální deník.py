from datetime import datetime
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Digitální Deník', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Strana {self.page_no()}', 0, 0, 'C')

def display_menu():
    print("Digitální Deník")
    print("1. Přidat záznam")
    print("2. Konec")

def add_entry(pdf):
    print("Zadejte svůj záznam:")
    content = input(">> ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {content}"
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, entry)
    print("Záznam byl přidán.\n")

def view_entries(pdf_file_name):
    if os.path.exists(pdf_file_name):
        print(f"Záznamy byly uloženy do souboru {pdf_file_name}.")
    else:
        print("Žádné záznamy nejsou k dispozici.")

def main():
    pdf_file_name = "Deník/denik.pdf"
    pdf = PDF()
    pdf.add_page()
    while True:
        display_menu()
        choice = input("Vyberte možnost: ")
        if choice == '1':
            add_entry(pdf)
        elif choice == '2':
            pdf.output(pdf_file_name)
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()
