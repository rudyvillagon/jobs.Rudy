DO $$

DECLARE
    V_Bill_Details_ID VARCHAR(40) := 'D003';
    V_Products_return INTEGER;
    V_Product_ID VARCHAR(40);
    V_ID_Bills VARCHAR(40);

BEGIN
    SELECT Bill_ID INTO V_ID_Bills
    FROM Bill_Details
    WHERE ID = V_Bill_Details_ID;

    SELECT Product_ID INTO V_Product_ID
    FROM Bill_Details
    WHERE ID = V_Bill_Details_ID;

    SELECT Quantity INTO V_Products_return
    FROM Bill_Details
    WHERE ID = V_Bill_Details_ID;


    IF NOT EXISTS (
    SELECT 1
    FROM Bill_Details 
    WHERE ID = V_Bill_Details_ID
    ) THEN 

    RAISE EXCEPTION 'THE BILL DONT EXISTS';
    END IF;
    
    UPDATE Products 
    SET Inventory = Inventory + V_Products_return
    WHERE ID = V_Product_ID;

    UPDATE Bills
    SET Status = 'Returned'
    WHERE ID = V_ID_Bills;

    RAISE NOTICE 'Transaction Complete';

END;

$$ LANGUAGE plpgsql;