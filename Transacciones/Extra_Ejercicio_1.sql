Do $$
DECLARE
    V_Bill_Details_ID VARCHAR(40) := 'D007';
    V_Status_Bill_Details VARCHAR(40);
    V_Products_return RECORD;

BEGIN
    SELECT Product_Status INTO V_Status_Bill_Details --'Pending'
    FROM Bill_Details
    WHERE ID = V_Bill_Details_ID;

    IF V_Status_Bill_Details != 'Pending' THEN
    RAISE EXCEPTION 'Shipment cannot be cancelled';
    END IF;

    BEGIN

        FOR V_Products_return IN (
        SELECT Quantity, Product_ID
        FROM Bill_Details
        WHERE ID = V_Bill_Details_ID
        AND Product_Status = 'Pending'
        )

        LOOP

        UPDATE Products 
        SET Inventory = Inventory + V_Products_return.Quantity
        WHERE ID = V_Products_return.Product_ID;

        END LOOP;

        UPDATE Bill_Details
        SET Product_Status = 'Canceled'
        WHERE ID = V_Bill_Details_ID
        AND Product_Status = 'Pending';

    END;

    RAISE NOTICE 'Transaction Complete';

END;

$$LANGUAGE plpgsql;