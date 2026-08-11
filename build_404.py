#!/usr/bin/env python3
from build import page

nf = """
<section class="hero" style="min-height:70vh;">
  <div class="hero-media"><img src="images/professional/pro-dunk-fiba.jpg" alt=""></div>
  <div class="hero-scrim"></div>
  <span class="hero-jersey" aria-hidden="true">404</span>
  <div class="hero-inner">
    <p class="eyebrow hero-eyebrow">Out Of Bounds</p>
    <h1 class="hero-title"><span>Page Not</span><span>Found</span></h1>
    <p class="hero-sub">That page doesn't exist. Let's get you back on the court.</p>
    <div class="hero-actions">
      <a href="index.html" class="btn btn-primary">Back to Home</a>
      <a href="contact.html" class="btn btn-ghost">Contact Adrian</a>
    </div>
  </div>
</section>
"""
page("404.html", "Page Not Found", "This page could not be found.", "", nf)
print("404 done")
