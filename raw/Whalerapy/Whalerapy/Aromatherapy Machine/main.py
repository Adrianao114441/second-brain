import customtkinter as ctk
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import serial
import time

# ==========================================
# 1. HARDWARE & AI INITIALIZATION
# ==========================================
print("Loading AI Models... (This takes a few seconds)")

model_path = 'fer2013_mini_XCEPTION.102-0.66.hdf5' 
classifier = load_model(model_path, compile=False)

base_options = python.BaseOptions(model_asset_path='detector.tflite')
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)

try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2) 
    print("Arduino Connected Successfully!")
except Exception:
    arduino = None
    print("WARNING: Arduino not found. Running in PC Test Mode.")

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

# ==========================================
# 2. BILINGUAL DICTIONARY & SURVEY DATA
# ==========================================
UI_TEXT = {
    "en": {
        "title": "WHALERAPY",
        "welcome": "Welcome to the Deep Sea. Let's align your senses.",
        "btn_start": "Start Camera Test",
        "cam_instruction": "Activating Whale Vision...\nPress SPACEBAR to snap your photo.",
        "survey_title": "DEEP SEA SURVEY • {} / 10",
        "results_title": "ALIGNMENT COMPLETE",
        "btn_restart": "Restart Journey",
        "wood_name": "🪵 Wood",
        "flower_name": "🪸 Flower",
        "fruit_name": "🥭 Fruit",
        "chill_name": "🧊 Chill (Prescribed)",
        "energy_name": "⚡ Energy (Prescribed)",
        "drops_text": "drops",
        "drop_text": "drop",
        "baseline_text": "Baseline Sensed: {}  |  Prescribed: {}"
    },
    "zh": {
        "title": "深海鯨癒 (WHALERAPY)",
        "welcome": "歡迎來到深海。讓我們調和您的感官。",
        "btn_start": "開始鏡頭檢測",
        "cam_instruction": "正在啟動鯨魚視覺...\n請在視窗中按下空白鍵拍攝照片。",
        "survey_title": "深海問卷 • {} / 10",
        "results_title": "調和完成",
        "btn_restart": "重新開始旅程",
        "wood_name": "🪵 木質",
        "flower_name": "🪸 花香",
        "fruit_name": "🥭 果香",
        "chill_name": "🧊 鎮靜 (處方)",
        "energy_name": "⚡ 活力 (處方)",
        "drops_text": "滴",
        "drop_text": "滴",
        "baseline_text": "檢測基準: {}  |  處方需求: {}"
    }
}

