#!/usr/bin/env python3
from build import page

services = """
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">What Adrian Offers</p>
    <h1>Training Programmes &amp; Services</h1>
    <p>Five ways to work with a coach who played Division I, competed professionally on four continents, and captained his country.</p>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="grid grid-3 reveal-stagger">
      <div class="card"><span class="card-num">01</span><h3>Private Training</h3><p>One-on-one skill development.</p><a href="#private" class="card-link">Details</a></div>
      <div class="card"><span class="card-num">02</span><h3>Team Training</h3><p>Practice planning and systems for clubs and schools.</p><a href="#team" class="card-link">Details</a></div>
      <div class="card"><span class="card-num">03</span><h3>Camps &amp; Clinics</h3><p>Multi-day intensives for every age group.</p><a href="#camps" class="card-link">Details</a></div>
    </div>
    <div class="grid grid-2 reveal-stagger" style="margin-top:28px;">
      <div class="card"><span class="card-num">04</span><h3>College / Pro Placement</h3><p>Scholarship and recruiting guidance from a certified agent.</p><a href="#placement" class="card-link">Details</a></div>
      <div class="card"><span class="card-num">05</span><h3>Speaking &amp; Consulting</h3><p>Motivational talks and programme consulting.</p><a href="#speaking" class="card-link">Details</a></div>
    </div>
  </div>
</section>

<section id="private" class="section section-white">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <p class="eyebrow">01 &middot; Private Training</p>
        <h2 style="font-size:clamp(26px,4vw,38px);color:var(--navy);margin:12px 0 16px;">One-On-One Development</h2>
        <p style="color:#33383f;font-size:17px;">Individual sessions built around ball-handling, shooting mechanics, footwork, finishing, and basketball IQ. Adrian works from the same fundamentals that carried him through the ACC and professional leagues in Spain, Qatar, and Mexico, adapted to the player's age, position, and goals.</p>
        <a href="contact.html" class="btn btn-dark" style="margin-top:6px;">Book A Private Session</a>
      </div>
      <div class="img-frame reveal"><img src="images/college/uva-dribble-mascot.jpg" alt="Adrian Joseph bringing the ball up the court for Virginia"></div>
    </div>
  </div>
</section>

<section id="team" class="section section-cream">
  <div class="container">
    <div class="two-col">
      <div class="img-frame reveal" style="order:2;"><img src="images/college/uva-huddle.jpg" alt="Team huddle during a Virginia Cavaliers game"></div>
      <div class="reveal" style="order:1;">
        <p class="eyebrow">02 &middot; Team Training</p>
        <h2 style="font-size:clamp(26px,4vw,38px);color:var(--navy);margin:12px 0 16px;">Systems For Clubs &amp; Schools</h2>
        <p style="color:#33383f;font-size:17px;">Structured sessions for existing teams: practice planning, offensive and defensive systems, conditioning, and game management, built on FIBA coaching methodology and years of leading St. Benedict's College and Advanced Genetics squads.</p>
        <a href="contact.html" class="btn btn-dark" style="margin-top:6px;">Enquire For Your Team</a>
      </div>
    </div>
  </div>
</section>

<section id="camps" class="section section-white">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <p class="eyebrow">03 &middot; Camps &amp; Clinics</p>
        <h2 style="font-size:clamp(26px,4vw,38px);color:var(--navy);margin:12px 0 16px;">IGNITE, Court to Court &amp; More</h2>
        <p style="color:#33383f;font-size:17px;">Multi-day camps and clinics combining skills training, competition, and mentorship, including the annual IGNITE Basketball Camp and the Court to Court Caravan, which brings coaching directly into communities across Trinidad. Programmes run for ages 5 through adult.</p>
        <a href="news.html" class="btn btn-dark" style="margin-top:6px;">See Upcoming Camps</a>
      </div>
      <div class="img-frame reveal"><img src="images/community/ignite-training-gym.jpg" alt="Young athlete training at an Advanced Genetics camp session"></div>
    </div>
  </div>
</section>

<section id="placement" class="section section-cream">
  <div class="container">
    <div class="two-col">
      <div class="img-frame reveal" style="order:2;"><img src="images/college/usa-commonwealth-classic.jpg" alt="Adrian Joseph at the Commonwealth Classic All-Star Game during his recruiting years"></div>
      <div class="reveal" style="order:1;">
        <p class="eyebrow">04 &middot; College / Pro Placement</p>
        <h2 style="font-size:clamp(26px,4vw,38px);color:var(--navy);margin:12px 0 16px;">Scholarship &amp; Recruiting Guidance</h2>
        <p style="color:#33383f;font-size:17px;">As a Sports Management Worldwide Certified Basketball Agent who was recruited by Miami, Villanova, Maryland, UConn, Penn State, Saint Joseph's, and Vanderbilt before choosing Virginia, Adrian guides student-athletes through scholarship preparation, highlight film, NCAA eligibility, and professional pathway planning.</p>
        <a href="contact.html" class="btn btn-dark" style="margin-top:6px;">Start The Conversation</a>
      </div>
    </div>
  </div>
</section>

<section id="speaking" class="section section-white">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <p class="eyebrow">05 &middot; Speaking &amp; Consulting</p>
        <h2 style="font-size:clamp(26px,4vw,38px);color:var(--navy);margin:12px 0 16px;">From La Romaine To The World Stage</h2>
        <p style="color:#33383f;font-size:17px;">Motivational talks and programme consulting for schools, corporate teams, and sports organizations, drawing on a journey from a Southern Region community with no elite basketball infrastructure to Division I basketball and a professional career across four countries.</p>
        <a href="contact.html" class="btn btn-dark" style="margin-top:6px;">Book Adrian To Speak</a>
      </div>
      <div class="img-frame reveal"><img src="images/press/infocus-magazine-cover.jpg" alt="Sports InFocus Magazine cover feature on Adrian Joseph"></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Not Sure Which Programme Fits?</h2>
    <p>Tell Adrian a bit about the player, and he'll point you to the right one.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Contact Adrian</a>
      <a href="schedule.html" class="btn btn-ghost">View Schedule &amp; Membership</a>
    </div>
  </div>
</section>
"""
page("services.html", "Services", "Private training, team training, camps and clinics, college and professional placement, and speaking and consulting with Adrian Joseph, NCAA Division I champion and former Trinidad & Tobago National Team Captain.", "services.html", services, extra_og_image="images/professional/pro-spain-warmup.jpg")
print("services done")
