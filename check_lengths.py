import yaml
with open('.agent/data/Abhishek/role_dubai.yaml', 'r') as f:
    data = yaml.safe_load(f)

for section in ['experience', 'projects', 'products']:
    if section in data:
        for item in data[section]:
            for b in item.get('bullets', []):
                print(f"{len(b)} chars: {b[:50]}...")
