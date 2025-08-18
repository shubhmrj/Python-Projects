import tkinter as tk
from tkinter import colorchooser
from abc import ABC, abstractmethod

# Shape interface
class Shape(ABC):
    @abstractmethod
    def draw(self, canvas, **kwargs):
        pass

class Circle(Shape):
    def draw(self, canvas, center, radius, fill, outline, width):
        x0 = center[0] - radius
        y0 = center[1] - radius
        x1 = center[0] + radius
        y1 = center[1] + radius
        canvas.create_oval(x0, y0, x1, y1, fill=fill, outline=outline, width=width)

class Square(Shape):
    def draw(self, canvas, center, side, fill, outline, width):
        half = side // 2
        x0 = center[0] - half
        y0 = center[1] - half
        x1 = center[0] + half
        y1 = center[1] + half
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=outline, width=width)

class Rectangle(Shape):
    def draw(self, canvas, center, width_r, height_r, fill, outline, width):
        x0 = center[0] - width_r // 2
        y0 = center[1] - height_r // 2
        x1 = center[0] + width_r // 2
        y1 = center[1] + height_r // 2
        canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=outline, width=width)

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        elif shape_type == 'rectangle':
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

class AdvancedShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Shape Factory GUI")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.bg_color = "#f2f2f2"
        self.selected_color = "#3498db"
        self.outline_color = "#222"
        self.outline_width = 3

        # Controls Frame
        self.controls = tk.Frame(root, bg="#e8eaf6", bd=2, relief=tk.GROOVE)
        self.controls.place(x=10, y=10, width=220, height=480)

        tk.Label(self.controls, text="Shape Type", bg="#e8eaf6", font=("Segoe UI", 11, "bold")).pack(pady=7)
        self.shape_var = tk.StringVar(value="circle")
        shapes = ["circle", "square", "rectangle"]
        for s in shapes:
            tk.Radiobutton(self.controls, text=s.title(), variable=self.shape_var, value=s, bg="#e8eaf6", font=("Segoe UI", 10)).pack(anchor=tk.W)

        # Size controls (dynamic)
        self.size_frame = tk.Frame(self.controls, bg="#e8eaf6")
        self.size_frame.pack(pady=8)
        self.size_labels = {}
        self.size_entries = {}
        self._create_size_controls()
        self.shape_var.trace_add('write', lambda *args: self._update_size_controls())

        # Color picker
        tk.Label(self.controls, text="Fill Color", bg="#e8eaf6", font=("Segoe UI", 11, "bold")).pack(pady=(12, 3))
        self.color_btn = tk.Button(self.controls, text="Choose Color", command=self.choose_color, bg=self.selected_color, fg="white", font=("Segoe UI", 10, "bold"))
        self.color_btn.pack(pady=2)

        # Outline width
        tk.Label(self.controls, text="Outline Width", bg="#e8eaf6", font=("Segoe UI", 11, "bold")).pack(pady=(10, 3))
        self.outline_entry = tk.Entry(self.controls, width=5, font=("Segoe UI", 10))
        self.outline_entry.insert(0, str(self.outline_width))
        self.outline_entry.pack(pady=2)

        # Draw & Clear
        self.draw_btn = tk.Button(self.controls, text="Draw Shape", command=self.draw_shape, bg="#43a047", fg="white", font=("Segoe UI", 11, "bold"))
        self.draw_btn.pack(pady=(16, 5), fill=tk.X)
        self.clear_btn = tk.Button(self.controls, text="Clear Canvas", command=self.clear_canvas, bg="#e53935", fg="white", font=("Segoe UI", 11, "bold"))
        self.clear_btn.pack(pady=2, fill=tk.X)

        # Canvas
        self.canvas = tk.Canvas(root, width=340, height=460, bg=self.bg_color, highlightthickness=2, highlightbackground="#888")
        self.canvas.place(x=250, y=15)

        # Status
        self.status_label = tk.Label(root, text="", fg="red", font=("Segoe UI", 10))
        self.status_label.place(x=250, y=480)

    def _create_size_controls(self):
        # Remove old
        for widget in self.size_frame.winfo_children():
            widget.destroy()
        self.size_labels.clear()
        self.size_entries.clear()
        # Create for default (circle)
        self._update_size_controls()

    def _update_size_controls(self):
        for widget in self.size_frame.winfo_children():
            widget.destroy()
        shape = self.shape_var.get()
        if shape == "circle":
            self.size_labels['radius'] = tk.Label(self.size_frame, text="Radius:", bg="#e8eaf6", font=("Segoe UI", 10))
            self.size_labels['radius'].grid(row=0, column=0, sticky=tk.W)
            self.size_entries['radius'] = tk.Entry(self.size_frame, width=8, font=("Segoe UI", 10))
            self.size_entries['radius'].insert(0, "60")
            self.size_entries['radius'].grid(row=0, column=1)
        elif shape == "square":
            self.size_labels['side'] = tk.Label(self.size_frame, text="Side:", bg="#e8eaf6", font=("Segoe UI", 10))
            self.size_labels['side'].grid(row=0, column=0, sticky=tk.W)
            self.size_entries['side'] = tk.Entry(self.size_frame, width=8, font=("Segoe UI", 10))
            self.size_entries['side'].insert(0, "100")
            self.size_entries['side'].grid(row=0, column=1)
        elif shape == "rectangle":
            self.size_labels['width'] = tk.Label(self.size_frame, text="Width:", bg="#e8eaf6", font=("Segoe UI", 10))
            self.size_labels['width'].grid(row=0, column=0, sticky=tk.W)
            self.size_entries['width'] = tk.Entry(self.size_frame, width=8, font=("Segoe UI", 10))
            self.size_entries['width'].insert(0, "150")
            self.size_entries['width'].grid(row=0, column=1)
            self.size_labels['height'] = tk.Label(self.size_frame, text="Height:", bg="#e8eaf6", font=("Segoe UI", 10))
            self.size_labels['height'].grid(row=1, column=0, sticky=tk.W)
            self.size_entries['height'] = tk.Entry(self.size_frame, width=8, font=("Segoe UI", 10))
            self.size_entries['height'].insert(0, "80")
            self.size_entries['height'].grid(row=1, column=1)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Fill Color", initialcolor=self.selected_color)
        if color[1]:
            self.selected_color = color[1]
            self.color_btn.config(bg=self.selected_color)

    def draw_shape(self):
        shape_type = self.shape_var.get()
        try:
            outline_width = int(self.outline_entry.get())
        except Exception:
            self.status_label.config(text="Outline width must be a number.", fg="red")
            return
        # Get size
        try:
            if shape_type == "circle":
                radius = int(self.size_entries['radius'].get())
                shape = ShapeFactory.create_shape(shape_type)
                shape.draw(self.canvas, center=(170, 230), radius=radius, fill=self.selected_color, outline=self.outline_color, width=outline_width)
            elif shape_type == "square":
                side = int(self.size_entries['side'].get())
                shape = ShapeFactory.create_shape(shape_type)
                shape.draw(self.canvas, center=(170, 230), side=side, fill=self.selected_color, outline=self.outline_color, width=outline_width)
            elif shape_type == "rectangle":
                width_r = int(self.size_entries['width'].get())
                height_r = int(self.size_entries['height'].get())
                shape = ShapeFactory.create_shape(shape_type)
                shape.draw(self.canvas, center=(170, 230), width_r=width_r, height_r=height_r, fill=self.selected_color, outline=self.outline_color, width=outline_width)
            self.status_label.config(text=f"Drew a {shape_type}.", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", fg="red")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.status_label.config(text="Canvas cleared.", fg="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedShapeApp(root)
    root.mainloop()
