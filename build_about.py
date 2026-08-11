#!/usr/bin/env python3
from build import page

about = """
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">About Adrian</p>
    <h1>The Most Decorated Basketball Player in Trinidad &amp; Tobago's History</h1>
    <p>B.A. Anthropology (University of Virginia) &middot; FIBA Certified Coach &middot; SMWW Certified Basketball Agent</p>
    <div class="badge-row">
      <span class="badge">NCAA Division I Champion</span>
      <span class="badge">Former T&amp;T National Team Captain</span>
      <span class="badge">Founder, Advanced Genetics</span>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <p class="eyebrow">Where It Started</p>
        <h2 style="font-size:clamp(28px,4vw,40px);color:var(--navy);margin:12px 0 18px;">La Romaine, San Fernando</h2>
        <p style="color:#33383f;font-size:18px;">Adrian Joseph was born and raised in La Romaine, Trinidad and Tobago, the very community his club now works to transform. Standing 6 feet 7 inches tall, he showed exceptional athletic ability early, but there was no elite basketball development infrastructure in the Southern Region built to nurture that kind of talent.</p>
        <p style="color:#33383f;font-size:18px;">He began his basketball journey at St. Benedict's College in La Romaine, where he later returned as head coach. The absence of a structured pathway at home eventually pushed him to migrate to the United States on a basketball scholarship at age 14, in pursuit of academic and athletic opportunities that did not yet exist in Trinidad.</p>
      </div>
      <div class="img-frame reveal">
        <img src="images/community/young-adrian-la-romaine.jpg" alt="A young Adrian Joseph in La Romaine, Trinidad">
      </div>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="two-col">
      <div class="img-frame reveal" style="order:2;">
        <img src="images/college/uva-huddle.jpg" alt="Adrian Joseph in a Virginia Cavaliers team huddle">
      </div>
      <div class="reveal" style="order:1;">
        <p class="eyebrow">USA &amp; NCAA Division I</p>
        <h2 style="font-size:clamp(28px,4vw,40px);color:var(--navy);margin:12px 0 18px;">Three High Schools, One Goal</h2>
        <p style="color:#33383f;font-size:18px;">After relocating to the United States, Joseph spent three more years in high school, moving from Marianapolis Preparatory School in Thompson, Connecticut, to Bergen Catholic High School in Oradell, New Jersey, and finally to Brewster Academy in New Hampshire. Each move was made to compete at a higher level and gain more exposure. He rapidly became one of the country's elite prospects, earning multiple MVP honours, All-State selections, a spot among the nation's Top 100 ranked players, and a nomination for the McDonald's All-American Game, a rare honour for a player from Trinidad and Tobago.</p>
        <p style="color:#33383f;font-size:18px;">Recruitment interest followed from Miami, Villanova, Maryland, UConn, Penn State, Saint Joseph's, Vanderbilt, and others. He chose the University of Virginia, where he played NCAA Division I basketball in the Atlantic Coast Conference, served as team co-captain, became the programme's 7th all-time leading three-point shooter, and won an ACC Regular Season Championship, graduating with a Bachelor of Arts in Anthropology in 2008.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <p class="eyebrow">Professional &amp; International</p>
        <h2 style="font-size:clamp(28px,4vw,40px);color:var(--navy);margin:12px 0 18px;">Four Countries, One Jersey Number</h2>
        <p style="color:#33383f;font-size:18px;">Joseph's professional career carried him across Europe, the Middle East, and Latin America, with stints at Ciudad de Vigo Basketball Club and Beirasar Rosalia in Spain's LEB League, Qatar Professional Basketball in Doha, Halcones UV in Mexico's LNBP, and the Blazers in the British Virgin Islands.</p>
        <p style="color:#33383f;font-size:18px;">Throughout, he represented Trinidad and Tobago internationally as Captain of the National Basketball Team, competing in the FIBA 3x3 AmeriCup, the FIBA 3x3 Copa Latino Americana in Puerto Rico, the FIBA 3x3 World Cup Qualifier, and the 2022 Commonwealth Games in Birmingham, UK. Domestically, he won championships and MVP honours with the La Romaine Jet Stars, Petrotrin Jazz, the Trinidad and Tobago Police Service, and the Caledonia Clippers.</p>
      </div>
      <div class="img-frame reveal">
        <img src="images/professional/pro-spain-dunk-18.jpg" alt="Adrian Joseph dunking during a professional game in Spain, wearing jersey number 18">
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <div class="two-col">
      <div class="img-frame reveal" style="order:2;">
        <img src="images/community/ignite-training-gym.jpg" alt="Young athlete training at an Advanced Genetics camp session">
      </div>
      <div class="reveal" style="order:1;">
        <p class="eyebrow on-dark">Coming Home</p>
        <h2 style="color:#fff;font-size:clamp(28px,4vw,40px);margin:12px 0 18px;">Building What Wasn't There For Him</h2>
        <p style="color:#c3cad8;font-size:18px;">Upon returning to Trinidad, Joseph became head coach of the St. Benedict's College basketball team and began developing grassroots programmes for young athletes in the Southern Region. In 2019, he founded Advanced Genetics Sports &amp; Cultural Club, a registered non-profit dedicated to youth development through basketball, education, mentorship, and community engagement.</p>
        <p style="color:#c3cad8;font-size:18px;">He also serves as Vice President of Operation Impact La Romaine, President of the La Romaine Community Council, and Managing Director of the Caribbean Basketball Association, and holds a Sports Management Worldwide Player Agent Representative credential alongside his FIBA coaching certification.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container" style="text-align:center;">
    <p class="pull-quote" style="margin:0 auto 22px;max-width:20ch;">&ldquo;Opportunity changes lives.&rdquo;</p>
    <p style="color:#565f6d;font-size:17px;max-width:56ch;margin:0 auto;">&mdash; Adrian Joseph, on why he founded Advanced Genetics Sports &amp; Cultural Club</p>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="two-col" style="align-items:center;">
      <div class="reveal" style="text-align:center;">
        <img src="images/logo/advanced-genetics-logo.png" alt="Advanced Genetics Sports and Cultural Club logo" style="max-width:340px;margin:0 auto;">
      </div>
      <div class="reveal">
        <p class="eyebrow">The Club</p>
        <h2 style="font-size:clamp(26px,4vw,36px);color:var(--navy);margin:12px 0 16px;">Advanced Genetics Sports &amp; Cultural Club</h2>
        <p style="color:#565f6d;font-size:17px;">Founded in 2019 and based in La Romaine, San Fernando, Advanced Genetics is a registered non-profit youth development organization. It is the engine behind Adrian's community camps, school outreach, and mentorship work, and the training programmes on this site operate alongside it.</p>
        <a href="services.html" class="btn btn-dark" style="margin-top:8px;">See Training Programmes</a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Train With A Coach Who's Lived It</h2>
    <p>From La Romaine to Division I to professional basketball on four continents, Adrian brings every mile of that road into every session.</p>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">Get In Touch</a>
      <a href="achievements.html" class="btn btn-ghost">See Full Achievements</a>
    </div>
  </div>
</section>
"""
page("about.html", "About", "Adrian Joseph's journey from La Romaine, Trinidad to NCAA Division I basketball at the University of Virginia, a professional career across four countries, and Captain of the Trinidad & Tobago National Team.", "about.html", about, extra_og_image="images/college/uva-huddle.jpg")
print("about done")
