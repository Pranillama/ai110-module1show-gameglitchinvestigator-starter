# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - it was a little confusing as had a lot of small bugs
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - Even when the number was lower that the actuall number, the hint keept on saying "Go lower" and vice versa
  - after you won the buttons don't work (new game)
  - something wrong with the history array. I guess it's delayed.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 - I used Claudcode as a AI tool.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
 - AI also gave me a suggestion for another related bug with the bug i told to fix.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
 - when asking to create a pytest for verifying error It gave me a lot of other files and stuff which i had to verify myself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - First, comparing the changes made by claude and analyzing if it matches with the logic or not.
  then, go to the web app and see if the logic worked or not.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
 - so, One of the test i ran inside tests/test_game_logic.py after fixing the two bugs is The test which confirmed that when the guess is higher than the secret, the hint now correctly says "Go LOWER!" instead of "Go HIGHER!".
- Did AI help you design or understand any tests? How?
 - Yes, I used the claude to help me understand and then build the tests one at a time with proper understanding and context.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
