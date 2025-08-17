from src.config.examples import EXAMPLES
from src.config.prompt import PROMPT
from .utils.extract import extract_result
import logging
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("langextract").setLevel(logging.ERROR)


input_text = """
In Cairo, a young architect named Amir was known for his rare skill in sketching intricate blueprints by hand. His dream was to design a bridge that would connect communities divided by a river. However, the city officials doubted him, saying his methods were old-fashioned in a world that relied on machines.
Meanwhile, in Istanbul, Leila, a gifted linguist, spent her days studying forgotten manuscripts. She stumbled upon an ancient scroll that described the mathematical principles behind an unbuilt structure. Curious, she realized these writings might hold the key to Amir’s dream, although she had never met him.
Far away in Lisbon, Mateo, a young engineer, was building models of futuristic bridges using advanced simulation software. Yet despite his precision, something was always missing. His designs lacked soul and balance.
Fate brought them together when a cultural exchange program invited Amir, Leila, and Mateo to collaborate on a single project. Amir’s hand-drawn visions provided the heart, Leila’s translations unlocked the ancient wisdom, and Mateo’s engineering grounded their ideas in modern reality.
In just one summer, the three strangers designed a bridge unlike any other, one that blended art, language, and science. It was not only a structure of steel and stone, but also a living symbol of collaboration across cultures and skills.
When it finally stood tall over Cairo’s river, people no longer doubted Amir’s methods, Leila’s old manuscripts, or Mateo’s futuristic models. The bridge belonged to all three cities and to all three dreamers.
"""

result = extract_result(input_text, PROMPT, EXAMPLES)

for ex in result.extractions:
    if ex.extraction_class == "person_name":
        print(ex.extraction_class)
        print(ex.extraction_text)
        print(ex.attributes)
        print(ex.char_interval)

    if ex.extraction_class == "country":
        print(ex.extraction_class)
        print(ex.extraction_text)
        print(ex.attributes)
        print(ex.char_interval)