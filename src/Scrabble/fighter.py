from location import *
from board import *
from move import *
import itertools
import string


class Fighter:
    def __init__(self):
        self._gatekeeper = None
        self._dictionary = self._dict()

    def _dict(self):
        current_dir = os.path.dirname(
            __file__)  # Current working directory, necessary for this to run when imported into a test
        with open(os.path.join(current_dir, 'words.txt')) as file:
            DICTIONARY = set(word.strip() for word in file)

        return DICTIONARY

    def set_gatekeeper(self, gatekeeper):
        self._gatekeeper = gatekeeper

    def choose_move(self):
        # First turn strategy
        if self._gatekeeper.get_square(CENTER) == DOUBLE_WORD_SCORE:
            return self._find_best_multi_tile_move(2, 3)

        # Try multi-tile moves first
        multi_tile_move = self._find_best_multi_tile_move(2, len(self._gatekeeper.get_hand()))
        if multi_tile_move:
            return multi_tile_move

        # If no multi-tile move, try single tile moves
        single_tile_move = self._find_best_single_tile_move()
        if single_tile_move:
            return single_tile_move

        # Last resort: exchange tiles
        return ExchangeTiles([True] * len(self._gatekeeper.get_hand()))

    def _find_best_multi_tile_move(self, min_tiles, max_tiles):
        hand = self._gatekeeper.get_hand()
        best_score = -1
        best_move = None

        # Generate all possible tile combinations
        for tile_count in range(min_tiles, max_tiles + 1):
            for tile_combo in itertools.combinations(range(len(hand)), tile_count):
                # Create word candidates using these tiles
                word_candidates = self._generate_word_candidates(
                    [hand[i] for i in tile_combo],
                    handle_blanks=True
                )

                for word in word_candidates:
                    # Try placing the word in every possible board location
                    for row in range(WIDTH):
                        for col in range(WIDTH):
                            for direction in [HORIZONTAL, VERTICAL]:
                                try:
                                    # Verify and score the move
                                    self._gatekeeper.verify_legality(word, Location(row, col), direction)
                                    score = self._gatekeeper.score(word, Location(row, col), direction)

                                    # Update best move if this scores higher
                                    if score > best_score:
                                        best_score = score
                                        best_move = PlayWord(word, Location(row, col), direction)
                                except:
                                    # Move is illegal, continue searching
                                    pass

        return best_move

    def _find_best_single_tile_move(self):
        hand = self._gatekeeper.get_hand()
        best_score = -1
        best_move = None

        for tile_index, tile in enumerate(hand):
            # Handle blank tiles more intelligently
            if tile == '_':
                tile_candidates = string.ascii_uppercase
            else:
                tile_candidates = [tile]

            for candidate_tile in tile_candidates:
                # Try both prefixing and suffixing the tile
                for word_pattern in [candidate_tile + ' ', ' ' + candidate_tile]:
                    for row in range(WIDTH):
                        for col in range(WIDTH):
                            for direction in [HORIZONTAL, VERTICAL]:
                                try:
                                    # Verify and score the move
                                    location = Location(row, col)
                                    self._gatekeeper.verify_legality(word_pattern, location, direction)
                                    score = self._gatekeeper.score(word_pattern, location, direction)

                                    # Update best move if this scores higher
                                    if score > best_score:
                                        best_score = score
                                        best_move = PlayWord(word_pattern, location, direction)
                                except:
                                    # Move is illegal, continue searching
                                    pass

        return best_move

    def _generate_word_candidates(self, tiles, handle_blanks=False):
        candidates = []

        # Generate permutations of tiles
        for r in range(1, len(tiles) + 1):
            for perm in itertools.permutations(tiles, r):
                word = ''.join(perm)

                # Handle blank tile substitution if enabled
                if handle_blanks and '_' in word:
                    word = word.replace('_', 'E')  # Default blank tile to 'E'

                # Check if the word is in our dictionary
                if word.lower() in self._dictionary:
                    candidates.append(word)

        return candidates

