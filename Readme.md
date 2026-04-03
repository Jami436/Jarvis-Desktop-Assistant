# JARVIS: Joint Artificial Real-time Virtual Interactive System 🚀

**JARVIS** is a lightweight, agentic desktop assistant designed for seamless Windows automation. Unlike static scripts, JARVIS utilizes **Asynchronous Processing** and **Persistent JSON Memory** to recognize its creator, manage system hardware, and execute proactive desktop workflows via voice command.

---

### 🛠️ Built With

* **Python & Asyncio**: Core logic engine for non-blocking task execution.
* **Edge-TTS (Liam Neural)**: High-fidelity, low-latency Neural Text-to-Speech.
* **Selenium & WebDriver**: Automated browser-based speech-to-text listener.
* **Persistent JSON Engine**: Dynamic local memory for user identity and preference tracking.
* **OS/Hardware Libraries**: `screen-brightness-control` (Display), `winshell` (File system), and `webbrowser`.

---

### 🧪 How to Test JARVIS Locally (Reproducible Testing)

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/Jami436/Jarvis-AI.git](https://github.com/Jami436/Jarvis-AI.git)
   cd Jarvis-AI

## Install the required dependencies:

    pip install edge-tts pygame screen-brightness-control winshell selenium webdriver-manager jami-speech-selenium-tool-2026

## Configure Environment:

    Ensure you have Google Chrome installed (required for the Selenium-based speech listener).

## Run the Application:

    Execute the main script to initialize core systems:

        python main.py

## Interaction & Commands
Identity & Contextual Memory
**Set Identity**: "Jarvis, my name is (Name)." (Stored in memory.json)

**Verification**: "Jarvis, who am I?"

## Hardware & System Reflex

**Display Control**: "Jarvis, set brightness to 80 percent."

**System Maintenance**: "Jarvis, empty the recycle bin."

**Temporal Query**: "Jarvis, what time is it?"

## Agentic Web Navigation
**Development**: "Jarvis, open GitHub."

**Media**: "Jarvis, open YouTube."
