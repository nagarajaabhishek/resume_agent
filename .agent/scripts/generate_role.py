import yaml
import sys
import os

def load_yaml(filepath):
    """Loads a YAML file."""
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {filepath}: {e}")
        sys.exit(1)

def filter_items_by_id(master_list, id_list):
    """
    Selects items from master_list that match IDs in id_list.
    Preserves the order defined in id_list.
    """
    if not id_list:
        return []
    
    # Create a lookup dictionary for O(1) access
    master_dict = {item['id']: item for item in master_list if 'id' in item}
    
    filtered_list = []
    for item_id in id_list:
        if item_id in master_dict:
            # Create a copy to avoid modifying the master data if we were to mutate it
            # (though we aren't mutating deep structures here, it's safer)
            item_copy = master_dict[item_id].copy()
            # Remove 'id' and 'tags' from the output to match the clean structure expected by resume generator
            # actually, keeping them might be fine, but let's clean up if strictness is needed.
            # For now, we will keep them or remove them based on preference.
            # The existing generate_resume.py likely ignores extra fields, but let's be clean.
            if 'id' in item_copy: del item_copy['id']
            if 'tags' in item_copy: del item_copy['tags']
            
            filtered_list.append(item_copy)
        else:
            print(f"Warning: Item ID '{item_id}' not found in master context.")
    
    return filtered_list

def filter_skills(master_skills, included_categories):
    """
    Selects skill categories from master_skills that match included_categories.
    Preserves order of included_categories.
    """
    if not included_categories:
        return []

    master_dict = {item['category']: item for item in master_skills}
    filtered_list = []

    for cat in included_categories:
        if cat in master_dict:
            filtered_list.append(master_dict[cat])
        else:
            print(f"Warning: Skill category '{cat}' not found in master context.")
            
    return filtered_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_role.py <config_file>")
        sys.exit(1)

    config_path = sys.argv[1]
    config = load_yaml(config_path)

    # Default paths
    base_dir = os.path.dirname(os.path.abspath(config_path))
    master_path = os.path.join(base_dir, 'master_context.yaml')
    
    # Allow override in config
    if 'master_file' in config:
        override_path = config['master_file']
        if not os.path.isabs(override_path):
            master_path = os.path.join(base_dir, override_path)
        else:
            master_path = override_path

    print(f"Loading Master Context from: {master_path}")
    master = load_yaml(master_path)

    # 1. Basics (Deep copy to avoid mutation)
    resume_data = {}
    resume_data['name'] = master['basics']['name']
    
    # Allow config to override specific contact details or summary
    resume_data['contact'] = master['basics'].copy()
    
    # Remove metadata fields from contact if they exist in master but aren't needed in resume
    # The resume generator expects: location, email, linkedin_url, linkedin_display, etc.
    # Our master has them nested differently? No, looks compatible.
    # Let's flatten specific fields if needed.
    
    contact_info = {}
    contact_info['location'] = master['basics']['location']
    contact_info['email'] = master['basics']['email']
    contact_info['linkedin_url'] = master['basics']['linkedin']['url']
    contact_info['linkedin_display'] = master['basics']['linkedin']['display']
    contact_info['website_url'] = master['basics']['website']['url']
    contact_info['website_display'] = master['basics']['website']['display']
    if 'phone' in master['basics'] and master['basics']['phone']:
        contact_info['phone'] = master['basics']['phone']
        
    resume_data['contact'] = contact_info

    # Meta
    resume_data['meta'] = config.get('meta', {'projects_first': True})

    # Summary
    if 'summary' in config:
        resume_data['summary'] = config['summary']
    else:
        # Fallback or empty?
        resume_data['summary'] = "Generated Resume"

    # 2. Education (Usually all, but can be filtered)
    # For now, include all education from master
    resume_data['education'] = []
    for edu in master['education']:
        cleaned_edu = edu.copy()
        if 'id' in cleaned_edu: del cleaned_edu['id']
        resume_data['education'].append(cleaned_edu)

    # 3. Experience
    if 'experience' in config:
        resume_data['experience'] = filter_items_by_id(master['experience'], config['experience'])
    else:
        resume_data['experience'] = []

    # 4. Projects
    if 'projects' in config:
        resume_data['projects'] = filter_items_by_id(master['projects'], config['projects'])
    else:
        resume_data['projects'] = []

    # 5. Skills
    if 'skills' in config:
        resume_data['skills'] = filter_skills(master['skills'], config['skills'])
    else:
        resume_data['skills'] = []

    # 6. Certifications
    # specific logic for certs? master has list of objects/strings?
    # Master has list of objects {name, date}. Resume YAML often has list of strings.
    # Let's check role_technical_product_manager.yaml.
    # It has a list of strings.
    
    # If master has objects, we should maybe extracting names?
    # role_technical_product_manager.yaml:
    # certifications:
    #   - "Certified Scrum Product Owner (CSPO)"
    # master_context.yaml:
    # certifications:
    #   - name: "Certified Scrum Product Owner (CSPO)"
    
    resume_data['certifications'] = []
    if 'certifications' in master:
        for cert in master['certifications']:
            if isinstance(cert, str):
                resume_data['certifications'].append(cert)
            elif isinstance(cert, dict) and 'name' in cert:
                resume_data['certifications'].append(cert['name'])

    # Output
    output_filename = config.get('output_file', 'generated_resume.yaml')
    output_path = os.path.join(base_dir, output_filename)
    
    with open(output_path, 'w') as f:
        yaml.dump(resume_data, f, sort_keys=False, allow_unicode=True, width=1000)
    
    print(f"Successfully generated resume YAML at: {output_path}")

if __name__ == "__main__":
    main()
