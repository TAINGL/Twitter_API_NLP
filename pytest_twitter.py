"""
Mini projet Twitter

Etape 3:
Créer une fonction qui compte le nombre de mots d'une phrase, un fonction qui prend en entrée une phrase et qui ressort une liste de mots sans les stopwords 
=> NEW : Faire des tests unitaires pour chaque fonction !

Run: pytest -q pytest_twitter.py
"""

import pytest
from apply_twitter import tweet_lower, tweet_tokenisation, del_stop_word, word_number

class TweetTest:
    """
    Test case utilisé pour tester les fonctions de NLP
    """
    def test_tweet_lower(self):
        """
        Test le fonctionnement de la fonction 'lower' sur une phrase
        """
        test_sentence = "Bonjour le #monde, ceci est un test de fonctionnement @twitter."  
        elt = tweet_lower(test_sentence)
        expected = 'bonjour le #monde, ceci est un test de fonctionnement @twitter.' 
        assert elt == expected
        
    def test_tweet_tokenisation(self):
        """
        Test le fonctionnement de la fonction 'tokenisation' sur une phrase
        """
        test_sentence = "Bonjour le #monde, ceci est un test de fonctionnement @twitter."  
        elt = tweet_tokenisation(test_sentence)
        expected = ['Bonjour','le','monde','ceci','est','un','test','de','fonctionnement','twitter']
        assert elt == expected
    
    def test_del_stop_word(self):
        """
        Test le fonctionnement de la fonction 'stop-word' sur une phrase (au préalable - lower only)
        """
        test_sentence = "Bonjour le #monde, ceci est un test de fonctionnement @twitter."    
        elt = del_stop_word(test_sentence)
        expected = ['Bonjour', 'monde', 'ceci', 'test', 'fonctionnement', 'twitter'] 
        assert elt == expected
        
    def test_word_number(self):
        """
        Test le fonctionnement de la fonction 'len' sur une phrase sans les stops-word
        """
        test_sentence = ['Bonjour', 'monde', 'ceci', 'test', 'fonctionnement', 'twitter']  
        elt = word_number(test_sentence)
        expected = 6
        assert elt == expected
        