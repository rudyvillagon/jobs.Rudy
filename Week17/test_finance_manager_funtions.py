import pytest 
from unittest.mock import patch,MagicMock
from logics import Category,MoneyMovements,Table

def test_input_category_works_correctly():

    assert Category("Gym stuff") == "Gym stuff"


@patch("logics.sg.Window")
@patch("logics.persistence.save_data_window")
@patch("logics.persistence.load_data_window",return_value=["Car"])
def test_input_in_add_spend_works(mock_load_data,mock_save_data, mock_window):
    mock_window_instance = mock_window.return_value
    mock_window_instance.read.side_effect = [
        ("Add File", {
            "Input_title": "Reparar motor",
            "Input_amount": "300",
            "-COMBO-": "Car"
        }),
        ("Cancel", {})  
    ]
    MoneyMovements.add_spend_log([])

    
    mock_save_data.assert_called_once_with({
        "Title": "Reparar motor",
        "Amount": "300",
        "Category": "Car"
    })


@patch("logics.sg.Window")
@patch("logics.persistence.save_data_window")
@patch("logics.persistence.load_data_window",return_value=["Job"])
def test_input_in_add_entry_works(mock_load_data,mock_save_data, mock_window):
    mock_window_instance = mock_window.return_value
    mock_window_instance.read.side_effect = [
        ("Add File", {
            "Input_title": "Montly payment June 2025",
            "Input_amount": "3000",
            "-COMBO-": "Job"
        }),
        ("Cancel", {})  
    ]
    MoneyMovements.add_entry_log([])

    
    mock_save_data.assert_called_once_with({
        "Title": "Montly payment June 2025",
        "Amount": "3000",
        "Category": "Job"
    })

@patch("logics.sg.popup_error")
@patch("logics.sg.Window")
@patch("logics.persistence.save_data_window")
@patch("logics.persistence.load_data_window",return_value=["Job"])
def test_input_in_add_entry_dont_work_without_category(mock_load_data,mock_save_data, mock_window,mock_popup_error):
    mock_window_instance = mock_window.return_value
    mock_window_instance.read.side_effect = [
        ("Add File", {
            "Input_title": "Montly payment June 2025",
            "Input_amount": "3000",
            "-COMBO-": ""
        }),
        ("Cancel", {})  
    ]

    val = []
    MoneyMovements.add_entry_log(val)

    
    mock_save_data.assert_not_called()

    mock_popup_error.assert_called_once_with("You need to select a Category ❌")


@patch("logics.sg.Window")
def test_that_the_window_add_spend_opens_correctly(mock_window):

    mock_window_instance = mock_window.return_value
    mock_window_instance.read.side_effect = [
        ("Add Spent", {}),
        ("Cancel", {})
    ]
    
    
    new_spend = []

    MoneyMovements.add_spend_log(new_spend)

    mock_window.assert_called_once()

    args, kwargs = mock_window.call_args
    assert args[0] == "New Spent"  

    assert mock_window_instance.read.call_count >= 1
    mock_window_instance.close.assert_called_once()


@patch("logics.sg.Window")
def test_that_the_window_new_category_opens_correctly(mock_window):

    mock_window_instance = mock_window.return_value
    mock_window_instance.read.side_effect = [
        ("New Category", {}),
        ("Cancel", {})
    ]
    
    
    test_categories = []

    Category.new_category(test_categories)

    mock_window.assert_called_once()

    args, kwargs = mock_window.call_args
    assert args[0] == "Personal Finance Manager"  

    assert mock_window_instance.read.call_count >= 1
    mock_window_instance.close.assert_called_once()


@patch("logics.sg.Window")
def test_that_the_window_add_entry_opens_correctly(mock_window):

    mock_window_instance = mock_window.return_value
    mock_window_instance.read.side_effect = [
        ("Add Entry", {}),
        ("Cancel", {})
    ]
    
    
    new_entry = []

    MoneyMovements.add_entry_log(new_entry)

    mock_window.assert_called_once()

    args, kwargs = mock_window.call_args
    assert args[0] == "New Entry"  

    assert mock_window_instance.read.call_count >= 1
    mock_window_instance.close.assert_called_once()


@patch("logics.persistence.load_data_window",return_value=[
    {"Title": "Salary", "Amount": 3800, "Category": "Job"}
    ])
def test_refresh_list_botton_works_correctly(mock_load_data_window):


    mock_window = MagicMock()
    mock_table = MagicMock()

    mock_window.__getitem__.return_value = mock_window


    Table.refresh_list_display(mock_window)

    mock_window.update.assert_called_once_with(values=[
        ["Salary", 3800, "Job"]
    ])





