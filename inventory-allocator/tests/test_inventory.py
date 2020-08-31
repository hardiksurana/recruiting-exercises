#!/usr/bin/env python3

from src.inventory_allocator import cheapest_shipment

######### Empty cases #########


def test_cheapest_shipment_no_order():
    """
    order need not be shipped as there are no items to ship
    """
    order = {}
    warehouses = [{"name": "owd", "inventory": {"apple": 1}}]
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_empty_order():
    """
    order need not be shipped as there is not enough items to ship
    """
    order = {"apple": 0}
    warehouses = [{"name": "owd", "inventory": {"apple": 5}}]
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_no_warehouses():
    """
    order cannot be shipped as there are no warehouses
    """
    order = {"apple": 1}
    warehouses = []
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment

######### One warehouse #########


def test_cheapest_shipment_one_warehouse_exact_quantity():
    """
    complete order is shipped from one warehouse, 
    has exact inventory as requested
    """
    order = {"apple": 1}
    warehouses = [{"name": "owd", "inventory": {"apple": 1}}]
    expected_shipment = [{"owd": {"apple": 1}}]

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_one_warehouse_excess_inventory():
    """
    complete order shipped from one warehouse, 
    has more inventory than requested
    """
    order = {"apple": 1, "banana": 1}
    warehouses = [{"name": "owd", "inventory": {"apple": 5, "banana": 5}}]
    expected_shipment = [{"owd": {"apple": 1, "banana": 1}}]

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment

######### Multiple Warehouses #########


def test_cheapest_shipment_choose_single_warehouse_over_multiple():
    """
    complete order shipped from multiple warehouses,
    has enough inventory to satisfy order
    """
    order = {"apple": 5, "banana": 5, "orange": 5}
    warehouses = [
        {"name": "owd", "inventory": {"apple": 5, "banana": 5, "orange": 5}},
        {"name": "dm:", "inventory": {"apple": 20, "banana": 20, "orange": 20}}
    ]
    expected_shipment = [
        {'owd': {"apple": 5, "banana": 5, "orange": 5}}]

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_multiple_warehouses_excess_inventory():
    """
    complete order shipped from multiple warehouses,
    has enough inventory to satisfy order
    """
    order = {"apple": 5, "banana": 5, "orange": 5}
    warehouses = [
        {"name": "owd", "inventory": {"apple": 15, "orange": 10}},
        {"name": "dm:", "inventory": {"banana": 15, "orange": 10}}
    ]
    expected_shipment = [
        {'owd': {'apple': 5, 'orange': 5}}, {'dm:': {'banana': 5}}]

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_multiple_warehouses_one_item_split_inventory():
    """
    complete order shipped from multiple warehouses
    """
    order = {"apple": 10}
    warehouses = [
        {"name": "owd", "inventory": {"apple": 5}},
        {"name": "dm", "inventory": {"apple": 5}}
    ]

    expected_shipment = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
    actual_shipment = cheapest_shipment(order, warehouses)

    assert actual_shipment == expected_shipment


def test_cheapest_shipment_multiple_warehouses_multiple_items_split_inventory():
    """
    complete order shipped from multiple warehouses
    """
    order = {"apple": 5, "banana": 5, "orange": 5, "peach": 5}
    warehouses = [
        {"name": "owd", "inventory": {"apple": 2, "banana": 3, "orange": 4}},
        {"name": "dm", "inventory": {"apple": 5, "banana": 10, "orange": 3, "peach": 7}}
    ]

    expected_shipment = [{"owd": {"apple": 2, "banana": 3, "orange": 4}}, {
        "dm": {"apple": 3, "banana": 2, "orange": 1, "peach": 5}}]
    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


######### Incomplete order #########

def test_cheapest_shipment_item_unavailable_in_all_warehouses():
    """
    order cannot be shipped as item is not available in any warehouse
    """
    order = {"apple": 1}
    warehouses = [
        {"name": "owd", "inventory": {"peach": 5, "orange": 10}},
        {"name": "dm:", "inventory": {"banana": 5, "orange": 10}}
    ]
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_single_item_deficit_in_warehouses():
    """
    not enough inventory, order cannot be shipped
    """
    order = {"apple": 100}
    warehouses = [
        {"name": "owd", "inventory": {"apple": 5, "orange": 5}},
        {"name": "dm:", "inventory": {"apple": 10, "peach": 10}}
    ]
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_multiple_items_deficit_in_warehouses():
    """
    not enough inventory, order cannot be shipped
    """
    order = {"apple": 5, "banana": 5, "orange": 5}
    warehouses = [
        {"name": "owd", "inventory": {"apple": 3, "orange": 2}},
        {"name": "dm:", "inventory": {"banana": 1, "orange": 2}}
    ]
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment

######### Large order #########


