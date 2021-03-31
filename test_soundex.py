from soundex import soundex

def test_soundex(): 
    assert soundex('Robert') == 'R163'
    assert soundex('Rupert') == 'R163'
    assert soundex('Rubin') == 'R150'
    assert soundex('Ashcraft') == 'A261'
    assert soundex('Ashcroft') == 'A261'
