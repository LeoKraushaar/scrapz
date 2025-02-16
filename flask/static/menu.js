document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('menu-btn');
    const closeBtn = document.getElementById('close-btn');
    const menuOverlay = document.getElementById('menu-overlay');
    const siteHeader = document.getElementById('site-header');
  
    menuBtn.addEventListener('click', () => {
      menuOverlay.classList.add('active');
      siteHeader.classList.add('overlay-active'); 
      menuBtn.style.display = 'none';
      closeBtn.style.display = 'block';
    });
  
    closeBtn.addEventListener('click', () => {
      menuOverlay.classList.remove('active');
      siteHeader.classList.remove('overlay-active'); 
      closeBtn.style.display = 'none';
      menuBtn.style.display = 'block';
    });
  });
  