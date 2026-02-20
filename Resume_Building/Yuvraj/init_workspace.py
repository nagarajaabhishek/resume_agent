
import os
import yaml

# Base path
base_path = "/Users/abhisheknagaraja/Documents/Resume_Agent"
data_path = f"{base_path}/.agent/data/Yuvraj"
build_path = f"{base_path}/Resume_Building/Yuvraj"

# Roles to create
roles = [
    "Agriculture_Engineer",
    "Product_Development_Engineer",
    "Mechanical_Engineer",
    "Product_Manager_Cleantech",
    "Circular_Economy_Solutions_Architect",
    "Biomedical_Engineer",
    "Robotics_Engineer",
    "Mechatronics_Engineer",
    "Manufacturing_Engineer",
    "Operations_Manager"
]

# Create directories
for role in roles:
    role_dir = os.path.join(build_path, role)
    os.makedirs(role_dir, exist_ok=True)
    print(f"Created directory: {role_dir}")

# Create master_profile.yaml content (Skeleton based on extraction)
master_profile = {
    "basics": {
        "name": "Yuvraj K",
        "label": "Mechanical Engineer | Product Manager | Entrepreneur",
        "email": "work.kyuvraj@gmail.com",
        "phone": "+91 6301421537",
        "location": "Hyderabad, India",
        "linkedin": {
            "url": "https://www.linkedin.com/in/kyuvraj/",
            "display": "linkedin.com/in/kyuvraj"
        },
        "website": {
            "url": "https://k-yuvraj.github.io/kyuvraj/",
            "display": "k-yuvraj.github.io/kyuvraj"
        }
    },
    "education": [
        {
            "institution": "Institute of Aeronautical Engineering",
            "area": "Mechanical Engineering",
            "studyType": "B.Tech",
            "startDate": "2021-09",
            "endDate": "2024-09",
            "score": "",
            "courses": []
        },
        {
            "institution": "TKR College of Engineering and Technology",
            "area": "Mechanical Engineering",
            "studyType": "Diploma",
            "startDate": "2018-06",
            "endDate": "2021-05",
            "score": "",
            "courses": []
        }
    ],
    "experience": [
        {
            "company": "Padverse", # Consolidated form /glbe
            "position": "Co-Founder & Head of Product Development",
            "startDate": "2022-08",
            "endDate": "Present",
            "summary": "Leading product development for a menstrual hygiene startup.",
            "highlights": [
                "Led product development at Padverse, taking MVPs from concept to prototyping.",
                "Built various machines to accommodate recycling capacity.",
                "Raised multiple grants including SISF from T-Hub."
            ]
        },
        {
            "company": "e-DAM",
            "position": "Human Resources Officer",
            "startDate": "2022-10",
            "endDate": "2023-01",
            "summary": "Managed HR operations.",
            "highlights": [
                "Recruitment, administration, compensation and benefits."
            ]
        },
        {
            "company": "Srikrishnaa Process Technologies Pvt Ltd",
            "position": "Engineering Trainee",
            "startDate": "2022-07",
            "endDate": "2022-07",
            "summary": "In-plant training.",
            "highlights": [
                "Acquired knowledge of Chemical Reactors.",
                "Used AutoCAD and Fusion 360 for designing chemical reactors."
            ]
        },
        {
            "company": "National Small Industries Corp (NSIC)",
            "position": "CNC Programmer Trainee",
            "startDate": "2020-04",
            "endDate": "2020-12",
            "summary": "CNC training.",
            "highlights": [
                "CNC programming, setup, and execution.",
                "CAD/CAM software proficiency."
            ]
        }
    ],
    "projects": [
         {"name": "CFD Analysis on Muffler", "description": "Simulated pressure drop and velocity using ANSYS Fluent."},
         {"name": "Cyber Scooter (e-Scooter)", "description": "Designed 3D CAD model using Fusion 360."},
         {"name": "Grass Cutting Machine", "description": "Designed using copper wire blade."},
         {"name": "Fork Lifter Component", "description": "Designed for 3D printing."},
         {"name": "Mid-Air Part Transfer", "description": "Robotic assembly method for aerospace."},
         {"name": "Chassis Design for Caravan", "description": "Lightweight chassis using FEA."},
         {"name": "Mobile Drone Ambulance", "description": "Conceptual design for emergency response."}
    ],
    "skills": [
        {"name": "Tools", "keywords": ["AutoCAD", "Fusion 360", "SolidWorks", "Ansys", "Catia", "Blender"]},
        {"name": "Technical", "keywords": ["Product Design", "PLM", "CNC", "GD&T", "Additive Manufacturing"]},
        {"name": "Programming", "keywords": ["Python", "HTML", "CSS"]},
        {"name": "Business", "keywords": ["Project Management", "Power BI", "Tableau"]}
    ]
}

# Write master profile
with open(os.path.join(data_path, "master_profile.yaml"), "w") as f:
    yaml.dump(master_profile, f, sort_keys=False)

print("Created master_profile.yaml and role directories.")
