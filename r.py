from fpdf import FPDF
from fpdf.enums import XPos, YPos

def sanitize(text):
    return text.replace("–", "-").replace("’", "'")

class PDF(FPDF):
    def add_clickable_links(self, github_url, live_url, h=6):
        self.set_font("Helvetica", size=10)
        self.set_text_color(0, 0, 255)  # Blue color for links
        
        # GitHub link
        self.write(h, "GitHub", github_url)
        
        # Separator
        self.set_text_color(0, 0, 0)  # Black color for separator
        self.cell(5, h, "|", align='C')
        
        # Live link
        self.set_text_color(0, 0, 255)  # Blue color for links
        self.write(h, "Live", live_url)
        
        # Reset styling
        self.set_text_color(0, 0, 0)
        self.set_font("Helvetica", size=12)
        self.ln(h + 2)

projects = [
    ("Book Store", "Team Lead", "HTML, CSS, JavaScript",
     "Built multi-page responsive e-commerce UI with routing, data handling, and animations.",
     "https://github.com/Dima2430/book.store", "https://dima2430.github.io/book.store/"),
    ("Vyshyvanka Vibes", "Footer + Menu Background Developer", "HTML, CSS",
     "Built responsive themed landing sections as part of a culturally styled team site.",
     "https://github.com/f0rd0101/Vyshyvanka-Vibes-Team---Unicodes-",
     "https://f0rd0101.github.io/Vyshyvanka-Vibes-Team---Unicodes-/"),
    ("Phonebook", "Developer", "React, Redux, Formik, Yup",
     "Created a contact manager with Redux state, form validation, and basic CRUD operations.",
     "https://github.com/Dima2430/goit-react-hw-07", "https://goit-react-hw-07-iota-seven.vercel.app/"),
    ("AQUATRACK", "'Add Water' Popup Developer", "React, Node.js, MongoDB, Express.js",
     "Implemented dynamic popup and contributed to backend integration in team project.",
     "https://github.com/Zymbsis/project-digitall3.0-r", "https://zymbsis.github.io/project-digitall3.0-r/")
]

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font("Helvetica", size=12)

# Header
pdf.set_font("Helvetica", 'B', 16)
pdf.cell(0, 10, "Dmytro Volk - Front-End Developer", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.set_font("Helvetica", '', 12)
pdf.cell(0, 8, "Remote | +380 97 7707021 | dima.volkkom@gmail.com", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.cell(0, 8, "GitHub: github.com/Dima2430 | LinkedIn: linkedin.com/in/dmytro-volk-7305b02a0", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.ln(10)

# Summary
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Summary", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)
pdf.multi_cell(0, 8, sanitize(
    "Ambitious front-end developer with hands-on experience building responsive, user-centric web applications. "
    "Skilled in HTML5, CSS3, JavaScript, React, and REST APIs. Proven ability to deliver production-ready code "
    "under real-world conditions. Passionate about clean design, performance optimization, and pushing beyond comfort zones."
))
pdf.ln(5)

# Work Experience
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Work Experience", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)
pdf.multi_cell(0, 8, sanitize(
    "Front-End Developer\n"
    "- Matching Story - Puzzle Games (Jan 2025)\n"
    "- Developed and deployed 5 production-grade sections (Hero, Header, Footer, About, Benefits) using HTML, CSS, and JavaScript.\n"
    "- Ensured responsiveness (desktop 1200px / mobile 320px) and pixel-perfect layout based on Figma design.\n"
    "- Delivered under a 7-day deadline and collaborated through GitHub.\n"
))
pdf.add_clickable_links(
    "https://github.com/Dima2430/Matching-Story---Puzzle-Games",
    "https://dima2430.github.io/Matching-Story---Puzzle-Games/"
)
pdf.ln(5)

# Academic Projects
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Academic Projects", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)

for name, role, stack, desc, gh, live in projects:
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 8, f"{sanitize(name)} | {sanitize(role)}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(0, 8, sanitize(stack), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.multi_cell(0, 8, sanitize(desc))
    
    # Use our new clickable links method
    pdf.add_clickable_links(gh, live)
    pdf.ln(3)

# Technical Skills
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Technical Skills", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)
pdf.multi_cell(0, 8, sanitize(
    "Languages: HTML5, CSS3, JavaScript\n"
    "Frameworks & Libraries: React, Redux\n"
    "Tools & Platforms: GitHub, REST APIs, Vercel, Figma\n"
    "Other: Responsive Design, Cross-browser Compatibility"
))
pdf.ln(5)

# Education
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Education", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)
pdf.multi_cell(0, 8, sanitize(
    "IU International University of Applied Sciences - Bachelor's in Computer Science (2024 - Present)\n"
    "GoIT - Fullstack Developer Certificate (2023 - 2024)"
))
pdf.ln(5)

# Languages
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Languages", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_font("Helvetica", '', 12)
pdf.multi_cell(0, 8, "English (Fluent), Ukrainian (Native)")

# Save PDF
pdf_output_path = "Dmytro_Volk_Resume.pdf"
pdf.output(pdf_output_path)

print(f"PDF successfully generated at: {pdf_output_path}")

# HTML Content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Dmytro Volk - Resume</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .container {{ max-width: 800px; margin: 0 auto; text-align: center; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .download-btn {{
            display: inline-block;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #0366d6;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Dmytro Volk</h1>
        <h2>Front-End Developer</h2>
        <p>Remote | +380 97 7707021 | dima.volkkom@gmail.com</p>
        
        <a href="Dmytro_Volk_Resume_Final.pdf" class="download-btn">
            Download Resume (PDF)
        </a>
        
        <p>Connect with me:</p>
        <p>
            <a href="https://github.com/Dima2430">GitHub</a> | 
            <a href="https://www.linkedin.com/in/dmytro-volk-7305b02a0">LinkedIn</a>
        </p>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("HTML page generated as index.html")