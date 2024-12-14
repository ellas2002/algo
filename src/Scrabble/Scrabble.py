"""""
Akshay Bhatia
Ben Oates
Ella Stiller
Iman Agic
"""""

from location import *
from board import *
from move import *
import itertools
from collections import Counter

class Scrabble_God:

    def __init__(self):
        self._gatekeeper = None
        self._tree = self._build_tree()

    @staticmethod
    def _build_tree():
        """"
        creates a tree to store words from words.txt
        """
        tree = {}
        # The dictionary of legal words.txt
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, 'words.txt')) as file:

            for word in file:
                word = word.strip().lower() #word is stripped of white space and all lowercase
                node = tree

                for char in word: #creates nodes for each char
                    node = node.setdefault(char, {})
                node[''] = True  # End of word

        return tree


    def set_gatekeeper(self, gatekeeper):
        """
        Intermediary between an AI and a Board, allowing the former to get information it needs without allowing full access
        """
        self._gatekeeper = gatekeeper


    def choose_move(self):
        """
        chooses a move through evaluating moves in ascending order of best to worst.
        """
        hand = self._gatekeeper.get_hand()

        # best case: multi-tile moves
        best_move = self._find_best(hand, min_tiles=2)
        if best_move:
            return best_move

        # not best or worst: single-tile moves
        single_tile_move = self._find_best(hand, min_tiles=1, max_tiles=1)
        if single_tile_move:
            return single_tile_move

        # worst case: exchange tiles
        return ExchangeTiles([True] * len(hand))


    def _find_best(self, hand, min_tiles=1, max_tiles=None):
        """"
        the best possible words for a hand of tiles
        """
        max_tiles = max_tiles or len(hand)
        best_score = 0
        best_move = None

        # move through possible tile combinations
        for tile in range(min_tiles, max_tiles + 1):
            for tile_combo in itertools.combinations(range(len(hand)), tile):
                tiles = [hand[i] for i in tile_combo] #get tiles
                words = self._generate_word(tiles) #generate words for tiles

                for word, blank_used in words: #try each generated word
                    for row in range(WIDTH):
                        for col in range(WIDTH):
                            for direction in [HORIZONTAL, VERTICAL]:
                                location = Location(row, col) #create location
                                try:
                                    self._gatekeeper.verify_legality(word, location, direction) #is word placement legal?
                                    score = self._gatekeeper.score(word, location, direction) # what's the score?

                                    # Favor strategic moves; some reinforcement :)
                                    if blank_used:
                                        score -= 5  # Penalize blank tile usage slightly

                                    if score > best_score:
                                        best_score = score #update
                                        best_move = PlayWord(word, location, direction) #generate best_moveeeee
                                except:
                                    continue

        return best_move

    def _generate_word(self, tiles):
        """"
        generates words based on tiles provided using depth first search algorithm
        """
        if not tiles or not self._tree:
            return []

        words = []
        tile_counter = Counter(tiles)

        def dfs(node, path, blanks_left):
            if '' in node:  # End of word
                words.append((''.join(path), blanks_left < tile_counter['_']))

            for char in node:
                if char == '': #skip empty string
                    continue

                if tile_counter[char] > 0:
                    tile_counter[char] -= 1 #Use the character and move to the next node.
                    dfs(node[char], path + [char], blanks_left)
                    tile_counter[char] += 1 #Restore

                elif tile_counter['_'] > 0 and blanks_left > 0:
                    tile_counter['_'] -= 1  # Use a blank and move to the next node.
                    dfs(node[char], path + [char], blanks_left - 1)
                    tile_counter['_'] += 1  #Restore

        dfs(self._tree, [], tile_counter['_'])
        return words