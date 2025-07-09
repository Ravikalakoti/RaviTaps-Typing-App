import random

TEXTS = [
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter in the English language, making it a favorite among typists. It's also used for testing fonts and keyboards across different platforms. With practice, you'll be able to type this sentence very quickly without any errors.",
    
    "Typing is a fundamental skill for developers. The ability to type quickly and accurately can greatly increase your productivity. Many software engineers practice touch typing to reduce their reliance on the backspace key and to focus better on the logic they’re writing. Like any skill, it improves with repetition and time.",
    
    "Practice makes perfect when it comes to speed typing. By repeating difficult words and phrases, your fingers will naturally learn the paths they need to take. This helps reduce mental effort and builds muscle memory. Consistent daily typing practice is the fastest way to improve your typing skills dramatically."
]

def get_random_text():
    return random.choice(TEXTS)
