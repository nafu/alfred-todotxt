import sys
import alp
import codecs # Using codecs to work with other languages. utf-8 codecs.open(todo_file,'r',encoding='utf-8')
from alp.item import Item as I

def build_line(words,start=1):
    """Returns a line made of the concatenation of all words
    starting from start
    words: list of words
    start: list index to start concatenation"""
    line = ''
    for word in words[start:]:
        if len(line)==0:
            line = word
        else:
            line = line + ' ' + word
    return line.decode('utf-8')

def main():
    q = sys.argv

    # Load todos from file
    todo_file = q.pop(1) # Path to todo.txt file

    feedback = []
    line = ''

    # Build command line.
    line = build_line(q,1)
    addItem = I(title="Add Todo", subtitle=line, arg=u"add {0}".format(line), valid=True)

    # No words written
    if len(q)==1:
        tmpfeedback.append(addItem)
    # Exactly one word written.
    elif len(q)==2:
        feedback.append(addItem)
    # More than one word:
    else:
        if len(q[1])==1 and q[1].isalpha():
            pri = '(' + q[1].upper() + ') '
            line = pri + build_line(q,2)
        addItem = I(title="Add Todo", subtitle=line, arg=u"add {0}".format(line), valid=True)
        feedback.append(addItem)

    alp.feedback(feedback)

if __name__ == "__main__":
    main()
