import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Controller
import threading
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Başlat ve Bitir Uygulaması")
        self.geometry("300x200")

        self.keyboard = Controller()
        self.running = False

        self.start_button = tk.Button(self, text="Başlat", command=self.start)
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(self, text="Bitir", command=self.stop)
        self.stop_button.pack(pady=20)

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.press_keys)
            self.thread.start()
            messagebox.showinfo("Başlat", "Tuşlara basmaya başlandı!")

    def stop(self):
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        messagebox.showinfo("Bitir", "Tuşlara basma işlemi durduruldu!")

    def press_keys(self):
        while self.running:
            self.keyboard.press('z')
            self.keyboard.release('z')
            time.sleep(0.5)  # 0.1 saniye bekler
            self.keyboard.press('1')
            self.keyboard.release('1')
            time.sleep(0.5)  # 0.1 saniye bekler

if __name__ == "__main__":
    app = Application()
    app.mainloop()
