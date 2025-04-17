import win32gui
import time
import datetime

now = datetime.datetime.now()

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

print("🖥️ Monitoring active window changes (press Ctrl+C to stop)...")
last_title = None

try:
    while True:
        current_title = get_active_window_title()
        if current_title != last_title and current_title.strip() != "":
            with open("F:/AI Assistant (Jarvis)/history.txt", "a") as f:
                f.write(f"{now}: {current_title}\n")
            print(f"🔔 Notification: {current_title}")
            last_title = current_title
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped.")
    f.close()
