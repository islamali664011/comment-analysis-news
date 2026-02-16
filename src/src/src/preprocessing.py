from clean_text import clean_arabic

def merge_common_words(text):
    corrections = {
        'ص ح ا': 'صحيح',
        'ا ران': 'ايران',
        'قو ه': 'قوية',
        'ا د': 'اكيد',
        'ا ل': 'امريكا',
        'ا رم ن ا': 'ارمينيا',
        'اذرب جان': 'اذربيجان',
        'السع ه': 'السعودية'
    }
    for wrong, right in corrections.items():
        text = text.replace(wrong, right)
    return text

def preprocess_comments(comments_list):
    """
    Input: قائمة التعليقات الخام
    Output: قائمة التعليقات بعد التنظيف ودمج الكلمات الشائعة
    """
    cleaned = [clean_arabic(c) for c in comments_list]
    final = [merge_common_words(c) for c in cleaned]
    return final
