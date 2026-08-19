#!/usr/bin/env python3
from build import page

achievements = """
<section class="page-hero">
  <span class="hero-jersey" style="opacity:0.55;" aria-hidden="true">30</span>
  <div class="container" style="position:relative;z-index:1;">
    <p class="eyebrow on-dark">The Full Record</p>
    <h1>Playing &amp; Coaching Achievements</h1>
    <p>A career built across high school, NCAA Division I, professional, and international basketball, laid out era by era.</p>
  </div>
</section>

<section class="section section-white">
  <div class="container">
    <div class="two-col" style="align-items:center;margin-bottom:20px;">
      <div class="reveal">
        <p class="eyebrow">National Colours</p>
        <h2 style="font-size:clamp(24px,3.4vw,32px);color:var(--navy);margin:10px 0 14px;">Captain, Trinidad &amp; Tobago</h2>
        <p style="color:#565f6d;font-size:17px;">Recognized by the National Basketball Federation of Trinidad and Tobago across a national team career spanning FIBA 3x3 competition and the Commonwealth Games.</p>
      </div>
      <div class="img-frame reveal">
        <img src="images/national-team/tt-federation-graphic.jpg" alt="Adrian Joseph featured by the National Basketball Federation of Trinidad and Tobago, wearing jersey number 30">
      </div>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="report reveal">

      <div class="report-era">
        <div class="report-era-head"><h3>High School &mdash; USA</h3><span class="era-range">2000&ndash;2004</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Marianapolis Preparatory School</span>, Thompson, Connecticut: Eastern Connecticut Conference All-State Team, All-Tournament Team, Conference MVP, Conference Champions (2000&ndash;01).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Bergen Catholic High School</span>, Oradell, New Jersey: 1st Team All-County (2001, 2003), New Jersey Parochial A MVP, 2nd Team All-State, Charlie Webber All-American Game, New Jersey All-Star Team, Adidas ABCD Camp (2003).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Brewster Academy</span>, New Hampshire: 2004 McDonald's All-American Nominee, #1 Ranked Player in New Hampshire, First-Team All-New England Class A, National Prep School Invitational All-Tournament, Commonwealth Classic All-Star Game (Richmond, VA), played AAU with the New York Gauchos and New York Elite.</p></div>
        </div>
      </div>

      <div class="report-era">
        <div class="report-era-head"><h3>College &mdash; University of Virginia</h3><span class="era-range">2004&ndash;2008</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p>NCAA Division I basketball, Atlantic Coast Conference (ACC), one of the most competitive conferences in the country.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">ACC Regular Season Conference Champions.</span></p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Named <span class="highlight">ACC Rookie of the Week</span> after scoring a team-high 19 points in 32 minutes in his first collegiate start, versus Wake Forest (1/2/05).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Team Co-Captain.</span></p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">7th all-time leading 3-point shooter</span> in University of Virginia history.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Graduated with a Bachelor of Arts in Anthropology, 2008.</p></div>
        </div>
      </div>

      <div class="report-era">
        <div class="report-era-head"><h3>Professional Basketball</h3><span class="era-range">Europe &middot; Middle East &middot; Americas</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Ciudad de Vigo Basketball Club</span> &amp; <span class="highlight">Beirasar Rosalia Basketball Team</span>, Spain (LEB League).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Qatar Professional Basketball</span>, Doha, Qatar.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Halcones UV Basketball Club</span>, Xalapa, Mexico (LNBP).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Blazers</span>, British Virgin Islands.</p></div>
        </div>
      </div>

      <div class="report-era">
        <div class="report-era-head"><h3>Trinidad &amp; Tobago &mdash; Domestic</h3><span class="era-range">Club &amp; League</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">La Romaine Jet Stars Basketball Club</span> &mdash; Captain, Ministry of National Security Hoop of Life Tournament Champions (also 4th place finish), Hoop of Life MVP honours.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Petrotrin Jazz Basketball Club</span>, Pleasantville &mdash; Mackeson Super 10 Basketball Champion and MVP, 2014.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Trinidad and Tobago Police Service Basketball Team</span> &mdash; North Zone Champions, National Champs of Champs winner, National All-Star Game MVP, Champs of Champs MVP.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Caledonia Clippers</span> &mdash; North Zone Champions, North Zone MVP.</p></div>
        </div>
      </div>

      <div class="report-era">
        <div class="report-era-head"><h3>National Team &mdash; Trinidad &amp; Tobago</h3><span class="era-range">Captain</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">FIBA 3x3 AmeriCup</span> &mdash; Semifinalist.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">FIBA 3x3 Copa Latino Americana</span>, Puerto Rico.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">2022 Commonwealth Games</span>, Birmingham, UK.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">FIBA 3x3 World Cup Qualifier.</span></p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Served as <span class="highlight">Captain</span> throughout his national team tenure.</p></div>
        </div>
      </div>

      <div class="report-era">
        <div class="report-era-head"><h3>Coaching &amp; Leadership</h3><span class="era-range">2012&ndash;Present</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p>Assistant Basketball Coach, Ministry of Sport and Youth Affairs Sports Camp, Barrackpore Secondary School (2007).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Head Basketball Coach, Skinner Park, San Fernando (2012) and Pleasantville Indoor Arena (2013).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Head Coach, St. Benedict's College basketball team, La Romaine.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Founder &amp; President</span>, Advanced Genetics Sports and Cultural Club (2019&ndash;present).</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">President</span>, La Romaine Community Council.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Vice President</span>, Operation Impact La Romaine.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">Managing Director</span>, Caribbean Basketball Association.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Level 1 Coaching Certificate, National Basketball Federation of Trinidad and Tobago; FIBA Certified Coach; Player Agent Representative, Sports Management Worldwide, U.S.A.</p></div>
        </div>
      </div>

      <div class="report-era">
        <div class="report-era-head"><h3>Honours &amp; Recognition</h3><span class="era-range">Selected</span></div>
        <div class="report-era-body">
          <div class="report-row"><span class="bullet">&mdash;</span><p>Featured on the <span class="highlight">Mackeson brand poster</span> and <span class="highlight">Gatorade basketball sports poster</span>.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p><span class="highlight">First Citizens Bank Sportsman of the Year</span> nominee, 2021 and 2022.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Penal/Debe Regional Corporation <span class="highlight">Sportsman of the Year</span>, 2013.</p></div>
          <div class="report-row"><span class="bullet">&mdash;</span><p>Featured in <span class="highlight">Sports InFocus Magazine</span>: &ldquo;Braving Basketball &mdash; Driving Force Behind the Next Generation of Players.&rdquo;</p></div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Bring That Experience To Your Game</h2>
    <p>Every drill in Adrian's programmes is shaped by what actually gets recognized at the college and professional level.</p>
    <div class="cta-actions">
      <a href="services.html" class="btn btn-primary">See Training Programmes</a>
      <a href="contact.html" class="btn btn-ghost">Book A Session</a>
    </div>
  </div>
</section>
"""
page("achievements.html", "Achievements", "The complete playing and coaching record of Adrian Joseph, from high school All-American nominations through NCAA Division I, professional basketball in Spain, Qatar and Mexico, and Captain of Trinidad & Tobago.", "achievements.html", achievements, extra_og_image="images/college/uva-championship-ring.jpg")
print("achievements done")