questions = [
    {
        "en": {"text": "1. Imagine you are living in your dream world. Where would you be?", "wood": "A cozy cabin hidden deep in a quiet forest.", "flower": "A sunny cottage in a bright, blooming garden.", "fruit": "A warm, tropical beach surrounded by fruit trees."},
        "zh": {"text": "1. 想像您生活在夢想世界中。您會在哪裡？", "wood": "隱藏在寧靜森林深處的舒適小木屋。", "flower": "陽光明媚、百花盛開的花園小屋。", "fruit": "被果樹環繞的溫暖熱帶海灘。"}
    },
    {
        "en": {"text": "2. How do you want this session to make you feel?", "wood": "Grounded, calm, and deeply relaxed.", "flower": "Uplifted, refreshed, and energized.", "fruit": "Bright, playful, and full of joy."},
        "zh": {"text": "2. 您希望這次香氛體驗帶給您什麼感受？", "wood": "沉穩、平靜且深度放鬆。", "flower": "振奮、清新且充滿活力。", "fruit": "明亮、俏皮且充滿喜悅。"}
    },
    {
        "en": {"text": "3. Which words best describe your favorite scents?", "wood": "Earthy, warm, and musky.", "flower": "Sweet, light, and floral.", "fruit": "Juicy, vibrant, and citrusy."},
        "zh": {"text": "3. 哪個詞最能形容您喜歡的氣味？", "wood": "泥土氣息、溫暖和麝香。", "flower": "甜美、清淡和花香。", "fruit": "多汁、鮮明和柑橘香。"}
    },
    {
        "en": {"text": "4. Which type of tea would you prefer to drink right now?", "wood": "A rich, earthy black tea or spiced chai.", "flower": "A delicate chamomile or floral tea.", "fruit": "A refreshing iced berry or citrus tea."},
        "zh": {"text": "4. 您現在最想喝哪種茶？", "wood": "濃郁的紅茶或香料茶。", "flower": "淡雅的洋甘菊或花茶。", "fruit": "清爽的冰鎮莓果茶或柑橘茶。"}
    },
    {
        "en": {"text": "5. Which seasons' atmosphere is the most comforting?", "wood": "Crisp Autumn with falling leaves.", "flower": "Bright Spring with fresh blooms.", "fruit": "Sunny Summer with a warm breeze."},
        "zh": {"text": "5. 哪個季節的氛圍讓您覺得最舒適？", "wood": "落葉紛飛的清爽秋季。", "flower": "百花齊放的明媚春季。", "fruit": "微風輕拂的陽光夏季。"}
    },
    {
        "en": {"text": "6. What is your favorite time of day?", "wood": "Late at night, watching the embers of a fire.", "flower": "Early morning, just as the sun touches the dew.", "fruit": "High noon, soaking up the bright sunshine."},
        "zh": {"text": "6. 您最喜歡一天中的哪個時間？", "wood": "深夜，看著火爐的餘燼。", "flower": "清晨，陽光剛接觸到露水時。", "fruit": "正午，沐浴在明亮的陽光下。"}
    },
    {
        "en": {"text": "7. If you could surround yourself with one color palette, what would it be?", "wood": "Deep greens, browns, and warm golds.", "flower": "Soft pinks, lavenders, and pastel blues.", "fruit": "Vibrant oranges, yellows, and coral pinks."},
        "zh": {"text": "7. 如果能被一種色系包圍，您會選擇？", "wood": "深綠色、棕色和溫暖的金黃色。", "flower": "柔和的粉紅色、薰衣草色和粉藍色。", "fruit": "充滿活力的亮橘色、黃色和珊瑚紅。"}
    },
    {
        "en": {"text": "8. What kind of soundscape relaxes you the most?", "wood": "Low acoustic guitar or a distant rolling thunderstorm.", "flower": "Gentle piano or a soft breeze blowing through chimes.", "fruit": "Upbeat acoustic rhythms or crashing ocean waves."},
        "zh": {"text": "8. 哪種聲音最能讓您放鬆？", "wood": "低沉的木吉他聲或遠處的雷聲。", "flower": "輕柔的鋼琴聲或微風吹過風鈴的聲音。", "fruit": "輕快的節奏或海浪拍打的聲音。"}
    },
    {
        "en": {"text": "9. How do you usually prefer to handle a stressful day?", "wood": "Retreating to a quiet, cozy place to reflect and reset.", "flower": "Going for a peaceful walk in nature to clear my head.", "fruit": "Doing something fun, active, or creative to burn off energy."},
        "zh": {"text": "9. 您通常喜歡如何應對壓力大的一天？", "wood": "退居到一個安靜、舒適的地方反思和重置。", "flower": "在大自然中平靜地散步以清理思緒。", "fruit": "做些有趣、活躍或有創意的事情來消耗能量。"}
    },
    {
        "en": {"text": "10. Which of these small moments brings you the most peace?", "wood": "Reading a book wrapped in a heavy blanket.", "flower": "Arranging a fresh bouquet of flowers in a vase.", "fruit": "Enjoying a cold, sweet drink on a hot afternoon."},
        "zh": {"text": "10. 以下哪個微小時刻最能為您帶來平靜？", "wood": "裹著厚重的毛毯看書。", "flower": "在花瓶裡整理一束鮮花。", "fruit": "在炎熱的下午享用一杯清涼的甜飲。"}
    }
]

