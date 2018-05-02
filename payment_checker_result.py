import datetime


# Represents a payment received
class PaymentInfo:
    def __init__(self, amount, time, to_addr, from_addr, no_confirm):
        #print("P", amount, time, to_addr, from_addr, no_confirm)
        self.amount = amount
        self.timestamp = time
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.no_confirm = no_confirm

    def to_string(self):
        return str(self.amount) + ", on " + datetime.datetime.fromtimestamp(self.timestamp).__str__() + ", from " + self.from_addr + " (" + str(self.no_confirm) + " confirmations)"
        

# Represents a payment check result, for one currency
class PaymentResult:
    def __init__(self, currency, address_to, time_from, time_to, sum_confirmed = 0, sum_nonconfirmed = 0, payments = []):
        self.currency = currency
        self.address_to = address_to
        self.time_from = time_from
        self.time_to = time_to
        self.sum_confirmed = sum_confirmed
        self.sum_nonconfirmed = sum_nonconfirmed
        self.payments = payments

    def print(self):
        if len(self.payments) == 0:
            print("There are no payments", end="")
        else:
            if self.sum_confirmed != self.sum_nonconfirmed:
                print("Sum:", self.sum_confirmed, self.currency, "(confirmed, ", self.sum_nonconfirmed, self.currency, "non-confirmed)", end="")
            else:
                print("Sum:", self.sum_confirmed, self.currency, "(confirmed)", end="")
            if len(self.payments) == 1:
                print("  There is one payment", end="")
            else:
                print("  There are", len(self.payments), "payments:", end="")
        print("  to address:", self.address_to, " period:", datetime.datetime.fromtimestamp(self.time_from).__str__(), "-", datetime.datetime.fromtimestamp(self.time_to).__str__() + " UTC")
        for p in self.payments:
            print("-", p.to_string())

    def count(self):
        return len(self.payments)
        

