#!/usr/bin/env python3

from copy import copy


def cheapest_shipment(order, inventory_distribution):
    """
    identifies the cheapest shipment 
    for a given order of items and 
    inventory of items across warehouses

    Parameters
    ----------
    current_order : dictionary
        order placed by customer with item:quantity as key-value pairs
    inventory_distribution : list
        name and inventory of all warehouses

    Returns
    ----------
    shipments: list
        identifies cheapest warehouses to ship each item from
        along with quantity to be shipped
    """
    # check for empty order or no warehouses
    if not order or not inventory_distribution:
        print("Empty order or no inventory")
        return []

    current_order = copy(order)
    shipments = []
    total_remaining_quantity = sum(
        quantity for item, quantity in order.items())

    for warehouse in inventory_distribution:
        # check if order has been completed, skip checking other warehouses
        if total_remaining_quantity <= 0:
            break

        shipment = {}
        inventory = {}

        # choose items greedily to minimize shipping cost
        for item, quantity in current_order.items():
            if item in warehouse["inventory"] and quantity > 0:
                inventory[item] = min(warehouse["inventory"][item], quantity)
                total_remaining_quantity -= inventory[item]

                # warehouse will have left over inventory
                if warehouse["inventory"][item] >= quantity:
                    warehouse["inventory"][item] -= quantity
                    current_order[item] = 0

                # warehouse has exactly the quantity requested
                else:
                    current_order[item] -= warehouse["inventory"][item]
                    warehouse["inventory"][item] = 0

        # add items chosen from a warehouse to the shipment
        if inventory:
            shipment[warehouse["name"]] = inventory
            shipments.append(shipment)

    # check for incomplete order
    return shipments if total_remaining_quantity <= 0 else []


if __name__ == "__main__":
    order = {"apple": 5, "banana": 5, "orange": 5}
    inventory_distribution = [
        {"name": "owd", "inventory": {"apple": 5, "orange": 10}},
        {"name": "dm:", "inventory": {"banana": 5, "orange": 10}}
    ]
    shipment = cheapest_shipment(order, inventory_distribution)
    print(shipment)
