// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__animated', 'animate__fadeInUp');
            }
        });
    }, observerOptions);

    // Observe all category cards
    document.querySelectorAll('.category-card').forEach(card => {
        observer.observe(card);
    });
});

// Add background animation
function createFloatingNotes() {
    const container = document.querySelector('.hero-section');
    const notes = '🎵🎶🎸🥁🎷🎺🎻';
    
    for (let i = 0; i < 20; i++) {
        const note = document.createElement('div');
        note.style.position = 'absolute';
        note.style.fontSize = Math.random() * 20 + 10 + 'px';
        note.style.opacity = Math.random() * 0.3 + 0.1;
        note.style.left = Math.random() * 100 + '%';
        note.style.top = Math.random() * 100 + '%';
        note.style.animation = `float ${Math.random() * 6 + 4}s ease-in-out infinite`;
        note.style.animationDelay = Math.random() * 5 + 's';
        note.textContent = notes[Math.floor(Math.random() * notes.length)];
        container.appendChild(note);
    }
}

// Uncomment to enable floating notes (can be heavy on performance)
// createFloatingNotes();


function scrollToCategories() {
    const categoriesSection = document.getElementById('categories');
    if (categoriesSection) {
        categoriesSection.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    } else {
        // Fallback: scroll down a bit
        window.scrollBy(0, 500);
    }
}





// Track playlist clicks
document.addEventListener('DOMContentLoaded', function() {
    // Track Spotify clicks
    document.querySelectorAll('a[href*="spotify.com"]').forEach(link => {
        link.addEventListener('click', function() {
            const playlistName = this.closest('.card').querySelector('.card-title').textContent;
            gtag('event', 'spotify_click', {
                'event_category': 'playlist',
                'event_label': playlistName
            });
        });
    });

    // Track Download clicks
    document.querySelectorAll('a[href*="drive.google.com"]').forEach(link => {
        link.addEventListener('click', function() {
            const playlistName = this.closest('.card').querySelector('.card-title').textContent;
            gtag('event', 'download_click', {
                'event_category': 'playlist',
                'event_label': playlistName
            });
        });
    });

    // Track category views
    document.querySelectorAll('.category-card a').forEach(link => {
        link.addEventListener('click', function() {
            const categoryName = this.closest('.card').querySelector('.card-title').textContent;
            gtag('event', 'category_view', {
                'event_category': 'navigation',
                'event_label': categoryName
            });
        });
    });
});