def test_cheapest_shipment_large_shipped_order():
    """
    enough inventory, order can be shipped
    """
    order = {
        "apple": 5, "apricots": 5, "avocado": 5, "banana": 5, "blueberries": 5, "cherries": 5, "cranberries": 5,
        "custard apple": 5, "figs": 5, "dates": 5, "gooseberries": 5, "grapes": 5, "guava": 5, "jackfruit": 5, 
        "lemon": 5, "mango": 5, "olives": 5, "orange": 5, "papaya": 5, "pear": 5, "pineapple": 5, "plums": 5,
        "pomegranate": 5
    }

    warehouses = [
        {"name": "warehouse_1", "inventory": {"apple": 2, "apricots": 2, "avocado": 5, "banana": 5, "pomegranate": 4}},
        {"name": "warehouse_2", "inventory": {"apricots": 10, "avocado": 5, "banana": 15, "blueberries": 2, "jackfruit": 2}},
        {"name": "warehouse_3", "inventory": {"avocado": 15, "banana": 10, "blueberries": 1, "cherries": 3, "jackfruit": 1}},
        {"name": "warehouse_4", "inventory": {"banana": 5, "blueberries": 5, "cherries": 15, "cranberries": 15, "jackfruit": 5}},
        {"name": "warehouse_5", "inventory": {"blueberries": 15, "cherries": 10, "cranberries": 5, "custard apple": 5, "dates": 1}},
        {"name": "warehouse_6", "inventory": {"custard apple": 2, "dates": 2, "figs": 3, "gooseberries": 10, "grapes": 15, "guava": 5}},
        {"name": "warehouse_7", "inventory": {"lemon": 2, "mango": 10, "olives": 2, "figs": 10, "pomegranate": 2}},
        {"name": "warehouse_8", "inventory": {"papaya": 20, "pear": 15, "pineapple": 5, "plums": 5}},
        {"name": "warehouse_9", "inventory": {"lemon": 5, "mango": 5, "olives": 5, "orange": 1, "papaya": 5, "pear": 5}},
        {"name": "warehouse_10", "inventory": {"custard apple": 5, "dates": 15, "orange": 10, "apple": 10}}
    ]

    expected_shipment = [
        {'warehouse_1': {'apple': 2, 'apricots': 2, 'avocado': 5, 'banana': 5, 'pomegranate': 4}}, 
        {'warehouse_2': {'apricots': 3, 'blueberries': 2, 'jackfruit': 2}}, 
        {'warehouse_3': {'blueberries': 1, 'cherries': 3, 'jackfruit': 1}}, 
        {'warehouse_4': {'blueberries': 2, 'cherries': 2, 'cranberries': 5, 'jackfruit': 2}}, 
        {'warehouse_5': {'custard apple': 5, 'dates': 1}}, 
        {'warehouse_6': {'figs': 3, 'dates': 2, 'gooseberries': 5, 'grapes': 5, 'guava': 5}}, 
        {'warehouse_7': {'figs': 2, 'lemon': 2, 'mango': 5, 'olives': 2, 'pomegranate': 1}}, 
        {'warehouse_8': {'papaya': 5, 'pear': 5, 'pineapple': 5, 'plums': 5}}, 
        {'warehouse_9': {'lemon': 3, 'olives': 3, 'orange': 1}}, 
        {'warehouse_10': {'apple': 3, 'dates': 2, 'orange': 4}}
    ]

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment


def test_cheapest_shipment_large_unshipped_order():
    """
    not enough inventory, order cannot be shipped
    """
    order = {
        "apple": 5, "apricots": 5, "avocado": 5, "banana": 5, "blueberries": 5, "cherries": 5, "cranberries": 5,
        "custard apple": 5, "figs": 5, "dates": 5, "gooseberries": 5, "grapes": 5, "guava": 5, "jackfruit": 5, 
        "lemon": 5, "mango": 5, "olives": 5, "orange": 5, "papaya": 5, "pear": 5, "pineapple": 5, "plums": 5,
        "pomegranate": 5
    }
    warehouses = [
        {"name": "warehouse_1", "inventory": {"apple": 2, "apricots": 2, "avocado": 5, "banana": 5}},
        {"name": "warehouse_2", "inventory": {"avocado": 5, "blueberries": 2, "jackfruit": 2}},
        {"name": "warehouse_3", "inventory": {"banana": 10, "blueberries": 1, "cherries": 3}},
        {"name": "warehouse_4", "inventory": {"banana": 5, "cherries": 15, "cranberries": 15, "jackfruit": 5}},
        {"name": "warehouse_5", "inventory": {"blueberries": 15, "cherries": 10, "cranberries": 5, "custard apple": 5}},
        {"name": "warehouse_6", "inventory": {"custard apple": 2, "dates": 2, "figs": 3, "grapes": 15, "guava": 5}},
        {"name": "warehouse_7", "inventory": {"lemon": 2, "olives": 2, "figs": 10, "pomegranate": 2}},
        {"name": "warehouse_8", "inventory": {"papaya": 20, "pear": 15}},
        {"name": "warehouse_9", "inventory": {"lemon": 5, "mango": 5, "olives": 5, "orange": 1, "pear": 5}},
        {"name": "warehouse_10", "inventory": {"custard apple": 5, "orange": 10, "apple": 10}}
    ]
    expected_shipment = []

    actual_shipment = cheapest_shipment(order, warehouses)
    assert actual_shipment == expected_shipment
