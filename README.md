## 🛡️ Software Monitor (Blacklist/Whitelist)
A Python-based system monitor that manages running processes based on security policies.

### How it works:
- **Blacklist**: Automatically terminates unauthorized applications (e.g., productivity blockers).
- **Whitelist**: Ensures only a specific set of trusted applications are allowed to execute.
- **Library used**: `psutil` for cross-platform process management.

### Setup:
1. Install requirements: `pip install psutil`
2. Define your `APPS_LIST`.
3. Set `MONITOR_MODE` to either 'blacklist' or 'whitelist'.
