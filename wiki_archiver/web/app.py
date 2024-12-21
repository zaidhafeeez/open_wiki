"""
Flask web application for browsing archived Wikipedia articles.
"""

import os
from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS
from math import ceil
from datetime import datetime

from . import get_archived_articles

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask application instance
    """
    app = Flask(__name__, 
                template_folder='templates', 
                static_folder='static')
    CORS(app)  # Enable CORS for all routes
    
    ARTICLES_PER_PAGE = 20  # Number of articles per page
    
    @app.context_processor
    def inject_current_time():
        """
        Inject current time into all templates.
        
        Returns:
            Dict with current time
        """
        return {'current_time': datetime.now()}
    
    @app.route('/')
    def index():
        """
        Render the main index page with article categories.
        
        Returns:
            Rendered HTML template
        """
        # Get unique categories from archived articles
        articles = get_archived_articles()
        categories = sorted(set(
            cat.lower() 
            for article in articles 
            for cat in article.get('categories', [])
        ))
        
        return render_template(
            'index.html', 
            categories=categories,
            total_articles=len(articles)
        )
    
    @app.route('/articles')
    def list_articles():
        """
        List articles with pagination, category, and search filtering.
        
        Returns:
            JSON response with articles or rendered HTML
        """
        # Get query parameters
        category = request.args.get('category', '').strip()
        search_query = request.args.get('search', '').strip()
        page = max(1, int(request.args.get('page', 1)))
        
        # Retrieve and filter articles
        articles = get_archived_articles(category, search_query)
        
        # Sort articles by title
        articles.sort(key=lambda x: x.get('title', ''))
        
        # Pagination
        total_articles = len(articles)
        total_pages = ceil(total_articles / ARTICLES_PER_PAGE)
        start_idx = (page - 1) * ARTICLES_PER_PAGE
        end_idx = start_idx + ARTICLES_PER_PAGE
        paginated_articles = articles[start_idx:end_idx]
        
        # Prepare pagination context
        pagination_context = {
            'current_page': page,
            'total_pages': total_pages,
            'total_articles': total_articles,
            'has_prev': page > 1,
            'has_next': page < total_pages
        }
        
        # Check request type (JSON for AJAX, HTML for page load)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'articles': paginated_articles,
                'pagination': pagination_context
            })
        
        return render_template(
            'articles.html', 
            articles=paginated_articles, 
            selected_category=category,
            search_query=search_query,
            pagination=pagination_context
        )
    
    @app.route('/article/<path:title>')
    def view_article(title):
        """
        View details of a specific article.
        
        Args:
            title (str): Article title
        
        Returns:
            Rendered article details page
        """
        # Find the specific article
        articles = get_archived_articles()
        article = next(
            (a for a in articles if a.get('title') == title), 
            None
        )
        
        if not article:
            abort(404)
        
        return render_template(
            'article_detail.html', 
            article=article
        )
    
    @app.errorhandler(404)
    def page_not_found(e):
        """
        Custom 404 error handler.
        
        Returns:
            Rendered 404 error page
        """
        return render_template('404.html'), 404
    
    return app

def run_server(host='0.0.0.0', port=5000, debug=True):
    """
    Run the Flask development server.
    
    Args:
        host (str): Host to bind the server
        port (int): Port to run the server
        debug (bool): Enable debug mode
    """
    app = create_app()
    app.run(host=host, port=port, debug=debug)
