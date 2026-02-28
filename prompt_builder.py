def build_prompt(language, style, mood, length, temperature):
    
    style_instructions = {
        "haiku": """Write a traditional Haiku:
        - Exactly 3 lines
        - Syllable structure: 5 / 7 / 5
        - Focus on a single moment or natural element from the image
        - No rhyme, no title""",

        "sonnet": """Write a Shakespearean Sonnet:
        - Exactly 14 lines
        - Rhyme scheme: ABAB CDCD EFEF GG
        - Final couplet delivers a twist or resolution
        - Iambic pentameter (10 syllables per line)""",

        "ode": """Write an Ode:
        - 3 to 5 stanzas, each 6-10 lines
        - Elevated, celebratory tone
        - Directly address the subject of the image
        - Rich with metaphor and sensory imagery""",

        "elegy": """Write an Elegy:
        - 3 to 4 stanzas of 4-6 lines each
        - Tone of mourning, loss, or quiet grief
        - End with acceptance or peace""",

        "ballad": """Write a Ballad:
        - 4-line stanzas, minimum 3 stanzas
        - Rhyme scheme: ABCB
        - Tell a small story inspired by the image
        - Simple, musical language""",

        "villanelle": """Write a Villanelle:
        - 19 lines: 5 tercets + 1 quatrain
        - Line 1 repeats as lines 6, 12, 18
        - Line 3 repeats as lines 9, 15, 19
        - Rhyme scheme: ABA throughout""",

        "free verse": f"""Write a Free Verse poem:
        - Approximately {length} lines
        - No rhyme scheme or fixed meter
        - Use line breaks intentionally for rhythm
        - Focus on vivid, concrete imagery""",

        "ghazal": """Write a Ghazal:
        - 5 to 7 couplets
        - Each couplet self-contained
        - Last word of line 2 in every couplet must be the same (radif)
        - Themes of longing, beauty, or loss""",

        "prose poem": """Write a Prose Poem:
        - One paragraph, no line breaks, 80-120 words
        - Density and imagery of poetry within flowing prose
        - Single compressed emotional moment""",

        "spoken word": """Write a Spoken Word poem:
        - 12 to 20 lines, written to be performed aloud
        - Punchy, rhythmic, conversational
        - Build toward emotional peak in final 4 lines
        - Raw and urgent in tone"""
    }

    style_guide = style_instructions.get(style, style_instructions["free verse"])

    prompt = f"""
You are an award-winning poet with deep sensitivity to visual imagery.

Analyze this image across THREE dimensions:
1. OBJECTS: What concrete things, people, or elements are visible?
2. SENTIMENT: What is the emotional atmosphere?
3. SCENE CONTEXT: What story, time of day, or setting does this suggest?

Now write a poem using these rules:

{style_guide}

LANGUAGE: Write entirely in {language}. Do not mix languages.
MOOD: {mood}
QUALITY RULES:
  - Avoid clichés
  - Use at least 2 poetic devices (metaphor, imagery, personification, symbolism)
  - Be specific and surprising with details
  - Output ONLY the poem, no explanation, no title

Begin now:
"""
    return prompt
