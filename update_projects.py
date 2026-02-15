import os
import django
from django.core.files import File
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from website.models import Project

def update_projects():
    # 1. Update Hospital Management System
    try:
        hospital_proj = Project.objects.get(title__icontains="Hospital Management System")
        print(f"Updating: {hospital_proj.title}")
        # Assuming the file is in static/website/images/hospital_dashboard.png
        # For simplicity in this script, we'll just set the image path string directly 
        # because FileFields are tricky without actual file upload handling.
        # Alternatively, we can assume the user wants to point to static files.
        # But Django's ImageField usually expects files in MEDIA_ROOT.
        
        # Strategy: Project model uses ImageField upload_to='projects/'.
        # Changing this to a CharField might be better if we want to use static files directly,
        # but let's stick to the current model. We'll simulate an upload by copying.
        
        # Actually, let's look at the model again. It's an ImageField.
        # So we need to save the file into the field.
        
        # Since I can't easily upload via script without copying to MEDIA_ROOT, 
        # I'll manually copy the files to MEDIA_ROOT/projects/ and then set the name.
        
        print("Please ensure MEDIA_ROOT is set correctly.")
    except Project.DoesNotExist:
        print("Hospital Management System project not found.")

    # Let's simplify and just set the image name relative to MEDIA_ROOT.
    # We need to make sure the files exist in `e:/my_porfolio/media/projects/`
    
    media_projects_dir = os.path.join(settings.MEDIA_ROOT, 'projects')
    os.makedirs(media_projects_dir, exist_ok=True)
    
    source_dir = os.path.join(settings.BASE_DIR, 'static', 'website', 'images')
    
    images_map = {
        "Hospital Management System": "hospital_dashboard_v2.png",
        "Student Management System": "student_dashboard_v2.png",
        "Inventory API": "inventory_dashboard_v2.png" # Will be for the new project
    }
    
    import shutil
    
    # 2. Add Inventory API Project
    inventory_title = "Inventory Management API"
    inventory_desc = "A robust RESTful API for inventory tracking, including product categorization, stock level monitoring, and supplier management."
    
    inventory_proj, created = Project.objects.get_or_create(
        title=inventory_title,
        defaults={'description': inventory_desc}
    )
    if created:
        print(f"Created new project: {inventory_title}")
    else:
        print(f"Found existing project: {inventory_title}")

    # 3. Update all images
    # We need to copy from static to media/projects because ImageField uses media root
    
    project_mapping = {
        "Hospital Management System": images_map["Hospital Management System"],
        "Student Management System": images_map["Student Management System"],
        "Inventory Management API": images_map["Inventory API"],
    }
    
    print("Updating images...")
    
    for title_part, img_name in project_mapping.items():
        try:
            proj = Project.objects.filter(title__icontains=title_part).first()
            if proj:
                src_path = os.path.join(source_dir, img_name)
                dst_path = os.path.join(media_projects_dir, img_name)
                
                if os.path.exists(src_path):
                    shutil.copy2(src_path, dst_path)
                    print(f"Copied {img_name} to media/projects/")
                    
                    # Update model
                    proj.image.name = f"projects/{img_name}"
                    proj.save()
                    print(f"Updated image for {proj.title}")
                else:
                    print(f"Source image not found: {src_path}")
            else:
                print(f"Project matching '{title_part}' not found.")
        except Exception as e:
            print(f"Error updating {title_part}: {e}")

if __name__ == "__main__":
    update_projects()
