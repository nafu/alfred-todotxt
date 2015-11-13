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
    f = codecs.open(todo_file,'r',encoding='utf-8')
    todos = f.readlines()
    f.close()

    feedback = []
    line = ''

    # Build command line.
    line = build_line(q,1)

    # No words written
    if len(q)==1:
        if len(todos):
            tmpfeedback = []
            for r in todos:
                if not r.strip():
                    continue
                if r[0] == '(' and r[2] == ')' and r[1]:
                    pri = r[1].upper()
                else:
                    pri = 'z'
                tmpfeedback.append((pri,I(title=format(todos.index(r)+1)+':'+r, subtitle="Mark as Done", arg=u"do {0}".format(todos.index(r)+1), valid=True)))
        tmpfeedback.sort(key=lambda reg: reg[0])
        feedback = [tmpfeedback[i][1] for i in range(len(tmpfeedback))]
    # Exactly one word written.
    elif len(q)==2:
        if len(todos):
            t = alp.fuzzy_search(line, todos, key=lambda x: x)
            tmpfeedback = []
            for r in t:
                if r[0] == '(' and r[2] == ')' and r[1]:
                    pri = r[1].upper()
                else:
                    pri = 'z'
                tmpfeedback.append((pri,I(title=format(todos.index(r)+1)+':'+r, subtitle="Mark as Done", arg=u"do {0}".format(todos.index(r)+1), valid=True)))
            tmpfeedback.sort(key=lambda reg: reg[0] )
            for i in range(len(tmpfeedback)):
                feedback.append(tmpfeedback[i][1])
    # More than one word:
    else:
        t = alp.fuzzy_search(line, todos, key=lambda x: x)
        tmpfeedback = []
        for r in t:
            if r[0] == '(' and r[2] == ')' and r[1]:
                pri = r[1].upper()
            else:
                pri = 'z'
            tmpfeedback.append((pri,I(title=format(todos.index(r)+1)+':'+r, subtitle="Mark as Done", arg=u"do {0}".format(todos.index(r)+1), valid=True)))
        tmpfeedback.sort(key=lambda reg: reg[0] )
        for i in range(len(tmpfeedback)):
            feedback.append(tmpfeedback[i][1])

    alp.feedback(feedback)

if __name__ == "__main__":
    main()
