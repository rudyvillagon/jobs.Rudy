DO $$

DECLARE
    V_Bill_ID VARCHAR(40) := 'B003';
    V_Product_ID VARCHAR(40);
    V_Products_return INTEGER;

BEGIN
    IF NOT EXISTS (
    SELECT 1
    FROM Bills
    WHERE ID = V_Bill_ID
    ) THEN

    RAISE EXCEPTION 'THE BILL DONT EXISTS';
    END IF;

    IF EXISTS (
    SELECT 1
    FROM Bills
    WHERE ID = V_Bill_ID
    AND Status = 'Returned'
    ) THEN

    RAISE EXCEPTION 'THE BILL IS ALL READY RETURNED';
    END IF;

    SELECT Product_ID INTO V_Product_ID
    FROM Bill_Details
    WHERE Bill_ID = V_Bill_ID;

    SELECT Quantity INTO V_Products_return
    FROM Bill_Details
    WHERE Bill_ID = V_Bill_ID;


    UPDATE Products 
    SET Inventory = Inventory + V_Products_return
    WHERE ID = V_Product_ID;

    UPDATE Bills
    SET Status = 'Returned'
    WHERE ID = V_Bill_ID;

    RAISE NOTICE 'Transaction Complete';

END;

$$ LANGUAGE plpgsql;