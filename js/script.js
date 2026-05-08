(function () {
    'use strict';

    // Mobile nav toggle
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.main-nav');
    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            nav.classList.toggle('open');
            const expanded = nav.classList.contains('open');
            toggle.setAttribute('aria-expanded', expanded);
        });
    }

    // Mobile dropdown toggles
    document.querySelectorAll('.main-nav .has-dropdown > a').forEach(function (link) {
        link.addEventListener('click', function (e) {
            if (window.innerWidth <= 720) {
                e.preventDefault();
                this.parentElement.classList.toggle('open');
            }
        });
    });

    // Modal handling for Enquiry
    const modal = document.getElementById('enquire-modal');
    const openers = document.querySelectorAll('[data-open-modal="enquire"]');
    const closer = modal ? modal.querySelector('.modal-close') : null;

    function openModal() {
        if (!modal) return;
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
    }
    function closeModal() {
        if (!modal) return;
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }
    openers.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            openModal();
        });
    });
    if (closer) closer.addEventListener('click', closeModal);
    if (modal) {
        modal.addEventListener('click', function (e) {
            if (e.target === modal) closeModal();
        });
    }
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeModal();
    });

    // Animated counter for stats
    const counters = document.querySelectorAll('[data-count]');
    if (counters.length && 'IntersectionObserver' in window) {
        const obs = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseInt(el.getAttribute('data-count'), 10);
                    const duration = 1400;
                    const start = performance.now();
                    function tick(now) {
                        const p = Math.min((now - start) / duration, 1);
                        const eased = 1 - Math.pow(1 - p, 3);
                        el.textContent = Math.floor(eased * target).toLocaleString();
                        if (p < 1) requestAnimationFrame(tick);
                        else el.textContent = target.toLocaleString();
                    }
                    requestAnimationFrame(tick);
                    obs.unobserve(el);
                }
            });
        }, { threshold: 0.4 });
        counters.forEach(function (c) { obs.observe(c); });
    }

    // Form submit (no backend — show thanks)
    document.querySelectorAll('form[data-stub]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            if (btn) {
                const orig = btn.textContent;
                btn.textContent = 'Thank you! We\'ll be in touch.';
                btn.disabled = true;
                setTimeout(function () {
                    btn.textContent = orig;
                    btn.disabled = false;
                    form.reset();
                    closeModal();
                }, 2400);
            }
        });
    });
})();
