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
