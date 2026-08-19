#!/usr/bin/env python3
from build import page

schedule = """
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">Plan Your Training</p>
    <h1>Schedule &amp; Membership</h1>
    <p>Programmes run year-round from Pleasantville Indoor Sports Arena and additional venues across South Trinidad.</p>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="note-box reveal" style="max-width:760px;margin:0 auto 56px;text-align:center;">
      <strong>Schedule and rates are updated seasonally.</strong> Contact Adrian directly for current training days, times, group sizes, and membership pricing. Availability is limited during camp weeks.
    </div>

    <div class="grid grid-2 reveal-stagger" style="max-width:940px;margin:0 auto;">
      <div class="tier">
        <h3>Private 1-on-1</h3>
        <p class="rate">Contact for schedule &amp; rates</p>
        <ul>
          <li>Individually tailored session plan</li>
          <li>Ball-handling, shooting, footwork, IQ</li>
          <li>Flexible scheduling by appointment</li>
          <li>Progress tracked session to session</li>
        </ul>
        <a href="contact.html" class="btn btn-dark btn-block">Enquire Now</a>
      </div>

      <div class="tier featured">
        <span class="flag">Most Popular</span>
        <h3>Small Group Training</h3>
        <p class="rate">Contact for schedule &amp; rates</p>
        <ul>
          <li>2&ndash;6 players per session</li>
          <li>Position-specific and skill-tier grouping</li>
          <li>Weekly sessions at Pleasantville Indoor Sports Arena</li>
          <li>Competitive drills and live reps</li>
        </ul>
        <a href="contact.html" class="btn btn-primary btn-block">Enquire Now</a>
      </div>

      <div class="tier">
        <h3>Team / Club Sessions</h3>
        <p class="rate">Contact for schedule &amp; rates</p>
        <ul>
          <li>Full practice planning &amp; systems</li>
          <li>Offensive and defensive installation</li>
          <li>Conditioning and game management</li>
          <li>Booked directly with your club or school</li>
        </ul>
        <a href="contact.html" class="btn btn-dark btn-block">Enquire Now</a>
      </div>

      <div class="tier">
        <h3>Camps &amp; Clinics</h3>
        <p class="rate">Contact for schedule &amp; rates</p>
        <ul>
          <li>IGNITE Basketball Camp &amp; Court to Court Caravan</li>
          <li>Multi-day, ages 5 through adult</li>
          <li>Skills, competition &amp; mentorship</li>
          <li>Registration opens ahead of each camp</li>
        </ul>
        <a href="news.html" class="btn btn-dark btn-block">See Camp Dates</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head center">
      <span class="watermark30" aria-hidden="true" style="right:50%;transform:translateX(50%);">30</span>
      <p class="eyebrow">Where We Train</p>
      <h2>Pleasantville Indoor Sports Arena</h2>
      <p class="section-lede" style="margin-left:auto;margin-right:auto;">Home base for regular training, with additional community venues across South Trinidad through the Court to Court Caravan.</p>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Get Current Availability</h2>
    <p>Reach out for this term's schedule, group openings, and membership rates.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Contact Adrian</a>
      <a href="tel:18684819414" class="btn btn-ghost">Call 1 (868) 481-9414</a>
    </div>
  </div>
</section>
"""
page("schedule.html", "Schedule & Membership", "Training schedule and membership information for Adrian Joseph's basketball programmes in Trinidad & Tobago. Contact for current rates and availability.", "schedule.html", schedule, extra_og_image="images/community/ignite-training-gym.jpg")
print("schedule done")
