from address import Address
from mailing import Mailing

to_address = Address('46020', 'Valencia', 'Albocásser', 26, 24)
from_address = Address('62-025', 'Trzek', 'Lipowa', 10, 11)

mailing = Mailing(to_address, from_address, 1200, '574630596')
print(mailing)