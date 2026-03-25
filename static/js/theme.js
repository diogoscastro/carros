document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('theme-toggle');
  const html = document.documentElement;

  const savedTheme = localStorage.getItem('theme') || 'light';
  html.setAttribute('data-bs-theme', savedTheme);

  if (toggleBtn) {
    toggleBtn.innerHTML = savedTheme === 'dark'
      ? '<i class="bi bi-sun"></i>'
      : '<i class="bi bi-moon"></i>';

    toggleBtn.addEventListener('click', () => {
      const currentTheme = html.getAttribute('data-bs-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';

      html.setAttribute('data-bs-theme', newTheme);
      localStorage.setItem('theme', newTheme);

      toggleBtn.innerHTML = newTheme === 'dark'
        ? '<i class="bi bi-sun"></i>'
        : '<i class="bi bi-moon"></i>';
    });
  }
});