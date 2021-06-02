def generate_hashtag(s):
    final_string = ""
    separated = s.split()
    if separated:
        final_string += "#"
        
        for w in separated:
            w = w.capitalize()
            final_string += w
    
    if len(final_string) > 140 or not final_string:
        return False
    return final_string
