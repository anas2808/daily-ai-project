import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import os

class InstagramFilterApp:
    def __init__(self, master):
        self.master = master
        master.title("Instagram-style Image Filter (Fresher Project)")
        master.geometry("1200x800") # A bit larger window for images

        self.original_image_path = None
        self.original_pil_image = None
        self.display_original_image = None # For Tkinter PhotoImage reference
        self.filtered_pil_image = None
        self.display_filtered_image = None # For Tkinter PhotoImage reference

        self.MAX_DISPLAY_SIZE = (500, 500) # Max size for images displayed in GUI

        # --- GUI Layout ---
        self.main_frame = ttk.Frame(master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Image Display Frame
        self.image_frame = ttk.Frame(self.main_frame)
        self.image_frame.pack(side=tk.TOP, pady=10)

        # Original Image Label
        ttk.Label(self.image_frame, text="Original Image:").grid(row=0, column=0, padx=5, pady=5)
        self.original_image_label = ttk.Label(self.image_frame, borderwidth=2, relief="groove")
        self.original_image_label.grid(row=1, column=0, padx=5, pady=5)

        # Filtered Image Label
        ttk.Label(self.image_frame, text="Filtered Image:").grid(row=0, column=1, padx=5, pady=5)
        self.filtered_image_label = ttk.Label(self.image_frame, borderwidth=2, relief="groove")
        self.filtered_image_label.grid(row=1, column=1, padx=5, pady=5)

        # Control Frame
        self.control_frame = ttk.Frame(self.main_frame, padding="10")
        self.control_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Open, Apply, Save Buttons
        self.open_button = ttk.Button(self.control_frame, text="Open Image", command=self.open_image)
        self.open_button.grid(row=0, column=0, padx=5, pady=5)

        self.apply_button = ttk.Button(self.control_frame, text="Apply Filter", command=self.apply_filter, state=tk.DISABLED)
        self.apply_button.grid(row=0, column=1, padx=5, pady=5)

        self.save_button = ttk.Button(self.control_frame, text="Save Filtered Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.grid(row=0, column=2, padx=5, pady=5)

        # Filter Selection
        ttk.Label(self.control_frame, text="Select Filter:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.filter_var = tk.StringVar(master)
        self.filter_var.set("None") # default value
        self.filter_options = [
            "None",
            "Grayscale",
            "Sepia",
            "Blur",
            "Sharpen",
            "Emboss",
            "Lighten (Brightness +20%)",
            "Darken (Brightness -20%)",
            "More Contrast (+20%)",
            "Less Contrast (-20%)"
        ]
        self.filter_menu = ttk.OptionMenu(self.control_frame, self.filter_var, *self.filter_options)
        self.filter_menu.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.EW)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.original_image_path = file_path
                # Ensure RGB mode for consistency across filters
                self.original_pil_image = Image.open(file_path).convert("RGB") 
                self.filtered_pil_image = None # Clear previous filtered image

                self.display_image(self.original_pil_image, self.original_image_label)
                self.filtered_image_label.config(image='') # Clear filtered image display
                self.display_filtered_image = None

                self.apply_button.config(state=tk.NORMAL)
                self.save_button.config(state=tk.DISABLED) # Cannot save until filtered
                self.filter_var.set("None") # Reset filter selection
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {e}")
                self.reset_app()

    def display_image(self, pil_image, label_widget):
        """Displays a PIL image in a Tkinter Label, resizing it for fit."""
        if pil_image is None:
            label_widget.config(image='')
            return

        display_image = pil_image.copy()
        display_image.thumbnail(self.MAX_DISPLAY_SIZE, Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage and store a reference to prevent garbage collection
        tk_image = ImageTk.PhotoImage(display_image)
        label_widget.config(image=tk_image)
        label_widget.image = tk_image # Store reference

        # Update specific references
        if label_widget == self.original_image_label:
            self.display_original_image = tk_image
        else:
            self.display_filtered_image = tk_image

    def apply_filter(self):
        if self.original_pil_image is None:
            messagebox.showwarning("Warning", "Please open an image first!")
            return

        selected_filter = self.filter_var.get()
        if selected_filter == "None":
            self.filtered_pil_image = self.original_pil_image.copy()
            self.display_image(self.filtered_pil_image, self.filtered_image_label)
            self.save_button.config(state=tk.NORMAL)
            return

        try:
            # Create a copy to apply filters, keeping original intact
            current_image = self.original_pil_image.copy()

            if selected_filter == "Grayscale":
                self.filtered_pil_image = current_image.convert("L").convert("RGB") # Convert to L (grayscale) then back to RGB
            elif selected_filter == "Sepia":
                self.filtered_pil_image = self._apply_sepia_filter(current_image)
            elif selected_filter == "Blur":
                self.filtered_pil_image = current_image.filter(ImageFilter.BLUR)
            elif selected_filter == "Sharpen":
                self.filtered_pil_image = current_image.filter(ImageFilter.SHARPEN)
            elif selected_filter == "Emboss":
                self.filtered_pil_image = current_image.filter(ImageFilter.EMBOSS)
            elif selected_filter == "Lighten (Brightness +20%)":
                enhancer = ImageEnhance.Brightness(current_image)
                self.filtered_pil_image = enhancer.enhance(1.2) # 20% brighter
            elif selected_filter == "Darken (Brightness -20%)":
                enhancer = ImageEnhance.Brightness(current_image)
                self.filtered_pil_image = enhancer.enhance(0.8) # 20% darker
            elif selected_filter == "More Contrast (+20%)":
                enhancer = ImageEnhance.Contrast(current_image)
                self.filtered_pil_image = enhancer.enhance(1.2) # 20% more contrast
            elif selected_filter == "Less Contrast (-20%)":
                enhancer = ImageEnhance.Contrast(current_image)
                self.filtered_pil_image = enhancer.enhance(0.8) # 20% less contrast
            else:
                self.filtered_pil_image = current_image.copy() # Fallback, should not happen

            self.display_image(self.filtered_pil_image, self.filtered_image_label)
            self.save_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply filter: {e}")
            self.filtered_pil_image = None
            self.display_image(None, self.filtered_image_label)
            self.save_button.config(state=tk.DISABLED)

    def _apply_sepia_filter(self, image):
        """Applies a sepia tone filter by direct pixel manipulation.
        This approach demonstrates basic pixel-level image processing.
        """
        # Ensure image is in RGB mode for consistent pixel manipulation
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Make a modifiable copy to prevent altering the original image
        sepia_image = image.copy()
        
        width, height = sepia_image.size
        # Load pixel data for faster access during iteration
        pixels = sepia_image.load() 

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                # Sepia transformation formulas
                # These are common matrix values for sepia conversion
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                # Cap values at 255 to ensure they stay within valid RGB range
                pixels[x, y] = (min(255, tr), min(255, tg), min(255, tb))
        return sepia_image

    def save_image(self):
        if self.filtered_pil_image is None:
            messagebox.showwarning("Warning", "No filtered image to save!")
            return

        # Suggest a filename based on original and applied filter
        if self.original_image_path:
            base_name = os.path.splitext(os.path.basename(self.original_image_path))[0]
            filter_name_short = self.filter_var.get().split('(')[0].strip().replace(" ", "_")
            suggested_name = f"{base_name}_{filter_name_short}.png"
        else:
            suggested_name = "filtered_image.png"

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", # Default to PNG if no extension given
            initialfile=suggested_name,
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.filtered_pil_image.save(file_path)
                messagebox.showinfo("Success", f"Image saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {e}")

    def reset_app(self):
        """Resets the application state, clearing images and disabling controls."""
        self.original_image_path = None
        self.original_pil_image = None
        self.filtered_pil_image = None
        
        self.display_image(None, self.original_image_label)
        self.display_image(None, self.filtered_image_label)
        
        self.apply_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)
        self.filter_var.set("None")


if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramFilterApp(root)
    root.mainloop()