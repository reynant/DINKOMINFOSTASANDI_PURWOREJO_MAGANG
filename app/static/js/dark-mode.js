document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const htmlElement = document.documentElement; // Target the <html> tag

    // Function to apply the theme
    const applyTheme = (isDark) => {
        if (isDark) {
            htmlElement.classList.add('dark');
            darkModeToggle.checked = true;
        } else {
            htmlElement.classList.remove('dark');
            darkModeToggle.checked = false;
        }
    };

    // Check for saved theme in localStorage on page load
    // 1. Check localStorage first
    if (localStorage.theme === 'dark') {
        applyTheme(true);
    // 2. If no setting in localStorage, check OS/browser preference
    } else if (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        applyTheme(true);
    // 3. Default to light mode
    } else {
        applyTheme(false);
    }

    // Event listener for the toggle switch
    darkModeToggle.addEventListener('change', () => {
        if (darkModeToggle.checked) {
            localStorage.theme = 'dark';
            applyTheme(true);
        } else {
            localStorage.theme = 'light';
            applyTheme(false);
        }
    });
});