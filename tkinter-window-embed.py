import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def include_graph(fig, master):
    for widget in master.winfo_children():
        widget.destroy()
    canv = FigureCanvasTkAgg(fig, master=master)
    canv.get_tk_widget().place(relwidth=1, relheight=1)


class PltCanvas:

    def __init__(self, main):
        self.plot_frame = tk.Frame(master=main)
        self.plot_frame.place(relx=0.35, rely=0.03, relheight=0.7, relwidth=0.632)
        self.fig = plt.figure()

    def create_graph2d(self, xs, ys):
        self.fig.clear()
        ax = self.fig.add_subplot()
        ax.plot(xs, ys)
        include_graph(self.fig, self.plot_frame)

    def create_graph3d(self, xs, ys, zs=None):
        if zs is None:
            zs = [0, 0]
        self.fig.clear()
        ax = self.fig.add_subplot(projection="3d")
        ax.plot(xs, ys, zs)
        include_graph(self.fig, self.plot_frame)

# color variables
bg = "#282c34"
canvas_bg = "#"
frame_bg = "#505255"
button_bg = "#A9B6C9"
# create main window
root = tk.Tk()
root.wm_iconbitmap('wave-square-solid.ico')
root.wm_title("Vector Program")
# root.overrideredirect(True)
root.geometry("+250+2500")
root.lift()
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-transparentcolor", "white")

# get screen size and center the generalised window
screen_Height = root.winfo_screenheight()
screen_Width = root.winfo_screenwidth()

Height = screen_Height/1.1
Width = screen_Width/1.1

x_cord = screen_Width / 2 - Width / 2
y_cord = (screen_Height - 80) / 2 - Height / 2

root.geometry("%dx%d+%d+%d" % (Width, Height, x_cord, y_cord))

# set mainframe
Mainframe = tk.Frame(root, bg=bg)
Mainframe.place(relheight=1, relwidth=1)

plot_frame = PltCanvas(Mainframe)

# create button_frame and buttons
button_frame = tk.Frame(master=Mainframe, bg=frame_bg)
button_frame.place(relx=0.0175, relwidth=0.315, rely=0.03, relheight=0.7)

button_2d = tk.Button(master=button_frame, text="2D", font="Helvetica 20",
                      command=lambda: plot_frame.create_graph2d([2, 4], [1, 7]))
button_3d = tk.Button(master=button_frame, text="3D", font="Helvetica 20",
                      command=lambda: plot_frame.create_graph3d([2, 4], [1, 7], [2, 5]))
button_2d.place(relx=0.05, relwidth=0.425, rely=0.025, relheight=0.1)
button_3d.place(relx=0.5125, relwidth=0.425, rely=0.025, relheight=0.1)

# create settings_frame
settings_frame = tk.Frame(master=Mainframe, bg=frame_bg)
settings_frame.place(relx=0.0175, relwidth=0.315, rely=0.75, relheight=0.22)

quit_button = tk.Button(master=settings_frame, text="Quit", bg = button_bg, command=root.quit)
quit_button.place(rely=0.75, relheight=0.22, relx=0.025, relwidth=0.95)

# create action_frame
action_frame = tk.Frame(master=Mainframe, bg=frame_bg)
action_frame.place(rely=0.75, relheight=0.22, relx=0.35, relwidth=0.632)

tk.mainloop()
