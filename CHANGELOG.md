# Changelog

All notable changes and progress for Assignment 10 will be documented in this file.

---

## [1.0.0] - 2025-04-20
### Added
- Implemented core business classes: `Product`, `Category`, `Supplier`, `Order`, `User`, `InventoryLog`.
- Created `/src` folder structure for source code.
- Added all six creational patterns:
  - Simple Factory (`VehicleFactory`)
  - Factory Method (`PaymentFactory`)
  - Abstract Factory (`GUIFactory`)
  - Builder (`PizzaBuilder`)
  - Prototype (`ShapeCache`)
  - Singleton (`DatabaseConnection`)
- Wrote unit tests for all six creational patterns under `unittest`.
- Ensured test coverage includes:
  - Correct object creation
  - Attribute initialization
  - Edge cases (e.g., invalid types, prototype cloning, singleton uniqueness)

