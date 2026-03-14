import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import threading

# 1. Setup Window
root = tk.Tk()
root.title("🛡️ DeepFakeGuard: Forensic Verifier")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

# 2. Load the Brain (Phase 2 Model)
try:
    model = load_model('deepfake_detection_model.h5')
    status_msg = "✅ AI Engine Ready (RTX 4050 Active)"
except Exception as e:
    status_msg = f"❌ Model Load Error: {e}"

# 3. Analysis Logic
def start_analysis():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
    if not file_path:
        return

    # Run in a thread so the window doesn't freeze
    threading.Thread(target=process_video, args=(file_path,)).start()

def process_video(path):
    btn_scan.config(state="disabled")
    lbl_result.config(text="🔍 Analyzing pixels...", fg="blue")
    progress['value'] = 0
    
    cap = cv2.VideoCapture(path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    preds = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        curr = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        if curr % 10 == 0: # Check every 10th frame
            img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (299, 299)) / 255.0
            p = model.predict(np.expand_dims(img, axis=0), verbose=0)[0][0]
            preds.append(p)
            # Update UI Progress
            progress['value'] = (curr / total_frames) * 100
            root.update_idletasks()
            
    cap.release()
    
    # Final Result
    avg_score = np.mean(preds)
    if avg_score > 0.4:
        lbl_result.config(text=f"⚠️ VERDICT: FAKE\n(Score: {avg_score*100:.1f}%)", fg="red")
    else:
        lbl_result.config(text=f"✅ VERDICT: REAL\n(Score: {(1-avg_score)*100:.1f}%)", fg="green")
    
    btn_scan.config(state="normal")

# --- UI Layout ---
tk.Label(root, text="DeepFakeGuard AI", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text=status_msg, font=("Arial", 9), bg="#f0f0f0").pack()

btn_scan = tk.Button(root, text="SELECT VIDEO & SCAN", command=start_analysis, 
                     font=("Arial", 12, "bold"), bg="#28a745", fg="white", padx=20, pady=10)
btn_scan.pack(pady=30)

progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=10)

lbl_result = tk.Label(root, text="Waiting for input...", font=("Arial", 14, "bold"), bg="#f0f0f0")
lbl_result.pack(pady=20)

root.mainloop()