# Base class for alphabets, providing a common structure.
class Alphabet:
    def __init__(self, letters):
        self.letters = letters

# Protein alphabets
class ExtendedIUPACProtein(Alphabet):
    """
    Extended uppercase IUPAC protein single letter alphabet including X etc.
    """
    def __init__(self):
        letters = 'ACDEFGHIKLMNPQRSTVWYBXZJUO'
        super().__init__(letters)

class IUPACProtein(ExtendedIUPACProtein):
    """
    IUPAC protein alphabet of the 20 standard amino acids.
    """
    def __init__(self):
        letters = 'ACDEFGHIKLMNPQRSTVWY'
        super().__init__()
        self.letters = letters

# DNA alphabets
class DNAAlphabet(Alphabet):
    pass

class IUPACAmbiguousDNA(DNAAlphabet):
    """
    Uppercase IUPAC ambiguous DNA.
    """
    def __init__(self):
        letters = 'GATCRYWSMKHBVDN'
        super().__init__(letters)

class IUPACUnambiguousDNA(IUPACAmbiguousDNA):
    """
    Uppercase IUPAC unambiguous DNA (letters GATC only).
    """
    def __init__(self):
        letters = 'GATC'
        super().__init__()
        self.letters = letters

class ExtendedIUPACDNA(DNAAlphabet):
    """
    Extended IUPAC DNA alphabet.
    """
    def __init__(self):
        letters = 'GATCBDSW'
        super().__init__(letters)

# RNA alphabets
class RNAAlphabet(Alphabet):
    pass

class IUPACAmbiguousRNA(RNAAlphabet):
    """
    Uppercase IUPAC ambiguous RNA.
    """
    def __init__(self):
        letters = 'GAUCRYWSMKHBVDN'
        super().__init__(letters)

class IUPACUnambiguousRNA(IUPACAmbiguousRNA):
    """
    Uppercase IUPAC unambiguous RNA (letters GAUC only).
    """
    def __init__(self):
        letters = 'GAUC'
        super().__init__()
        self.letters = letters
