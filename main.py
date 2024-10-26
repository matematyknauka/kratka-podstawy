import tkinter as tk

# Funkcja do tworzenia kratki
def stworz_kratke():
    for i in range(15):  # 15 wierszy
        for j in range(10):  # 10 kolumn
            # Tworzymy ramkę (komórkę) w kratce
            komorka = tk.Frame(root, width=30, height=30, borderwidth=1, relief="solid")
            komorka.grid(row=i, column=j)  # Ustawiamy pozycję komórki w siatce

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Kratka w zeszycie")  # Tytuł okna

# Ustawiamy rozmiar okna
root.geometry("320x480")  # Szerokość x Wysokość

# Wywołujemy funkcję do tworzenia kratki
stworz_kratke()

# Uruchamiamy pętlę główną
root.mainloop()