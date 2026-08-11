#!/usr/bin/env python3
import os
from build import page, ROOT

# ============================================================ HOME
home = """
<section class="hero">
  <div class="hero-media"><img src="images/hero/hero-main.jpg" alt="Adrian Joseph elevating for a dunk during a professional FIBA match" loading="eager"></div>
  <div class="hero-scrim"></div>
  <span class="hero-jersey" aria-hidden="true">30</span>
  <div class="hero-inner">
    <p class="eyebrow hero-eyebrow">Adrian Joseph &middot; Elite Basketball Training</p>
    <h1 class="hero-title">
      <span>PASSION.</span>
      <span>PURPOSE.</span>
      <span>PERFORMANCE.</span>
    </h1>
    <p class="hero-sub">Former Trinidad &amp; Tobago National Team Captain. NCAA Division I champion at the University of Virginia. International professional across four countries. Now training the next generation in Trinidad &amp; Tobago.</p>
    <div class="hero-actions">
      <a href="contact.html" class="btn btn-primary">Book Training</a>
      <a href="achievements.html" class="btn btn-ghost">View Achievements</a>
    </div>
  </div>
</section>

<div class="stat-strip section-dark">
  <div><span class="stat-num">NCAA D1</span><span class="stat-label">Virginia Cavaliers</span></div>
  <div><span class="stat-num">Captain</span><span class="stat-label">Trinidad &amp; Tobago</span></div>
  <div><span class="stat-num">4</span><span class="stat-label">Countries Played Pro</span></div>
  <div><span class="stat-num">FIBA</span><span class="stat-label">Certified Coach</span></div>
</div>

<section class="section section-cream">
  <div class="container">
    <div class="two-col">
      <div class="img-frame reveal">
        <img src="images/profile/headshot.jpg" alt="Adrian Joseph, professional headshot">
      </div>
      <div class="reveal">
        <p class="eyebrow">Meet Coach Adrian</p>
        <h2 style="font-size:clamp(28px,4vw,42px);color:var(--navy);margin:12px 0 18px;">From La Romaine to Division I, and back to build the next generation.</h2>
        <p style="color:#565f6d;font-size:18px;">Adrian Joseph grew up in La Romaine, Trinidad, with no elite basketball pathway in the Southern Region to develop his talent. That gap sent him to the United States on scholarship at 14. It also became the reason he came home to build one. Today he holds a B.A. in Anthropology from the University of Virginia, a FIBA Coaching Certification, and a Sports Management Worldwide Certified Basketball Agent credential, and he has turned every mile of that journey into a training programme for Trinidad &amp; Tobago's next athletes.</p>
        <a href="about.html" class="btn btn-dark" style="margin-top:10px;">Read Adrian's Story</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head">
      <span class="watermark30" aria-hidden="true">30</span>
      <p class="eyebrow">Training Programmes</p>
      <h2>Built On What Actually<br>Gets Players Seen</h2>
      <p class="section-lede">Every session draws on Division I, professional, and national team experience, not a generic drill sheet.</p>
    </div>
    <div class="grid grid-3 reveal-stagger">
      <div class="card">
        <span class="card-num">01</span>
        <h3>Private Training</h3>
        <p>One-on-one sessions built around ball-handling, shooting mechanics, footwork, and basketball IQ, tailored to the player in front of him.</p>
        <a href="services.html#private" class="card-link">Learn More</a>
      </div>
      <div class="card">
        <span class="card-num">02</span>
        <h3>Camps &amp; Clinics</h3>
        <p>IGNITE Basketball Camp, the Court to Court Caravan, and multi-day clinics combining skills, competition, and mentorship.</p>
        <a href="services.html#camps" class="card-link">Learn More</a>
      </div>
      <div class="card">
        <span class="card-num">03</span>
        <h3>College &amp; Pro Placement</h3>
        <p>Scholarship prep, recruiting film, and NCAA guidance from a certified agent who has lived the recruiting process himself.</p>
        <a href="services.html#placement" class="card-link">Learn More</a>
      </div>
    </div>
    <div style="text-align:center;margin-top:44px;">
      <a href="services.html" class="btn btn-primary">View All Services</a>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="section-head center">
      <span class="watermark30" aria-hidden="true" style="right:50%;transform:translateX(50%);">30</span>
      <p class="eyebrow on-dark">Camp Parent Feedback</p>
      <h2>What Families Are Saying</h2>
    </div>
    <div class="grid grid-2 reveal-stagger">
      <div class="quote-card">
        <span class="mark">&ldquo;</span>
        <p class="quote">In just one week, I saw such a positive transformation in my 14 year old son. He became more confident, more active, and even started coming out of his shell socially.</p>
        <p class="attrib">Camp Parent &middot; IGNITE Basketball Camp 2026</p>
      </div>
      <div class="quote-card">
        <span class="mark">&ldquo;</span>
        <p class="quote">This was one of the best basketball camps I have ever witnessed. My son got so much out of it, including new friendships.</p>
        <p class="attrib">Camp Parent &middot; IGNITE Basketball Camp 2026</p>
      </div>
    </div>
    <div style="text-align:center;margin-top:40px;">
      <a href="testimonials.html" class="btn btn-ghost">Read All Testimonials</a>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="section-head">
      <span class="watermark30" aria-hidden="true">30</span>
      <p class="eyebrow">On The Calendar</p>
      <h2>Upcoming Events</h2>
    </div>
    <div class="grid grid-3 reveal-stagger">
      <div class="card">
        <span class="card-num">Jul 13&ndash;17</span>
        <h3>IGNITE Basketball Camp</h3>
        <p>Five days of elite training, competitions, and mentorship at Pleasantville Indoor Sports Arena.</p>
        <a href="news.html" class="card-link">Details</a>
      </div>
      <div class="card">
        <span class="card-num">2026</span>
        <h3>Court to Court Caravan</h3>
        <p>Taking basketball to the community across 20&ndash;25 venues throughout Trinidad.</p>
        <a href="news.html" class="card-link">Details</a>
      </div>
      <div class="card">
        <span class="card-num">Aug 17&ndash;21</span>
        <h3>USA Coaches Collaboration Camp</h3>
        <p>Train with elite USA coaches for high-level instruction, competition, and exposure.</p>
        <a href="news.html" class="card-link">Details</a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <span class="hero-jersey" style="opacity:0.5;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <h2>Ready To Elevate Your Game?</h2>
    <p>Spots fill fast for private sessions and upcoming camps. Reach out today to find the right programme.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Book Training</a>
      <a href="tel:18684819414" class="btn btn-ghost">Call 1 (868) 481-9414</a>
    </div>
  </div>
</section>
"""
page("index.html", "Home", "Adrian Joseph — former Trinidad & Tobago National Team Captain, NCAA Division I champion, and elite basketball trainer in Trinidad & Tobago. Private training, camps, and college/pro placement.", "index.html", home)

print("home done")
