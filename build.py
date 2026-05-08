#!/usr/bin/env python3
"""Build all Study India HTML pages from a shared template."""
import os
from pathlib import Path

ROOT = Path(__file__).parent

# ---------- Shared fragments ----------
def base(depth):
    """Path prefix to repo root from a page at given depth."""
    return "../" * depth if depth else ""

def head(title, depth):
    p = base(depth)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Study India</title>
<meta name="description" content="STUDY INDIA — leading educational consultancy in India. Career guidance, admission consulting, placement support across 700+ universities.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{p}css/style.css">
<link rel="icon" type="image/png" href="{p}assets/study_logo.png">
</head>
<body>
"""

def topbar(depth):
    p = base(depth)
    return f"""<div class="topbar">
<div class="container">
<div class="top-info">
<a href="tel:+919789993666">📞 +91 9789993666</a>
<a href="tel:+919585552525">+91 9585552525</a>
<a href="mailto:enquiry@studyindiaedu.com">✉ enquiry@studyindiaedu.com</a>
</div>
<div class="top-social">
<a href="#" aria-label="Facebook">Facebook</a>
<a href="#" aria-label="Instagram">Instagram</a>
<a href="#" aria-label="LinkedIn">LinkedIn</a>
<a href="#" aria-label="YouTube">YouTube</a>
</div>
</div>
</div>
"""

COURSES = [
    ("Engineering", "engineer"),
    ("Medical", "medical"),
    ("MBBS / BDS", "mbbs"),
    ("Nursing", "nursing"),
    ("Pharmacy", "pharmacy"),
    ("Allied Health Science", "allied-health"),
    ("Law", "law"),
    ("Agricultural Sciences", "agriculture"),
    ("Art and Science", "art-science"),
    ("Management", "management"),
    ("Architecture", "architecture"),
    ("Marine", "marine"),
    ("Physiotherapy & Occupational Therapy", "physiotherapy-and-occupational-therapi"),
]

COLLEGES = [
    ("Top Medical Colleges", "top-medical-collegse"),
    ("Top Dental Colleges", "top-dental-collegse"),
    ("Top Engineering Colleges", "top-engineering-collegse"),
    ("Deemed Universities", "deemed-universites"),
    ("B-School (Business School)", "b-school"),
    ("Marine Colleges", "marine-colleges"),
    ("Architecture Colleges", "architecture-colleges"),
    ("Arts & Science Colleges", "art-and-science-colleges"),
]

def header(depth, active=""):
    p = base(depth)
    courses_dd = "".join(
        f'<a href="{p}courses/{slug}/">{name}</a>' for name, slug in COURSES
    )
    colleges_dd = "".join(
        f'<a href="{p}colleges/{slug}/">{name}</a>' for name, slug in COLLEGES
    )
    def cls(name):
        return ' style="background:var(--bg-soft);color:var(--brand-blue);"' if name == active else ""
    return f"""<header class="site-header">
<div class="container">
<div class="header-inner">
<a href="{p}" class="logo" aria-label="Study India home">
<img src="{p}assets/study_logo.png" alt="Study India">
</a>
<nav class="main-nav" aria-label="Primary">
<a href="{p}about/"{cls('about')}>About</a>
<a href="{p}services/"{cls('services')}>Services</a>
<div class="has-dropdown">
<a href="#"{cls('courses')}>Courses</a>
<div class="dropdown">{courses_dd}</div>
</div>
<div class="has-dropdown">
<a href="#"{cls('colleges')}>Colleges</a>
<div class="dropdown">{colleges_dd}</div>
</div>
<a href="{p}team/"{cls('team')}>Team</a>
<a href="{p}contact/"{cls('contact')}>Contact</a>
<a href="#" class="cta-btn header-cta" data-open-modal="enquire">Enquire Now</a>
</nav>
<button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
</button>
</div>
</div>
</header>
<a href="#" class="enquire-side" data-open-modal="enquire">Enquire Now</a>
<a href="https://wa.me/919789993666" class="whatsapp-float" aria-label="WhatsApp" target="_blank" rel="noopener">
<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>
"""

def footer(depth):
    p = base(depth)
    return f"""<footer class="site-footer">
<div class="container">
<div class="footer-grid">
<div>
<div class="footer-logo"><img src="{p}assets/study_logo.png" alt="Study India"></div>
<p>STUDY INDIA is a leading educational consultancy with over a decade of experience in career guidance, admission counselling and placement support across 700+ partner universities.</p>
<div class="footer-social">
<a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg></a>
<a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a>
<a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/></svg></a>
<a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg></a>
</div>
</div>
<div>
<h4>Quick Links</h4>
<ul>
<li><a href="{p}about/">About Us</a></li>
<li><a href="{p}services/">Services</a></li>
<li><a href="{p}team/">Our Team</a></li>
<li><a href="{p}contact/">Contact</a></li>
<li><a href="#" data-open-modal="enquire">Enquire Now</a></li>
</ul>
</div>
<div>
<h4>Top Courses</h4>
<ul>
<li><a href="{p}courses/mbbs/">MBBS / BDS</a></li>
<li><a href="{p}courses/engineer/">Engineering</a></li>
<li><a href="{p}courses/management/">Management</a></li>
<li><a href="{p}courses/nursing/">Nursing</a></li>
<li><a href="{p}courses/law/">Law</a></li>
</ul>
</div>
<div>
<h4>Reach Us</h4>
<p style="color:#cbd5e1;font-size:.92rem;line-height:1.7">
49/24, 4th Ave, Sarvamangala Colony,<br>
Sri Devi Colony, Ashok Nagar,<br>
Chennai, Tamil Nadu 600083
</p>
<p style="margin-top:14px"><a href="tel:+919789993666">+91 9789993666</a><br>
<a href="tel:+919585552525">+91 9585552525</a><br>
<a href="tel:+919976908140">+91 9976908140</a></p>
<p><a href="mailto:enquiry@studyindiaedu.com">enquiry@studyindiaedu.com</a></p>
</div>
</div>
<div class="footer-bottom">
<div>© <span id="year">2025</span> Study India. All Rights Reserved.</div>
<div class="links">
<a href="#">Terms of Use</a>
<a href="#">Privacy Policy</a>
<a href="#">Login</a>
</div>
</div>
</div>
</footer>
"""

def modal():
    return """<div class="modal-backdrop" id="enquire-modal" role="dialog" aria-modal="true" aria-labelledby="enquire-title">
<div class="modal">
<button class="modal-close" aria-label="Close">×</button>
<h2 id="enquire-title">Enquire Now</h2>
<p>Tell us a bit about yourself and our counsellor will get in touch.</p>
<form data-stub>
<div class="form-row full"><input class="form-control" name="name" placeholder="Your full name" required></div>
<div class="form-row">
<input class="form-control" name="email" type="email" placeholder="Email" required>
<input class="form-control" name="phone" type="tel" placeholder="Phone" required>
</div>
<div class="form-row full">
<select class="form-control" name="course" required>
<option value="">Course of interest</option>
<option>MBBS / BDS</option><option>Engineering</option><option>Management</option>
<option>Nursing</option><option>Pharmacy</option><option>Law</option>
<option>Agriculture</option><option>Architecture</option><option>Allied Health</option>
<option>Art &amp; Science</option><option>Marine</option><option>Other</option>
</select>
</div>
<div class="form-row full"><textarea class="form-control" name="message" placeholder="Your message (optional)"></textarea></div>
<button class="cta-btn" type="submit" style="width:100%">Submit Enquiry</button>
</form>
</div>
</div>
"""

def scripts(depth):
    p = base(depth)
    return f"""<script src="{p}js/script.js"></script>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>"""

# ---------- Page bodies ----------
HOME = """<section class="hero">
<div class="container">
<div class="hero-grid">
<div>
<span style="display:inline-block;background:rgba(255,255,255,.15);color:#fff;padding:6px 14px;border-radius:999px;font-size:.85rem;font-weight:600;margin-bottom:18px;">🎓 Trusted by 50,000+ students</span>
<h1>Welcome to <span style="color:var(--brand-yellow)">Study India</span></h1>
<p>We offer 100% assurance in top universities all over India. Career guidance, admission consulting and placement support — all under one roof.</p>
<div class="btn-row">
<a href="#" class="cta-btn" data-open-modal="enquire">Enquire Now</a>
<a href="about/" class="btn-outline" style="color:#fff;border-color:#fff;">Learn More</a>
</div>
<div class="hero-stats">
<div><div class="stat-num">2010</div><div class="stat-label">Established</div></div>
<div><div class="stat-num">100%</div><div class="stat-label">Assurance in top universities</div></div>
<div><div class="stat-num"><span data-count="50000">0</span>+</div><div class="stat-label">Students</div></div>
</div>
</div>
<div class="hero-image">
<img src="assets/home-img.png" alt="Study India" onerror="this.src='assets/home-banner-3.jpg';this.style.aspectRatio='4/5';this.style.objectFit='cover';">
</div>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-head">
<span class="eyebrow">What We Do</span>
<h2>Career Guidance &amp; Admission Consulting<br>For Higher Education</h2>
<p>Expert career guidance for better college prospects — helping you choose a career of your choice, live a happy and prosperous life, and earn a good income to support yourself and your loved ones.</p>
</div>
<div class="grid grid-3">
<div class="card"><div class="card-icon">🎯</div><h3>Right Career Path</h3><p>Helps you choose a career of your choice that aligns with your strengths, ambitions and the demands of tomorrow's workplace.</p></div>
<div class="card"><div class="card-icon">🌟</div><h3>Happy &amp; Prosperous Life</h3><p>The right course at the right institution sets the foundation for a fulfilling career and a prosperous life ahead.</p></div>
<div class="card"><div class="card-icon">💰</div><h3>Strong Earning Potential</h3><p>Earn a good income to support yourself and your loved ones — backed by a degree from a recognised top university.</p></div>
</div>
</div>
</section>

