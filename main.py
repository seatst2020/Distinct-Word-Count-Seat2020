def distinct_words():
  lst = []
  file = open('lyrics.txt', 'r')
  lyrics = file.read()
  lyrics = lyrics.lower()
  words = lyrics.split()
  words = [word.strip('.,!;()[]') for word in words] # took from resource 
  words = [word.replace("'s", '') for word in words] # took from resource 
  for word in words:
    if word not in lst:
      lst.append(word)
  return len(lst)


def total_words():
  lmao = open("lyrics.txt", "r")
  lyrics = lmao.read()
  total = len(lyrics.split())
  return total
  

def ratio():
  return distinct_words() / total_words()
