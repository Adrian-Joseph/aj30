#!/usr/bin/env python3
from build import page

news = """
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">Stay In The Loop</p>
    <h1>News &amp; Upcoming Events</h1>
    <p>Three events, one mission: building players and changing lives across Trinidad &amp; Tobago.</p>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="section-head">
      <span class="watermark30" aria-hidden="true">30</span>
      <p class="eyebrow">2026 Calendar</p>
      <h2>Upcoming Events</h2>
    </div>

    <div class="reveal">
      <div class="event-row">
        <div class="event-date"><span class="d">13&ndash;17</span><span class="m">July</span></div>
        <div class="event-info">
          <h3>IGNITE Basketball Camp 2026</h3>
          <p>9:00 AM&ndash;2:00 PM &middot; Pleasantville Indoor Sports Arena &middot; Five days of elite training, skill development, competitions &amp; games, mentorship &amp; life lessons.</p>
        </div>
        <a href="contact.html" class="btn btn-dark">Register Interest</a>
      </div>

      <div class="event-row">
        <div class="event-date"><span class="d">20&ndash;25</span><span class="m">Venues</span></div>
        <div class="event-info">
          <h3>Court to Court Caravan 2026</h3>
          <p>Taking basketball to the community across 20&ndash;25 venues throughout Trinidad. Youth development, skill training &amp; games, community engagement, exposure &amp; opportunities. One court, one community, one game.</p>
        </div>
        <a href="contact.html" class="btn btn-dark">Register Interest</a>
      </div>

      <div class="event-row">
        <div class="event-date"><span class="d">17&ndash;21</span><span class="m">August</span></div>
        <div class="event-info">
          <h3>USA Coaches Collaboration Camp</h3>
          <p>9:00 AM&ndash;2:00 PM &middot; Pleasantville Indoor Sports Arena &middot; Train with elite USA coaches for high-level instruction, competitions &amp; showcase, scholarship &amp; exposure opportunities.</p>
        </div>
        <a href="contact.html" class="btn btn-dark">Register Interest</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="section-head">
      <span class="watermark30" aria-hidden="true">30</span>
      <p class="eyebrow">In The Press</p>
      <h2>Media &amp; Recognition</h2>
    </div>
    <div class="reveal" style="background:#fff;border:1px solid var(--line-dark);border-radius:4px;padding:6px 28px;">
      <div class="press-card">
        <img src="images/press/infocus-magazine-cover.jpg" alt="Sports InFocus Magazine cover feature on Adrian Joseph">
        <div>
          <h3>Sports InFocus Magazine: &ldquo;Braving Basketball&rdquo;</h3>
          <p>Featured as the driving force behind the next generation of players in Trinidad and Tobago basketball.</p>
        </div>
      </div>
      <div class="press-card">
        <img src="images/press/halftime-live-show.jpg" alt="Adrian Joseph as a guest on the HALF/TIME live show">
        <div>
          <h3>Guest Appearance, HALF/TIME Live</h3>
          <p>Joined fellow Trinidad and Tobago basketball figure Kemrick Julien for a live conversation on the local game.</p>
        </div>
      </div>
      <div class="press-card">
        <img src="images/press/gatorade-poster.jpg" alt="Gatorade Trinidad basketball sports poster featuring Adrian Joseph">
        <div>
          <h3>Gatorade Trinidad &ldquo;#WinFromWithin&rdquo;</h3>
          <p>Featured athlete for Gatorade's basketball sports poster and hydration campaign.</p>
        </div>
      </div>
      <div class="press-card">
        <img src="images/press/mackeson-billboard.jpg" alt="Mackeson Elevate Like A King campaign billboard featuring Adrian Joseph">
        <div>
          <h3>Mackeson &ldquo;Elevate #LikeAKing&rdquo;</h3>
          <p>Face of Mackeson's national billboard and television campaign built around the game's elevation.</p>
        </div>
      </div>
      <div class="press-card">
        <img src="images/press/first-citizens-clipping.jpg" alt="Newspaper coverage of Adrian Joseph's First Citizens Bank Sportsman of the Year nomination">
        <div>
          <h3>First Citizens Bank Sportsman of the Year</h3>
          <p>Nominated in both 2021 and 2022, with coverage in the national press.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Don't Miss The Next Camp</h2>
    <p>Spots are limited for every IGNITE, Caravan, and USA Coaches session. Reach out to register early.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Register Interest</a>
      <a href="https://www.instagram.com/advancedgenetics868" target="_blank" rel="noopener" class="btn btn-ghost">Follow For Updates</a>
    </div>
  </div>
</section>
"""
page("news.html", "News & Events", "Upcoming Adrian Joseph and Advanced Genetics events including IGNITE Basketball Camp 2026, the Court to Court Caravan, and the USA Coaches Collaboration Camp, plus press features.", "news.html", news, extra_og_image="images/press/infocus-magazine-cover.jpg")
print("news done")
