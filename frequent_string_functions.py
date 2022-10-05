
# this function filters out from a string (set_o_words) anything
# that comes
# ===== BEFORE =======
# another specified string or letter (cur_letter)
def post_filter(set_o_words, cur_letter):
    index = set_o_words.find(cur_letter)
    set_o_words = (set_o_words[index:])
    return set_o_words

# this function filters out from a string (set_o_words) anything
# that comes
# ===== AFTER =======
# another specified string or letter (cur_letter)
def pre_filter(set_o_words, cur_letter):
    index = set_o_words.find(cur_letter)
    set_o_words = (set_o_words[:index])
    return set_o_words