from client import LoyaltyPointsRedemptionArbitrageCalculatorClient

def main():
    client = LoyaltyPointsRedemptionArbitrageCalculatorClient()
    res = client.compute_optimal_redemption(5000, 200.00)
    print('Loyalty Points Arbitrage: ' + res['arbitrage_calc_id'] + ' (' + res['optimal_redemption_tier'] + ')')
    print('Points Spent: ' + str(res['points_spent']) + ' | Discount: $' + str(res['discount_value_usd']))
    print('Voucher URL: ' + res['redemption_voucher_url'])

if __name__ == '__main__':
    main()
