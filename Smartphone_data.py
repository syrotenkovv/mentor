from Smartphone import Smartphone



smartphone = Smartphone(lable="Lenovo", model="M6", ram=64, isc=60, price=21000)
smartphone2 = Smartphone(lable="Apple", model="15ProMax", ram=128, isc=30 ,price=22000)
smartphone3 = Smartphone(lable="Samsung", model="L200", ram=256, isc=70, price=32000)
smartphone4 = Smartphone(lable="Nokia", model="3600", ram=2, isc=60000, price=42000)

smartphone.display_info()
smartphone2.display_info()
smartphone3.display_info()
smartphone4.display_info()
smartphone.is_high_end()
smartphone2.is_high_end()
smartphone3.is_high_end()
smartphone4.is_high_end()