import os
import time
import subprocess
import sys

# Configuration
DATA_DIR = ".agent/data/Abhishek"
GENERATOR_SCRIPT = ".agent/scripts/generate_resume.py"
POLL_INTERVAL = 2  # Seconds

def watch():
    """ Monitors the directory for changes in YAML files. """
    print(f"--- Resume Watcher Started ---")
    print(f"Monitoring: {DATA_DIR}")
    print(f"Check interval: {POLL_INTERVAL}s")
    print(f"Press Ctrl+C to stop.")

    # initial state
    last_modified = {}
    for f in os.listdir(DATA_DIR):
        if f.endswith(".yaml"):
            path = os.path.join(DATA_DIR, f)
            last_modified[path] = os.path.getmtime(path)

    try:
        while True:
            time.sleep(POLL_INTERVAL)
            
            # Check for new or modified files
            current_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".yaml")]
            
            for f in current_files:
                path = os.path.join(DATA_DIR, f)
                try:
                    mtime = os.path.getmtime(path)
                except FileNotFoundError:
                    continue # File deleted during check

                if path not in last_modified or mtime > last_modified[path]:
                    print(f"\n[DETECTED] Change in {f}")
                    last_modified[path] = mtime
                    
                    # Trigger generation
                    try:
                        print(f"[RUNNING] python3 {GENERATOR_SCRIPT} {path}")
                        result = subprocess.run(
                            [sys.executable, GENERATOR_SCRIPT, path],
                            capture_output=True,
                            text=True
                        )
                        if result.returncode == 0:
                            print(f"[SUCCESS] {f} updated successfully.")
                        else:
                            print(f"[ERROR] Generation failed for {f}:")
                            print(result.stderror or result.stdout)
                    except Exception as e:
                        print(f"[CRITICAL] Failed to run generator: {e}")

            # Clean up tracking for deleted files
            paths_to_remove = [p for p in last_modified if not os.path.exists(p)]
            for p in paths_to_remove:
                del last_modified[p]

    except KeyboardInterrupt:
        print("\n--- Resume Watcher Stopped ---")

if __name__ == "__main__":
    # Ensure we are in the project root
    if not os.path.exists(GENERATOR_SCRIPT):
        print(f"Error: Could not find generator at {GENERATOR_SCRIPT}")
        print("Please run this script from the project root directory.")
        sys.exit(1)
        
    watch()
