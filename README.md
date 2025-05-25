# 🪨📄✂️ Rock Paper Scissors
A program that uses a Markov model to develop a Rock-Paper-Scissors player that beats four bots (each with different strategies) at least 60% of the time. The bots were called Quincy, Abbey, Kris, and Mrugesh. 

Quincy cycles through the same five-move pattern: rock, paper, paper, scissors, rock.

Abbey uses a Markov chain to predict the opponent’s next move based on the frequency of their last two moves and counters it accordingly.

Kris always plays the move that beats the opponent’s previous move.

Mrugesh finds the opponent’s most frequent move based on the last 10 plays, then plays the move that beats it.


> 🧠 **This challenge was provided by [freeCodeCamp’s Machine Learning with Python course](https://www.freecodecamp.org/learn/machine-learning-with-python/).**

## 🛠 What I Did
- Implemented a Markov model by:
    - Creating a global dictionary `pattern_dict` to track frequencies of opponent move sequences of length 7
    - Updating the dictionary to keep track of how many times a particular sequence comes up
    - Predicting the opponent’s next move by selecting the most frequent continuation of their last 6 moves, and returning the move that beats it


## 🤔 What I Learned

- **Using a Markov chain**: I tried many different methods, with varying success, but the one bot that was consistently difficult to beat was Abbey. Upon looking at her code, I saw that she was basing her moves off of my last two plays, i.e. a first-order Markov chain. A Markov chain is a system that predicts the next event in a sequence based solely on the current state or a fixed number of previous states. So, I made a higher-order Markov chain, using a longer memory compared to Abbey, which enabled my bot to make better-informed predictions.


## 🚀 Future Improvements

- **Opponent Detection**: Instead of relying on one prediction method, I could create a program that first identifies  which bot I’m playing against based on early moves. This could help tailor the best counter-strategy more quickly, leading to a higher win rate.
- **Different Memory Length**: I could experiment with different orders of Markov chains to see which memory length strikes the best balance between prediction accuracy and computational efficiency.
