from caesar_cipher.caesar_cipher import encrypt, decrypt, crack

# Excrypt string with given shift
def test_encrypt_string():
    actual = encrypt('abc', 2)
    expected = 'cde'
    assert actual == expected

# Decrypt previously encrypted string with same shift
def test_decrypt_string():
    actual = decrypt('cde', 2)
    expected = 'abc'
    assert actual == expected

# Encryption should handle upper and lowercase letters
def test_encrypt_string_upper_and_lower():
    actual = encrypt('abcABC', 3)
    expected = 'defDEF'
    assert actual == expected

# Encryption should allow non-alpha but ignore them
def test_encrypt_string_non_alpha():
    actual = encrypt('ABC 1 2', 4)
    expected = 'EFG 1 2'
    assert actual == expected

# Decrypt encrypted version of "It was the best of times, it was the worst of times." WITHOUT knowing shift.
def test_crack():
    actual = crack('Lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv.')
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected
