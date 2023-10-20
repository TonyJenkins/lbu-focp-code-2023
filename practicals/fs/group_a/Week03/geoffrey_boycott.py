#!/usr/bin/env python3

if __name__ == '__main__':
    player = "Geoffrey Boycott"
    games = 609
    batted = 1014
    not_out = 162
    total_score = 48426

    # The following 3 lines are examples of how print can be used
    # each one is valid and could be re-written in a format matching the others

    print("Player:", player, sep=" ")
    print("Played " + str(games) + " Matches")
    print(f'Average score  {total_score / (batted - not_out):.2f}')