# ==========================================
# 3. MAIN APPLICATION
# ==========================================
class WhalerapyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WHALERAPY")
        self.root.geometry("800x480")
        
        # Use fg_color so CustomTkinter uniformly applies the theme
        self.root.configure(fg_color="#0B192C") 

        self.current_q = 0
        self.wood_score = 0
        self.flower_score = 0
        self.fruit_score = 0
        self.camera_sensed = "Unknown"
        self.camera_needs = "Unknown"
        self.lang = "en" 

        # --- UI ELEMENTS ---
        self.title_label = ctk.CTkLabel(root, text="WHALERAPY / 深海鯨癒", font=("Helvetica", 36, "bold"), text_color="#00D2C4")
        self.title_label.pack(pady=35)

        self.info_label = ctk.CTkLabel(root, text="Please select your language\n請選擇您的語言", font=("Helvetica", 20), text_color="#E0F7FA", wraplength=650)
        self.info_label.pack(pady=25)

        # Buttons
        self.btn_a = ctk.CTkButton(root, text="English", font=("Helvetica", 18, "bold"), fg_color="#1F4068", hover_color="#162447", width=550, height=70, corner_radius=20, command=lambda: self.set_language("en"))
        self.btn_a.pack(pady=10)

        self.btn_b = ctk.CTkButton(root, text="繁體中文", font=("Helvetica", 18, "bold"), fg_color="#00B4D8", hover_color="#0077B6", width=550, height=70, corner_radius=20, command=lambda: self.set_language("zh"))
        self.btn_b.pack(pady=10)
        
        self.btn_c = ctk.CTkButton(root, text="", font=("Helvetica", 18, "bold"), fg_color="#F2A65A", hover_color="#D1813A", width=550, height=70, corner_radius=20)
        self.btn_c.pack_forget() 

        self.exit_btn = ctk.CTkButton(root, text="✕", font=("Helvetica", 12), fg_color="#3A1010", width=30, height=30, corner_radius=8, command=root.destroy)
        self.exit_btn.place(relx=0.95, rely=0.03)

    def set_language(self, chosen_lang):
        self.lang = chosen_lang
        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.btn_b.pack_forget()
        self.title_label.configure(text=UI_TEXT[self.lang]["title"])
        self.info_label.configure(text=UI_TEXT[self.lang]["welcome"])
        self.btn_a.configure(text=UI_TEXT[self.lang]["btn_start"], command=self.run_camera_scan)

    def run_camera_scan(self):
        self.btn_a.pack_forget()
        self.info_label.configure(text=UI_TEXT[self.lang]["cam_instruction"])
        self.root.update() 

        cap = cv2.VideoCapture(0)
        final_frame = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break

            display_frame = frame.copy()
            cv2.putText(display_frame, "Press SPACEBAR to snap photo", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Whale Vision - Photo Booth', display_frame)

            key = cv2.waitKey(1) & 0xFF
            if key == 32: 
                final_frame = frame 
                break
            elif key == ord('q'): 
                break

        if final_frame is not None:
            rgb_frame = cv2.cvtColor(final_frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            detection_result = detector.detect(mp_image)

            if detection_result.detections:
                detection = detection_result.detections[0]
                bbox = detection.bounding_box
                x, y, w, h = max(0, bbox.origin_x), max(0, bbox.origin_y), bbox.width, bbox.height
                
                face_roi = final_frame[y:y+h, x:x+w]
                if face_roi.size > 0:
                    gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                    gray_face = cv2.resize(gray_face, (64, 64)).astype('float32') / 255.0
                    gray_face = np.expand_dims(img_to_array(gray_face), axis=0)

                    prediction = classifier.predict(gray_face, verbose=0)[0]
                    energetic_score = prediction[3] + prediction[5]
                    chill_score = prediction[0] + prediction[1] + prediction[2] + prediction[4] + prediction[6]

                    if energetic_score > chill_score:
                        self.camera_sensed = "Energetic"
                        self.camera_needs = "Chill"
                        box_color = (0, 255, 255) 
                    else:
                        self.camera_sensed = "Chill"
                        self.camera_needs = "Energetic"
                        box_color = (255, 150, 0) 

                    cv2.rectangle(final_frame, (x, y), (x+w, y+h), box_color, 2)
                    cv2.putText(final_frame, f"Sensed: {self.camera_sensed}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, box_color, 2)
                    
                    cv2.imshow('Whale Vision - Photo Booth', final_frame)
                    cv2.waitKey(2500)
            else:
                self.camera_sensed = "Unknown"
                self.camera_needs = "Unknown"

        cap.release()
        cv2.destroyAllWindows()
        self.start_survey()

    def start_survey(self):
        self.btn_a.pack(pady=10)
        self.btn_b.pack(pady=10)
        self.btn_c.pack(pady=10)
        self.btn_a.configure(command=lambda: self.record_answer("wood"))
        self.btn_b.configure(command=lambda: self.record_answer("flower"))
        self.btn_c.configure(command=lambda: self.record_answer("fruit"))
        
        self.current_q = 0
        self.wood_score = self.flower_score = self.fruit_score = 0
        self.load_question()

    def load_question(self):
        if self.current_q < len(questions):
            q_data = questions[self.current_q][self.lang]
            formatted_title = UI_TEXT[self.lang]["survey_title"].format(self.current_q + 1)
            self.title_label.configure(text=formatted_title)
            
            self.info_label.configure(text=q_data["text"])
            self.btn_a.configure(text=q_data["wood"])
            self.btn_b.configure(text=q_data["flower"])
            self.btn_c.configure(text=q_data["fruit"])
        else:
            self.show_results()

    def record_answer(self, choice):
        if choice == "wood": self.wood_score += 1
        elif choice == "flower": self.flower_score += 1
        elif choice == "fruit": self.fruit_score += 1
        self.current_q += 1
        self.load_question()

    def show_results(self):
        self.btn_a.pack_forget()
        self.btn_b.pack_forget()
        self.btn_c.pack_forget()

        # --- 1. CAMERA OVERRIDE & DROP CALCULATION ---
        chill_drops = 1.0 if self.camera_needs == "Chill" else 0.0
        energetic_drops = 1.0 if self.camera_needs == "Energetic" else 0.0

        wood_drops = flower_drops = fruit_drops = 0.0
        total_score = self.wood_score + self.flower_score + self.fruit_score
        
        if total_score > 0:
            exact_wood = (self.wood_score / total_score) * 4.0
            exact_flower = (self.flower_score / total_score) * 4.0
            exact_fruit = (self.fruit_score / total_score) * 4.0

            drops = {
                "wood": int(exact_wood * 2) / 2.0,
                "flower": int(exact_flower * 2) / 2.0,
                "fruit": int(exact_fruit * 2) / 2.0
            }

            remainders = {
                "wood": exact_wood - drops["wood"],
                "flower": exact_flower - drops["flower"],
                "fruit": exact_fruit - drops["fruit"]
            }

            allocated = sum(drops.values())
            missing_chunks = int(round((4.0 - allocated) / 0.5))
            sorted_by_remainder = sorted(remainders.keys(), key=lambda k: remainders[k], reverse=True)
            
            for i in range(missing_chunks):
                drops[sorted_by_remainder[i]] += 0.5

            wood_drops = drops["wood"]
            flower_drops = drops["flower"]
            fruit_drops = drops["fruit"]

        # --- 2. UPDATE TEXT HEADERS ---
        txt = UI_TEXT[self.lang]
        self.title_label.configure(text=txt["results_title"])
        
        sensed_trans = "鎮靜 (Chill)" if self.camera_sensed == "Chill" else "活力 (Energetic)" if self.camera_sensed == "Energetic" else "未知"
        needs_trans = "鎮靜 (Chill)" if self.camera_needs == "Chill" else "活力 (Energetic)" if self.camera_needs == "Energetic" else "未知"
        disp_sensed = sensed_trans if self.lang == "zh" else self.camera_sensed
        disp_needs = needs_trans if self.lang == "zh" else self.camera_needs
        
        self.info_label.configure(text=txt["baseline_text"].format(disp_sensed, disp_needs))

        # --- 3. DRAW NATIVE PIE CHART ---
        self.chart_canvas = ctk.CTkCanvas(self.root, width=700, height=260, bg="#0B192C", highlightthickness=0)
        self.chart_canvas.pack(pady=10)

        # Pie chart data structure [Value, Color, Name]
        wedges = [
            (wood_drops, '#A67B5B', txt['wood_name']),       # Soft Brown
            (flower_drops, '#FF9A9E', txt['flower_name']),   # Soft Pink
            (fruit_drops, '#FEC163', txt['fruit_name']),     # Soft Orange
            (chill_drops, '#A1C4FD', txt['chill_name']),     # Ice Blue
            (energetic_drops, '#00B4D8', txt['energy_name']) # Vibrant Blue
        ]

        def d_txt(val): return txt["drop_text"] if val == 1.0 else txt["drops_text"]

        total_drops = 5.0
        start_angle = 90 # Start drawing from the top
        
        # Bounding box for the pie circle (Maximized size: 240x240 inside the canvas height!)
        x0, y0, x1, y1 = 40, 10, 280, 250 
        
        # Coordinates for the text legend (Moved further right to accommodate the massive chart)
        legend_x, legend_y = 380, 35 

        for val, color, name in wedges:
            if val > 0:
                # Calculate how many degrees this slice takes up (e.g. 1 drop = 72 degrees)
                extent = -(val / total_drops) * 360 
                
                # Draw the pie slice
                self.chart_canvas.create_arc(x0, y0, x1, y1, start=start_angle, extent=extent, fill=color, outline="#0B192C", width=2)
                
                # Draw the legend color box
                self.chart_canvas.create_rectangle(legend_x, legend_y, legend_x+20, legend_y+20, fill=color, outline="")
                
                # Draw the legend text
                font_setup = ("Microsoft YaHei", 14) if self.lang == "zh" else ("Helvetica", 14)
                self.chart_canvas.create_text(legend_x+35, legend_y+10, text=f"{name}: {val} {d_txt(val)}", fill="white", font=font_setup, anchor="w")
                
                start_angle += extent
                legend_y += 35 # Move down for the next legend item

        # --- 4. SEND TO ARDUINO ---
        command_string = f"{wood_drops},{flower_drops},{fruit_drops},{chill_drops},{energetic_drops}\n"
        if arduino:
            arduino.write(command_string.encode('utf-8'))
            print(f"Sent to Arduino: {command_string}")
        else:
            print(f"PC Test Mode - Pretending to send: {command_string}")
        
        self.btn_a.configure(text=txt["btn_restart"], command=self.reset_app)
        self.btn_a.pack(pady=10)

    def reset_app(self):
        self.btn_a.pack_forget()
        
        # Destroy the pie chart so it doesn't overlap on the next run!
        if hasattr(self, 'chart_canvas'):
            self.chart_canvas.destroy()
            
        self.title_label.configure(text="WHALERAPY / 深海鯨癒")
        self.info_label.configure(text="Please select your language\n請選擇您的語言")
        
        self.btn_a.configure(text="English", command=lambda: self.set_language("en"))
        self.btn_b.configure(text="繁體中文", command=lambda: self.set_language("zh"))
        
        self.btn_a.pack(pady=10)
        self.btn_b.pack(pady=10)

if __name__ == "__main__":
    root = ctk.CTk() 
    app = WhalerapyApp(root)
    root.mainloop()