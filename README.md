# AIOS – Open Source Artificial Intelligence Operating System (in progress)

**AIOS** is an on-premise, modular system that captures screen context, interprets it with local or remote LLMs, and executes automated actions via keyboard/mouse emulation, APIs, or shell commands. It is designed as a minimal AI-native desktop automation layer.

---

## 🔧 Architecture Overview

AIOS follows a modular 5-step pipeline:

| Step | Module            | Description                                                                 | Tools / Libraries                               |
|------|-------------------|-----------------------------------------------------------------------------|-------------------------------------------------|
| 1    | **Screen Capture**| Capture real-time screenshots or video frames from the desktop environment | `mss`, `PIL`, `pyautogui`                       |
| 2    | **Context Extraction** | OCR text extraction and UI detection via object detection              | `pytesseract`, `OpenCV`, `YOLOv8`               |
| 3    | **LLM Reasoning**  | Encode screen state, feed it into an LLM for contextual action planning   | `OpenAI`, `TinyLlama`, `GPT4All`, `LangChain`   |
| 4    | **Action Execution**| Perform user actions (clicks, typing, shortcuts, scripts)                 | `pyautogui`, `subprocess`, `os`, `platform`     |
| 5    | **IFTTT Automation**| Trigger workflows based on screen context, events, or user behavior      | `Zapier`, `IFTTT`, `Python`, `LangChain`        |

---

## 🔍 Features

- **On-Prem / Local-LLM Support:** Works with TinyLlama, GPT4All, Ollama, and OpenAI.
- **Event-Based Triggers:** Automate actions based on desktop state, app events, or external APIs (e.g., Gmail, Discord).
- **Multi-modal Input:** OCR from images or screen; potential extension to voice/text.
- **Replayable Logs:** Store screen state + actions with timestamp for debugging and iteration.
- **Embedding-based Recall:** Use FAISS to remember and retrieve screen states and actions over time.

---

## 🧠 Example Use Case

> Given a screen containing a meeting reminder, AIOS can:
1. Extract text using OCR
2. Understand intent

## 🧪 Use Case Example

> Scenario: You receive a payment reminder email on your screen.

**Pipeline:**
1. `capture`: AIOS screenshots the visible screen.
2. `ocr`: Text like "Pay invoice by July 16" is extracted using `pytesseract`.
3. `llm`: LLM determines intent → "This is a bill payment task."
4. `actions`: AIOS opens your banking app and autofills payment.
5. `automation`: Marks task as "done" in a Notion board via API.

## Vision

**Empower users with a truly autonomous, privacy‑first desktop assistant** that…

- **Thinks Ahead, Acts Instantly**  
  Anticipates your needs—scheduling meetings, replying to messages, managing reminders—without lifting a finger.

- **Runs Entirely On‑Premise**  
  All ML inference and decision‑making happen locally, so your data never leaves your device.

- **Seamlessly Integrates Into Your Workflow**  
  From opening apps to filling forms, AIOS handles end‑to‑end task automation based on your screen context.

- **Learns and Evolves Over Time**  
  Embedding‑based recall (via FAISS) lets AIOS remember past actions and optimize future automation.

- **Makes Every Device Smarter**  
  Your desktop, phone, or tablet become proactive partners—no cloud lock‑in, no privacy trade‑offs.


