def numhand(hand):
	rank=[r for r,s in hand]
	return rank
def dokhand(hand):
    suit=[s for r,s in hand]
    return suit
def flush(hand):
        suits = [s for r,s in hand]
        return len(set(suits)) == 1
