from PIL import Image, ImageDraw, ImageFont
import os
import random
import math

def create_advanced_dashboard(filename, title, theme_color):
    width, height = 800, 600
    bg_color = "#f4f6f8"
    sidebar_color = "#1a202e"
    header_color = "#ffffff"
    
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    # Sidebar
    draw.rectangle([0, 0, 220, height], fill=sidebar_color)
    # Sidebar Logo area
    draw.rectangle([0, 0, 220, 60], fill="#121621")
    # Sidebar items
    for i in range(8):
        y = 100 + (i * 50)
        # Icon placeholder
        draw.ellipse([20, y+5, 40, y+25], fill="#2d3748")
        # Text line
        draw.rectangle([55, y+10, 180, y+20], fill="#2d3748")

    # Header
    draw.rectangle([220, 0, width, 60], fill=header_color)
    # Header title
    try:
        font_title = ImageFont.truetype("arial.ttf", size=20)
        font_small = ImageFont.truetype("arial.ttf", size=12)
    except IOError:
        font_title = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    draw.text((240, 18), title.upper(), fill="#333", font=font_title)

    # Main Content Area
    start_x = 240
    start_y = 80
    content_width = width - start_x - 20
    
    # Top Stats Cards
    card_count = 3
    card_w = (content_width - (20 * (card_count - 1))) / card_count
    
    for i in range(card_count):
        x = start_x + (i * (card_w + 20))
        draw.rectangle([x, start_y, x + card_w, start_y + 100], fill="white", outline="#e2e8f0")
        # Card formatting
        draw.text((x+15, start_y+15), "METRIC " + str(i+1), fill="#718096", font=font_small)
        draw.text((x+15, start_y+40), str(random.randint(100, 9999)), fill="#2d3748", font=font_title)
        # Little color bar
        draw.rectangle([x, start_y+95, x+card_w, start_y+100], fill=theme_color)

    # Big Chart Section
    chart_y = start_y + 120
    draw.rectangle([start_x, chart_y, width - 20, chart_y + 200], fill="white", outline="#e2e8f0")
    draw.text((start_x+15, chart_y+15), "ANALYTICS OVERVIEW", fill="#718096", font=font_small)
    
    # Draw a line graph
    prev_x = start_x + 20
    prev_y = chart_y + 150
    for i in range(10):
        next_x = prev_x + ((content_width - 40) / 10)
        next_y = chart_y + 150 - random.randint(10, 100)
        draw.line([prev_x, prev_y, next_x, next_y], fill=theme_color, width=2)
        # Dot
        draw.ellipse([next_x-3, next_y-3, next_x+3, next_y+3], fill=theme_color)
        prev_x = next_x
        prev_y = next_y

    # Bottom Data Table
    table_y = chart_y + 220
    draw.rectangle([start_x, table_y, width - 20, height - 20], fill="white", outline="#e2e8f0")
    # Header row
    draw.rectangle([start_x, table_y, width - 20, table_y + 40], fill="#f7fafc")
    draw.text((start_x+15, table_y+12), "RECENT TRANSACTIONS", fill="#4a5568", font=font_small)
    
    # Rows
    for i in range(4):
        row_y = table_y + 50 + (i * 35)
        if row_y > height - 30: break
        draw.line([start_x, row_y, width-20, row_y], fill="#edf2f7", width=1)
        # Fake data blocks
        draw.rectangle([start_x+20, row_y-20, start_x+100, row_y-10], fill="#cbd5e0")
        draw.rectangle([start_x+150, row_y-20, start_x+250, row_y-10], fill="#e2e8f0")
        draw.rectangle([width-100, row_y-20, width-40, row_y-10], fill=theme_color)

    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/website/images')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, filename)
    image.save(output_path)
    print(f"Created advanced dashboard: {output_path}")

if __name__ == "__main__":
    # Student System - Blue theme
    create_advanced_dashboard("student_dashboard_v2.png", "Student Management System", "#3182ce")
    # Inventory System - Purple theme
    create_advanced_dashboard("inventory_dashboard_v2.png", "Inventory Management API", "#805ad5")
    # Hospital System - Teal/Green theme
    create_advanced_dashboard("hospital_dashboard_v2.png", "Hospital Management System", "#319795")