<section class="stats-band">
<div class="container">
<div class="section-head" style="color:#fff;margin-bottom:40px"><h2 style="color:#fff">Why Choose Study India?</h2></div>
<div class="grid grid-4">
<div class="stat-item"><div class="num"><span data-count="100">0</span>%</div><div class="label">Career Guidance</div></div>
<div class="stat-item"><div class="num"><span data-count="400">0</span>+</div><div class="label">Partner Universities</div></div>
<div class="stat-item"><div class="num"><span data-count="3000">0</span>+</div><div class="label">Success Stories</div></div>
<div class="stat-item"><div class="num"><span data-count="99">0</span>%</div><div class="label">Success Rate</div></div>
</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="section-head"><span class="eyebrow">Explore Programs</span><h2>Discover Your Study Dream with Us</h2></div>
<div class="grid grid-4">
__COURSE_TILES__
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">Top Institutions</span><h2>Find Your Dream College</h2></div>
<div class="grid grid-4">
__COLLEGE_TILES__
</div>
<div class="text-center mt-3"><a href="#" class="cta-btn" data-open-modal="enquire">Click Here to Apply</a></div>
</div>
</section>

<section class="stats-band">
<div class="container">
<div class="section-head" style="color:#fff;margin-bottom:40px"><h2 style="color:#fff">Study India gives wings to your ambition</h2></div>
<div class="grid grid-4">
<div class="stat-item"><div class="num"><span data-count="5000">0</span>+</div><div class="label">Students Enrolled</div></div>
<div class="stat-item"><div class="num"><span data-count="8000">0</span>+</div><div class="label">Course Options</div></div>
<div class="stat-item"><div class="num"><span data-count="700">0</span>+</div><div class="label">Top Universities</div></div>
<div class="stat-item"><div class="num"><span data-count="15">0</span>+</div><div class="label">Awards Achieved</div></div>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">Our Process</span><h2>How It Works</h2><p>Four simple steps from exploration to admission letter.</p></div>
<div class="steps">
<div class="step"><h3>Explore Options</h3><p>We support your exploration of every available institute option for the course of your choice — under one roof.</p></div>
<div class="step"><h3>Admission Guidance</h3><p>Expert guidance based on your profile, area of interest, academic scores, budget and preferred location.</p></div>
<div class="step"><h3>Application Process</h3><p>Process your application at the institute of your choice as per the given admission procedure.</p></div>
<div class="step"><h3>Secure Admission</h3><p>Secure your admission letter in your choice of course and institute — and start your journey.</p></div>
</div>
<div class="text-center mt-3"><a href="about/" class="btn-outline">More About Us</a></div>
</div>
</section>
"""

# Course tiles for home
def course_tiles_html():
    tiles = []
    course_data = [
        ("Medical", "medical", "assets/bg/medical.jpg"),
        ("Engineering", "engineer", "assets/bg/engineer.jpg"),
        ("Management", "management", "assets/bg/manager.jpg"),
        ("Law", "law", "assets/bg/law.jpg"),
        ("MBBS / BDS", "mbbs", "assets/bg/mbbs.jpg"),
        ("Agriculture", "agriculture", "assets/bg/agri.jpg"),
        ("Allied Health", "allied-health", "assets/bg/allied.jpg"),
        ("Art &amp; Science", "art-science", "assets/bg/art.jpg"),
        ("Marine", "marine", "assets/bg/marine.jpg"),
        ("Architecture", "architecture", "assets/bg/archi (2).jpg"),
        ("Nursing", "nursing", "assets/placement.jpg"),
        ("Pharmacy", "pharmacy", "assets/library.jpg"),
    ]
    for name, slug, img in course_data:
        tiles.append(f'<a href="courses/{slug}/" class="tile"><div class="tile-img"><img src="{img}" alt="{name}" loading="lazy"></div><div class="tile-body"><h3>{name}</h3><p>Top universities, expert guidance and admission support across India.</p><span class="tile-link">Explore</span></div></a>')
    return "\n".join(tiles)

def college_tiles_html():
    tiles = []
    college_data = [
        ("Top Medical Colleges", "top-medical-collegse", "assets/course/medical2.png"),
        ("Top Dental Colleges", "top-dental-collegse", "assets/course/dental.png"),
        ("Deemed Universities", "deemed-universites", "assets/course/deemed.png"),
        ("Art &amp; Science Colleges", "art-and-science-colleges", "assets/course/artandscience.png"),
        ("Architecture Colleges", "architecture-colleges", "assets/course/architect.png"),
        ("Top Engineering Colleges", "top-engineering-collegse", "assets/course/engineer.png"),
        ("Marine Colleges", "marine-colleges", "assets/course/marine.png"),
        ("B-School (Business)", "b-school", "assets/bg/manager.jpg"),
    ]
    for name, slug, img in college_data:
        tiles.append(f'<a href="colleges/{slug}/" class="tile"><div class="tile-img"><img src="{img}" alt="{name}" loading="lazy"></div><div class="tile-body"><h3>{name}</h3><p>Discover top colleges with strong reputations and excellent placement records.</p><span class="tile-link">Explore</span></div></a>')
    return "\n".join(tiles)

def assemble(title, depth, body, active=""):
    return head(title, depth) + topbar(depth) + header(depth, active) + body + footer(depth) + modal() + scripts(depth)

def write(rel_path, content):
    full = ROOT / rel_path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content)
    print(f"  wrote {rel_path}")

# ---------- Build home ----------
home_body = HOME.replace("__COURSE_TILES__", course_tiles_html()).replace("__COLLEGE_TILES__", college_tiles_html())
write("index.html", assemble("Home — Career Starts Here", 0, home_body))

# ---------- About ----------
ABOUT = """<section class="page-banner bg-about"><div class="container"><h1>About Study India</h1><div class="breadcrumb"><a href="../">Home</a><span>/</span>About</div></div></section>

