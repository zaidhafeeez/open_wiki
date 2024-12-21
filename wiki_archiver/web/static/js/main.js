document.addEventListener('DOMContentLoaded', function() {
    // Category filter functionality
    const categoryLinks = document.querySelectorAll('.list-group-item');
    
    categoryLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const category = this.textContent.trim();
            
            fetch(`/articles?category=${encodeURIComponent(category)}`)
                .then(response => response.json())
                .then(articles => {
                    // Update articles list dynamically (if on articles page)
                    const articlesList = document.querySelector('.list-group');
                    if (articlesList) {
                        articlesList.innerHTML = articles.map(article => `
                            <a href="/article/${encodeURIComponent(article.title)}" 
                               class="list-group-item list-group-item-action">
                                <div class="d-flex w-100 justify-content-between">
                                    <h5 class="mb-1">${article.title}</h5>
                                    <small>
                                        Categories: ${article.categories ? article.categories.join(', ') : 'N/A'}
                                    </small>
                                </div>
                                <p class="mb-1">
                                    ${article.summary ? article.summary.substring(0, 200) + '...' : 'No summary available'}
                                </p>
                            </a>
                        `).join('');
                    }
                })
                .catch(error => {
                    console.error('Error fetching articles:', error);
                });
        });
    });
});

// Performance optimizations and utility functions

// Implement a simple resource prefetching mechanism
const ResourcePrefetcher = {
    prefetchedUrls: new Set(),
    
    prefetch: function(url) {
        if (this.prefetchedUrls.has(url)) return;
        
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = url;
        link.as = 'document';
        document.head.appendChild(link);
        
        this.prefetchedUrls.add(url);
    },
    
    preconnect: function(url) {
        const link = document.createElement('link');
        link.rel = 'preconnect';
        link.href = url;
        document.head.appendChild(link);
    }
};

// Performance tracking
const PerformanceTracker = {
    init: function() {
        if (!window.performance) return;
        
        window.addEventListener('load', () => {
            const timing = window.performance.timing;
            const loadTime = timing.loadEventEnd - timing.navigationStart;
            
            console.log(`Page load time: ${loadTime}ms`);
            
            // Optional: Send performance data to analytics
            this.sendPerformanceData(loadTime);
        });
    },
    
    sendPerformanceData: function(loadTime) {
        // Placeholder for sending performance metrics
        // Could be integrated with Google Analytics, custom analytics, etc.
        try {
            if (window.ga) {
                window.ga('send', 'timing', {
                    'timingCategory': 'Page Load',
                    'timingVar': 'load',
                    'timingValue': loadTime
                });
            }
        } catch (error) {
            console.error('Error sending performance data', error);
        }
    }
};

// Initialize performance tracking
PerformanceTracker.init();

// Preconnect to critical domains
ResourcePrefetcher.preconnect('https://cdn.jsdelivr.net');

// Add event listeners for hover prefetching
document.addEventListener('DOMContentLoaded', () => {
    const prefetchLinks = document.querySelectorAll('[data-prefetch]');
    
    prefetchLinks.forEach(link => {
        link.addEventListener('mouseenter', (event) => {
            const url = event.currentTarget.getAttribute('data-prefetch');
            ResourcePrefetcher.prefetch(url);
        });
    });
});

// Optional: Implement a simple lazy loading mechanism
const LazyLoader = {
    init: function() {
        const lazyImages = document.querySelectorAll('.lazy-load');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const image = entry.target;
                        image.src = image.dataset.src;
                        image.classList.remove('lazy-load');
                        observer.unobserve(image);
                    }
                });
            });
            
            lazyImages.forEach(image => imageObserver.observe(image));
        } else {
            // Fallback for browsers without IntersectionObserver
            lazyImages.forEach(image => {
                image.src = image.dataset.src;
                image.classList.remove('lazy-load');
            });
        }
    }
};

// Initialize lazy loading
LazyLoader.init();
