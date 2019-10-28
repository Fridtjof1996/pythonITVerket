from blackjack.deck import Deck


rank_dict = {
    1: 'A', 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
    8: 8, 9: 9, 10: 10, 11: 'J', 12: 'Q', 13: 'K'
}


def main():
    deck = Deck()
    player_hand = []
    player_total = 0
    dealer_hand = []
    card = deck.cards.pop()
    dealer_hand.append(card)
    dealer_total = calc_hand_value(dealer_hand)
    print('Dealers first card is {} {}.'.format(
        card.suit.name, rank_dict.get(card.rank)
    ))
    while True:
        read = input('Stand, Hit:\n')
        if read == 'Hit':
            card = deck.cards.pop()
            player_hand.append(card)
            player_total = calc_hand_value(player_hand)
            print('Hit with {} {}. Your total is {}'.format(
                card.suit.name, rank_dict.get(card.rank), player_total
            ))
            if player_total > 21:
                print('Your score is over 21. The dealer wins!')
                break
        elif read == 'Stand':
            print('You decided to stand. Your total is {}'.format(
                player_total
            ))
            while dealer_total < 17:
                card = deck.cards.pop()
                dealer_hand.append(card)
                dealer_total = calc_hand_value(dealer_hand)
                print('Dealer hits with {} {}. His total is {}'.format(
                    card.suit.name, rank_dict.get(card.rank), dealer_total
                ))

            if dealer_total > 21:
                print('Dealer got over 21 and busted. You win!')
            elif player_total > dealer_total:
                print('You win with {} points over {} points!'.format(
                    player_total, dealer_total
                ))
            elif player_total < dealer_total:
                print('The dealer wins with {} points over {} points!'.format(
                    dealer_total, player_total
                ))
            else:
                print('The game ends in a tie at {} points!'.format(
                    player_total
                ))
            break


def calc_hand_value(hand):
    total = 0
    num_ace = 0
    for card in hand:
        if card.rank != 1:
            total += min(card.rank, 10)
        else:
            num_ace += 1
    if num_ace != 0:
        if total <= 11 - num_ace:
            total += num_ace + 10
        else:
            total += num_ace
    return total


if __name__ == '__main__':
    main()