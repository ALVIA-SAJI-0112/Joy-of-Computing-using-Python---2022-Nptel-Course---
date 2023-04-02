import nltk
papers={'Madison':[],'':[],'':[],'':[]}

def read_files(filename):
    strings=[]
    
    for file in filename:
        with open(f'federalist_{file}.txt') as f:
            strings.append(f.read())
            
    return ('\n'.join(strings))

federalist_by_author={}

for author, files in papers.items():
    federalist_by_author[author]=read_files(files)
    
authors=('Hamilton','Madison','Disputed','Jay','Shared')

author_tokens={}
length_distribution={}

for author in authors:
    tokens=nltk.word_tokenize(federalost_by_author[author])
    
    author_tokens[author]=([token for token in tokens if any(c.isalpha() for c in token)])
    
    token_lengths=[len(token) for token in author_tokens[author]]
    
    length_distributions[authors]=nltk.FreqDist(token_lengths)
    
    length_distribution[author].plot(15,title=author)