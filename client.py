class LoyaltyPointsRedemptionArbitrageCalculatorClient:
    def compute_optimal_redemption(self, points_balance=2400, cart_total_usd=120.00, available_rewards=None):
        return {
            'arbitrage_calc_id': 'loy_arb_7721',
            'points_balance': points_balance,
            'optimal_redemption_tier': 'REDEEM_2000_PTS_FOR_25_USD_COUPON',
            'points_spent': 2000,
            'discount_value_usd': 25.00,
            'effective_point_yield_cents': 1.25,
            'retained_points_balance': points_balance - 2000,
            'next_tier_progress_pct': 84.0,
            'redemption_voucher_url': 'https://smile.loyalty.genpark.ai/redemptions/7721.json'
        }
