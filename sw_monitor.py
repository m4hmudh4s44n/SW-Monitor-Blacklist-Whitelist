import psutil
import time

# --- CONFIGURATION ---
# Mode: 'whitelist' (only allowed apps run) or 'blacklist' (specific apps blocked)
MONITOR_MODE = 'blacklist' 

# List of process names (check Task Manager/Activity Monitor for exact names)
APPS_LIST = ['CalculatorApp.exe', 'Notepad.exe']

def monitor_processes():
    print(f"--- Monitoring started in {MONITOR_MODE} mode ---")
    
    while True:
        for proc in psutil.process_iter(['name']):
            try:
                p_name = proc.info['name']
                
                if MONITOR_MODE == 'blacklist':
                    # If the app is in the list, kill it
                    if p_name in APPS_LIST:
                        print(f"[!] Terminating forbidden app: {p_name}")
                        proc.kill()
                        
                elif MONITOR_MODE == 'whitelist':
                    # If the app is NOT in the list (and isn't a system process), kill it
                    # Note: Be careful! Killing unknown system processes can crash your PC.
                    if p_name not in APPS_LIST and not p_name.startswith('System'):
                        # Caution: Real whitelists need a very long list of safe apps
                        pass 

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        time.sleep(2) # Wait 2 seconds before checking again

if __name__ == "__main__":
    monitor_processes()