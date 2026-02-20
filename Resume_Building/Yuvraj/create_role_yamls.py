
import yaml
import os
import subprocess

BASE_DIR = "/Users/abhisheknagaraja/Documents/Resume_Agent"
DATA_DIR = os.path.join(BASE_DIR, ".agent/data/Yuvraj")
OUTPUT_DIR = os.path.join(BASE_DIR, "Resume_Building/Yuvraj")
SCRIPT_PATH = os.path.join(BASE_DIR, ".agent/scripts/generate_resume.py")

# Role Definitions: Which IDs to use for each role
ROLE_CONFIGS = {
    "Agriculture_Engineer": {
        "experience": ["marktech_cofounder", "srikrishnaa_trainee", "nsic_cnc_trainee", "avhea_hr_intern"],
        "projects": ["grass_cutter", "cyber_scooter", "drone_ambulance", "cfd_muffler", "fork_lifter", "caravan_chassis"],
        "summary": "Innovative Mechanical Engineer with agriculture-focused design experience, skilled in prototyping low-cost machinery and applying engineering principles to sustainable solutions.",
        "skills_focus": ["Mechanical Design (CAD/CAE)", "Manufacturing & Prototyping", "Project Management Tools", "Soft Skills & Leadership"]
    },
    "Product_Development_Engineer": {
        "experience": ["marktech_cofounder", "srikrishnaa_trainee", "nsic_cnc_trainee", "avhea_hr_intern"],
        "projects": ["cyber_scooter", "drone_ambulance", "grass_cutter", "mid_air_transfer", "cfd_muffler", "fork_lifter"],
        "summary": "Product Development Engineer with a track record of taking concepts from MVP to full-scale production, leveraging CAD/CAM proficiency and rapid prototyping skills.",
        "skills_focus": ["Product Management", "Mechanical Design (CAD/CAE)", "Manufacturing & Prototyping", "Soft Skills & Leadership"]
    },
    "Mechanical_Engineer": {
        "experience": ["srikrishnaa_trainee", "nsic_cnc_trainee", "marktech_cofounder", "avhea_hr_intern"],
        "projects": ["cfd_muffler", "caravan_chassis", "fork_lifter", "cyber_scooter", "grass_cutter", "drone_ambulance"],
        "summary": "Detail-oriented Mechanical Engineer proficient in GD&T, FEA, and CFD analysis, with hands-on experience in CNC programming and complex assembly design.",
        "skills_focus": ["Mechanical Design (CAD/CAE)", "Manufacturing & Prototyping", "Robotics & Automation", "Project Management Tools"]
    },
    "Product_Manager_Cleantech": {
        "experience": ["marktech_cofounder", "edam_hr_officer", "avhea_hr_intern", "srikrishnaa_trainee"],
        "projects": ["cyber_scooter", "grass_cutter", "drone_ambulance", "market_monitor", "ev_adoption", "netflix_analysis"],
        "summary": "Cleantech Product Manager with entrepreneurial experience in sustainable hardware, adept at securing grants, conducting market research, and leading cross-functional teams.",
        "skills_focus": ["Product Management", "Data Visualization & BI", "Project Management Tools", "Soft Skills & Leadership"]
    },
    "Circular_Economy_Solutions_Architect": {
        "experience": ["marktech_cofounder", "srikrishnaa_trainee", "nsic_cnc_trainee", "avhea_hr_intern"],
        "projects": ["grass_cutter", "cyber_scooter", "cfd_muffler", "fork_lifter", "caravan_chassis", "mid_air_transfer"],
        "summary": "Solutions Architect focused on circular economy principles, designing systems for waste reduction and material recovery in hardware manufacturing.",
        "skills_focus": ["Product Management", "Mechanical Design (CAD/CAE)", "Manufacturing & Prototyping", "Soft Skills & Leadership"]
    },
    "Biomedical_Engineer": {
        "experience": ["marktech_cofounder", "srikrishnaa_trainee", "nsic_cnc_trainee", "avhea_hr_intern"],
        "projects": ["drone_ambulance", "mid_air_transfer", "cyber_scooter", "grass_cutter", "cfd_muffler", "fork_lifter"],
        "summary": "Biomedical Engineering enthusiast with experience designing hygiene-critical hardware solutions and conceptualizing emergency medical response systems.",
        "skills_focus": ["Mechanical Design (CAD/CAE)", "Product Management", "Manufacturing & Prototyping", "Soft Skills & Leadership"]
    },
    "Robotics_Engineer": {
        "experience": ["nsic_cnc_trainee", "srikrishnaa_trainee", "marktech_cofounder", "avhea_hr_intern"],
        "projects": ["mid_air_transfer", "drone_ambulance", "cyber_scooter", "fork_lifter", "grass_cutter", "cfd_muffler"],
        "summary": "Robotics Engineer with expertise in automation, CNC programming, and designing robotic assembly methods for precision manufacturing.",
        "skills_focus": ["Robotics & Automation", "Manufacturing & Prototyping", "Mechanical Design (CAD/CAE)", "Data Analysis & Programming"]
    },
    "Mechatronics_Engineer": {
        "experience": ["marktech_cofounder", "nsic_cnc_trainee", "srikrishnaa_trainee", "avhea_hr_intern"],
        "projects": ["cyber_scooter", "drone_ambulance", "grass_cutter", "mid_air_transfer", "fork_lifter", "cfd_muffler"],
        "summary": "Mechatronics Engineer integrating mechanical design with electronic control systems, experienced in prototyping IoT-enabled hardware and autonomous systems.",
        "skills_focus": ["Mechanical Design (CAD/CAE)", "Robotics & Automation", "Data Analysis & Programming", "Project Management Tools"]
    },
    "Manufacturing_Engineer": {
        "experience": ["nsic_cnc_trainee", "srikrishnaa_trainee", "marktech_cofounder", "avhea_hr_intern"],
        "projects": ["fork_lifter", "mid_air_transfer", "cfd_muffler", "caravan_chassis", "grass_cutter", "cyber_scooter"],
        "summary": "Manufacturing Engineer with hands-on expertise in CNC programming, process optimization, and quality control for precision machining operations.",
        "skills_focus": ["Manufacturing & Prototyping", "Mechanical Design (CAD/CAE)", "Robotics & Automation", "Project Management Tools"]
    },
    "Operations_Manager": {
        "experience": ["edam_hr_officer", "marktech_cofounder", "avhea_hr_intern", "srikrishnaa_trainee"],
        "projects": ["market_monitor", "netflix_analysis", "automotive_dashboard", "cyber_scooter", "grass_cutter", "ev_adoption"],
        "summary": "Operations Manager with a strong background in process improvement, team leadership, and data-driven decision making to streamline workflows and enhance productivity.",
        "skills_focus": ["Project Management Tools", "Data Visualization & BI", "Soft Skills & Leadership", "Product Management"]
    },
    "Data_Analyst": {
        "experience": ["marktech_cofounder", "avhea_hr_intern", "srikrishnaa_trainee", "nsic_cnc_trainee"],
        "projects": ["netflix_analysis", "automotive_dashboard", "ev_adoption", "market_monitor", "cyber_scooter", "grass_cutter"],
        "summary": "Data Analyst with extensive experience in Power BI, Tableau, and SQL, specializing in transforming complex datasets into actionable business intelligence dashboards.",
        "skills_focus": ["Data Visualization & BI", "Data Analysis & Programming", "Project Management Tools", "Soft Skills & Leadership"]
    },
    "Product_Analyst": {
        "experience": ["marktech_cofounder", "avhea_hr_intern", "srikrishnaa_trainee", "nsic_cnc_trainee"],
        "projects": ["market_monitor", "netflix_analysis", "automotive_dashboard", "ev_adoption", "cyber_scooter", "drone_ambulance"],
        "summary": "Product Analyst bridging data insights with product strategy, leveraging KPI analysis and A/B testing to optimize user experience and drive growth.",
        "skills_focus": ["Data Visualization & BI", "Product Management", "Data Analysis & Programming", "Soft Skills & Leadership"]
    }
}