<section>
<div class="container">
<div class="split">
<img src="../assets/about-img.jpg" alt="About Study India">
<div>
<span class="eyebrow" style="color:var(--brand-blue);font-weight:700;text-transform:uppercase;letter-spacing:1.5px;font-size:.85rem">Who We Are</span>
<h2>Study India</h2>
<p>STUDY INDIA is a leading Educational Consultancy in India, with 15 years of experience across various parts of the education field including career guidance, admission guidance and placement assistance.</p>
<p>We continually monitor the education field by observing the current situations of market strategy and its growth, and advise students to choose the right career path to achieve their successive goals.</p>
<a href="../contact/" class="cta-btn">Get In Touch</a>
</div>
</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="grid grid-3">
<div class="card"><div class="card-icon">🎯</div><h3>Vision</h3><p>To emerge as a World-Class University in creating and disseminating knowledge and providing students a unique learning experience in Science, Technology, Medicine, Management and other areas of scholarship that will best serve the world and for the betterment of mankind.</p></div>
<div class="card"><div class="card-icon">🚀</div><h3>Mission</h3><p>MOVE UP through international alliances and collaborative initiatives to achieve global excellence. ACCOMPLISH A PROCESS to advance knowledge in a rigorous academic and research environment. ATTRACT AND BUILD PEOPLE in a rewarding and inspiring environment fostering freedom, empowerment, creativity and innovation.</p></div>
<div class="card"><div class="card-icon">⭐</div><h3>Core Values</h3><p>Excellence, Integrity and Academic Freedom; Global Vision and Local Commitment; Inclusiveness, Diversity and Respect — these guide every interaction and decision we make on behalf of our students.</p></div>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">Our Values In Detail</span><h2>What We Stand For</h2></div>
<div class="grid grid-3">
<div class="card"><h3>Excellence, Integrity and Academic Freedom</h3><p>The University is committed to being a leading player in the academic world through excellence in teaching and research, while placing utmost value on the freedom to conduct academic activities subject to the highest standards of academic integrity.</p></div>
<div class="card"><h3>Global Vision and Local Commitment</h3><p>Study India brings together global thought leaders to make significant contributions to the economic and social development both locally and nationally. We encourage faculty, staff and students to dedicate themselves to serve the local community.</p></div>
<div class="card"><h3>Inclusiveness, Diversity and Respect</h3><p>We value and respect the differences of individuals — whether they are from different geographies, socio-economic status, cultural backgrounds or religions — fostering an inclusive and caring environment.</p></div>
</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="section-head"><h2>Empowering Educational Journeys with STUDY INDIA</h2></div>
<p style="max-width:900px;margin:0 auto 30px;text-align:center;color:var(--text-muted);font-size:1.05rem">STUDY INDIA stands as a premier Educational Consultancy in India, boasting a decade of expertise across diverse educational domains. With a steadfast commitment to excellence, we offer comprehensive services including Career Guidance, Admission Assistance and Placement Support. Our extensive experience allows us to navigate the dynamic landscape of the education sector, continually assessing market trends and growth strategies. We are dedicated to empowering students to make informed decisions about their future.</p>
<div class="grid grid-4">
<div class="stat-item"><div class="num" style="color:var(--brand-blue)"><span data-count="5000">0</span>+</div><div class="label" style="color:var(--text-muted)">Students Enrolled</div></div>
<div class="stat-item"><div class="num" style="color:var(--brand-blue)"><span data-count="8000">0</span>+</div><div class="label" style="color:var(--text-muted)">Course Options</div></div>
<div class="stat-item"><div class="num" style="color:var(--brand-blue)"><span data-count="700">0</span>+</div><div class="label" style="color:var(--text-muted)">Top Universities</div></div>
<div class="stat-item"><div class="num" style="color:var(--brand-blue)"><span data-count="15">0</span>+</div><div class="label" style="color:var(--text-muted)">Awards Achieved</div></div>
</div>
</div>
</section>
"""
write("about/index.html", assemble("About", 1, ABOUT, "about"))

# ---------- Services ----------
SERVICES_LIST = [
    ("Career guidance", "Personalised guidance to help you choose a career that fits your interests, strengths and ambitions."),
    ("Entrance Exam Information", "Up-to-date details on every major entrance exam — eligibility, dates and prep strategies."),
    ("Application Process", "End-to-end assistance with applications across hundreds of partner institutions."),
    ("Special Education Planning", "Customised academic plans for students with specific learning needs and goals."),
    ("Motivational Counselling", "Confidence-building sessions to keep students focused and resilient through the journey."),
    ("Psychological Advice", "Professional counselling support for stress, decision-making and goal setting."),
    ("Bank Loan Assistance", "Help you connect with the right financial institutions for education loans."),
    ("Scholarship Information", "Stay updated on scholarships you may qualify for — never miss an opportunity."),
    ("Local Guardianship Assistance", "Trusted guardian network for students studying away from home."),
    ("Performance Follow-up", "Continuing support and tracking of student performance even after admission."),
]
services_cards = "".join(
    f'<div class="card"><div class="card-icon">✓</div><h3>{name}</h3><p>{desc}</p></div>'
    for name, desc in SERVICES_LIST
)
SERVICES = f"""<section class="page-banner bg-services"><div class="container"><h1>Services</h1><div class="breadcrumb"><a href="../">Home</a><span>/</span>Services</div></div></section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">What We Offer</span><h2>Make Smart Decisions with Study India</h2><p>End-to-end services that take you from career exploration to a confirmed seat at your dream institution.</p></div>
<div class="grid grid-3">{services_cards}</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="section-head"><span class="eyebrow">Terms</span><h2>How We Work</h2></div>
<p style="max-width:900px;margin:0 auto 36px;text-align:center;color:var(--text-muted);font-size:1.05rem">At STUDY INDIA, our commitment lies in delivering services imbued with ethical and moral principles, rooted in our dedication to serving humanity. We operate with integrity, ensuring our services are provided solely for a service charge, without any involvement in cash handling at our premises.</p>
<div class="grid grid-3">
<div class="card"><div class="card-icon">🤝</div><h3>Ethical Service Commitment</h3><p>STUDY INDIA always delivers services with ethical and moral values to serve on a humanity basis. Our principles are non-negotiable.</p></div>
<div class="card"><div class="card-icon">💼</div><h3>Service Charge Only</h3><p>We charge only for services rendered. No hidden fees, no commissions in disguise — fair and transparent pricing always.</p></div>
<div class="card"><div class="card-icon">🛡️</div><h3>No Cash Handling</h3><p>No cash handling is done at our premises. All transactions are routed through legitimate, traceable channels for your safety.</p></div>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">Highlights</span><h2>Where We Go the Extra Mile</h2></div>
<div class="grid grid-3">
<div class="card"><h3>Low Marks &amp; Just-Pass</h3><p>Don't lose hope with average scores. We have pathways for students with low marks or just-pass results — there is always an option.</p></div>
<div class="card"><h3>40% Marks MBBS, BDS</h3><p>Yes — admission to MBBS and BDS programs is possible with 40% marks. Talk to our counsellors about your eligibility.</p></div>
<div class="card"><h3>College Transfer Support</h3><p>Looking to switch colleges mid-program? We help with the paperwork and the placement at a more suitable institute.</p></div>
<div class="card"><h3>SC/ST Quota — Free Admissions</h3><p>Free admissions for eligible SC/ST quota candidates with full guidance through the documentation and application process.</p></div>
<div class="card"><h3>Management / NRI Quota</h3><p>Specialist counselling for management and NRI quota seats — we help you understand the full cost and the right institutions.</p></div>
<div class="card"><h3>Entrance Exam Alerts</h3><p>Real-time alerts for entrance exams, application windows and admission procedures across India.</p></div>
</div>
</div>
</section>
"""
write("services/index.html", assemble("Services", 1, SERVICES, "services"))

# ---------- Team ----------
TEAM = """<section class="page-banner bg-team"><div class="container"><h1>Our Team</h1><div class="breadcrumb"><a href="../">Home</a><span>/</span>Team</div></div></section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">Leadership</span><h2>Meet the People Behind Study India</h2><p>A team that brings decades of combined expertise in education consulting, admissions and student mentorship.</p></div>
<div class="team-grid">
<div class="team-card"><img src="../assets/ceo.jpeg" alt="Founder & CEO" onerror="this.src='../assets/ceo1.jpeg'"><div class="body"><div class="role">Founder &amp; C.E.O</div><h3>Kuppuraj @ Sampath</h3></div></div>
<div class="team-card"><img src="../assets/director-1.jpeg" alt="Director" onerror="this.src='../assets/director-11.jpeg'"><div class="body"><div class="role">Director</div><h3>Aravinth Kumar</h3></div></div>
<div class="team-card"><img src="../assets/director-2.jpeg" alt="Director" onerror="this.src='../assets/director-21.jpeg'"><div class="body"><div class="role">Director</div><h3>Karthikeya</h3></div></div>
</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="section-head"><h2>Why Our Team Stands Out</h2></div>
<div class="grid grid-3">
<div class="card"><div class="card-icon">🎓</div><h3>15+ Years of Experience</h3><p>Decades of combined experience across career guidance, admission counselling and placement support.</p></div>
<div class="card"><div class="card-icon">🤝</div><h3>Personalised Approach</h3><p>Every student is unique. Our counsellors craft a path tailored to each student's strengths and ambitions.</p></div>
<div class="card"><div class="card-icon">🌐</div><h3>700+ University Network</h3><p>Direct relationships with 700+ partner universities across India give students real options.</p></div>
</div>
</div>
</section>
"""
write("team/index.html", assemble("Our Team", 1, TEAM, "team"))

# ---------- Contact ----------
CONTACT = """<section class="page-banner bg-contact"><div class="container"><h1>Contact Us</h1><div class="breadcrumb"><a href="../">Home</a><span>/</span>Contact</div></div></section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">How To Reach Us</span><h2>We'd Love to Hear From You</h2><p>Reach out for a free counselling session — our team will get back to you within 24 hours.</p></div>
<div class="contact-grid">
<div class="contact-card"><div class="icon">📍</div><h3>Address</h3><p>49/24, 4th Ave, Sarvamangala Colony, Sri Devi Colony, Ashok Nagar, Chennai, Tamil Nadu 600083</p></div>
<div class="contact-card"><div class="icon">📞</div><h3>Call Us</h3><p><a href="tel:+919789993666">+91 9789993666</a><br><a href="tel:+919585552525">+91 9585552525</a><br><a href="tel:+919976908140">+91 9976908140</a></p></div>
<div class="contact-card"><div class="icon">✉</div><h3>Email Us</h3><p><a href="mailto:enquiry@studyindiaedu.com">enquiry@studyindiaedu.com</a></p></div>
</div>

