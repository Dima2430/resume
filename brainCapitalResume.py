from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import inch
from reportlab.lib.colors import blue

def generate_brain_capital_resume(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=LETTER,
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=72)

    styles = getSampleStyleSheet()
    story = []

    # Create centered style for contact info
    centered_style = ParagraphStyle(
        name='Centered',
        parent=styles['Normal'],
        alignment=1,  # 1 = TA_CENTER
        spaceAfter=12
    )
    styles.add(centered_style)

    def add_paragraph(text, style="Normal"):
        story.append(Paragraph(text, styles[style]))
        story.append(Spacer(1, 0.2 * inch))

    # Add custom style for clickable links
    styles.add(ParagraphStyle(name='Link', parent=styles['Normal']))

    # Header - Centered contact information
    story.append(Paragraph("<b>Dmytro Volk</b>", ParagraphStyle(
        name='TitleCentered',
        parent=styles['Title'],
        alignment=1,
        spaceAfter=6
    )))
    
    contact_info = "Carretería 28, Málaga, Spain<br/>Phone: +380 97 7707021 | Email: dima.volkkom@gmail.com"
    story.append(Paragraph(contact_info, centered_style))
    story.append(Spacer(1, 0.3 * inch))

    # Education
    add_paragraph("<b>EDUCATION</b>", "Heading2")
    add_paragraph("<b>IU International University of Applied Sciences</b> – Remote<br/>Bachelor of Science in Computer Science | 2025 – 2027")

    # Work Experience
    add_paragraph("<b>WORK & LEADERSHIP EXPERIENCE</b>", "Heading2")
    
    add_paragraph("<b>Matching Story - Puzzle Games</b> – Remote<br/>Front-End Developer (Commercial Project) | Jan 2025<br/>"
                 "• Delivered five pixel-perfect, mobile-responsive UI sections based on Figma design<br/>"
                 "• Built using HTML, CSS, JavaScript; completed and shipped within 7 days<br/>"
                 "• GitHub: <a href='https://github.com/Dima2430/Matching-Story---Puzzle-Games' color='blue'>Matching Story</a> | "
                 "Live: <a href='https://dima2430.github.io/Matching-Story---Puzzle-Games/' color='blue'>Live Site</a>", "Link")
    
    add_paragraph("<b>Book Store</b> – Remote<br/>Team Lead | 2024<br/>"
                 "• Led development of a responsive two-page UI with dynamic book listings and animations<br/>"
                 "• Coordinated team contributions and ensured deployment via GitHub Pages<br/>"
                 "• GitHub: <a href='https://github.com/Dima2430/book.store' color='blue'>Book Store</a> | "
                 "Live: <a href='https://dima2430.github.io/book.store/' color='blue'>Live Site</a>", "Link")

    # Skills and Interests
    add_paragraph("<b>SKILLS, ACTIVITIES & INTERESTS</b>", "Heading2")
    add_paragraph("Languages: Ukrainian (Native), English (Upper-Intermediate)<br/>"
                 "Technical Skills: HTML, CSS, JavaScript, React, GitHub, REST APIs, Vercel, Figma<br/>"
                 "Certifications & Training: Full-Stack Web Developer – GoIT Bootcamp (2023–2024)<br/>"
                 "Interests: Building purposeful digital products, table tennis")

    doc.build(story)
    print(f"✅ Brain Capital resume saved as: {output_filename}")

generate_brain_capital_resume("Dmytro_Volk_Brain_Capital_CV.pdf")