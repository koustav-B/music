import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.configure(bg="#FFFFFF")  # Set background color to white
        self.music_folder = tk.StringVar()
        self.music_files = []
        self.current_index = 0
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Music Folder:", bg="#FFFFFF").pack()
        tk.Entry(self.root, textvariable=self.music_folder, state='readonly').pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="Browse", command=self.browse_music_folder, bg="#6495ED", fg="#FFFFFF").pack(side=tk.RIGHT, padx=5)
        tk.Button(self.root, text="Play", command=self.play_music, bg="#6495ED", fg="#FFFFFF").pack(pady=10)
        tk.Button(self.root, text="Pause", command=self.pause_music, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Resume", command=self.resume_music, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Stop", command=self.stop_music, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Increase Volume", command=self.increase_volume, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Decrease Volume", command=self.decrease_volume, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Skip Forward", command=self.skip_forward, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Skip Backward", command=self.skip_backward, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Next Music", command=self.next_music, bg="#6495ED", fg="#FFFFFF").pack(pady=5)
        tk.Button(self.root, text="Previous Music", command=self.previous_music, bg="#6495ED", fg="#FFFFFF").pack(pady=5)

    def browse_music_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.music_folder.set(folder)
            self.music_files = [file for file in os.listdir(folder) if file.endswith((".mp3", ".wav"))]

    def play_music(self):
        music_folder = self.music_folder.get()

        if not os.path.exists(music_folder) or not os.path.isdir(music_folder):
            messagebox.showerror("Error", "Invalid directory. Please provide a valid directory path.")
            return

        if not self.music_files:
            messagebox.showinfo("Information", "No music files found in the folder. Please select a different folder.")
            return

        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)

        pygame.mixer.music.load(os.path.join(music_folder, self.music_files[self.current_index]))
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def increase_volume(self):
        current_volume = pygame.mixer.music.get_volume()
        if current_volume < 1:
            pygame.mixer.music.set_volume(current_volume + 0.1)

    def decrease_volume(self):
        current_volume = pygame.mixer.music.get_volume()
        if current_volume > 0:
            pygame.mixer.music.set_volume(current_volume - 0.1)

    def skip_forward(self):
        current_pos = pygame.mixer.music.get_pos() / 1000  # Current position in seconds
        pygame.mixer.music.set_pos(current_pos + 10)  # Skip forward by 10 seconds

    def skip_backward(self):
        current_pos = pygame.mixer.music.get_pos() / 1000  # Current position in seconds
        pygame.mixer.music.set_pos(current_pos - 10)  # Skip backward by 10 seconds

    def next_music(self):
        if self.current_index < len(self.music_files) - 1:
            self.current_index += 1
            self.play_music()

    def previous_music(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_music()

if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
