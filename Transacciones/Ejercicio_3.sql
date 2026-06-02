DO $$

DECLARE
    V_Bill_ID VARCHAR(40) := 'B003';
    V_Product_Record RECORD;    

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

    FOR V_Product_Record IN (

    SELECT Product_ID, Quantity
    FROM Bill_Details
    WHERE Bill_ID = V_Bill_ID

    )
    LOOP

    UPDATE Products 
    SET Inventory = Inventory + V_Product_Record.Quantity
    WHERE ID = V_Product_Record.Product_ID;

    END LOOP;

    UPDATE Bills
    SET Status = 'Returned'
    WHERE ID = V_Bill_ID;

    RAISE NOTICE 'Transaction Complete';

END;

$$ LANGUAGE plpgsql;