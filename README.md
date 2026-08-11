# Adrian Joseph — Elite Basketball Training Website

A static, mobile-friendly website for Adrian Joseph: former Trinidad & Tobago
National Team Captain, NCAA Division I champion (University of Virginia),
and founder of Advanced Genetics Sports & Cultural Club.

No build step, no framework, no dependencies. Plain HTML, CSS, and
JavaScript, ready to host on GitHub Pages as-is.

## Pages

- `index.html` — Home
- `about.html` — About Adrian
- `achievements.html` — Playing & coaching record
- `services.html` — Training programmes
- `schedule.html` — Schedule & membership
- `gallery.html` — Photo & video gallery (filterable + lightbox)
- `testimonials.html` — Camp parent feedback
- `news.html` — Events & press
- `contact.html` — Contact form (opens a pre-filled email) & map
- `404.html` — Custom not-found page

## Hosting on GitHub Pages (repo: `aj30`)

1. Create a new **public** repository on GitHub named `aj30`.
2. Upload every file in this folder to the repo, keeping the folder
   structure exactly as-is (`css/`, `js/`, `images/`, `video/` must stay
   alongside the `.html` files). Easiest way from a computer:

   ```bash
   cd aj30
   git init
   git add .
   git commit -m "Launch site"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/aj30.git
   git push -u origin main
   ```

3. On GitHub, go to the repo's **Settings → Pages**.
4. Under "Build and deployment", set **Source** to `Deploy from a branch`,
   branch `main`, folder `/ (root)`. Save.
5. GitHub will publish the site at:
   `https://YOUR-USERNAME.github.io/aj30/`
   (takes 1–2 minutes on the first deploy)
6. Optional: to use a custom domain later, add a `CNAME` file with your
   domain and configure DNS per GitHub's custom domain docs.

## Editing content later

Every page was generated from a small Python script (`build_pages.py`,
`build_about.py`, etc., driven by shared templates in `build.py`) purely
as a development convenience — you do **not** need Python or to run
anything to host or update the site. To edit copy, images, or layout, you
have two options:

- **Quick edits:** open the relevant `.html` file directly and edit the
  text or `<img src="...">` paths. No build step required.
- **Regenerating pages:** if you'd rather edit the Python source (useful
  for keeping the header/nav/footer consistent across all 9 pages), edit
  the relevant `build_*.py` file and run `python3 build_pages.py` (etc.)
  locally, or hand the repo back to Claude and describe the change.

## Images

Photos are organized by category under `images/`:
`college/`, `professional/`, `national-team/`, `community/`, `press/`,
`profile/`, `hero/`, `logo/`. The Gallery page's filter buttons and photo
grid pull directly from these folders — add a new photo to the right
folder and add one line to `build_gallery.py`'s `items` list (or just
copy an existing `<div class="gallery-item">` block directly in
`gallery.html`).

## Known placeholders to fill in

- **Schedule & membership rates** (`schedule.html`): currently reads
  "Contact for schedule & rates" throughout, as requested. Replace with
  real pricing/times whenever ready.
- **Contact form**: submits via a `mailto:` link (opens the visitor's
  email app pre-filled, addressed to advancedgenetics868@gmail.com). If
  you later want real in-page email delivery without opening a mail app,
  a free service like Formspree can be wired in with a few lines of JS.

## Social links

Instagram (personal), Instagram (club), TikTok, and YouTube are linked in
the header, footer, and Contact page. Facebook is linked in the footer
with a placeholder handle (`advancedgenetics868`) — confirm/update the
URL in `build.py`'s `SOCIAL_LINKS` dict (or find-and-replace across the
`.html` files) once you have the exact Facebook page link.

## Before going live

`robots.txt` and `sitemap.xml` contain a placeholder
`YOUR-USERNAME.github.io/aj30` URL. Once the repo is live, replace
`YOUR-USERNAME` in both files with the actual GitHub username.
