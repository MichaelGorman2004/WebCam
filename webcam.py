import cv2
import tkinter as tk
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        self.video_source = 0  # Use default camera
        self.vid = cv2.VideoCapture(self.video_source)
        
        self.canvas = tk.Canvas(window, width=320, height=240)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.btn_quit = tk.Button(window, text="Quit", width=10, command=self.close)
        self.btn_quit.pack(anchor=tk.SE, padx=5, pady=5)
        
        self.delay = 15
        self.update()
        
        self.window.attributes('-topmost', True)  # Keep window on top
        self.window.overrideredirect(True)  # Remove window decorations
        self.window.geometry('320x240+1600+840')  # Initial position and size
        
        # Bind events for dragging and resizing
        self.canvas.bind("<ButtonPress-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.on_move)
        self.canvas.bind("<ButtonRelease-1>", self.stop_move)
        
        self.window.bind("<Configure>", self.on_resize)
        
        # Add resize grip
        self.grip = tk.Label(window, bitmap="gray25")
        self.grip.place(relx=1.0, rely=1.0, anchor="se")
        self.grip.bind("<B1-Motion>", self.on_resize_drag)
        
    def update(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.resize(frame, (self.window.winfo_width(), self.window.winfo_height()))
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_resize(self, event):
        self.canvas.config(width=event.width, height=event.height)

    def on_resize_drag(self, event):
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        width = event.x_root - x
        height = event.y_root - y
        self.window.geometry(f"{width}x{height}+{x}+{y}")
    
    def close(self):
        self.vid.release()
        self.window.quit()

# Create a window and pass it to the Application object
root = tk.Tk()
app = WebcamApp(root, "Webcam")
root.mainloop()
