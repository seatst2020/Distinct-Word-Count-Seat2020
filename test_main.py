import main

def test_distinct():
  assert main.distinct_words() == 373

def test_total():
  assert main.total_words() == 697

def test_ratio():
  assert main.ratio() == 0.5351506456241033