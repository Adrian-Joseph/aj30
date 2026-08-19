#!/usr/bin/env python3
from build import page

items = [
    ("images/college/uva-gohoos-jumper.jpg","college","Rising for a jumper at John Paul Jones Arena"),
    ("images/college/uva-vs-unc.jpg","college","Guarding a North Carolina ball-handler"),
    ("images/college/uva-layup-georgiatech.jpg","college","Attacking the rim against Georgia Tech"),
    ("images/college/uva-vs-fsu-drive.jpg","college","Driving the baseline versus Florida State"),
    ("images/college/uva-dunk-scoreboard.jpg","college","Finishing above the rim for Virginia"),
    ("images/college/uva-dribble-mascot.jpg","college","Bringing the ball up the court, Virginia Cavaliers"),
    ("images/college/uva-huddle.jpg","college","Team huddle, Virginia Cavaliers"),
    ("images/college/uva-teammates.jpg","college","Sideline by sideline with Virginia teammates"),
    ("images/college/uva-championship-ring.jpg","college","ACC Championship ring"),
    ("images/college/usa-commonwealth-classic.jpg","college","Commonwealth Classic All-Star Game"),
    ("images/college/usa-brewster-teammates.jpg","college","With teammates at Brewster Academy"),
    ("images/college/usa-bergen-catholic-team.jpg","college","Bergen Catholic High School team photo"),
    ("images/college/usa-adidas-abcd-camp.jpg","college","Competing at the Adidas ABCD Camp"),

    ("images/professional/pro-spain-dunk-18.jpg","professional","Dunking professionally in Spain, #18"),
    ("images/professional/pro-dunk-fiba.jpg","professional","Finishing at the rim in professional competition"),
    ("images/professional/pro-mexico-team.jpg","professional","Team photo, Halcones UV, Mexico"),

    ("images/national-team/tt-federation-graphic.jpg","national-team","Featured by the National Basketball Federation of Trinidad and Tobago"),
    ("images/national-team/hooplife-la-romaine.jpg","national-team","Captaining La Romaine at the Hoop of Life Tournament"),
    ("images/national-team/caledonia-clippers-jumpshot.jpg","national-team","In action for the Caledonia Clippers"),
    ("images/national-team/caledonia-clippers-portrait.jpg","national-team","Caledonia Clippers, North Zone Champions"),

    ("images/community/ignite-training-gym.jpg","community","Skills training at an Advanced Genetics camp"),
    ("images/community/malick-eagles-team.jpg","community","A young Adrian with the Malick Eagles, Philadelphia"),
    ("images/community/young-adrian-la-romaine.jpg","community","A young Adrian Joseph in La Romaine, Trinidad"),
    ("images/profile/headshot.jpg","community","Adrian Joseph, professional headshot"),

    ("images/press/infocus-magazine-cover.jpg","press","Sports InFocus Magazine feature"),
    ("images/press/halftime-live-show.jpg","press","Guest appearance on HALF/TIME Live"),
    ("images/press/gatorade-poster.jpg","press","Gatorade Trinidad #WinFromWithin campaign"),
    ("images/press/mackeson-billboard.jpg","press","Mackeson Elevate Like A King campaign billboard"),
    ("images/press/mackeson-commercial-still.jpg","press","Still from the Mackeson television commercial"),
    ("images/press/caledonia-celebration.jpg","press","Championship celebration, Caledonia Clippers"),
    ("images/press/first-citizens-clipping.jpg","press","First Citizens Bank Sportsman of the Year press coverage"),
    ("images/press/adrian-joseph-30-poster.jpg","press","&ldquo;I Lived What I Teach&rdquo; campaign graphic"),
]

cat_labels = {"all":"All","college":"College (UVA)","professional":"Professional","national-team":"National Team","community":"Coaching & Community","press":"Press"}

filter_btns = "".join(
    f'<button class="filter-btn{" active" if k=="all" else ""}" data-filter="{k}">{v}</button>'
    for k,v in cat_labels.items()
)

grid_items = ""
for src, cat, cap in items:
    grid_items += f"""<div class="gallery-item" data-cat="{cat}" data-caption="{cap}">
      <img src="{src}" alt="{cap}" loading="lazy">
      <span class="tag">{cat_labels[cat]}</span>
    </div>\n"""

gallery = f"""
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">The Archive</p>
    <h1>Photo &amp; Video Gallery</h1>
    <p>From La Romaine playgrounds to NCAA arenas to professional courts in Spain, Qatar, and Mexico.</p>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="filter-bar reveal">
      {filter_btns}
    </div>
    <div class="gallery-grid reveal">
      {grid_items}
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="section-head">
      <span class="watermark30" aria-hidden="true">30</span>
      <p class="eyebrow">Camp Reel</p>
      <h2>IGNITE Basketball Camp 2026</h2>
      <p class="section-lede">A short recap from parent feedback collected after IGNITE Basketball Camp 2026.</p>
    </div>
    <div class="reveal" style="max-width:420px;">
      <video controls preload="metadata" style="width:100%;border-radius:4px;box-shadow:var(--shadow);" poster="images/community/ignite-training-gym.jpg">
        <source src="video/ignite-camp-2026-recap.mp4" type="video/mp4">
        Your browser does not support embedded video. <a href="video/ignite-camp-2026-recap.mp4">Download the video</a> instead.
      </video>
    </div>
  </div>
</section>

<div class="lightbox">
  <button class="lightbox-close" aria-label="Close">&times;</button>
  <button class="lightbox-nav lightbox-prev" aria-label="Previous image">&#8249;</button>
  <img src="" alt="">
  <button class="lightbox-nav lightbox-next" aria-label="Next image">&#8250;</button>
  <p class="lightbox-caption"></p>
</div>

<section class="cta-band">
  <div class="container">
    <h2>Want To Be In The Next Gallery Update?</h2>
    <p>Book a session or join the next camp, and tag Advanced Genetics on Instagram to be featured.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Book Training</a>
      <a href="https://www.instagram.com/adrianjosephelite" target="_blank" rel="noopener" class="btn btn-ghost">Follow on Instagram</a>
    </div>
  </div>
</section>
"""
page("gallery.html", "Gallery", "Photo and video gallery of Adrian Joseph across his College, professional, national team, and coaching career, plus press features and Advanced Genetics community camps.", "gallery.html", gallery, extra_og_image="images/college/uva-vs-duke-cox.jpg")
print("gallery done")
