DO $$

DECLARE
    V_Product_ID VARCHAR(40) := 'P003';
    V_Inventory_Stock INTEGER;
    V_Row_Update INTEGER;    

BEGIN
    SELECT Inventory
    INTO V_Inventory_Stock
    FROM Products
    WHERE ID = V_Product_ID;

    IF V_Inventory_Stock <= 0 THEN
        RAISE EXCEPTION '-- Stock Not Available--'; 
    END IF;

    PERFORM pg_sleep(10);

    UPDATE Products
    SET Inventory = Inventory - 1
    WHERE ID = V_Product_ID 
    AND Inventory = V_Inventory_Stock;

    GET DIAGNOSTICS V_Row_Update = ROW_COUNT;

    IF V_Row_Update <= 0 THEN
        RAISE EXCEPTION '-- The purchase could not be completed; another user has purchased the last product BY USER 1 --';
    END IF;

    RAISE NOTICE '--The Purchese has been completed by USER 2 --';

END;

$$ LANGUAGE plpgsql;