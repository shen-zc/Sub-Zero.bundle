# coding=utf-8
import re

from subzero.modification.mods import SubtitleTextModification, empty_line_post_processors
from subzero.modification.processors.re_processor import NReProcessor
from subzero.modification import registry


class HearingImpaired(SubtitleTextModification):
    identifier = "remove_HI"
    description = "Remove Hearing Impaired tags"
    exclusive = True
    order = 10

    long_description = """\
    Removes tags, text and characters from subtitles that are meant for hearing impaired people
    """

    processors = [
        # brackets (only remove if at least 3 consecutive uppercase chars in brackets
        NReProcessor(re.compile(ur'(?sux)[([].+(?=[A-ZÀ-Ž]{3,}).+[)\]]'), "", name="HI_brackets"),

        # text before colon (and possible dash in front), max 11 chars after the first whitespace (if any)
        # NReProcessor(re.compile(r'(?u)(^[A-z\-\'"_]+[\w\s]{0,11}:[^0-9{2}][\s]*)'), "", name="HI_before_colon"),

        # text before colon (at least 4 consecutive uppercase chars)
        NReProcessor(re.compile(ur'(?u)(^(?=.*[A-ZÀ-Ž]{4,})[A-ZÀ-Ž-_\s]+:\s*)'), "", name="HI_before_colon"),

        # text in brackets at start, after optional dash, before colon or at end of line
        # fixme: may be too aggressive
        NReProcessor(re.compile(ur'(?um)(^-?\s?[([][A-zÀ-ž-_\s]{3,}[)\]](?:(?=$)|:\s*))'), "",
                     name="HI_brackets_special"),

        # all caps line (at least 4 consecutive uppercase chars)
        NReProcessor(re.compile(ur'(?u)(^(?=.*[A-ZÀ-Ž]{4,})[A-ZÀ-Ž-_\s]+$)'), "", name="HI_all_caps"),

        # dash in front
        # NReProcessor(re.compile(r'(?u)^\s*-\s*'), "", name="HI_starting_dash"),

        # all caps at start before new sentence
        NReProcessor(re.compile(ur'(?u)^(?=[A-ZÀ-Ž]{4,})[A-ZÀ-Ž-_\s]+\s([A-ZÀ-Ž][a-zà-ž].+)'), r"\1",
                     name="HI_starting_upper_then_sentence"),
    ]

    post_processors = empty_line_post_processors


registry.register(HearingImpaired)