<div class="form-card">
<h2 style="margin-bottom:8px">Send a Message</h2>
<p style="color:var(--text-muted);margin-bottom:26px">Fill out the form and our admission counsellor will get in touch.</p>
<form data-stub>
<div class="form-row">
<input class="form-control" name="name" placeholder="Full name" required>
<input class="form-control" name="email" type="email" placeholder="Email address" required>
</div>
<div class="form-row">
<input class="form-control" name="phone" type="tel" placeholder="Phone number" required>
<input class="form-control" name="city" placeholder="City">
</div>
<div class="form-row full">
<select class="form-control" name="course" required>
<option value="">Select course of interest</option>
<option>MBBS / BDS</option><option>Engineering</option><option>Management</option>
<option>Nursing</option><option>Pharmacy</option><option>Law</option>
<option>Agriculture</option><option>Architecture</option><option>Allied Health</option>
<option>Art &amp; Science</option><option>Marine</option><option>Other</option>
</select>
</div>
<div class="form-row full"><textarea class="form-control" name="message" placeholder="Tell us a bit more about what you're looking for..."></textarea></div>
<button class="cta-btn" type="submit">Submit Enquiry</button>
</form>
</div>
</div>
</section>
"""
write("contact/index.html", assemble("Contact Us", 1, CONTACT, "contact"))

# ---------- Course pages ----------
COURSE_CONTENT = {
    "engineer": {
        "title": "Engineering",
        "tagline": "Engineering is part of STEM education",
        "intro": [
            "Engineering is a stream of education that involves the application of Science, Technology and Mathematics to innovate, design, develop and maintain machines, structures, software, hardware and systems &amp; processes.",
            "The engineering field offers a range of career opportunities across all industries and engages students with science, technology, engineering and mathematics. Engineers are involved in the design, evaluation, development, testing, modification, inspection and maintenance of a wide range of products, structures and systems.",
        ],
        "eligibility": "The criteria of eligibility for taking admission in engineering courses vary from institute to institute. However, one of the basic conditions is that students must have passed Class 12 with Physics, Chemistry and Mathematics as core subjects.",
        "popular_heading": "Popular Engineering Courses",
        "popular_lead": "Engineering programs in India are offered at the undergraduate (UG), postgraduate, and Ph.D. levels:",
        "popular": [
            ("BE / BTech", "Class 12 from a recognised board with Physics, Chemistry and Mathematics, with a minimum aggregate of 60%."),
            ("ME / MTech", "Completed BE/BTech with a valid GATE score is required for ME/MTech programs."),
            ("Diploma", "Passed SSLC / Class 10 / equivalent with at least 45% in Science and Maths."),
            ("PhD", "Minimum 55% marks or 5.5 CPI in BTech/MTech or equivalent in appropriate branches."),
        ],
        "exams": "Some popular engineering exams in India: JEE Main / Advanced, MHT CET, UPCET (UPSEE), BCECE, AP EAMCET, TS EAMCET, BITSAT, KEAM, SRMJEEE, MET, SAEEE, WBJEE, LPU NEST and more.",
        "feature_course": ("BTech (Bachelor of Technology)", "BTech is a four-year professional engineering program spread over eight semesters. Bachelor of Technology is the full form of B.Tech, a highly preferred undergraduate course in India and a gateway to the field of engineering. B.Tech graduates have strong careers as Mechanical Engineers, Electrical Engineers, Software Engineers, consultants, managers and researchers."),
        "image": "bg/engineer.jpg",
    },
    "medical": {
        "title": "Medical",
        "tagline": "Medicine is one of the most valued and well-respected professions",
        "intro": [
            "India is becoming a hub for medical education with a host of medical courses available for aspiring doctors. Being a health professional is a difficult but rewarding career — soft skills like empathy, communication and cooperation are essential.",
            "Medicine and Health degrees include subdisciplines such as Biomedicine, Public Health, Human Medicine, Veterinary Medicine, Dentistry, Nursing, Health Management and Nutrition. Graduates enter careers as surgeons, medical technicians, psychiatrists, nurses, nutritionists, veterinary doctors and more.",
        ],
        "eligibility": "Students who have studied PCB (Physics, Chemistry, Biology) in Class 12 and secured a minimum 50% aggregate are eligible for medical courses. NEET is one of the prime entrance exams for MBBS admission and other medical courses.",
        "popular_heading": "Popular Medical Courses",
        "popular_lead": "Medical courses include MBBS, MD, BAMS, MS, BHMS, BDS — top professional choices after Class 12.",
        "popular": [
            ("MBBS", "Class 12 with Physics, Chemistry and Biology with minimum aggregate marks of 40-50%."),
            ("BHMS", "Class 12 with Physics, Chemistry, Biology and English with minimum 50% aggregate."),
            ("BAMS", "Class 12 with Physics, Chemistry, Biology and English with minimum 50% aggregate."),
            ("BDS / VET / Naturopathy", "Class 12 with PCB and English with minimum 50% aggregate."),
        ],
        "exams": "Popular medical entrance exams: NEET, NEET PG, NEET MDS, USMLE, MCAT, FPMT, JIPMER, AIIMS-MBBS, OJEE, CMSE, FMGE, NEET SS, AIAPGET and more.",
        "feature_course": ("MBBS (Bachelor of Medicine &amp; Bachelor of Surgery)", "MBBS is a 5½-year undergraduate program covering Clinical, Pre-clinical and Para-clinical subjects. Students get both Bachelor of Medicine and Bachelor of Surgery degrees and complete a 1-year mandatory internship after 4.5 years of theory."),
        "image": "bg/medical.jpg",
    },
    "mbbs": {
        "title": "MBBS / BDS",
        "tagline": "MBBS / BDS is one of the most valued and well-respected professions",
        "intro": [
            "Embarking on the journey of MBBS/BDS studies signifies stepping into one of the most esteemed and revered professions, where the pursuit of healing meets utmost respect. India emerges as a pivotal destination for medical education, offering a plethora of courses catering to aspiring doctors.",
            "Venturing into healthcare is both challenging and fulfilling, demanding a blend of technical expertise and soft skills like compassion, effective communication and collaboration. Aspiring candidates must approach their education with sincerity, recognising the responsibility they bear in serving the nation's people.",
        ],
        "eligibility": "Students who have completed Class 12 with PCB (Physics, Chemistry, Biology) and obtained a minimum 50% aggregate are eligible to apply. NEET serves as the primary entrance exam for MBBS programs and other related medical courses.",
        "popular_heading": "Popular MBBS / BDS Courses",
        "popular_lead": "Top medical courses include MBBS, MD, BAMS, MS, BHMS, BDS — spanning medical, biomedical, paramedical sciences, pharmacy, nursing and allied health.",
        "popular": [
            ("MBBS", "Class 12 with Physics, Chemistry and Biology with minimum 40-50% aggregate."),
            ("MD", "MBBS from a recognised institute plus a 1-year internship with at least 50% aggregate."),
            ("MS", "Minimum 50-60% in UG along with a valid GATE score."),
            ("BDS", "Class 12 with PCB and English with at least 50% aggregate."),
        ],
        "exams": "Prominent medical entrance exams: NEET, NEET PG, NEET MDS, USMLE, MCAT, JIPMER, AIIMS-MBBS, OJEE, CMSE, FMGE, NEET SS, AIAPGET.",
        "feature_course": ("MBBS (Bachelor of Medicine &amp; Bachelor of Surgery)", "MBBS is one of the predominant medical graduate degrees for becoming a doctor — a 5-year and 6-month long undergraduate program."),
        "image": "bg/mbbs.jpg",
    },
    "nursing": {
        "title": "Nursing",
        "tagline": "Nursing is referred to as the noble profession",
        "intro": [
            "Nursing professionals play a prominent role across hospitals and healthcare sectors. Focused on the care of individuals and families, nursing is an important part of healthcare. Nurses are often the second touchpoint for a patient after doctors.",
            "Nursing is among the noblest and oldest occupations, requiring time and energy devoted to sick and needy patients. It combines physical healing with mental assistance to patients and their families. Students can pursue a nursing course at the diploma, undergraduate, postgraduate and certification levels.",
        ],
        "eligibility": "The basic eligibility criteria to pursue any nursing course is to score 40-55% marks in 10+2 (Biology, Chemistry, Physics and Mathematics). Other prerequisites include state nursing council registration (for B.Sc Nursing Post Basic and M.Sc Nursing) and at least 1 year of work experience (for M.Sc Nursing).",
        "popular_heading": "Popular Nursing Courses",
        "popular_lead": "Top Nursing Courses after Class 12: B.Sc Nursing, GNM, ANM, M.Sc Nursing and 1-year Diploma in Nursing.",
        "popular": [
            ("GNM", "Class 12 with English as a subject and more than 40% aggregate."),
            ("P.B.B.Sc", "Qualified GNM after 10+2 with Science (PCB) with 50% aggregate."),
            ("B.Sc Nursing", "10+2 with Science (PCB) and English with 45% aggregate from a recognised board."),
            ("M.Sc Nursing", "B.Sc Nursing / Hons / Post Basic B.Sc Nursing with minimum 55% from an Indian Nursing Council recognised institution."),
        ],
        "exams": "Popular nursing entrance exams: NEET, SAAT, AIIMS B.Sc Nursing, DSAT, ITM NEST, PGIMER B.Sc/M.Sc Nursing, CMC Ludhiana B.Sc Nursing, Indian Army Nursing, JIPMER Nursing, KGMU Nursing, RUHS Nursing.",
        "feature_course": ("GNM (General Nursing and Midwifery)", "GNM is a 3-year diploma course followed by 6 months of mandatory internship. GNM nurses practice in niche segments like maternity care, post-trauma, rehabilitation, mental care and data collection. The curriculum covers all aspects of nursing care, enabling candidates to address the health needs of individuals, communities and the country."),
        "image": "placement.jpg",
    },
    "pharmacy": {
        "title": "Pharmacy",
        "tagline": "Pharmaceutical science is one of the leading industries today",
        "intro": [
            "Pharmacy is one of the most opted professional courses in India. The rapidly growing pharmaceutical industry and pharmaceutical research have attracted aspirants to take pharmacy as a career — gaining intense knowledge about production, dosage, dispensing and other information related to medicines.",
            "Pharmacy courses deal with subjects like biology, medicine and chemistry, offering foundational knowledge to develop pharmaceutical drugs for safe and effective use in healthcare. The pharmaceutical industry in India is growing at a rapid pace, demonstrating the influx of students enrolling in pharmacy courses.",
        ],
        "eligibility": "The eligibility criteria is to study Physics, Chemistry and Biology in Class 12 and secure more than 50% marks. For postgraduate and PhD level courses, students must complete graduation and postgraduation in Pharmacy.",
        "popular_heading": "Popular Pharmacy Courses",
        "popular_lead": "Pharmacy is offered at undergraduate, postgraduate and doctoral levels. Popular options include B.Pharm, M.Pharm and Diploma in Pharmacy.",
        "popular": [
            ("Diploma in Pharmacy (D.Pharm)", "Class 12 with Physics, Chemistry, Biology and Mathematics."),
            ("Bachelor in Pharmacy (B.Pharm)", "Higher education from a national or state board with Physics, Chemistry, Mathematics or Biology and English."),
            ("Master of Pharmacy (M.Pharm)", "Completed B.Pharm with minimum qualifying marks from a college approved by the Pharmacy Council of India (PCI)."),
        ],
        "exams": "Popular pharmacy entrance exams: GPAT, NIPER JEE, NMIMS NPAT, RUHS Pharmacy, CG PPHT, GITAM GAT, MET, Delhi CET, KCET.",
        "feature_course": ("D.Pharm (Diploma in Pharmacy)", "D.Pharm is a two-year, entry-level certificate course on the science and art of preparing and dispensing medicines. Students gain knowledge of basic pharmacy education including chemistry, biochemistry, pharmacology and toxicology — leading to careers as Clinical Pharmacists, Pharmacologists and Clinical Research Associates (CRA)."),
        "image": "library.jpg",
    },
    "allied-health": {
        "title": "Allied Health Science",
        "tagline": "Exploring the Vital Field: Allied Health Sciences Courses",
        "intro": [
            "Allied Health Sciences stand at the forefront of healthcare, playing a pivotal role in supporting patient care and wellness. These courses offer a gateway to a dynamic and rewarding career path, characterised by its significant impact on individuals and communities.",
            "The scope of Allied Health Sciences courses is expansive, encompassing a diverse range of specialties and disciplines within the healthcare sector. Aspiring professionals delve into the intricacies of medical science, gaining knowledge and skills necessary to thrive in various clinical and administrative roles.",
        ],
        "eligibility": "Candidates must have completed high school education (Class 12 or equivalent). While specific requirements may vary, candidates are generally expected to have completed high school with a minimum aggregate score ranging from 55% to 60%.",
        "popular_heading": "Popular Allied Health Sciences Courses",
        "popular_lead": "Allied Health Sciences are offered as certification, diploma and degree programs across specialised focus areas like Medical Laboratory Technology and Radiography.",
        "popular": [
            ("BSc Ophthalmology", "Class 12 with minimum aggregate of 45-50%, available across streams."),
            ("Radiology", "Class 12 with relevant subjects and minimum aggregate marks."),
            ("Cardiac Assistant", "Class 12 with relevant subjects and minimum aggregate marks."),
            ("Emergency &amp; Accident Care", "Class 12 with relevant subjects and minimum aggregate marks."),
            ("OT &amp; AT (Anaesthesia Technology)", "Class 12 with relevant subjects and minimum aggregate marks."),
            ("BPT (Bachelor of Physiotherapy)", "Class 12 with PCB and English with at least 50% aggregate."),
        ],
        "exams": "Various national, state and university-level entrance exams are conducted for Allied Health Sciences admission.",
        "feature_course": ("BSc Allied Health Sciences", "Bachelor of Science in Allied Health Sciences is a comprehensive undergraduate program preparing students for diverse healthcare roles including diagnostics, therapy and clinical support."),
        "image": "placement.jpg",
    },
    "law": {
        "title": "Law",
        "tagline": "Law is the basic part of our constitution",
        "intro": [
            "Law is one of the most sought after and long-standing professions in India and has always been one of the most popular courses for Indian students to pursue. Law is a career stream that aspirants can pursue at the Undergraduate (UG), Postgraduate (PG) or Doctorate (PhD) level.",
            "The scope of law as a career is immense in India, with opportunities in corporate houses, law firms, agencies, administrative services and more. A person can work in different types of law — civil, criminal, business or corporate.",
        ],
        "eligibility": "Students from any academic background can pursue law courses after Class 12 or graduation. Admission to law courses is based on national or state-level entrance exams like CLAT, LSAT and TS-LAWCET.",
        "popular_heading": "Popular Law Courses",
        "popular_lead": "Students can specialise in law by pursuing LLB at the bachelor's level and LLM at the master's level. Integrated programs like BBA LLB, BSc LLB and BCom LLB are also available.",
        "popular": [
            ("Bachelor of Laws (LL.B.)", "3-year program after graduation, or 5-year integrated program directly after Class 12."),
            ("Master of Laws (LL.M.)", "1 or 2 year postgraduate program for in-depth specialisation in a specific field of law."),
            ("Integrated Law (BBA LLB / BCom LLB)", "5-year integrated programs combining management or commerce with law."),
        ],
        "exams": "Popular law entrance exams: CLAT, LSAT India, AILET, MH CET Law, AP-LAWCET, TS-LAWCET, KLEE, CUET BA LLB, SLAT, CUSAT CAT BBA LLB, ULSAT, ILSAT, AMU Law.",
        "feature_course": ("LLB (Bachelor of Legislative Law)", "LLB is the most common law education degree — a three-year undergraduate course introducing students to corporate, legislative, business and other forms of law for critical understanding and application in legal affairs. LLB is mandatory for students who wish to become a lawyer."),
        "image": "bg/law.jpg",
    },
    "agriculture": {
        "title": "Agriculture",
        "tagline": "Agriculture plays an essential role in economy",
        "intro": [
            "Agriculture courses have emerged as one of the popular options for students. The career scope in the agriculture stream is never-ending, as there is always demand for innovative farming techniques. Agriculture is one stream where job opportunities keep increasing considering the demand for food production in India.",
            "Agriculture is one of the oldest and most significant parts of human society, providing not only food but also various raw materials. With modern technology and innovation, the scope of careers has grown tremendously — students can choose from specialisations like meteorology, agronomy, horticulture, breeding and plant pathology.",
        ],
        "eligibility": "The criteria of eligibility for taking admission in agriculture courses is to pass Class 12 from science or any stream with a minimum aggregate of 40% to 45% marks.",
        "popular_heading": "Popular Agriculture Courses",
        "popular_lead": "Agriculture courses are offered at bachelor's, master's, diploma and certificate levels covering scientific, technological and business topics associated with farming, farm management, poultry, horticulture, dairy farming and agricultural biotechnology.",
        "popular": [
            ("B.Sc. Agriculture", "4-year undergraduate program. Class 12 with PCM/B with minimum 50% aggregate."),
            ("M.Sc. Agriculture", "2-year postgraduate course after a 4-year graduation in Agriculture/Horticulture/Forestry with 50% aggregate."),
            ("B.Sc. Horticulture", "4-year undergraduate program. Class 12 with PCM/B with minimum 50% aggregate."),
            ("B.Tech Agriculture", "4-year undergraduate program. Class 12 with PCM/B with minimum 50% aggregate."),
        ],
        "exams": "Popular agriculture exams in India: ICAR-AIEEA, KEAM, KCET, AP EAMCET, TJEE, BCECE, MHT CET, ICAR, OUAT, LPUNEST, AAU VET.",
        "feature_course": ("B.Sc. Agriculture", "B.Sc. Agriculture is a four-year undergraduate science program focused on research and practices in agricultural science, dealing with disciplines like Genetics and Plant Breeding, Agricultural Microbiology, Soil Science and Plant Pathology. Graduates work as Agricultural Engineers, Food Technologists and Agronomists."),
        "image": "bg/agri.jpg",
    },
    "art-science": {
        "title": "Art and Science",
        "tagline": "Art and Science is one of the most valued and well-respected professions",
        "intro": [
            "Art and Science are two of the most esteemed and revered domains of study. India is emerging as a focal point for educational pursuits in both artistic and scientific fields, offering a plethora of courses to nurture aspiring individuals. Pursuing a career in either art or science demands dedication and perseverance but promises gratifying outcomes.",
            "Art and Science encompass a broad spectrum — Fine Arts, Literature, Mathematics, Physics, Biology, Chemistry and more. Graduates venture into diverse professions: artists, writers, mathematicians, physicists, biologists, chemists, educators, researchers and innovators. The fusion of art and science opens up boundless opportunities for exploration and advancement.",
        ],
        "eligibility": "Candidates typically need to have completed Class 12 with relevant subjects (English, Mathematics, Physics, Chemistry, Biology) depending on the program, with a minimum aggregate score of 50%. Entrance exams like JEE Main, JEE Advanced or state-level tests may be necessary.",
        "popular_heading": "Popular Art and Science Courses",
        "popular_lead": "Art and Science courses encompass literature, history, mathematics, physics, chemistry, biology and more — catering to diverse interests and career paths.",
        "popular": [
            ("BA (Bachelor of Arts)", "Class 12 with English as a compulsory subject and minimum 50% aggregate."),
            ("BSc (Bachelor of Science)", "Class 12 with PCB/PCM/Computer Science and minimum 50% aggregate."),
            ("BFA (Bachelor of Fine Arts)", "Class 12 with proficiency in Fine Arts or related subjects and minimum 50% aggregate."),
            ("BCom (Bachelor of Commerce)", "Class 12 with Commerce or relevant subjects and minimum 50% aggregate."),
            ("BCA (Bachelor of Computer Applications)", "Class 12 with relevant subjects and minimum 50% aggregate."),
        ],
        "exams": "Various national, state and university-level entrance exams are conducted for art and science admissions.",
        "feature_course": ("BA / BSc Programs", "BA and BSc programs offer a strong foundation across humanities and sciences — opening doors to careers in research, education, government services, content creation and more."),
        "image": "bg/art.jpg",
    },
    "management": {
        "title": "Management",
        "tagline": "Businesses need strong leaders",
        "intro": [
            "Management courses provide a multidisciplinary discipline focused on the foundation of business — economics, finance, marketing — with the study of basic administration practices. You'll understand various management theories and their relationships with different industries.",
            "Management is a very important stream after Class 12 as it opens up numerous career opportunities. It enhances planning, execution, analysis, directing and supervising skills. Management courses are open to students from all streams — science, arts or commerce — and are offered at certificate, diploma, PG diploma, UG, PG and Doctoral levels.",
        ],
        "eligibility": "The criteria of eligibility is to pass Class 12 from any stream with a minimum of 50% aggregate and English as a compulsory subject.",
        "popular_heading": "Popular Management Courses",
        "popular_lead": "Management courses are offered across specialisations in Marketing, Finance and Human Resources at various academic levels.",
        "popular": [
            ("BBA", "Class 12 from a recognised board with minimum 60% aggregate."),
            ("MBA", "Bachelor's degree in any discipline with minimum aggregate marks and a valid entrance exam score."),
            ("PGDM", "Bachelor's degree with minimum aggregate marks and a valid entrance exam score."),
            ("BBM (Bachelor of Business Management)", "Class 12 from a recognised board with minimum aggregate marks."),
        ],
        "exams": "Popular management exams: GMAT, CAT, MAT, NMAT, XAT, CMAT, IIFT, TISSNET, AIMA UGAT, CUET, SET, IPM, IBSAT.",
        "feature_course": ("BBA (Bachelor of Business Administration)", "BBA is a 3-year undergraduate program providing students with professional managerial and entrepreneurial skills. Ideal for individuals with a knack for business, management or entrepreneurship — students can choose specialisations like Finance, Marketing, Management and HR."),
        "image": "bg/manager.jpg",
    },
    "architecture": {
        "title": "Architecture",
        "tagline": "Embarking on the Architectural Journey",
        "intro": [
            "Architecture stands as a testament to creativity, innovation and the shaping of the built environment. Pursuing a course in architecture opens doors to a realm of endless possibilities, where aspiring architects can unleash their imagination and leave an indelible mark on the world.",
            "Architecture courses offer a dynamic platform for learning and growth, presenting a wide spectrum of career avenues. These courses delve into the intricacies of design, construction and urban planning — equipping students with the skills needed to thrive in this multifaceted field.",
        ],
        "eligibility": "Prospective students are generally required to have completed Class 12 or its equivalent with a minimum aggregate of 50%, regardless of stream, provided English is one of the subjects studied. The school/board must be recognised by relevant authorities.",
        "popular_heading": "Popular Architecture Courses",
        "popular_lead": "Architecture courses are offered at Bachelor's, Postgraduate, Doctorate and diploma levels, accessible through online, offline and distance learning modes.",
        "popular": [
            ("Bachelor of Architecture (B.Arch)", "Class 12 with minimum 50% aggregate from a recognised board."),
            ("Master of Architecture (M.Arch)", "Bachelor's degree in architecture or related field, plus entrance exam if required."),
            ("Doctor of Philosophy (Ph.D.)", "Master's degree in architecture or relevant discipline."),
        ],
        "exams": "Important entrance exams: JEE Main, NATA (National Aptitude Test in Architecture), CEED (Common Entrance Examination for Design), GATE.",
        "feature_course": ("Bachelor of Architecture (B.Arch)", "B.Arch is a professional undergraduate degree spanning five years, focused on training individuals aspiring to become architects. The course equips students with skills to design and oversee the construction of buildings and structures, combining artistic creativity with technical proficiency."),
        "image": "bg/archi (2).jpg",
    },
    "marine": {
        "title": "Marine",
        "tagline": "Marine is one of the most valued and well-respected professions",
        "intro": [
            "Marine studies stand as a cornerstone of esteemed and respected professions, blending the intricacies of both art and science. India is emerging as a focal point for educational pursuits in the maritime field. Pursuing a career in the marine industry demands unwavering dedication and perseverance but promises fulfilling outcomes.",
            "Marine studies encompass a broad spectrum — marine biology, oceanography, maritime engineering, naval architecture and more. Graduates venture into diverse professions: marine biologists, oceanographers, marine engineers, naval architects, researchers, policymakers and conservationists.",
        ],
        "eligibility": "Candidates usually need to have completed Class 12 with subjects like Mathematics, Physics, Chemistry and English with a minimum aggregate of 50%. Entrance examinations like IMU CET and MERI CET may be compulsory.",
        "popular_heading": "Popular Marine Courses",
        "popular_lead": "Maritime studies cover marine engineering, navigation, maritime law, oceanography and more — offering students diverse career opportunities.",
        "popular": [
            ("BSc in Maritime Studies", "Class 12 with PCM and English with minimum 50% aggregate."),
            ("BTech in Marine Engineering", "Class 12 with PCM and English with minimum 50% aggregate."),
            ("Diploma in Nautical Science", "Class 12 with Mathematics, Physics and Chemistry with minimum 50% aggregate."),
        ],
        "exams": "Important entrance exams: SAT, ACT, GRE, TOEFL, IELTS, IMU CET, MERI CET, IIT JAM and various state-level tests.",
        "feature_course": ("BTech Marine Engineering", "BTech in Marine Engineering is a 4-year undergraduate degree training students for design, operation, maintenance and repair of marine vessels and offshore structures. Graduates work as Marine Engineers, Naval Architects, Ship Surveyors and more."),
        "image": "bg/marine.jpg",
    },
    "physiotherapy-and-occupational-therapi": {
        "title": "Physiotherapy and Occupational Therapy",
        "tagline": "Embracing the Essential Fields of Healthcare",
        "intro": [
            "Physiotherapy and Occupational Therapy stand as fundamental pillars in healthcare, esteemed for their pivotal roles in enhancing mobility, managing pain and promoting overall well-being. Courses in these disciplines serve as gateways to indispensable professions, furnishing aspiring therapists with comprehensive knowledge of human anatomy and the skills essential for facilitating recovery and functional independence.",
            "The domain encompasses a diverse spectrum of specialisations — from orthopaedic rehabilitation to neurological intervention. These courses provide learners with the expertise necessary to address a variety of patient needs.",
        ],
        "eligibility": "Eligibility criteria vary across institutions and programs, but applicants typically need a minimum aggregate score of 55% to 60% in their high school examinations, ensuring a robust academic foundation.",
        "popular_heading": "Popular Physiotherapy and Occupational Therapy Courses",
        "popular_lead": "Students can pursue courses at undergraduate, postgraduate and doctoral levels: BPT, MPT and Diploma in Occupational Therapy (DOT) are some popular options.",
        "popular": [
            ("Diploma in Occupational Therapy (DOT)", "Class 12 with science subjects (PCB and Mathematics)."),
            ("Bachelor of Physiotherapy (BPT)", "Class 12 with PCB or PCM and English from a recognised board."),
            ("Master of Physiotherapy (MPT)", "BPT degree with minimum qualifying marks from a recognised college."),
        ],
        "exams": "Various national, state and university-level entrance exams: NEET-UG, AIIMS, JIPMER, CETPPMC, BHU PAT, KEAM.",
        "feature_course": ("Diploma in Occupational Therapy (DOT)", "DOT is a comprehensive two-year program designed to equip students with essential knowledge and skills in occupational therapy. The course focuses on principles of occupational therapy, therapeutic interventions and rehabilitation techniques — preparing students for careers across public and private healthcare sectors."),
        "image": "placement.jpg",
    },
}

def course_page(slug, depth=2):
    c = COURSE_CONTENT[slug]
    intro_html = "".join(f"<p>{para}</p>" for para in c['intro'])
    popular_html = "".join(
        f'<div class="card"><h3>{name}</h3><p>{desc}</p></div>'
        for name, desc in c['popular']
    )
    body = f"""<section class="page-banner bg-courses"><div class="container"><h1>{c['title']}</h1><div class="breadcrumb"><a href="../../">Home</a><span>/</span><a href="../../#">Courses</a><span>/</span>{c['title']}</div></div></section>