def load_master_profile():
    with open(os.path.join(DATA_DIR, "master_profile.yaml"), "r") as f:
        return yaml.safe_load(f)

def filter_by_id(items, ids):
    """Returns list of items whose 'id' is in the ids list, preserving order of ids."""
    item_map = {item['id']: item for item in items}
    result = []
    for i in ids:
        if i in item_map:
            result.append(item_map[i])
        else:
            print(f"Warning: ID '{i}' not found in master data.")
    return result

def generate_role_yaml(role_name, config, master_data):
    basics = master_data['basics']
    
    # Transform basics to match template structure
    # Template expects: name, contact: {location, email, linkedin_url, linkedin_display, website_url, website_display, phone}
    role_data = {
        "name": basics['name'],
        "contact": {
            "location": basics['location'],
            "email": basics['email'],
            "phone": basics.get('phone', ''),
            "linkedin_url": basics['linkedin']['url'],
            "linkedin_display": basics['linkedin']['display'],
            "website_url": basics['website']['url'],
            "website_display": basics['website']['display']
        },
        "education": master_data['education'],
        "certifications": master_data.get('certifications', []),
        "awards": master_data.get('awards', []),
        "publications": master_data.get('publications', []),
        "meta": {
            "filename": f"Yuvraj_K_{role_name}_Resume"
        }
    }

    # Override summary
    role_data['summary'] = config['summary']
    
    # Filter Experience
    role_data['experience'] = filter_by_id(master_data['experience'], config['experience'])
    
    # Filter Projects
    role_data['projects'] = filter_by_id(master_data['projects'], config['projects'])
    
    # Filter Skills (Keep only relevant categories)
    # If skills_focus is empty or None, keep all skills
    if config.get('skills_focus'):
        role_data['skills'] = [
            cat for cat in master_data['skills'] 
            if cat['skill_list'] and any(focus in cat.get('category', '') or focus == cat.get('name', '') for focus in config['skills_focus'])
        ]
        # Fallback if filter is too aggressive (keep all categories but prioritize order maybe? 
        # For simplicity, if we filter out everything, revert to all)
        if not role_data['skills']:
             role_data['skills'] = master_data['skills']
    else:
        role_data['skills'] = master_data['skills']

    # Write to file
    filename = f"role_{role_name.lower()}.yaml"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w") as f:
        yaml.dump(role_data, f, sort_keys=False)
    
    print(f"Generated YAML for {role_name}: {filepath}")
    return filepath

def main():
    print("Loading Master Profile...")
    master_data = load_master_profile()
    
    for role_name, config in ROLE_CONFIGS.items():
        print(f"\nProcessing {role_name}...")
        try:
            yaml_path = generate_role_yaml(role_name, config, master_data)
            
            # Identify output directory based on role name
            output_dir = os.path.join(OUTPUT_DIR, role_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            output_pdf_path = os.path.join(output_dir, f"Yuvraj_K_{role_name}_Resume.tex")

            print(f"Running generator for {role_name}...")
            cmd = [
                "python3", 
                SCRIPT_PATH, 
                yaml_path,
                "--output",
                output_pdf_path
            ]
            subprocess.run(cmd, check=True)
            print(f"✅ Generated LaTeX for {role_name}")
            
        except Exception as e:
            print(f"❌ Failed to generate {role_name}: {e}")

if __name__ == "__main__":
    main()
