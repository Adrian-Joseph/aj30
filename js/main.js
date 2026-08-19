// Adrian Joseph site — shared behavior
(function(){
  "use strict";

  /* Mobile nav toggle */
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if(toggle && links){
    toggle.addEventListener('click', function(){
      var open = links.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true':'false');
    });
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        links.classList.remove('open');
        toggle.classList.remove('open');
      });
    });
  }

  /* Scroll reveal */
  var revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
  if('IntersectionObserver' in window && revealEls.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold:0.12, rootMargin:'0px 0px -60px 0px' });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('in'); });
  }

  /* Header shadow on scroll */
  var header = document.querySelector('.site-header');
  if(header){
    window.addEventListener('scroll', function(){
      header.style.boxShadow = window.scrollY > 8 ? '0 8px 24px rgba(0,0,0,0.28)' : 'none';
    }, { passive:true });
  }

  /* Gallery filter */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var galleryItems = document.querySelectorAll('.gallery-item');
  if(filterBtns.length && galleryItems.length){
    filterBtns.forEach(function(btn){
      btn.addEventListener('click', function(){
        filterBtns.forEach(function(b){ b.classList.remove('active'); });
        btn.classList.add('active');
        var f = btn.getAttribute('data-filter');
        galleryItems.forEach(function(item){
          var show = (f === 'all') || item.getAttribute('data-cat') === f;
          item.classList.toggle('hide', !show);
        });
      });
    });
  }

  /* Lightbox */
  var lightbox = document.querySelector('.lightbox');
  if(lightbox && galleryItems.length){
    var lbImg = lightbox.querySelector('img');
    var lbCaption = lightbox.querySelector('.lightbox-caption');
    var visibleItems = function(){
      return Array.prototype.filter.call(galleryItems, function(i){ return !i.classList.contains('hide'); });
    };
    var current = 0;

    function openAt(idx){
      var items = visibleItems();
      if(!items.length) return;
      current = (idx + items.length) % items.length;
      var item = items[current];
      var img = item.querySelector('img');
      lbImg.src = img.getAttribute('src');
      lbImg.alt = img.getAttribute('alt') || '';
      lbCaption.textContent = item.getAttribute('data-caption') || img.getAttribute('alt') || '';
      lightbox.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function close(){
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
    }
    galleryItems.forEach(function(item, i){
      item.addEventListener('click', function(){
        var items = visibleItems();
        var idx = items.indexOf(item);
        openAt(idx < 0 ? 0 : idx);
      });
    });
    lightbox.querySelector('.lightbox-close').addEventListener('click', close);
    lightbox.querySelector('.lightbox-prev').addEventListener('click', function(){ openAt(current-1); });
    lightbox.querySelector('.lightbox-next').addEventListener('click', function(){ openAt(current+1); });
    lightbox.addEventListener('click', function(e){ if(e.target === lightbox) close(); });
    document.addEventListener('keydown', function(e){
      if(!lightbox.classList.contains('open')) return;
      if(e.key === 'Escape') close();
      if(e.key === 'ArrowLeft') openAt(current-1);
      if(e.key === 'ArrowRight') openAt(current+1);
    });
  }

  /* Testimonial slider (auto-rotate, dots) */
  var slider = document.querySelector('.testi-slider');
  if(slider){
    var slides = slider.querySelectorAll('.quote-card');
    var dotsWrap = document.querySelector('.testi-dots');
    var idx = 0, timer;
    if(slides.length > 1){
      slides.forEach(function(s, i){
        var dot = document.createElement('button');
        dot.className = 'testi-dot';
        dot.setAttribute('aria-label', 'Show testimonial ' + (i+1));
        dot.addEventListener('click', function(){ show(i); reset(); });
        dotsWrap.appendChild(dot);
      });
      function show(i){
        idx = (i + slides.length) % slides.length;
        slides.forEach(function(s, si){ s.style.display = si === idx ? 'block' : 'none'; });
        dotsWrap.querySelectorAll('.testi-dot').forEach(function(d, di){ d.classList.toggle('active', di === idx); });
      }
      function reset(){
        clearInterval(timer);
        timer = setInterval(function(){ show(idx+1); }, 6500);
      }
      show(0);
      reset();
    }
  }

  /* Contact form -> mailto */
  var contactForm = document.getElementById('contact-form');
  if(contactForm){
    contactForm.addEventListener('submit', function(e){
      e.preventDefault();
      var name = contactForm.querySelector('#cf-name').value.trim();
      var email = contactForm.querySelector('#cf-email').value.trim();
      var phone = contactForm.querySelector('#cf-phone').value.trim();
      var program = contactForm.querySelector('#cf-program').value;
      var message = contactForm.querySelector('#cf-message').value.trim();

      var subject = 'Training Inquiry: ' + (program || 'General') + ' — ' + name;
      var bodyLines = [
        'Name: ' + name,
        'Email: ' + email,
        'Phone: ' + (phone || 'Not provided'),
        'Program of interest: ' + (program || 'Not specified'),
        '',
        'Message:',
        message
      ];
      var mailto = 'mailto:advancedgenetics868@gmail.com'
        + '?subject=' + encodeURIComponent(subject)
        + '&body=' + encodeURIComponent(bodyLines.join('\n'));
      window.location.href = mailto;
    });
  }

  /* Current year in footer */
  document.querySelectorAll('.js-year').forEach(function(el){ el.textContent = new Date().getFullYear(); });

})();
