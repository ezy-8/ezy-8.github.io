document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const navMenu = document.getElementById('nav-menu');

  mobileMenuBtn.addEventListener('click', () => {
    navMenu.classList.toggle('show');
  });

  // Dark/Light Theme Toggle
  const themeToggle = document.getElementById('themeToggle');
  const currentTheme = localStorage.getItem('theme');

  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  }

  themeToggle.addEventListener('click', () => {
    let theme = document.documentElement.getAttribute('data-theme');
    if (theme === 'dark') {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('theme', 'light');
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    }
  });

  // Tab System
  const tabLinks = document.querySelectorAll('.tab-link');
  const sections = document.querySelectorAll('.section');

  function switchTab(targetId) {
    // Remove active classes
    tabLinks.forEach(link => link.classList.remove('active'));
    sections.forEach(section => section.classList.remove('active-tab'));

    // Add active class to target section and link
    const targetSection = document.getElementById(targetId);
    const targetLink = document.querySelector(`.tab-link[href="#${targetId}"]`);
    
    if (targetSection) targetSection.classList.add('active-tab');
    if (targetLink) targetLink.classList.add('active');
  }

  tabLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href').substring(1);
      switchTab(targetId);
      
      // Update URL hash without jumping
      history.pushState(null, null, `#${targetId}`);
      
      // Close mobile menu on link click
      if (navMenu.classList.contains('show')) {
        navMenu.classList.remove('show');
      }
    });
  });

  // Init default tab based on URL hash or default to 'about'
  const initialHash = window.location.hash.substring(1);
  if (initialHash && document.getElementById(initialHash)) {
    switchTab(initialHash);
  } else {
    switchTab('about'); // Default tab
  }
});
