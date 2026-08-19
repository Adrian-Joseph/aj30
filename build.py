#!/usr/bin/env python3
"""Static site generator for adrianjoseph30 site. Run: python3 build.py
Produces fully static .html files with shared header/nav/footer so the
repo can be hosted as-is on GitHub Pages, no build step required at
serve time (this script is a dev-time convenience only)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("achievements.html", "Achievements"),
    ("services.html", "Services"),
    ("schedule.html", "Schedule"),
    ("gallery.html", "Gallery"),
    ("testimonials.html", "Testimonials"),
    ("news.html", "News"),
    ("contact.html", "Contact"),
]

SOCIAL_LINKS = {
    "instagram_personal": "https://www.instagram.com/adrianjosephelite?igsh=cnZwNXZ4cWgxaGww&utm_source=qr",
    "instagram_club": "https://www.instagram.com/advancedgenetics868?igsh=MWtrZm1rdnlzZTlxeA%3D%3D&utm_source=qr",
    "tiktok": "https://www.tiktok.com/@adrianjosephelite?_r=1&_t=ZS-98m241reOur",
    "youtube": "https://youtube.com/@adrianjoseph30?si=adlhOmzxjAE3vpNb",
    "facebook": "https://www.facebook.com/adrian.joseph.9406/",
}

SOCIAL_ICONS = {
    "instagram_personal": '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.06 2 .25 2.5.42a5 5 0 0 1 1.8 1.17 5 5 0 0 1 1.17 1.8c.17.5.36 1.3.42 2.5.06 1.3.07 1.7.07 4.9s0 3.6-.07 4.9c-.06 1.2-.25 2-.42 2.5a5 5 0 0 1-1.17 1.8 5 5 0 0 1-1.8 1.17c-.5.17-1.3.36-2.5.42-1.3.06-1.7.07-4.9.07s-3.6 0-4.9-.07c-1.2-.06-2-.25-2.5-.42a5 5 0 0 1-1.8-1.17 5 5 0 0 1-1.17-1.8c-.17-.5-.36-1.3-.42-2.5C2.21 15.6 2.2 15.2 2.2 12s0-3.6.07-4.9c.06-1.2.25-2 .42-2.5a5 5 0 0 1 1.17-1.8A5 5 0 0 1 5.66 1.63c.5-.17 1.3-.36 2.5-.42C9.4 2.21 9.8 2.2 12 2.2Zm0 3a6.8 6.8 0 1 0 0 13.6 6.8 6.8 0 0 0 0-13.6Zm0 11.2a4.4 4.4 0 1 1 0-8.8 4.4 4.4 0 0 1 0 8.8Zm7-11.4a1.59 1.59 0 1 1-3.18 0 1.59 1.59 0 0 1 3.18 0Z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24"><path d="M16.6 2h-3.2v13.6a2.9 2.9 0 1 1-2.05-2.77V9.6a6.1 6.1 0 1 0 5.25 6.03V8.36a7.6 7.6 0 0 0 4.4 1.4V6.55a4.3 4.3 0 0 1-4.4-4.24Z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M22 12s0-3.4-.43-5a2.8 2.8 0 0 0-2-2C17.9 4.5 12 4.5 12 4.5s-5.9 0-7.57.5a2.8 2.8 0 0 0-2 2C2 8.6 2 12 2 12s0 3.4.43 5a2.8 2.8 0 0 0 2 2C6.1 19.5 12 19.5 12 19.5s5.9 0 7.57-.5a2.8 2.8 0 0 0 2-2c.43-1.6.43-5 .43-5ZM9.8 15.3V8.7l5.8 3.3-5.8 3.3Z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V8c0-.9.25-1.5 1.55-1.5H16.7V3.7C16.4 3.66 15.4 3.6 14.24 3.6c-2.4 0-4.05 1.47-4.05 4.16v2.13H7.5v3.1h2.69V21Z"/></svg>',
}

def head(title, desc, active, extra_og_image="images/hero/hero-main.jpg", body_class=""):
    canonical = active
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Adrian Joseph — Elite Basketball Training</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} | Adrian Joseph">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{extra_og_image}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0a1526">
<link rel="icon" type="image/png" href="images/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body class="{body_class}">
<a class="skip-link" href="#main">Skip to content</a>
{header_html(canonical)}
<main id="main">
"""

def header_html(active):
    items = ""
    for href, label in NAV_ITEMS:
        cls = "active" if href == active else ""
        items += f'<a href="{href}" class="{cls}">{label}</a>\n'
    return f"""<header class="site-header">
  <nav class="nav">
    <a href="index.html" class="brand">
      <span class="brand-badge"><img src="images/logo/ajoseph-icon.png" alt="Adrian Joseph logo"></span>
      <span class="brand-text"><span class="name">ADRIAN JOSEPH</span><span class="role">Elite Basketball Training</span></span>
    </a>
    <div class="nav-links">
      {items}
      <a href="contact.html" class="nav-cta">Book Training</a>
    </div>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </nav>
</header>
"""

def footer_html():
    social = "".join(f'<a href="{SOCIAL_LINKS[k]}" target="_blank" rel="noopener" aria-label="{k}">{SOCIAL_ICONS[k]}</a>' for k in ["instagram_personal","tiktok","youtube","facebook"])
    return f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand-line">
          <span class="brand-badge"><img src="images/logo/ajoseph-icon.png" alt=""></span>
          <span>ADRIAN JOSEPH</span>
        </div>
        <p style="max-width:34ch;color:#8b95a6;font-size:15px;">Former Trinidad &amp; Tobago National Team Captain, NCAA Division I champion (Virginia), and founder of Advanced Genetics Sports &amp; Cultural Club. Elite basketball training for the next generation.</p>
        <div class="social-row">{social}</div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="about.html">About Adrian</a></li>
          <li><a href="achievements.html">Achievements</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="gallery.html">Gallery</a></li>
        </ul>
      </div>
      <div>
        <h4>Programs</h4>
        <ul>
          <li><a href="services.html#private">Private Training</a></li>
          <li><a href="services.html#camps">Camps &amp; Clinics</a></li>
          <li><a href="services.html#placement">College / Pro Placement</a></li>
          <li><a href="schedule.html">Schedule &amp; Membership</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:18684819414">1 (868) 481-9414</a></li>
          <li><a href="tel:18683673656">1 (868) 367-3656</a></li>
          <li><a href="mailto:advancedgenetics868@gmail.com">advancedgenetics868@gmail.com</a></li>
          <li>9 Murli Street, La Romaine,<br>San Fernando, Trinidad &amp; Tobago</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span class="js-year"></span> Adrian Joseph / Advanced Genetics Sports &amp; Cultural Club. All rights reserved.</span>
      <span>&ldquo;To Foster Growth and Development of All Members by Providing Quality Service.&rdquo;</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""

def page(filename, title, desc, active, content, extra_og_image="images/hero/hero-main.jpg", body_class=""):
    html = head(title, desc, active, extra_og_image, body_class) + content + footer_html()
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)
