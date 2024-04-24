class Envelope:
    paid_postage = 0

    def __init__(self, weight, was_sent=False):
        self.weight = weight
        self.was_sent = was_sent

    def postage_needed(self):
        return self.weight * 10

    def add_postage(self, added_postage):
        self.paid_postage += added_postage

    def send(self):
        if self.paid_postage >= self.postage_needed():
            self.was_sent = True


class BigEnvelope(Envelope):
    def postage_needed(self):
        return self.weight * 15


e1 = Envelope(5.3)
e1.add_postage(53)
e1.send()
print(e1.was_sent)

b1 = BigEnvelope(5.3)
b1.add_postage(79)
b1.send()
print(b1.was_sent)

b2 = BigEnvelope(5.3)
b2.add_postage(79.5)
b2.send()
print(b2.was_sent)



