import random
from math import sin, cos, pi, log
from tkinter import *

CANVAS_WIDTH = 800  
CANVAS_HEIGHT = 600  
CANVAS_CENTER_X = CANVAS_WIDTH / 2  
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2  
IMAGE_ENLARGE = 11  
HEART_COLOR = "#f76070"  

# ================= CẤU HÌNH CHỮ =================
LOVE_TEXT = "Hà Phương Linh"
SUB_TEXT = "Anh Yêu Em Mãi Mãi ❤"
TEXT_COLOR = "#ffffff"
SUB_TEXT_COLOR = "#ffc0cb"
FONT_MAIN = ("Arial", 25, "bold")
FONT_SUB = ("Arial", 20, "italic")
# ================================================

def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
    x *= shrink_ratio
    y *= shrink_ratio
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y
    return int(x), int(y)

def scatter_inside(x, y, beta=0.15):
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())
    dx = ratio_x * (x - CANVAS_CENTER_X)
    dy = ratio_y * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy

def shrink(x, y, ratio):
    force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)  
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy

def curve(p):
    return 2 * (2 * sin(4 * p)) / (2 * pi)

class Heart:
    def __init__(self, generate_frame=20):
        self._points = set()  
        self._edge_diffusion_points = set()  
        self._center_diffusion_points = set()  
        self.all_points = {}  
        self.build(2000)
        self.random_halo = 1000
        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
        for _ in range(number):
            t = random.uniform(0, 2 * pi)  
            x, y = heart_function(t)
            self._points.add((x, y))
        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))
        point_list = list(self._points)
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calc_position(x, y, ratio):
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520)
        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)
        return x - dx, y - dy

    def calc(self, generate_frame):
        ratio = 10 * curve(generate_frame / 10 * pi)  
        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
        all_points = []
        heart_halo_point = set()  
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)  
            x, y = heart_function(t, shrink_ratio=11.6)  
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))
        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))
        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))
        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))
        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)

class TextAnimation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.text_id = None
        self.sub_text_id = None
        self.char_index = 0
        self.display_text = ""
        self.max_chars = len(LOVE_TEXT)
        self.visible = False
        self.frame_count = 0
        self.glow_frame = 0
        
    def update(self, frame):
        self.frame_count = frame
        
        if frame > 20 and not self.visible:
            self.visible = True
            
        if self.visible:
            if self.char_index < self.max_chars:
                self.display_text += LOVE_TEXT[self.char_index]
                self.char_index += 1
            
            if self.text_id:
                self.canvas.delete(self.text_id)
            if self.sub_text_id:
                self.canvas.delete(self.sub_text_id)
            
            self.glow_frame += 1
            
            self.canvas.create_text(
                CANVAS_CENTER_X + 2, 
                CANVAS_CENTER_Y + 2,
                text=self.display_text,
                font=FONT_MAIN,
                fill="#ff69b4",
                tags="text_glow"
            )
            
            self.text_id = self.canvas.create_text(
                CANVAS_CENTER_X, 
                CANVAS_CENTER_Y,
                text=self.display_text,
                font=FONT_MAIN,
                fill=TEXT_COLOR,
                tags="text"
            )
            
            if self.char_index >= self.max_chars and frame > 60:
                self.sub_text_id = self.canvas.create_text(
                    CANVAS_CENTER_X, 
                    CANVAS_CENTER_Y + 60,
                    text=SUB_TEXT,
                    font=FONT_SUB,
                    fill=SUB_TEXT_COLOR,
                    tags="subtext"
                )
    
    def reset(self):
        self.char_index = 0
        self.display_text = ""
        self.visible = False
        self.frame_count = 0
        self.glow_frame = 0
        if self.text_id:
            self.canvas.delete(self.text_id)
        if self.sub_text_id:
            self.canvas.delete(self.sub_text_id)

def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, text_anim: TextAnimation, render_frame=0):
    render_canvas.delete('all')
    render_heart.render(render_canvas, render_frame)
    text_anim.update(render_frame)
    
    if render_frame > 250:
        text_anim.reset()
        render_frame = 0
    
    main.after(100, draw, main, render_canvas, render_heart, text_anim, render_frame + 1)

if __name__ == '__main__':
    root = Tk()  
    root.title("❤️ Gửi Hà Phương Linh ❤️")
    root.configure(bg='black')
    
    canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack(pady=10)
    
    heart = Heart()  
    text_animation = TextAnimation(canvas)
    
    draw(root, canvas, heart, text_animation)  
    
    label = Label(root, text="🌹 Gửi người đặc biệt - Click để thoát 🌹", 
                  bg='black', fg='gray', font=("Arial", 12))
    label.pack(pady=5)
    
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - CANVAS_WIDTH) // 2
    y = (screen_height - CANVAS_HEIGHT) // 2
    root.geometry(f'{CANVAS_WIDTH}x{CANVAS_HEIGHT}+{x}+{y}')
    
    root.mainloop()