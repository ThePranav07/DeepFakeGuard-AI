# 🛡️ DeepFakeGuard: AI-Powered Forensic Detection System

DeepFakeGuard is a high-performance forensic tool designed to detect facial manipulations and synthetic media. By leveraging the **InceptionResNetV2** architecture and **NVIDIA GPU acceleration**, the system identifies subtle GAN (Generative Adversarial Network) artifacts that are invisible to the naked eye.

## 🚀 Key Features
- **InceptionResNetV2 Backbone:** Utilizes a hybrid deep learning model combining residual connections and inception blocks for multi-scale feature extraction.
- **Hardware Optimized:** Fully integrated with **NVIDIA RTX 4050 GPU** using CUDA 11 and cuDNN for near real-time inference.
- **Forensic Sampling:** Implements a strategic 1:5 frame-sampling protocol to analyze temporal inconsistencies while maintaining computational efficiency.
- **User-Friendly GUI:** A native Desktop interface built with Tkinter for seamless "Select & Scan" operations.

## 🛠️ Project Phases
1. **Phase 1: Research & Data Ingestion** - Analyzing Celeb-DF v2 datasets and establishing forensic requirements.
2. **Phase 2: Model Training** - Fine-tuning the CNN on high-quality deepfake samples to identify pixel-level inconsistencies.
3. **Phase 3: Deployment** - Developing a multithreaded GUI and optimizing the software stack (Protobuf 3.19.6 compatibility) for stable GPU performance.

## 📂 Repository Structure
- `final_gui.py`: The main application script (Phase 3).
- `Deepfake_Data.ipynb`: Research notebook containing model training and evaluation (Phase 2).
- `requirements.txt`: List of dependencies and environment configurations.
- `README.md`: Project documentation.
