from logic_utils import check_guess

# --- Tests targeting bugs fixed in app.py ---

def test_too_high_message_is_go_lower():
    # Bug: when guess > secret, message incorrectly said "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"

def test_too_low_message_is_go_higher():
    # Bug: when guess < secret, message incorrectly said "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"

def test_secret_as_string_does_not_corrupt_outcome():
    # Bug: on even attempts the secret was cast to str, causing wrong comparisons
    # e.g. check_guess(9, "10") would incorrectly return "Too High" via string comparison
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low", f"Expected 'Too Low' for guess=9, secret=10, got: {outcome}"

# --- Existing tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
