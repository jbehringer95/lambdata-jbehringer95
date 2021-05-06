"""an example of a more intense pytest"""

import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """Returns empty wallet"""
    return Wallet()


@pytest.fixture
def wallet_with_funds():
    """Returns wallet with balance 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    """Testing balance is zero"""
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet_with_funds):
    """Testing constructor initial balance"""
    assert wallet_with_funds.balance == 20


def test_wallet_add_cash(wallet_with_funds):
    """Testing add_cash method in wallet object"""
    wallet_with_funds.add_cash(80)
    assert wallet_with_funds.balance == 100

    
def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    """Test proper exception is raised when spend cash exceed balance"""
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)