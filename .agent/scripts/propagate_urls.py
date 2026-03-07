import yaml
import os
import glob

DATA_DIR = ".agent/data"
YAML_FILES = glob.glob(os.path.join(DATA_DIR, "*.yaml"))

URL_MAP = {
    "University of Texas at Dallas": "https://www.uta.edu/",
    "Jawaharlal Nehru Technological University": "https://www.jntuh.ac.in/",
    "Thara": "https://withthara.com/",
    "Google Maps": "https://abhishekn.in/content/google-maps-teardown",
    "Clash of Clans": "https://abhishekn.in/content/clash-of-clans-teardown",
    "Split-Wiser": "https://abhishekn.in/content/splitwise-teardown"
}

def update_yaml(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"Error reading {file_path}: {exc}")
            return

    modified = False

    # Update Education
    if 'education' in data:
        for edu in data['education']:
            school = edu.get('school')
            for key, url in URL_MAP.items():
                if key in school:
                    if 'url' not in edu or edu['url'] != url:
                        edu['url'] = url
                        modified = True
                        print(f"  Added URL for School: {school}")

    # Update Projects
    if 'projects' in data:
        for proj in data['projects']:
            name = proj.get('name')
            for key, url in URL_MAP.items():
                if key in name:
                     if 'url' not in proj or proj['url'] != url:
                        proj['url'] = url
                        modified = True
                        print(f"  Added URL for Project: {name}")

    if modified:
        with open(file_path, 'w') as f:
            yaml.dump(data, f, sort_keys=False, width=1000)
        print(f"  Saved updates to {file_path}")
    else:
        print(f"  No changes needed for {file_path}")

def main():
    print(f"Found {len(YAML_FILES)} YAML files.")
    for f in YAML_FILES:
        # Skip the one we already manually edited if we want, but the script is idempotent
        update_yaml(f)

if __name__ == "__main__":
    main()
