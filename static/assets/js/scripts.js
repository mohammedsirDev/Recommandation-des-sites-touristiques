/* MarocTour — main.js */

document.addEventListener('DOMContentLoaded', function () {


  // ── Favorite button toggle
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', function () {

    // Remove active from all links
    document.querySelectorAll('.nav-link')
      .forEach(l => l.classList.remove('active'));

    // Add active to clicked link
    this.classList.add('active');

  });
});

  // ── Star rating picker (modal)
  const stars = document.querySelectorAll('.star-pick');
  stars.forEach(star => {
    star.addEventListener('click', function () {
      const val = parseInt(this.dataset.val);
      stars.forEach((s, i) => {
        s.className = i < val ? 'fas fa-star star-pick lit' : 'far fa-star star-pick';
      });
    });
    star.addEventListener('mouseover', function () {
      const val = parseInt(this.dataset.val);
      stars.forEach((s, i) => {
        s.style.color = i < val ? '#f59e0b' : '';
      });
    });
    star.addEventListener('mouseout', () => {
      stars.forEach(s => { if (!s.classList.contains('lit')) s.style.color = ''; });
    });
  });

  // ── Filter star buttons
  document.querySelectorAll('.star-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.star-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
    });
  });

  // ── View toggle (grid / list)
  const gridBtn = document.getElementById('gridView');
  const listBtn = document.getElementById('listView');
  const grid = document.getElementById('sitesGrid');
  if (gridBtn && listBtn && grid) {
    gridBtn.addEventListener('click', () => {
      gridBtn.classList.add('active'); listBtn.classList.remove('active');
      grid.querySelectorAll('[class*="col-"]').forEach(c => {
        c.className = 'col-md-6 col-xl-4';
      });
    });
    listBtn.addEventListener('click', () => {
      listBtn.classList.add('active'); gridBtn.classList.remove('active');
      grid.querySelectorAll('[class*="col-"]').forEach(c => {
        c.className = 'col-12';
      });
    });
  }

  // ── Auto-dismiss alerts
  document.querySelectorAll('.alert-dismissible').forEach(el => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
      if (bsAlert) bsAlert.close();
    }, 4500);
  });

  // ── Animate cards on scroll (Intersection Observer)
  const cards = document.querySelectorAll('.site-card, .category-card');
  if ('IntersectionObserver' in window && cards.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'translateY(0)';
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });

    cards.forEach((c, i) => {
      c.style.opacity = '0';
      c.style.transform = 'translateY(20px)';
      c.style.transition = `opacity .4s ease ${i * 0.07}s, transform .4s ease ${i * 0.07}s`;
      io.observe(c);
    });
  }

});
