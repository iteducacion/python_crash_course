
import Cars as Autos


tesla   = Autos.ElectricCar('tesla', 'Model S', 2019)
corolla = Autos.Car('toyota', 'corolla', 2019)
print(tesla.get_descriptive_name()) # 2019 Tesla Model S (Electric)


tesla.fill_gas_tank()
corolla.fill_gas_tank()

tesla.battery.upgrade_battery()

tesla.battery.upgrade_battery()

tesla.battery.describe_battery()




