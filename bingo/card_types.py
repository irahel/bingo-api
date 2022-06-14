from bingo.card_generator import JKClassicGenerator

CARD_TYPES_MAP = {"jk_classic": JKClassicGenerator}


def get_card_type_generator(type_identifyer):
    return CARD_TYPES_MAP.get(type_identifyer, None)