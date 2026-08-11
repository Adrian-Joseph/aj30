#!/usr/bin/env python3
from build import page

contact = """
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">Let's Talk</p>
    <h1>Contact Adrian</h1>
    <p>Questions about private training, camps, or bringing Adrian in to speak? Reach out below.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="contact-wrap">
      <div class="reveal">
        <div class="img-frame" style="max-width:220px;margin-bottom:28px;">
          <img src="images/profile/headshot.jpg" alt="Adrian Joseph, professional headshot">
        </div>
        <p class="eyebrow on-dark">Get In Touch</p>
        <h2 style="color:#fff;font-size:clamp(24px,3.4vw,32px);margin:10px 0 24px;">Contact Information</h2>

        <div class="info-row">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
          <div><span class="label">Phone</span><a href="tel:18684819414">1 (868) 481-9414</a> &middot; <a href="tel:18683673656">1 (868) 367-3656</a></div>
        </div>
        <div class="info-row">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z" opacity="0"/><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg></span>
          <div><span class="label">Email</span><a href="mailto:advancedgenetics868@gmail.com">advancedgenetics868@gmail.com</a></div>
        </div>
        <div class="info-row">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
          <div><span class="label">Location</span><span>9 Murli Street, La Romaine, San Fernando, Trinidad and Tobago</span></div>
        </div>
        <div class="info-row">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>
          <div><span class="label">Training Hours</span><span>By appointment &mdash; contact to confirm current session times</span></div>
        </div>

        <p class="eyebrow on-dark" style="margin-top:30px;">Follow Along</p>
        <div class="social-row">
          <a href="https://www.instagram.com/adrianjosephelite?igsh=cnZwNXZ4cWgxaGww&utm_source=qr" target="_blank" rel="noopener" aria-label="Adrian Joseph on Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.06 2 .25 2.5.42a5 5 0 0 1 1.8 1.17 5 5 0 0 1 1.17 1.8c.17.5.36 1.3.42 2.5.06 1.3.07 1.7.07 4.9s0 3.6-.07 4.9c-.06 1.2-.25 2-.42 2.5a5 5 0 0 1-1.17 1.8 5 5 0 0 1-1.8 1.17c-.5.17-1.3.36-2.5.42-1.3.06-1.7.07-4.9.07s-3.6 0-4.9-.07c-1.2-.06-2-.25-2.5-.42a5 5 0 0 1-1.8-1.17 5 5 0 0 1-1.17-1.8c-.17-.5-.36-1.3-.42-2.5C2.21 15.6 2.2 15.2 2.2 12s0-3.6.07-4.9c.06-1.2.25-2 .42-2.5a5 5 0 0 1 1.17-1.8A5 5 0 0 1 5.66 1.63c.5-.17 1.3-.36 2.5-.42C9.4 2.21 9.8 2.2 12 2.2Zm0 3a6.8 6.8 0 1 0 0 13.6 6.8 6.8 0 0 0 0-13.6Zm0 11.2a4.4 4.4 0 1 1 0-8.8 4.4 4.4 0 0 1 0 8.8Zm7-11.4a1.59 1.59 0 1 1-3.18 0 1.59 1.59 0 0 1 3.18 0Z"/></svg></a>
          <a href="https://www.instagram.com/advancedgenetics868?igsh=MWtrZm1rdnlzZTlxeA%3D%3D&utm_source=qr" target="_blank" rel="noopener" aria-label="Advanced Genetics on Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.06 2 .25 2.5.42a5 5 0 0 1 1.8 1.17 5 5 0 0 1 1.17 1.8c.17.5.36 1.3.42 2.5.06 1.3.07 1.7.07 4.9s0 3.6-.07 4.9c-.06 1.2-.25 2-.42 2.5a5 5 0 0 1-1.17 1.8 5 5 0 0 1-1.8 1.17c-.5.17-1.3.36-2.5.42-1.3.06-1.7.07-4.9.07s-3.6 0-4.9-.07c-1.2-.06-2-.25-2.5-.42a5 5 0 0 1-1.8-1.17 5 5 0 0 1-1.17-1.8c-.17-.5-.36-1.3-.42-2.5C2.21 15.6 2.2 15.2 2.2 12s0-3.6.07-4.9c.06-1.2.25-2 .42-2.5a5 5 0 0 1 1.17-1.8A5 5 0 0 1 5.66 1.63c.5-.17 1.3-.36 2.5-.42C9.4 2.21 9.8 2.2 12 2.2Zm0 3a6.8 6.8 0 1 0 0 13.6 6.8 6.8 0 0 0 0-13.6Zm0 11.2a4.4 4.4 0 1 1 0-8.8 4.4 4.4 0 0 1 0 8.8Zm7-11.4a1.59 1.59 0 1 1-3.18 0 1.59 1.59 0 0 1 3.18 0Z"/></svg></a>
          <a href="https://www.tiktok.com/@adrianjosephelite?_r=1&_t=ZS-98m241reOur" target="_blank" rel="noopener" aria-label="Adrian Joseph on TikTok"><svg viewBox="0 0 24 24"><path d="M16.6 2h-3.2v13.6a2.9 2.9 0 1 1-2.05-2.77V9.6a6.1 6.1 0 1 0 5.25 6.03V8.36a7.6 7.6 0 0 0 4.4 1.4V6.55a4.3 4.3 0 0 1-4.4-4.24Z"/></svg></a>
          <a href="https://youtube.com/@adrianjoseph30?si=adlhOmzxjAE3vpNb" target="_blank" rel="noopener" aria-label="Adrian Joseph on YouTube"><svg viewBox="0 0 24 24"><path d="M22 12s0-3.4-.43-5a2.8 2.8 0 0 0-2-2C17.9 4.5 12 4.5 12 4.5s-5.9 0-7.57.5a2.8 2.8 0 0 0-2 2C2 8.6 2 12 2 12s0 3.4.43 5a2.8 2.8 0 0 0 2 2C6.1 19.5 12 19.5 12 19.5s5.9 0 7.57-.5a2.8 2.8 0 0 0 2-2c.43-1.6.43-5 .43-5ZM9.8 15.3V8.7l5.8 3.3-5.8 3.3Z"/></svg></a>
        </div>

        <div class="reveal" style="margin-top:32px;border-radius:4px;overflow:hidden;border:1px solid rgba(255,255,255,0.15);">
          <iframe title="Map showing La Romaine, San Fernando, Trinidad and Tobago" src="https://www.openstreetmap.org/export/embed.html?bbox=-61.4750%2C10.2650%2C-61.4250%2C10.3050&layer=mapnik&marker=10.2850%2C-61.4500" width="100%" height="230" style="border:0;display:block;filter:grayscale(0.15) contrast(1.05);" loading="lazy"></iframe>
        </div>
      </div>

      <div class="reveal" style="background:#fff;border-radius:4px;padding:34px 30px;color:var(--ink);">
        <p class="eyebrow">Send A Message</p>
        <h2 style="font-size:24px;color:var(--navy);margin:8px 0 22px;">Book Training Or Ask A Question</h2>
        <form id="contact-form">
          <div class="form-field">
            <label for="cf-name">Full Name</label>
            <input type="text" id="cf-name" name="name" required>
          </div>
          <div class="form-field">
            <label for="cf-email">Email</label>
            <input type="email" id="cf-email" name="email" required>
          </div>
          <div class="form-field">
            <label for="cf-phone">Phone</label>
            <input type="tel" id="cf-phone" name="phone">
          </div>
          <div class="form-field">
            <label for="cf-program">Programme Of Interest</label>
            <select id="cf-program" name="program">
              <option value="">Select a programme</option>
              <option>Private Training</option>
              <option>Team Training</option>
              <option>Camps &amp; Clinics</option>
              <option>College / Pro Placement</option>
              <option>Speaking &amp; Consulting</option>
              <option>Other</option>
            </select>
          </div>
          <div class="form-field">
            <label for="cf-message">Message</label>
            <textarea id="cf-message" name="message" required placeholder="Tell us about the player and what you're looking for..."></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Send Message</button>
          <p style="font-size:13px;color:#7a8290;margin-top:12px;">This opens your email app with the message pre-filled, addressed to advancedgenetics868@gmail.com.</p>
        </form>
      </div>
    </div>
  </div>
</section>
"""
page("contact.html", "Contact", "Contact Adrian Joseph and Advanced Genetics Sports & Cultural Club for private training, camps, team sessions, and speaking engagements in Trinidad & Tobago.", "contact.html", contact)
print("contact done")
