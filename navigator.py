"""
Navigation module for Force of Will application.
This module provides navigation functions without creating circular imports.
"""

def go_landing(page):
    """Navigate to the landing page."""
    # Import here to avoid circular imports
    from landing import landing_page
    landing_page(page)

def go_browser(page):
    """Navigate to the card browser."""
    # Import here to avoid circular imports
    from CardBrowser.Browser import card_browser
    page.clean()
    card_browser(page)

def go_deck(page):
    """Navigate to the deck builder.""" 
    # Import here to avoid circular imports
    from DeckBuilder.Deck import deck_placeholder
    page.clean()
    deck_placeholder(page)