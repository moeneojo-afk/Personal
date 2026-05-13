class SavingsBankAccount:
    """
    A savings bank account with withdrawal limits between 0 and the account balance.
    """

    def __init__(self, account_holder, initial_balance=0.0, minimum_balance=0.0):
        """
        Initialize a savings bank account.

        Args:
            account_holder (str): Name of the account holder
            initial_balance (float): Starting balance (must be >= minimum_balance)
            minimum_balance (float): Minimum required balance (default 0.0)
        """
        if initial_balance < minimum_balance:
            raise ValueError(f"Initial balance cannot be less than minimum balance of ${minimum_balance:.2f}")

        self.account_holder = account_holder
        self._balance = initial_balance
        self.minimum_balance = minimum_balance
        self._is_active = True
        self._transaction_history = []

        # Record initial deposit if there's an initial balance
        if initial_balance > 0:
            self._transaction_history.append(f"Account opened with ${initial_balance:.2f}")

    @property
    def balance(self):
        """Get current balance."""
        return self._balance

    @property
    def available_balance(self):
        """Get available balance for withdrawal (balance - minimum_balance)."""
        return max(0, self._balance - self.minimum_balance)

    @property
    def is_active(self):
        """Check if account is active."""
        return self._is_active

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit (must be positive)

        Returns:
            bool: True if successful
        """
        if not self._is_active:
            raise ValueError("Cannot deposit to an inactive account")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        self._transaction_history.append(f"Deposit: +${amount:.2f} | Balance: ${self._balance:.2f}")
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Withdrawal amount must be between 0 and available balance.

        Args:
            amount (float): Amount to withdraw

        Returns:
            bool: True if successful
        """
        if not self._is_active:
            raise ValueError("Cannot withdraw from an inactive account")

        # Check if withdrawal amount is within valid range (0 < amount <= available_balance)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")

        if amount > self.available_balance:
            raise ValueError(
                f"Withdrawal amount ${amount:.2f} exceeds available balance ${self.available_balance:.2f}. "
                f"Minimum balance of ${self.minimum_balance:.2f} must be maintained."
            )

        self._balance -= amount
        self._transaction_history.append(f"Withdrawal: -${amount:.2f} | Balance: ${self._balance:.2f}")

        return True

    def get_transaction_history(self):
        """Get list of all transactions."""
        return self._transaction_history.copy()

    def print_transaction_history(self):
        """Print transaction history in a formatted way."""
        print(f"\n--- Transaction History for {self.account_holder} ---")
        for i, transaction in enumerate(self._transaction_history, 1):
            print(f"{i}. {transaction}")
        print(f"Current Balance: ${self._balance:.2f}")
        print(f"Available Balance: ${self.available_balance:.2f}")
        print("-" * 50)

    def close_account(self):
        """Close the account."""
        self._is_active = False
        self._transaction_history.append("Account closed")

    def __str__(self):
        """String representation of the account."""
        status = "Active" if self._is_active else "Closed"
        return (f"Savings Account - Holder: {self.account_holder} | "
                f"Balance: ${self._balance:.2f} | "
                f"Available: ${self.available_balance:.2f} | "
                f"Status: {status}")

    def __repr__(self):
        """Detailed representation of the account."""
        return (f"SavingsBankAccount(account_holder='{self.account_holder}', "
                f"balance={self._balance}, "
                f"minimum_balance={self.minimum_balance}, "
                f"is_active={self._is_active})")


# Demo function to show usage
def demo_account():
    """Demonstrate the SavingsBankAccount functionality."""
    print("=" * 60)
    print("SAVINGS BANK ACCOUNT DEMO")
    print("=" * 60)

    # Create account with minimum balance requirement
    account = SavingsBankAccount("John Doe", initial_balance=1000.0, minimum_balance=100.0)
    print(account)
    print(f"Available balance for withdrawal: ${account.available_balance:.2f}")

    # Test deposits
    print("\n1. Making deposits...")
    try:
        account.deposit(500)
        print(f"Deposited $500. New balance: ${account.balance:.2f}")
        account.deposit(250.75)
        print(f"Deposited $250.75. New balance: ${account.balance:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    # Test valid withdrawal
    print("\n2. Making valid withdrawal...")
    try:
        account.withdraw(300)
        print(f"Withdrew $300. New balance: ${account.balance:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    # Test withdrawal exceeding available balance
    print("\n3. Attempting withdrawal exceeding available balance...")
    try:
        account.withdraw(2000)
    except ValueError as e:
        print(f"Error: {e}")

    # Test withdrawal that would go below minimum balance
    print("\n4. Attempting withdrawal below minimum balance...")
    try:
        account.withdraw(1400)
    except ValueError as e:
        print(f"Error: {e}")

    # Test zero or negative withdrawal
    print("\n5. Attempting invalid withdrawal amounts...")
    try:
        account.withdraw(0)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        account.withdraw(-50)
    except ValueError as e:
        print(f"Error: {e}")

    # Print transaction history
    account.print_transaction_history()

    # Test account closure
    print("\n6. Closing account...")
    account.close_account()
    print(f"Account active status: {account.is_active}")

    # Try to withdraw after closing
    print("\n7. Attempting withdrawal on closed account...")
    try:
        account.withdraw(100)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    demo_account()