<section>
<div class="container">
<div class="split">
<div>
<span class="eyebrow" style="color:var(--brand-blue);font-weight:700;text-transform:uppercase;letter-spacing:1.5px;font-size:.85rem">Course Overview</span>
<h2>{c['tagline']}</h2>
{intro_html}
<a href="../../contact/" class="cta-btn">Know More</a>
</div>
<img src="../../assets/{c['image']}" alt="{c['title']}">
</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="grid grid-2">
<div class="card"><div class="card-icon">📋</div><h3>Eligibility for {c['title']} Courses</h3><p>{c['eligibility']}</p></div>
<div class="card"><div class="card-icon">📝</div><h3>Popular {c['title']} Entrance Exams</h3><p>{c['exams']}</p></div>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-head"><span class="eyebrow">Popular Courses</span><h2>{c['popular_heading']}</h2><p>{c['popular_lead']}</p></div>
<div class="grid grid-3">{popular_html}</div>
</div>
</section>

<section class="bg-soft">
<div class="container">
<div class="section-head"><span class="eyebrow">Featured Course</span><h2>{c['feature_course'][0]}</h2></div>
<div class="form-card" style="max-width:860px;margin:0 auto"><h3 style="color:var(--brand-blue);margin-bottom:14px">Course Description</h3><p>{c['feature_course'][1]}</p><div class="text-center mt-3"><a href="../../contact/" class="cta-btn">Apply Now</a></div></div>
</div>
</section>
"""
    return assemble(c['title'], depth, body, "courses")

for slug in COURSE_CONTENT:
    write(f"courses/{slug}/index.html", course_page(slug))

# ---------- College pages ----------
COLLEGE_CONTENT = {
    "top-medical-collegse": {
        "title": "Top Medical Colleges",
        "heading": "Medical Colleges",
        "intro": [
            "STUDY INDIA stands as a premier educational consultancy in India, boasting a decade of invaluable experience across various facets of the education sector. Specialising in career guidance, admission assistance and placement support, we are dedicated to steering students towards their academic and professional aspirations.",
            "In the realm of medical education, we leverage our expertise to navigate the complexities of choosing the right institution. With a finger on the pulse of market trends and educational advancements, we meticulously analyse the landscape to provide informed recommendations.",
        ],
        "colleges": [
            "Arunai Medical College", "St. Peter's Medical College", "Dhanalakshmi Srinivasan Medical College",
            "PSP Oragadam Medical College", "Panimalar Medical College", "Vels Medical College",
            "Meenakshi Medical College and Research Institute", "Mahatma Gandhi Medical College, Pondicherry",
            "Sri Manakula Vinayagar Medical College, Pondicherry", "Pondicherry Institute of Medical Sciences",
            "Sri Venkateswaraa Medical College, Pondicherry", "Sri Balaji Medical College, Chennai",
            "Velammal Medical College, Madurai", "Dhanalakshmi Srinivasan Medical College, Perambalur",
            "Sree Mookambika Institute of Medical Sciences", "Chennai Medical College &amp; Research Centre, Trichy",
            "Melmaruvathur Adiparasakthi Institute", "Shri Satya Sai Medical College", "Tagore Medical College, Chennai",
            "Aarupadai Veedu Medical College, Pondicherry", "Sri Ramachandra Medical College", "SRM Medical College Hospital",
            "Chettinad Hospital &amp; Research Institute", "Christian Medical College", "Saveetha Medical College and Hospital",
            "Vinayaka Missions Medical College, Pondicherry", "Vinayaka Missions Kirupananda Variyar Medical College, Salem",
            "Sri Muthukumaran Medical College, Chennai", "Karpaga Vinayaga Institute of Medical Science",
            "Karpagam Faculty of Medical Science Research, Coimbatore", "Sri Lakshmi Narayana Institute, Pondicherry",
            "ACS Medical College and Hospital, Chennai", "Annapoorna Medical College, Salem", "Madha Medical College, Chennai",
        ],
        "image": "course/medical2.png",
    },
    "top-dental-collegse": {
        "title": "Top Dental Colleges",
        "heading": "Dental Colleges",
        "intro": [
            "STUDY INDIA stands as a premier educational consultancy in India, backed by a decade of experience in diverse realms of the education sector. Specialising in career guidance, admission assistance and placement support, we have continually served as a beacon for students seeking to navigate complex educational pathways.",
            "In dental education, STUDY INDIA excels in offering comprehensive support to aspiring dental professionals. With a keen understanding of the evolving demands of the industry, we steer students towards esteemed dental colleges that align with their career aspirations and academic capabilities.",
        ],
        "colleges": [
            "SRM Dental College &amp; Hospital", "Sathyabama University Dental College", "Saveetha Dental College",
            "Chettinad Dental College and Research Institute", "Sree Balaji Dental College", "Ragas Dental College",
            "Sree Balaji Dental College &amp; Hospital", "Sree Mookambika Institute of Dental Sciences",
            "Sri Ramachandra Dental College, Porur", "Sri Ramakrishna Dental College, Avarampalayam",
            "Sri Venkateshwar Dental College, Kancheepuram", "SRM Kattankulathur Dental College",
            "Tagore Dental College, Rathinamangalam", "Tamil Nadu Dental College", "Adhiparasakthi Dental College, Cheyyar",
            "Best Dental Sciences College, Madurai", "CSI College of Dental Sciences and Research",
            "J.K.K. Natarajah Dental College", "K.S.R. Institute of Dental Science &amp; Research",
            "Karpaga Vinayaga Institute of Dental Science", "Madha Dental College, Chennai",
            "Meenakshi Ammai Dental College &amp; Hospital", "Priyadarshini Dental College &amp; Hospital",
            "R.V.S. Dental College", "Rajah Muthiah Dental College", "Rajas Dental College",
            "Thai Moogambigai Dental College &amp; Hospital", "Vinayaka Mission's Sankarachariyar Dental College",
            "Vivekananda Dental College for Women",
        ],
        "image": "course/dental.png",
    },
    "top-engineering-collegse": {
        "title": "Top Engineering Colleges",
        "heading": "Engineering Colleges",
        "intro": [
            "STUDY INDIA, a premier educational consultancy with a decade-long expertise in various facets of the education sector, offers invaluable insights into choosing the right path, especially in engineering education. With a profound understanding of career guidance, admission procedures and placement assistance, we stand as a beacon for aspiring engineers seeking excellence.",
            "In today's dynamic world where technology reigns supreme, the choice of an engineering college holds paramount importance. Through our years of experience and continuous monitoring of market trends and educational landscapes, we provide informed recommendations to guide students towards the most suitable engineering colleges.",
        ],
        "colleges": [
            "Anna University CEG Campus", "Anna University ACT Campus", "Anna University MIT Campus",
            "Sri Sivasubramaniya Nadar College of Engineering", "Sri Venkateswara College of Engineering",
            "St. Joseph's College of Engineering", "Panimalar Engineering College", "Jeppiar Engineering College",
            "RMK Engineering College", "RMD Engineering College", "Velammal Engineering College",
            "Rajalakshmi Engineering College", "PSG College of Technology", "Kumaraguru College of Engineering",
            "Ramakrishna Engineering College", "Kongu Engineering College", "Maamalan Institute of Technology",
            "Sairam Engineering College", "Veltech Engineering College", "Saveetha School of Engineering",
            "Meenakshi Engineering College", "Sri Muthukumaran Institute of Technology", "KCG College of Technology",
            "Arulmigu Meenakshi Amman College", "Jaya Engineering College", "Prathyusha Institute",
            "Anand Institute of Higher Technology", "St. Peters Engineering College", "Sree Sastha Institute",
            "S.A. Engineering College", "MNM Jain Engineering College", "RVS Padhmavathy College",
            "Adhiparasakthi Engineering College", "Kingston Engineering College", "Saranathan College of Engineering",
            "Thiagarajar College of Engineering", "Mepco Schlenk Engineering College", "K.L.N. College of Engineering",
            "Kalasalingam Institute of Technology", "PSNA College of Engineering", "Karpagam College of Engineering",
            "Hindustan College of Engineering", "Sona College of Technology", "Excel Engineering College",
            "Paavai Engineering College", "Adhiyamaan College of Engineering",
        ],
        "image": "course/engineer.png",
    },
    "deemed-universites": {
        "title": "Deemed Universities",
        "heading": "Deemed Universities",
        "intro": [
            "STUDY INDIA stands at the forefront of guiding students towards their educational aspirations. Our expertise spans various facets of the education sector, including career guidance, admission assistance and placement support. With a keen eye on market trends and growth strategies, we continually monitor the evolving landscape of the education sector to offer informed advice to students.",
            "In the realm of higher education, Deemed Universities hold a significant place. These institutions, granted autonomy and deemed status by the University Grants Commission (UGC), offer a diverse range of academic programs across disciplines. We recognise their importance in providing students with quality education and unique learning opportunities.",
        ],
        "colleges": [
            "SRM University", "VIT University", "Sathyabama University", "Hindustan University",
            "AMET University", "Amrita University", "B.S. Abdur Rahman University", "Bharath University",
            "Dr. M.G.R. Educational and Research Institute", "Kalasalingam University", "Karpagam University",
            "Karunya University", "Meenakshi Academy of Higher Education and Research", "Noorul Islam University",
            "Periyar Maniammai University", "PRIST University", "Saveetha University", "St. Peter's University",
            "Vel Tech Institute of Science and Technology", "Vels University", "Vinayaka Missions University",
        ],
        "image": "course/deemed.png",
    },
    "b-school": {
        "title": "B-School (Business School)",
        "heading": "Business School Colleges",
        "intro": [
            "STUDY INDIA boasts a decade-long expertise in various realms of the education sector, with a particular emphasis on guiding students through their academic and professional journeys. With a focus on B-School admissions, we leverage our extensive experience to provide comprehensive career guidance, admission support and placement assistance tailored specifically for aspiring business leaders.",
            "Our seasoned team continuously monitors the dynamic landscape of business education, meticulously analysing market trends and growth strategies to ensure our guidance remains relevant and effective in navigating the competitive realm of business education.",
        ],
        "colleges": [
            "Great Lakes Institute of Management, Chennai", "Loyola Institute of Business Administration, Chennai",
            "Department of Management Studies, IIT Madras", "SRM School of Management, Chennai",
            "Amrita School of Business, Coimbatore", "PSG College of Management, Coimbatore",
            "Thiagarajar School of Management, Thiruparankundram", "Department of Management Studies, VIT Vellore",
            "School of Management, Hindustan University, Chennai",
        ],
        "image": "bg/manager.jpg",
    },
    "marine-colleges": {
        "title": "Marine Colleges",
        "heading": "Marine Colleges",
        "intro": [
            "Diving into the realm of marine education, STUDY INDIA extends its expertise as a premier educational consultancy in India. With a rich decade-long experience spanning various facets of the education sector, including career guidance, admission assistance and placement support, we navigate the waves of academia to guide aspiring marine professionals.",
            "Our journey in the educational landscape has equipped us with a deep understanding of the intricate dynamics of career choices. We meticulously monitor market trends and growth strategies, staying attuned to the ever-evolving educational landscape and empowering students to make strategic decisions about their educational journey.",
        ],
        "colleges": [
            "AMET University", "IMA (Indian Maritime Academy)", "Vels University",
            "G.K.M. College of Engineering and Technology", "Cape Institute of Technology",
            "Mohamed Sathak Engineering College", "Noorul Islam University",
            "Park College of Engineering and Technology", "SAMS College of Engineering and Technology",
            "SCAD College of Engineering and Technology", "Sri Venkateswara College of Engineering",
        ],
        "image": "course/marine.png",
    },
    "architecture-colleges": {
        "title": "Architecture Colleges",
        "heading": "Architecture Colleges",
        "intro": [
            "STUDY INDIA stands as a premier educational consultancy in India, boasting a decade of invaluable experience in diverse realms of the education sector. Our expertise extends to providing comprehensive assistance in career guidance, admission counselling and placement support. With a keen eye on the dynamic landscape of the education market, we continually monitor evolving trends and strategies to offer informed guidance to students.",
            "When it comes to architecture colleges, our insights and support are unparalleled. Recognising the significance of choosing the right educational path, especially in fields as specialised as architecture, STUDY INDIA serves as a beacon of guidance for aspiring architects. We understand that architecture demands not only creativity but also a profound understanding of technicalities, design principles and industry dynamics.",
        ],
        "colleges": [
            "Measi Academy of Architecture", "SRM University", "Sathyabama University",
            "Meenakshi College of Engineering", "Mohamed Sathak Engineering College", "Bharath University",
            "National Institute of Technology", "Thiagarajar College of Engineering",
            "Adhiyamaan College of Engineering", "Anand School of Architecture",
            "Da Vinci School of Design and Architecture",
        ],
        "image": "course/architect.png",
    },
    "art-and-science-colleges": {
        "title": "Arts &amp; Science Colleges",
        "heading": "Art &amp; Science Colleges",
        "intro": [
            "STUDY INDIA brings over a decade of expertise to the realm of arts and science colleges. With our extensive experience spanning various facets of the education sector, including career guidance, admission assistance and placement support, we are dedicated to empowering students in their academic journey.",
            "In the dynamic landscape of higher education, we remain vigilant, continuously monitoring market trends and strategies. Understanding the evolving demands of the job market and the evolving nature of academic disciplines, we provide tailored advice to help students navigate their educational choices effectively.",
        ],
        "colleges": [
            "S.R.M. Arts and Science College, Chengalpattu", "Vels University (Vel's College of Science), Chennai",
            "M.O.P. Vaishnav College for Women, Chennai", "P.S.G. College of Arts and Science, Chennai",
            "S.I.E.T. College, Chennai", "Guru Nanak College, Chennai", "Loyola College, Chennai",
            "Madras Christian College, Chennai", "New College, Chennai", "S.I.V.E.T. College for Women, Chennai",
            "Anna Adarsh College for Women, Chennai", "Hindustan College of Arts and Science, Kelambakkam",
        ],
        "image": "course/artandscience.png",
    },
}

def college_page(slug):
    c = COLLEGE_CONTENT[slug]
    intro_html = "".join(f"<p>{p}</p>" for p in c['intro'])
    colleges_html = "".join(f'<div class="college-item">{name}</div>' for name in c['colleges'])
    body = f"""<section class="page-banner bg-colleges"><div class="container"><h1>{c['title']}</h1><div class="breadcrumb"><a href="../../">Home</a><span>/</span><a href="../../#">Colleges</a><span>/</span>{c['title']}</div></div></section>

<section>
<div class="container">
<div class="split">
<div>
<span class="eyebrow" style="color:var(--brand-blue);font-weight:700;text-transform:uppercase;letter-spacing:1.5px;font-size:.85rem">Overview</span>
<h2>{c['heading']}</h2>
{intro_html}
<a href="../../contact/" class="cta-btn">Get Admission Help</a>
</div>
<img src="../../assets/{c['image']}" alt="{c['title']}" onerror="this.src='../../assets/colleges.jpg'">
</div>
</div>
</section>

<section class="bg-soft list-section">
<div class="container">
<div class="section-head"><span class="eyebrow">Partner Institutions</span><h2>Top {c['heading']}</h2><p>Direct relationships with these institutions help us secure admissions for our students.</p></div>
<div class="college-grid">{colleges_html}</div>
<div class="text-center mt-3"><a href="#" class="cta-btn" data-open-modal="enquire">Enquire About Admission</a></div>
</div>
</section>
"""
    return assemble(c['title'], 2, body, "colleges")

for slug in COLLEGE_CONTENT:
    write(f"colleges/{slug}/index.html", college_page(slug))

print("\nBuild complete.")
