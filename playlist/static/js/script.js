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

    // Observe category and event cards
    document.querySelectorAll('.category-card, .event-card').forEach(card => {
        observer.observe(card);
    });

    // 3D Tilt Effect for Event Cards
    document.querySelectorAll('.event-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const tiltX = (centerY - y) / 25;
            const tiltY = (x - centerX) / 25;
            card.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
        });
    });
});

// Add background animation
function createFloatingNotes() {
    const container = document.querySelector('.hero-section, .events-section');
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

// Enable floating notes for events page
createFloatingNotes();