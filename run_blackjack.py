from blackjack import Game
import sys


def main():
    player_original_cash_balance = 200
    blackjack = Game(
        name_player='player',
        player_cash_balance=player_original_cash_balance,
        dealer_cash_balance=1000,
        number_of_decks=1
    )
    blackjack.welcome()

    round_number = 1
    while blackjack.player_cash_balance >= blackjack.player.minimum_bet:
        print(
            f'''
                    ********************
                          ROUND {round_number}
                    ********************
              '''
        )

        (player_bet, dealer_bet) = blackjack.bets()
        blackjack.deal_cards()

        blackjack.player.show_balance()
        blackjack.player.show_player_card_values()
        if blackjack.player.hand.get_card_value() < 21:
            blackjack.adjust_player_hand()
        blackjack.adjust_dealer_hand()
        blackjack.dealer.show_dealer_card_values()
        blackjack.blackjack_result(player_bet, dealer_bet)
        exit_game = blackjack.exit_game()
        if exit_game == True:
            print('Thank you for playing with us')
            if blackjack.gain_losses(player_original_cash_balance) > 0:
                print(
                    f'You gained: {blackjack.gain_losses(player_original_cash_balance)} $.'
                )
            elif blackjack.gain_losses(player_original_cash_balance) < 0:
                print(
                    f'You lost: {blackjack.gain_losses(player_original_cash_balance)} $.'
                )
            elif blackjack.gain_losses(player_original_cash_balance) == 0:
                print(f'You broke even.')
            sys.exit()
        discard_pot = blackjack.collect_and_discard_card()
        blackjack.return_cards_to_deck_and_reshuffle(discard_pot)
        round_number += 1
    else:
        'Sorry you no longer have a balance to play. You lost everything.'


if __name__ == '__main__':
    main()
