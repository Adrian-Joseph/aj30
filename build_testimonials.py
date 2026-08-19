#!/usr/bin/env python3
from build import page

quotes = [
    "Thank you, Coach, for an outstanding week at the basketball camp. Your dedication, encouragement, and excellent program made it a truly rewarding experience for the kids.",
    "This was one of the best basketball camps I have ever witnessed. My son got so much out of it, including new friendships.",
    "In just one week, I saw such a positive transformation in my 14 year old son. He became more confident, more active, and even started coming out of his shell socially. Your patience, encouragement, and dedication made all the difference.",
    "A heartfelt thank you to the Coach and the entire team, for an amazing and successful training camp. Your dedication, patience, and encouragement made it wonderful. She said it was the best basketball experience she has ever had since deciding to play the sport a year ago.",
    "It was a great experience. Coach gave the kids such a great session.",
]

slides = "".join(f"""<div class="quote-card" style="display:{'block' if i==0 else 'none'};max-width:720px;margin:0 auto;">
  <span class="mark">&ldquo;</span>
  <p class="quote" style="font-size:21px;">{q}</p>
  <p class="attrib">Camp Parent Feedback &middot; IGNITE Basketball Camp 2026</p>
</div>""" for i,q in enumerate(quotes))

testimonials = f"""
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">In Their Words</p>
    <h1>What Camp Families Are Saying</h1>
    <p>Real feedback collected from parents after IGNITE Basketball Camp 2026.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="testi-slider reveal">
      {slides}
    </div>
    <div class="testi-dots" style="display:flex;justify-content:center;gap:8px;margin-top:30px;"></div>
  </div>
</section>

<style>
  .testi-dot{{ width:10px;height:10px;border-radius:50%;border:1px solid rgba(255,255,255,0.4);background:transparent;cursor:pointer;padding:0; }}
  .testi-dot.active{{ background:var(--orange); border-color:var(--orange); }}
</style>

<section class="section section-cream">
  <div class="container">
    <div class="section-head center">
      <span class="watermark30" aria-hidden="true" style="right:50%;transform:translateX(50%);">30</span>
      <p class="eyebrow">Camp Recap</p>
      <h2>Hear It In Their Voices</h2>
      <p class="section-lede" style="margin-left:auto;margin-right:auto;">The full feedback reel shared after IGNITE Basketball Camp 2026.</p>
    </div>
    <div class="reveal" style="max-width:420px;margin:0 auto;">
      <video controls preload="metadata" style="width:100%;border-radius:4px;box-shadow:var(--shadow);" poster="images/community/ignite-training-gym.jpg">
        <source src="video/ignite-camp-2026-recap.mp4" type="video/mp4">
        Your browser does not support embedded video. <a href="video/ignite-camp-2026-recap.mp4">Download the video</a> instead.
      </video>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Loved A Session Or Camp?</h2>
    <p>Tag Advanced Genetics on Instagram or Facebook to share your story, or send it directly.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Share Your Story</a>
      <a href="gallery.html" class="btn btn-ghost">View Gallery</a>
    </div>
  </div>
</section>
"""
page("testimonials.html", "Testimonials", "Read what parents are saying about Adrian Joseph's IGNITE Basketball Camp 2026 and Advanced Genetics training programmes in Trinidad & Tobago.", "testimonials.html", testimonials, extra_og_image="images/community/ignite-training-gym.jpg")
print("testimonials done")
